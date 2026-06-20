#!/usr/bin/env python3
"""
Buscador de IPA para Kalfírvach — Traducciones + IPA real desde Wiktionary
===========================================================================
FASE 1: Dado un concepto en español/inglés, busca {concepto}/translations
        en Wiktionary EN y extrae las palabras REALES en lenguas fuente.
FASE 2: Para cada palabra real, extrae su IPA desde su propia entrada.

Esto evita ALUCINAR palabras raíz y ALUCINAR IPAs: todo viene de Wiktionary.

Uso:
  python3 buscador_ipa.py dios
  python3 buscador_ipa.py dios --lenguas sanscrito,copto,griego
  python3 buscador_ipa.py "luna" --forjar
  python3 buscador_ipa.py "agua" --ingres
  python3 buscador_ipa.py "water" --ingres   # ya en inglés
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse
import urllib.error

# =============================================================================
# CONFIGURACIÓN
# =============================================================================

CACHE_PATH = os.path.expanduser("~/.kfa_ipa_cache.json")
WIKTIONARY_EN_API = "https://en.wiktionary.org/w/api.php"
WIKTIONARY_ES_API = "https://es.wiktionary.org/w/api.php"
USER_AGENT = "KalfirvachForge/1.4 (lexicon generator; kalfirvach@local)"

# Nombres de lenguas TAL COMO APARECEN en la página de traducciones
TRANSLATION_LANG_NAMES = {
    "sanscrito": "Sanskrit",
    "copto": "Coptic",
    "egipcio": "Egyptian",
    "avestico": "Avestan",
    "persa_mod": "Persian",
    "arabe": "Arabic",
    "griego": "Ancient Greek",
    "tibetano": "Tibetan",
}

# Mapeo para búsqueda de IPA por sección (reutilizado del viejo script)
LANG_CONFIG = {
    "copto": {
        "wiktionary_section": "Coptic",
        "aliases": ["Copto"],
    },
    "egipcio": {
        "wiktionary_section": "Egyptian",
        "aliases": ["Demotic", "Egyptian Demotic"],
    },
    "avestico": {
        "wiktionary_section": "Avestan",
        "aliases": ["Avestan"],
    },
    "persa_mod": {
        "wiktionary_section": "Persian",
        "aliases": ["Persian", "Modern Persian"],
    },
    "arabe": {
        "wiktionary_section": "Arabic",
        "aliases": ["Arabic"],
    },
    "sanscrito": {
        "wiktionary_section": "Sanskrit",
        "aliases": ["Sanskrit"],
    },
    "griego": {
        "wiktionary_section": "Ancient Greek",
        "aliases": ["Greek", "Ancient Greek", "Koine Greek"],
    },
    "tibetano": {
        "wiktionary_section": "Tibetan",
        "aliases": ["Tibetan"],
    },
}

# Caracteres exclusivamente IPA (no-ASCII) — solo estos cuentan para el score.
# Excluye ASCII como t, d, s, n que aparecen en texto normal.
IPA_CHARS = set(
    # IPA Extensions (U+0250–U+02AF)
    'ɐɑɒɓɔɕɖɗɘəɚɛɜɝɞɟɠɡɢɣɤɥɦɧɨɩɪɫɬɭɮɯɰɱɲɳɴɵɶɷɸɹɺɻɼɽɾɿʀʁʂʃʄʅʆʇʈʉʊʋʌʍʎʏʐʑʒʓʔʕʖʗʘʙʚʛʜʝʞʟ'
    # Modifier letters for stress/length
    'ˈˌːˑ'
    # Combining diacritics used in IPA
    '\u0300\u0301\u0302\u0303\u0304\u0308\u030a\u030b\u030c\u0323\u0325\u032a\u0330\u0331'
    # Tone letters (some)
    '˥˦˧˨˩'
)

# Palabras comunes en HTML que NO son IPA (falsos positivos adicionales)
IPA_BLACKLIST = {
    'edit', 'title', 'section', 'link', 'class', 'style', 'script',
    'wiki', 'index', 'php', 'action', 'submit', 'delete', 'move',
    'protect', 'unprotect', 'view', 'source', 'history', 'watch',
}

# =============================================================================
# CACHÉ LOCAL
# =============================================================================

def load_cache():
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH) as f:
            return json.load(f)
    return {}

def save_cache(cache):
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    with open(CACHE_PATH, 'w') as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

def cache_get(key):
    cache = load_cache()
    return cache.get(key)

def cache_set(key, data):
    cache = load_cache()
    cache[key] = data
    save_cache(cache)

# =============================================================================
# API DE WIKTIONARY
# =============================================================================

def api_call(word, api_url=WIKTIONARY_EN_API, section=None):
    """Wrapper base para action=parse con o sin section."""
    params = {
        "action": "parse",
        "page": word,
        "prop": "text",
        "format": "json",
        "redirects": 1,
    }
    if section is not None:
        params["section"] = section

    url = f"{api_url}?{urllib.parse.urlencode(params)}"
    data, error = http_get(url)
    if error:
        return None, error

    text = data.get("parse", {}).get("text", {}).get("*", "") if data else ""
    if not text:
        return None, f"Page '{word}' not found or empty"
    return text, None


def api_sections(word, api_url=WIKTIONARY_EN_API):
    """Obtener la lista de secciones de una página (con caché)."""
    global _sections_cache
    cache_key = f"{api_url}:{word}"
    if cache_key in _sections_cache:
        return _sections_cache[cache_key], None

    params = urllib.parse.urlencode({
        "action": "parse", "page": word, "prop": "sections", "format": "json", "redirects": 1,
    })
    url = f"{api_url}?{params}"
    data, error = http_get(url)
    if error:
        return None, error
    sections = data.get("parse", {}).get("sections", []) if data else []
    if not sections and (not data or "parse" not in data):
        return None, f"Page '{word}' not found"
    _sections_cache[cache_key] = sections
    return sections, None

# =============================================================================
# FASE 1: Encontrar palabras reales en lenguas fuente
# =============================================================================

def detectar_idioma(texto):
    """Detecta si el input parece español o inglés."""
    # Palabras muy españolas que rara vez aparecen en inglés
    es_indicators = ['el ', 'la ', 'los ', 'las ', 'un ', 'una ',
                     'ción', 'dad ', 'mente', 'miento', 'dios', 'agua',
                     'luna', 'sol', 'rio', 'mar', 'fuego', 'tierra',
                     'cielo', 'noche', 'dia ', 'ojo', 'mano', 'pie',
                     'sangre', 'lengua', 'nombre', 'mundo', 'corazon']
    texto_lower = texto.lower()
    score = 0
    for ind in es_indicators:
        if ind in texto_lower:
            score += 1
    if texto_lower.endswith('ción') or texto_lower.endswith('dad') or \
       texto_lower.endswith('mente') or texto_lower.endswith('miento'):
        score += 2
    return 'es' if score >= 1 else 'en'


def traducir_es_a_en(concepto):
    """
    Traduce un concepto de español a inglés usando es.wiktionary.org.
    Busca la palabra en español y extrae el enlace a la entrada en inglés.
    """
    cache_key = f"trans:es_en:{concepto}"
    cached = cache_get(cache_key)
    if cached:
        return cached

    html, error = api_call(concepto, api_url=WIKTIONARY_ES_API)
    if error:
        return None

    # En la página española, las traducciones están en listas:
    #   <li>Inglés: &#91;1&#93;&#160;<a href="/wiki/god#Inglés" title="god">god</a> ...
    # Buscar "Inglés:" y extraer el primer <a> después (non-greedy)
    m = re.search(r'Inglés:.*?<a\s+href="/wiki/([^"#]+)', html)
    if m:
        word = urllib.parse.unquote(m.group(1)).replace('_', ' ')
        cache_set(cache_key, word)
        return word

    return None


def _parse_translations_html(html):
    """Dado HTML con lista de traducciones (<li>Lengua: ...</li>),
    extrae las entradas para las lenguas fuente de Kalfírvach.

    Retorna dict: {lang_id: [(word, section_from_href), ...], ...}
    """
    resultados = {}

    for lang_id, lang_name in TRANSLATION_LANG_NAMES.items():
        pattern = re.compile(
            r'<li>' + re.escape(lang_name) + r':\s*(.*?)</li>',
            re.DOTALL
        )

        entries = []
        for m in pattern.finditer(html):
            li_content = m.group(1)
            for a in re.finditer(
                r'<a\s+href="/wiki/([^"#]+)(#[^"]*)?"\s+title="([^"]*)">',
                li_content
            ):
                word = a.group(3).strip()
                section = a.group(2) or ""
                if word and word not in [e[0] for e in entries]:
                    entries.append((word, section.lstrip("#")))

        if entries:
            resultados[lang_id] = entries

    return resultados


def find_translations_page(concept_en):
    """
    Busca traducciones para un concepto en inglés en Wiktionary EN.

    Primero intenta {concept}/translations (subpágina dedicada).
    Si no existe, busca la sección 'Translations' en la página principal
    (algunas palabras tienen las traducciones inline).

    Retorna dict: {lang_id: [(word, section_from_href), ...], ...}
    """
    cache_key = f"translations:{concept_en}"
    cached = cache_get(cache_key)
    if cached:
        return cached

    # Estrategia 1: {concept}/translations subpage
    html, error = api_call(f"{concept_en}/translations")

    if not error:
        # Subpage exists — parsear directamente
        resultados = _parse_translations_html(html)
        cache_set(cache_key, resultados)
        return resultados

    # Estrategia 2: Translations section in main page
    html, error = api_call(concept_en)
    if error:
        return None

    sections, error = api_sections(concept_en)
    if error:
        # No podemos obtener secciones, pero tenemos el HTML completo.
        # Intentar parsear las traducciones del HTML completo directamente.
        resultados = _parse_translations_html(html)
        if resultados:
            cache_set(cache_key, resultados)
            return resultados
        return None

    # Buscar sección "Translations" en la página principal
    trans_index = None
    for sec in sections:
        line = sec.get("line", "").lower()
        if "translation" in line or "translations" in line:
            trans_index = sec.get("index")
            break

    if trans_index is None:
        # No hay sección de traducciones — intentar con HTML completo
        resultados = _parse_translations_html(html)
        if resultados:
            cache_set(cache_key, resultados)
            return resultados
        return None

    # Obtener HTML de la sección de traducciones
    section_html, error = api_call(concept_en, section=trans_index)
    if error:
        # Fallback: HTML completo
        resultados = _parse_translations_html(html)
        if resultados:
            cache_set(cache_key, resultados)
            return resultados
        return None

    resultados = _parse_translations_html(section_html)
    cache_set(cache_key, resultados)
    return resultados


# =============================================================================
# FASE 2: Extraer IPA de cada palabra real
# =============================================================================

def es_ipa_valido(candidato):
    """Filtra falsos positivos: solo acepta si hay suficientes chars IPA reales
    y no está en la blacklist de palabras HTML comunes."""
    limpio = candidato.strip().lower()
    if limpio in IPA_BLACKLIST:
        return False
    score = sum(1 for c in candidato if c in IPA_CHARS)
    return score >= 3 and len(candidato) >= 2


# Rate limiter: al menos 2s entre requests a Wiktionary
_last_api_call = 0
def rate_limit():
    global _last_api_call
    now = time.time()
    elapsed = now - _last_api_call
    if elapsed < 2.0:
        time.sleep(2.0 - elapsed)
    _last_api_call = time.time()


def http_get(url, retries=3):
    """GET con retry y backoff exponencial para 429s."""
    for attempt in range(retries):
        rate_limit()
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read()), None
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                wait = (attempt + 1) * 5
                print(f"      ⏱ 429, esperando {wait}s (intento {attempt+2}/{retries})...")
                time.sleep(wait)
                continue
            return None, f"HTTP Error {e.code}: {e.reason}"
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(3)
                continue
            return None, str(e)
    return None, "Max retries exceeded"

# Caché de secciones (evita llamadas repetidas a la misma página)
_sections_cache = {}


def extract_ipa_from_html(html_text):
    """Extrae IPA del HTML renderizado de una sección de Wiktionary."""
    ipas = []

    # Pattern 1: <span class="IPA">/ipa/</span>
    for m in re.finditer(r'<span[^>]*class="[^"]*IPA[^"]*"[^>]*>(.*?)</span>', html_text):
        content = re.sub(r'<[^>]+>', '', m.group(1))
        content = content.strip('/[] \t\n\r')
        if content and len(content) >= 2 and content not in ipas and es_ipa_valido(content):
            ipas.append(content)

    # Pattern 2: /.../ en texto plano (sin tags)
    text = re.sub(r'<[^>]+>', ' ', html_text)
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    for m in re.finditer(r'/([^/]{2,25})/', text):
        ipa = m.group(1).strip()
        if es_ipa_valido(ipa) and ipa not in ipas:
            ipas.append(ipa)

    # Pattern 3: [...] que parezcan IPA
    for m in re.finditer(r'\[([^\[\]]{2,25})\]', text):
        ipa = m.group(1).strip()
        if es_ipa_valido(ipa) and ipa not in ipas:
            ipas.append(ipa)

    return ipas


def lookup_word_ipa(lang_id, word, section_hint=""):
    """
    Busca IPA para una palabra real en una lengua fuente.
    Reutiliza la lógica del viejo buscador pero simplificada.
    """
    # Cache key incluye el hint de sección
    cache_key = f"ipa:{lang_id}:{word}"
    cached = cache_get(cache_key)
    if cached:
        return cached

    config = LANG_CONFIG.get(lang_id)
    if not config:
        result = {"error": f"Unknown lang: {lang_id}", "ipa": []}
        cache_set(cache_key, result)
        return result

    wiktionary_section = config["wiktionary_section"]

    # Obtener secciones de la palabra
    sections, error = api_sections(word)
    if error:
        result = {"error": error, "ipa": []}
        cache_set(cache_key, result)
        return result

    # Buscar la sección que coincide
    section_index = None
    for sec in sections:
        sec_line = sec.get("line", "")
        # Coincidencia exacta
        if sec_line == wiktionary_section:
            section_index = sec.get("index")
            break
        # Coincidencia por alias
        if sec_line in config.get("aliases", []):
            section_index = sec.get("index")
            break
        # Coincidencia por hint de la URL (section_hint)
        if section_hint and sec.get("anchor") == section_hint:
            section_index = sec.get("index")
            break
        # Coincidencia case-insensitive
        if sec_line.lower() == wiktionary_section.lower():
            section_index = sec.get("index")
            break

    if section_index is None:
        # Fallback: buscar en TODA la página (sin sección)
        html, error = api_call(word)
        if error:
            result = {"error": error, "ipa": [], "note": "Section not found"}
            cache_set(cache_key, result)
            return result

        # Intentar extraer IPA de toda la página (poco preciso)
        ipas = extract_ipa_from_html(html)
        if ipas:
            result = {"error": None, "ipa": ipas,
                       "note": "Extracted from full page (section not found)"}
        else:
            result = {"error": f"Section '{wiktionary_section}' not found for '{word}'",
                       "ipa": [], "note": f"Available: {[s.get('line') for s in sections[:10]]}"}
        cache_set(cache_key, result)
        return result

    # Obtener HTML de la sección
    html, error = api_call(word, section=section_index)
    if error:
        # Fallback: página completa
        html, error = api_call(word)
        if error:
            result = {"error": error, "ipa": []}
            cache_set(cache_key, result)
            return result
        ipas = extract_ipa_from_html(html)
        result = {"error": None if ipas else "IPA not found (fallback)",
                   "ipa": ipas, "note": "Full page fallback"}
        cache_set(cache_key, result)
        return result

    # Extraer IPA
    ipas = extract_ipa_from_html(html)
    result = {
        "error": None if ipas else "IPA not found in section",
        "ipa": ipas,
    }
    cache_set(cache_key, result)
    return result


# =============================================================================
# FLUJO PRINCIPAL
# =============================================================================

def buscar_concepto(concepto, langs_filter=None):
    """
    Busca un concepto en español o inglés y devuelve las palabras reales
    con sus IPAs en las lenguas fuente de Kalfírvach.

    Args:
        concepto: str - El concepto a buscar (ej: "dios", "water")
        langs_filter: list[str] o None - IDs de lenguas a filtrar (ej: ["sanscrito", "copto"])

    Returns:
        dict con:
          concepto_es: str - concepto original
          concepto_en: str - concepto en inglés
          lenguas: dict {lang_id: {word, ipa, error, ...}}
    """
    # Detectar y traducir si es necesario
    idioma = detectar_idioma(concepto)
    concepto_en = concepto

    if idioma == 'es':
        print(f"  → Detectado español, traduciendo a inglés...")
        en_word = traducir_es_a_en(concepto)
        if en_word:
            concepto_en = en_word
            print(f"  → '{concepto}' → '{concepto_en}'")
        else:
            print(f"  ⚠ No se pudo traducir '{concepto}', intentando como inglés...")

    # FASE 1: Buscar traducciones
    print(f"\n  FASE 1: Buscando '{concepto_en}' en Wiktionary traducciones...")
    translations = find_translations_page(concepto_en)

    if translations is None:
        return {
            "concepto": concepto,
            "concepto_en": concepto_en,
            "error": f"No se encontró la página '{concepto_en}' o '{concepto_en}/translations'",
            "lenguas": {},
        }

    # Filtrar lenguas si se especificó
    if langs_filter:
        translations = {k: v for k, v in translations.items() if k in langs_filter}

    if not translations:
        return {
            "concepto": concepto,
            "concepto_en": concepto_en,
            "error": f"No se encontraron traducciones para las lenguas solicitadas",
            "lenguas": {},
        }

    # FASE 2: Buscar IPA para cada palabra
    print(f"  FASE 2: Extrayendo IPA de cada palabra encontrada...\n")

    lenguas_result = {}
    for lang_id, entries in translations.items():
        lang_name = TRANSLATION_LANG_NAMES.get(lang_id, lang_id)
        palabras = []

        for word, section_hint in entries:
            ipa_result = lookup_word_ipa(lang_id, word, section_hint)
            palabras.append({
                "word": word,
                "ipa": ipa_result.get("ipa", []),
                "error": ipa_result.get("error"),
                "note": ipa_result.get("note", ""),
            })

        lenguas_result[lang_id] = {
            "nombre": lang_name,
            "palabras": palabras,
        }

    return {
        "concepto": concepto,
        "concepto_en": concepto_en,
        "error": None,
        "lenguas": lenguas_result,
    }


# =============================================================================
# INTERFAZ DE USUARIO
# =============================================================================

def mostrar_resultado(resultado):
    """Muestra el resultado en formato legible."""
    concepto = resultado.get("concepto", "?")
    concepto_en = resultado.get("concepto_en", "?")
    error = resultado.get("error")

    print(f"\n{'='*60}")
    print(f"  CONCEPTO: {concepto}")
    if concepto_en != concepto:
        print(f"  INGLÉS:   {concepto_en}")
    print(f"{'='*60}")

    if error:
        print(f"\n  ✗ {error}")
        return

    lenguas = resultado.get("lenguas", {})
    if not lenguas:
        print("  (sin resultados)")
        return

    for lang_id, data in lenguas.items():
        nombre = data.get("nombre", lang_id)
        palabras = data.get("palabras", [])

        print(f"\n  ── {nombre} ({lang_id}) ──")

        for p in palabras:
            word = p.get("word", "?")
            ipas = p.get("ipa", [])
            error = p.get("error")

            if ipas:
                for ipa in ipas:
                    print(f"    ✓ {word}  /{ipa}/")
            elif error and "IPA not found" in error:
                print(f"    ~ {word}  ⚠ (IPA no encontrada en sección)")
            elif error:
                print(f"    ✗ {word}  ✗ {error}")
            else:
                print(f"    - {word}  (sin datos)")


def forjar_desde_resultado(resultado):
    """Pasa los IPAs encontrados a la forja léxica."""
    all_ipas = {}
    for lang_id, data in resultado.get("lenguas", {}).items():
        for p in data.get("palabras", []):
            if p.get("ipa"):
                for ipa in p["ipa"]:
                    if ipa not in all_ipas:
                        all_ipas[ipa] = []
                    all_ipas[ipa].append(f"{lang_id}:{p['word']}")

    if not all_ipas:
        print("  No hay IPAs para forjar.")
        return

    print(f"\n  IPAs encontradas para forjar:")
    for ipa, sources in all_ipas.items():
        print(f"    /{ipa}/  ←  {', '.join(sources)}")

    concepto = resultado.get("concepto_en", resultado.get("concepto", "concepto"))
    import subprocess
    forge_path = os.path.join(os.path.dirname(__file__), "forja_lexica_kfa.py")
    cmd = [sys.executable, forge_path, "--ipa"] + [f"/{ipa}/" for ipa in all_ipas] + ["--concepto", concepto]
    print(f"\n  Ejecutando: {' '.join(cmd)}\n")
    subprocess.run(cmd)


# =============================================================================
# CLI
# =============================================================================

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Buscador de IPA para Kalfírvach — Traducciones + IPA real desde Wiktionary",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python3 buscador_ipa.py dios
  python3 buscador_ipa.py "luna" --lenguas sanscrito,copto,griego
  python3 buscador_ipa.py water --ingres     # si ya está en inglés, evitar detección
  python3 buscador_ipa.py dios --forjar
  python3 buscador_ipa.py dios --json
        """,
    )
    parser.add_argument('concepto', nargs='?', help='Concepto en español o inglés')
    parser.add_argument('--lenguas', help='Filtrar lenguas (separadas por coma)')
    parser.add_argument('--forjar', action='store_true', help='Pasar IPAs a la forja léxica')
    parser.add_argument('--json', action='store_true', help='Salida en JSON')
    parser.add_argument('--ingres', action='store_true', help='Forzar input como inglés (saltar detección)')
    parser.add_argument('--clean-cache', action='store_true', help='Limpiar caché local')
    parser.add_argument('--interactive', action='store_true', help='Modo interactivo')

    args = parser.parse_args()

    if args.clean_cache:
        if os.path.exists(CACHE_PATH):
            os.remove(CACHE_PATH)
            print("Caché limpiada.")
        return

    if args.interactive:
        interactive_mode()
        return

    if not args.concepto:
        parser.print_help()
        return

    # Filtrar lenguas
    langs_filter = None
    if args.lenguas:
        langs_filter = [l.strip() for l in args.lenguas.split(',')]
        # Validar
        for l in langs_filter:
            if l not in LANG_CONFIG:
                print(f"  ✗ Lengua desconocida: '{l}'. Opciones: {', '.join(LANG_CONFIG.keys())}")
                return

    # Forzar inglés
    if args.ingres:
        # Patear la detección: meter prefijo
        concepto = args.concepto
        idioma = 'en'
    else:
        concepto = args.concepto

    print(f"\n{'='*60}")
    print(f"  BUSCADOR DE IPA — Kalfírvach v1.4")
    print(f"{'='*60}")

    resultado = buscar_concepto(concepto, langs_filter)

    if args.json:
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
    else:
        mostrar_resultado(resultado)

    if args.forjar and resultado and not resultado.get("error"):
        forjar_desde_resultado(resultado)


def interactive_mode():
    print("""
╔════════════════════════════════════════════╗
║    BUSCADOR DE IPA — Kalfírvach v1.4      ║
║   Traducciones + IPA real desde Wiktionary ║
╚════════════════════════════════════════════╝
""")
    try:
        concepto = input("Concepto (español o inglés): ").strip()
        if not concepto:
            return

        langs_input = input("Lenguas (separadas por coma, Enter = todas): ").strip()
        langs_filter = [l.strip() for l in langs_input.split(',')] if langs_input else None

        if langs_filter:
            for l in langs_filter:
                if l not in LANG_CONFIG:
                    print(f"  ✗ Lengua desconocida: '{l}'")
                    return

        forjar = input("¿Forjar con los IPAs? [s/N]: ").strip().lower() == 's'

        print()
        resultado = buscar_concepto(concepto, langs_filter)
        mostrar_resultado(resultado)

        if forjar and resultado and not resultado.get("error"):
            forjar_desde_resultado(resultado)

    except (KeyboardInterrupt, EOFError):
        print("\n\n  Hasta luego!")
        sys.exit(0)


if __name__ == '__main__':
    main()

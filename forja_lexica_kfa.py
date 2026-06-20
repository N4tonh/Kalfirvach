#!/usr/bin/env python3
"""
Forja Léxica Kalfírvach — Motor de Síntesis Fonotáctica v1.4.1
==============================================================
Port del generador HTML a Python. Uso interactivo en terminal.

Uso:
  python3 forja_lexica_kfa.py                    # Modo interactivo
  python3 forja_lexica_kfa.py --batch            # Modo batch rápido
  python3 forja_lexica_kfa.py --help             # Ayuda detallada
"""

import sys
import re
import json
import random
from collections import Counter
from dataclasses import dataclass, field
from typing import List, Optional

# =============================================================================
# FONOLOGÍA KALFÍRVACH v1.4
# =============================================================================

CONSONANTS = [
    'p', 'b', 't', 'd', 'k', 'g', 'm', 'n', 'f', 'v', 's', 'z', 'h',
    'ch', 'j', 'r', 'l', 'y', 'w', 'sh', 'zh', 'kh', 'th', 'dh', 'gh'
]

VOWELS = ['a', 'e', 'i', 'o', 'u']
LONG_VOWELS = ['ā', 'ē', 'ī', 'ō', 'ū']
ALL_VOWELS = VOWELS + LONG_VOWELS

VALID_CODAS = ['m', 'n', 'r', 'l', 's', 'sh', 'p', 't', 'k', 'ch', 'kh', 'h']
DIGRAPHS = ['ch', 'sh', 'zh', 'kh', 'th', 'dh', 'gh']

VOWEL_TO_LONG = {'a': 'ā', 'e': 'ē', 'i': 'ī', 'o': 'ō', 'u': 'ū'}
LONG_TO_VOWEL = {v: k for k, v in VOWEL_TO_LONG.items()}

# Para display prosódico
ACCENT_MAP = {
    'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú',
    'ā': 'ā́', 'ē': 'ḗ', 'ī': 'ī́', 'ō': 'ṓ', 'ū': 'ū́'
}

# IPA → Kalfírvach: mapping usado en limpiarIPA()
IPA_KAL_MAP = {
    # africadas
    'tʃ': 'ch', 'dʒ': 'j',
    # fricativas
    'θ': 'th', 'ð': 'dh', 'x': 'kh', 'ɣ': 'gh', 'ʃ': 'sh', 'ʒ': 'zh',
    # nasales
    'ŋ': 'n', 'ɲ': 'n',
    # oclusivas
    'q': 'k',
    # faringales/glotales
    'ʕ': 'h', 'ħ': 'h',
    # otras
    'ɸ': 'f', 'β': 'v', 'ç': 'sh', 'ɬ': 'l',
}
# Nota: j→y se maneja con cuidado (la j del IPA se mapea primero a y)
# y después y→i también


# =============================================================================
# LENGUAS FUENTE
# =============================================================================

LENGUAS = [
    {"id": "copto",      "nombre": "Copto"},
    {"id": "egipcio",    "nombre": "Egipcio Demótico"},
    {"id": "avestico",   "nombre": "Persa Avéstico"},
    {"id": "persa_mod",  "nombre": "Persa Moderno"},
    {"id": "arabe",      "nombre": "Árabe Esotérico"},
    {"id": "sanscrito",  "nombre": "Sánscrito"},
    {"id": "griego",     "nombre": "Griego Koiné"},
    {"id": "tibetano",   "nombre": "Tibetano"},
]


# =============================================================================
# FUNCIONES DE LIMPIEZA Y TOKENIZACIÓN
# =============================================================================

def clean_ipa(ipa: str) -> str:
    """Limpia y mapea IPA a alfabeto Kalfírvach (equivalente a limpiarIPA del JS)."""
    s = ipa.lower()

    # 1. Quitar acentos IPA, corchetes, slashes, puntos de sílaba
    s = re.sub(r'[\u0361\u035c\u02bc\u02b0\u02c8\u02ccˈˌ.\[\]/]', '', s)

    # 2. Longitud: ː ˑ → vocal larga
    s = re.sub(r'([aeiou])[ːˑ]', lambda m: VOWEL_TO_LONG.get(m.group(1), m.group(1)), s)

    # 3. Mapeo de IPA a consonantes KFA
    #    Orden importa: dígrafos primero
    for ipa_sound, kal_sound in sorted(IPA_KAL_MAP.items(), key=lambda x: -len(x[0])):
        s = s.replace(ipa_sound, kal_sound)

    # 4. j → y (IPA j es glide palatal)
    s = s.replace('j', 'y')

    # 5. y → i (cuando y no representa /j/ sino /y/)
    #    Esto es post-j→y para capturar las /y/ que eran /j/ en IPA
    s = s.replace('y', 'i')

    # 6. Otros: vocales
    s = s.replace('ɛ', 'e').replace('æ', 'e')
    s = s.replace('ɔ', 'o').replace('ɒ', 'o')
    s = s.replace('ɪ', 'i')
    s = s.replace('ʊ', 'u')
    s = s.replace('ə', 'a').replace('ʌ', 'a')

    # 7. ʔ se elimina
    s = s.replace('ʔ', '')

    return s


def tokenize(word: str) -> List[str]:
    """Divide palabra en tokens de Kalfírvach (dígrafos son 1 token)."""
    tokens = []
    i = 0
    while i < len(word):
        if i + 1 < len(word) and word[i:i+2] in DIGRAPHS:
            tokens.append(word[i:i+2])
            i += 2
        elif word[i] in CONSONANTS or word[i] in ALL_VOWELS:
            tokens.append(word[i])
            i += 1
        else:
            i += 1
    return tokens


def syllabify(word: str) -> List[str]:
    """Divide en sílabas siguiendo la lógica del JS."""
    tokens = tokenize(word)

    # Encontrar índices de vocales
    vowel_indices = [i for i, t in enumerate(tokens) if t in ALL_VOWELS]

    if len(vowel_indices) <= 1:
        return [word]

    syllables = []
    start = 0

    for i in range(len(vowel_indices) - 1):
        v_curr = vowel_indices[i]
        v_next = vowel_indices[i + 1]
        dist = v_next - v_curr - 1  # consonantes entre vocales

        if dist == 1:
            split = v_curr + 1
        elif dist >= 2:
            split = v_curr + 2
        else:
            split = v_curr + 1

        syllables.append(''.join(tokens[start:split]))
        start = split

    syllables.append(''.join(tokens[start:]))
    return syllables


def get_stressed_syllable_idx(syllables: List[str]) -> int:
    """Sílaba tónica: la primera con vocal larga, si no, penúltima."""
    if len(syllables) == 1:
        return 0
    for i, syl in enumerate(syllables):
        if any(v in syl for v in LONG_VOWELS):
            return i
    # Si no hay larga, penúltima
    return len(syllables) - 2 if len(syllables) >= 2 else 0


# =============================================================================
# VALIDACIÓN FONOTÁCTICA
# =============================================================================

def is_valid_kalfirvach(word: str) -> bool:
    """Valida si una palabra cumple fonotáctica Kalfírvach (equivalente al JS)."""
    tokens = tokenize(word)

    # Largo 4-8 (máx 8 para mantener palabras compactas)
    if len(word) < 4 or len(word) > 8:
        return False

    # Sin vocales consecutivas
    for i in range(len(tokens) - 1):
        if tokens[i] in ALL_VOWELS and tokens[i+1] in ALL_VOWELS:
            return False

    # Máx 2 consonantes seguidas
    cons_count = 0
    for t in tokens:
        if t in CONSONANTS:
            cons_count += 1
        else:
            cons_count = 0
        if cons_count >= 3:
            return False

    # Cluster consonántico: primera debe ser coda válida
    for i in range(len(tokens) - 1):
        if tokens[i] in CONSONANTS and tokens[i+1] in CONSONANTS:
            if tokens[i] not in VALID_CODAS:
                return False

    # Último token
    last = tokens[-1]
    if last in CONSONANTS and last not in VALID_CODAS:
        return False

    return True


# =============================================================================
# GENERACIÓN
# =============================================================================

def build_syllable(pool_c: List[str], pool_v: List[str]) -> str:
    """Construye una sílaba C?V(C)? usando los pools dados."""
    onset = random.choice(pool_c) if random.random() > 0.15 else ""
    nucleus = random.choice(pool_v)
    coda = ""
    if random.random() > 0.5:
        candidate = random.choice(pool_c)
        if candidate in VALID_CODAS:
            coda = candidate
    return onset + nucleus + coda


def generate_word(pool_c: List[str], pool_v: List[str]) -> str:
    """Genera una palabra aleatoria de 1-3 sílabas (compacta)."""
    r = random.random()
    if r < 0.15:
        num_syllables = 1
    elif r < 0.65:
        num_syllables = 2
    else:
        num_syllables = 3

    return ''.join(build_syllable(pool_c, pool_v) for _ in range(num_syllables))


def score_word(word: str, original_fonemes: List[str]) -> float:
    """
    Puntúa una palabra candidata.
    - +5 por cada fonema del pool original usado
    - -20 por cada consonante repetida (penalización agresiva)
    - +2 si largo entre 5 y 8
    - +random(4) jitter para diversidad
    """
    score = 0.0
    tokens = tokenize(word)

    if len(word) <= 7:
        score += 3
    elif len(word) == 8:
        score += 1

    seen = set()
    for t in tokens:
        if t in original_fonemes:
            score += 5
        if t in CONSONANTS and t in seen:
            score -= 20
        seen.add(t)

    score += random.random() * 4
    return score


# =============================================================================
# PROSODIA Y DISPLAY
# =============================================================================

def format_prosody(word: str) -> dict:
    """Devuelve {syllabified, stressed_display, ipa_estimate}."""
    syls = syllabify(word)
    tonic = get_stressed_syllable_idx(syls)

    formatted = []
    for i, s in enumerate(syls):
        if i == tonic:
            # Marcar acento en la vocal de esta sílaba
            tokens = tokenize(s)
            accented = []
            for t in tokens:
                if t in ALL_VOWELS:
                    accented.append(ACCENT_MAP.get(t, t))
                else:
                    accented.append(t)
            formatted.append(''.join(accented))
        else:
            formatted.append(s)

    return {
        "syllabified": '.'.join(formatted),
        "stressed": syls[tonic] if tonic < len(syls) else syls[-1],
        "ipa_estimate": estimate_ipa(syls, tonic)
    }


def estimate_ipa(syllables: List[str], tonic_idx: int) -> str:
    """Estima IPA desde la ortografía Kalfírvach (inverso de clean_ipa)."""
    rev_map = {
        'th': 'θ', 'dh': 'ð', 'kh': 'x', 'gh': 'ɣ',
        'sh': 'ʃ', 'zh': 'ʒ', 'ch': 'tʃ', 'j': 'dʒ',
        'y': 'j', 'ā': 'aː', 'ē': 'eː', 'ī': 'iː',
        'ō': 'oː', 'ū': 'uː',
    }

    parts = []
    for i, syl in enumerate(syllables):
        s = syl
        for k, v in sorted(rev_map.items(), key=lambda x: -len(x[0])):
            s = s.replace(k, v)
        if i == tonic_idx and i < len(syllables):
            s = 'ˈ' + s
        parts.append(s)

    return '[' + '.'.join(parts) + ']'


# =============================================================================
# MOTOR PRINCIPAL
# =============================================================================

@dataclass
class ForjaResult:
    word: str
    score: float
    prosody: dict
    etymology: str


def forjar(ipa_inputs: List[str], concepto: str = "",
           num_candidates: int = 800, top_n: int = 5) -> List[ForjaResult]:
    """
    Ejecuta el motor de síntesis.
    
    Args:
        ipa_inputs: Lista de strings IPA (mín 2)
        concepto: Concepto/significado opcional
        num_candidates: Cuántos candidatos generar
        top_n: Cuántos devolver (ordenados por score)
    """
    if len(ipa_inputs) < 2:
        raise ValueError("Se necesitan al menos 2 raíces IPA")

    # Limpiar IPAs
    cleaned = []
    original_fonemes = []
    for ipa in ipa_inputs:
        ipa_clean = ipa.replace('/', '').replace('[', '').replace(']', '')
        c = clean_ipa(ipa_clean)
        t = tokenize(c)
        cleaned.append(c)
        original_fonemes.extend(t)

    # Construir pools de frecuencia
    freq_c = Counter(t for t in original_fonemes if t in CONSONANTS)
    freq_v = Counter(t for t in original_fonemes if t in ALL_VOWELS)

    pool_c = []
    for cons, count in freq_c.items():
        pool_c.extend([cons] * count)
    pool_v = []
    for vow, count in freq_v.items():
        pool_v.extend([vow] * count)

    # Fallbacks si el pool está vacío
    if not pool_c:
        pool_c = list(CONSONANTS)
    if not pool_v:
        pool_v = list(VOWELS)

    # Generar candidatos
    candidates = []
    for _ in range(num_candidates):
        w = generate_word(pool_c, pool_v)
        if is_valid_kalfirvach(w):
            candidates.append(w)

    # Únicos
    candidates = list(set(candidates))

    # Puntuar y ordenar
    candidates.sort(key=lambda w: score_word(w, original_fonemes), reverse=True)

    # Construir string de etimología
    # (los nombres de lenguas se pasan aparte, aquí solo registramos)
    etymology = f"- Concepto: '{concepto or '—'}'. "
    etymology += "Fonemas base: " + ', '.join(sorted(set(original_fonemes)))

    results = []
    for w in candidates[:top_n]:
        pros = format_prosody(w)
        sc = score_word(w, original_fonemes)
        results.append(ForjaResult(word=w, score=sc, prosody=pros, etymology=etymology))

    return results


# =============================================================================
# INTERFAZ INTERACTIVA
# =============================================================================

def print_banner():
    print("""
╔══════════════════════════════════════════════════╗
║       FORJA LÉXICA KALFÍRVACH v1.4              ║
║   Motor de Síntesis Fonotáctica — Terminal       ║
╚══════════════════════════════════════════════════╝
""")


def interactive_mode():
    print_banner()
    print("Ingresá las raíces IPA de las lenguas fuente.")
    print("(Mínimo 2, dejá vacío para saltar una lengua)")
    print()

    ipa_inputs = []
    lang_info = []

    for lang in LENGUAS:
        val = input(f"  {lang['nombre']:20s} IPA: ").strip()
        if val:
            ipa_inputs.append(val)
            lang_info.append((lang['nombre'], val))

    if len(ipa_inputs) < 2:
        print("\n✗ Se necesitan al menos 2 raíces IPA. Abortando.")
        return

    concepto = input("\n  Concepto / significado: ").strip()

    print()
    try:
        n_candidates = int(input("  Candidatos a generar [800]: ").strip() or "800")
    except ValueError:
        n_candidates = 800
    
    try:
        top_n = int(input("  Cuántos mostrar [5]: ").strip() or "5")
    except ValueError:
        top_n = 5

    batch_mode = False
    if len(ipa_inputs) >= 3:
        resp = input("\n  Modo batch (generar varias tandas)? [s/N]: ").strip().lower()
        batch_mode = resp == 's'

    print()
    print("=" * 60)
    print("  FORJANDO...")
    print("=" * 60)

    if batch_mode:
        batch_interactive(ipa_inputs, lang_info, concepto, n_candidates, top_n)
    else:
        single_forge(ipa_inputs, lang_info, concepto, n_candidates, top_n)


def single_forge(ipa_inputs, lang_info, concepto, n_candidates, top_n):
    print()

    # Mostrar log de procesamiento
    for nombre, ipa in lang_info:
        c = clean_ipa(ipa.replace('/', '').replace('[', '').replace(']', ''))
        tokens = tokenize(c)
        print(f"  > {nombre}: {ipa} → {c} → [{', '.join(tokens)}]")

    results = forjar(ipa_inputs, concepto, n_candidates, top_n)

    print()
    print("  ▸▸▸ RESULTADOS ◅◅◅")
    print()

    for i, r in enumerate(results, 1):
        print(f"  [{i}]  \033[1;35m{r.word}\033[0m  (score: {r.score:.1f})")
        print(f"       Silabeo:   {r.prosody['syllabified']}")
        print(f"       IPA estim: {r.prosody['ipa_estimate']}")
        print()

    # Mostrar etimología
    print(f"  Etimología: {r.etymology}")
    print()


def batch_interactive(ipa_inputs, lang_info, concepto, n_candidates, top_n):
    """Modo batch: genera múltiples tandas con distinta semilla."""
    print()
    print("  Batch: generando 5 tandas con distinta semilla...")
    print()

    all_words = []
    for batch_num in range(5):
        random.seed(random.randint(0, 2**32))
        results = forjar(ipa_inputs, concepto, n_candidates, top_n)
        for r in results:
            all_words.append((r.word, r.score, r.prosody))

    # Dedeuplicar y ordenar global
    seen = set()
    unique = []
    for w, s, p in all_words:
        if w not in seen:
            seen.add(w)
            unique.append((w, s, p))
    unique.sort(key=lambda x: -x[1])

    for i, (w, s, p) in enumerate(unique[:15], 1):
        print(f"  [{i:2d}]  \033[1;35m{w:12s}\033[0m  ─  {p['syllabified']:20s}  ─  {p['ipa_estimate']}")
    print()


# =============================================================================
# MODO JSON/BATCH (no interactivo)
# =============================================================================

def json_output(ipa_inputs: List[str], concepto: str = "",
                n_candidates: int = 800, top_n: int = 10) -> None:
    """Genera resultados como JSON."""
    results = forjar(ipa_inputs, concepto, n_candidates, top_n)
    output = []
    for r in results:
        output.append({
            "word": r.word,
            "score": round(r.score, 1),
            "syllabified": r.prosody.get("syllabified", ""),
            "ipa": r.prosody.get("ipa_estimate", ""),
        })
    print(json.dumps(output, indent=2, ensure_ascii=False))


def batch_loop(ipa_inputs: List[str], concepto: str = "",
               n_candidates: int = 800, top_n: int = 5,
               rounds: int = 10) -> None:
    """Modo batch silencioso: imprime resultados sin interacción."""
    random.seed()
    seen = set()
    for rnd in range(rounds):
        random.seed(random.randint(0, 2**32))
        results = forjar(ipa_inputs, concepto, n_candidates // 2, top_n)
        for r in results:
            if r.word not in seen:
                seen.add(r.word)
                print(
                    f"{r.word:12s} │ {r.prosody.get('syllabified',''):20s} │ "
                    f"{r.prosody.get('ipa_estimate',''):20s} │ {r.score:.1f}"
                )


# =============================================================================
# CLI
# =============================================================================

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Forja Léxica Kalfírvach — Motor de Síntesis Fonotáctica",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python3 forja_lexica_kfa.py
    → Modo interactivo: ingresás IPAs por teclado

  python3 forja_lexica_kfa.py --ipa "/t͡ʃʼoː.me/" "/ˈt͡ʃʼaː.miʕ/" --concepto "Libro"
    → Genera 5 candidatos y los muestra

  python3 forja_lexica_kfa.py --ipa "/t͡ʃʼoː.me/" "/ˈt͡ʃʼaː.miʕ/" --json
    → Salida en JSON

  python3 forja_lexica_kfa.py --ipa "/t͡ʃʼoː.me/" "/ˈt͡ʃʼaː.miʕ/" --batch --rounds 20
    → Batch: 20 tandas con distinta semilla
        """
    )
    parser.add_argument('--ipa', nargs='+', help='Raíces IPA (mín 2)')
    parser.add_argument('--concepto', default='', help='Concepto/significado')
    parser.add_argument('--candidates', type=int, default=800, help='Candidatos a generar (def 800)')
    parser.add_argument('--top', type=int, default=5, help='Cuántos mostrar (def 5)')
    parser.add_argument('--json', action='store_true', help='Salida en JSON')
    parser.add_argument('--batch', action='store_true', help='Modo batch')
    parser.add_argument('--rounds', type=int, default=10, help='Rondas en batch (def 10)')

    args = parser.parse_args()

    if args.ipa:
        if len(args.ipa) < 2:
            print("✗ Se necesitan al menos 2 raíces IPA")
            sys.exit(1)
        
        if args.json:
            json_output(args.ipa, args.concepto, args.candidates, args.top)
        elif args.batch:
            batch_loop(args.ipa, args.concepto, args.candidates, args.top, args.rounds)
        else:
            print_banner()
            print(f"  Concepto: {args.concepto or '—'}")
            print(f"  IPAs: {', '.join(args.ipa)}")
            print()
            results = forjar(args.ipa, args.concepto, args.candidates, args.top)
            for i, r in enumerate(results, 1):
                print(f"  [{i}]  \033[1;35m{r.word}\033[0m  (score: {r.score:.1f})")
                print(f"       Silabeo:   {r.prosody['syllabified']}")
                print(f"       IPA estim: {r.prosody['ipa_estimate']}")
                print()
            print(f"  {r.etymology}")
    else:
        interactive_mode()


if __name__ == '__main__':
    main()

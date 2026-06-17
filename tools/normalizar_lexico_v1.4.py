#!/usr/bin/env python3
"""
Fase 1: Normalización estructural del léxico Kalfírvach v1.3 → v1.4

Ejecuta:
  1.1 — Eliminar campo duplicado `forma_final` (canónico: `kalfirvach`)
  1.2 — Normalizar etiquetas de `origen.lengua` a nombres canónicos
  1.3 — Eliminar lenguas no permitidas
  1.4 — Generar reporte de cambios + lista de entradas que requieren Fase 2/3

Uso:
  python3 tools/normalizar_lexico_v1.4.py
"""

import json
import re
import shutil
import sys
from pathlib import Path
from collections import Counter, defaultdict

LEXICON_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v1.3.json"
BACKUP_PATH = LEXICON_PATH.with_suffix(".json.v1.3.bak")
OUTPUT_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v1.4.json"
REPORT_PATH = Path(__file__).parent.parent / "tools" / "reporte_normalizacion_v1.4.json"

# Normalización: entrada en minúscula (sin paréntesis) → nombre canónico
LANG_MAP = {
    "sanscrito": "Sánscrito Védico",
    "sánscrito": "Sánscrito Védico",
    "sánscrito védico": "Sánscrito Védico",
    "sánscrito tántrico": "Sánscrito Védico",
    "griego": "Griego Koiné",
    "griego koiné": "Griego Koiné",
    "avestan": "Persa Avéstico",
    "avéstico": "Persa Avéstico",
    "persa": "Persa Avéstico",
    "persa avéstico": "Persa Avéstico",
    "persa medio": "Persa Avéstico",
    "persa clásico": "Persa Avéstico",
    "árabe": "Árabe esotérico",
    "árabe esotérico": "Árabe esotérico",
    "arabe": "Árabe esotérico",
    "arabe esoterico": "Árabe esotérico",
    "egipcio": "Egipcio Demótico",
    "egipcio demótico": "Egipcio Demótico",
    "egipcio antiguo": "Egipcio Demótico",
    "copto": "Copto",
    "tibetano": "Tibetano Clásico",
    "tibetano clásico": "Tibetano Clásico",
    "pali": None,  # No permitida — se marca como no permitida
}

DISALLOWED = {"hebreo", "latin", "latín", "arameo", "acadio", "sumerio", "pie", "pali"}


def clean_language_label(raw: str) -> tuple[str | None, str | None]:
    """
    Limpia una etiqueta de lengua individual.
    Retorna (lengua_normalizada, nota_extraida) o (None, nota) si es inválida/descartada.
    """
    raw = raw.strip()
    if not raw or raw in ("—", "-", ""):
        return None, None

    # Extraer anotación parentética (ej: "árabe (ḥall → hal)" → lang="árabe", note="ḥall → hal")
    note = None
    m = re.match(r'^([^(]+?)\s*\((.+?)\)\s*$', raw)
    if m:
        raw = m.group(1).strip()
        note = m.group(2).strip()

    lower = raw.lower().strip()

    # Si es una lengua no permitida directamente
    if lower in DISALLOWED:
        return None, note

    # Normalizar
    normalized = LANG_MAP.get(lower)
    if normalized is not None:
        return normalized, note

    # Si tiene forma tipo "árabe (palabra → palabra)" pero no matchó el regex
    # o es algo no mapeado → registrar como desconocido
    return None, note


def split_languages(lengua_str: str) -> list[str]:
    """Divide el string de lenguas separado por /."""
    parts = re.split(r'\s*/\s*', lengua_str)
    return [p.strip() for p in parts if p.strip()]


def process_entry(entry: dict, cat_name: str, idx: int) -> dict:
    """
    Procesa una entrada individual. Retorna la entrada modificada.
    También acumula estadísticas.
    """
    changes = []
    warnings = []

    # 1.1 Eliminar forma_final
    if "forma_final" in entry:
        old_val = entry.pop("forma_final")
        if old_val != entry.get("kalfirvach", ""):
            warnings.append(f"forma_final ('{old_val}') ≠ kalfirvach ('{entry.get('kalfirvach', '')}')")
        changes.append("forma_final eliminado")

    # Asegurar que kalfirvach existe
    if "kalfirvach" not in entry or not entry["kalfirvach"]:
        changes.append("⚠️ SIN KALFIRVACH — pendiente de revisión")

    # 1.2 + 1.3 Normalizar lenguas
    origen = entry.get("origen", {})
    if not isinstance(origen, dict):
        entry["origen"] = {"lengua": "", "raiz_original": "", "corpus": ""}
        origen = entry["origen"]
        changes.append("origen reconstruido (no era dict)")

    lengua_raw = origen.get("lengua", "")
    if not lengua_raw or lengua_raw.strip() in ("—", "-", ""):
        changes.append("origen.lengua vacío — pendiente de revisión")
        origen["lengua"] = ""
        return entry

    # Dividir lenguas
    raw_langs = split_languages(lengua_raw)
    normalized_langs = []
    extracted_notes = []

    for rl in raw_langs:
        lang, note = clean_language_label(rl)
        if lang is not None:
            normalized_langs.append(lang)
        if note:
            extracted_notes.append(note)

    # Guardar notas extraídas en transformacion si hay
    if extracted_notes:
        if "transformacion" not in entry:
            entry["transformacion"] = []
        if not isinstance(entry["transformacion"], list):
            entry["transformacion"] = [str(entry["transformacion"])]
        for note in extracted_notes:
            entry["transformacion"].append(f"(nota extraída de origen.lengua: {note})")
        changes.append(f"notas extraídas de origen.lengua: {extracted_notes}")

    # Detectar cambios
    if normalized_langs != raw_langs:
        changes.append("origen.lengua normalizado")

    # Unir lenguas normalizadas
    origen["lengua"] = " / ".join(normalized_langs) if normalized_langs else ""

    # Detectar entrada que requiere Fase 3
    if len(normalized_langs) == 0:
        changes.append("🔴 FASE 3: 0 lenguas válidas después de limpieza")
    elif len(normalized_langs) == 1:
        changes.append("🟡 FASE 3: 1 sola lengua válida")
    elif len(normalized_langs) == 2:
        # Verificar que no sea Skt + otra (50% >40%)
        if "Sánscrito Védico" in normalized_langs:
            changes.append("🟡 REQUIERE VERIFICACIÓN: 2 lenguas con Sánscrito (50%)")

    # Detectar corpus vacío
    corpus = origen.get("corpus", "")
    if not corpus or corpus.strip() == "":
        changes.append("🟡 FASE 2: corpus vacío")

    # Detectar raíces placeholder
    raiz = origen.get("raiz_original", "")
    if not raiz or raiz.strip() == "" or re.search(r'\(ra[ií]z', raiz, re.IGNORECASE):
        changes.append("🔴 FASE 2: raíz placeholder o vacía")

    return entry


def main():
    print("=" * 60)
    print("Fase 1 — Normalización estructural del léxico")
    print("=" * 60)

    # ── Backup ──
    if not BACKUP_PATH.exists():
        shutil.copy2(LEXICON_PATH, BACKUP_PATH)
        print(f"✅ Backup creado: {BACKUP_PATH}")
    else:
        print(f"ℹ️  Backup ya existe: {BACKUP_PATH}")

    # ── Cargar ──
    with open(LEXICON_PATH, "r", encoding="utf-8") as f:
        lexicon = json.load(f)

    data = lexicon.get("kalfirvach_lexicon_v1.3", lexicon)
    cats = data.get("categorias", {})

    total_entries = 0
    category_stats = {}
    global_stats = Counter()
    fase2_entries = []   # entries that need Phase 2 (corpus/roots)
    fase3_entries = []   # entries that need Phase 3 (reformulation)
    all_changes = []

    # ── Procesar cada categoría ──
    for cat_name in sorted(cats.keys()):
        cat = cats[cat_name]
        entries = cat.get("entradas", [])
        cat_changes = []
        cat_fase2 = 0
        cat_fase3 = 0

        new_entries = []
        for idx, entry in enumerate(entries):
            proc_entry = process_entry(entry, cat_name, idx)
            new_entries.append(proc_entry)

            entry_changes = []
            if "forma_final" not in proc_entry:
                entry_changes.append("1.1 forma_final eliminado")

            origen = proc_entry.get("origen", {})
            if isinstance(origen, dict):
                langs = origen.get("lengua", "")
                num_langs = len(split_languages(langs))
                if num_langs == 0:
                    cat_fase3 += 1
                    entry_changes.append("🔴 FASE 3: 0 lenguas válidas")
                    fase3_entries.append({
                        "categoria": cat_name,
                        "concepto": proc_entry.get("concepto", "?"),
                        "kalfirvach": proc_entry.get("kalfirvach", "?"),
                        "razon": "0 lenguas válidas después de limpieza"
                    })
                elif num_langs == 1:
                    cat_fase3 += 1
                    entry_changes.append("🟡 FASE 3: 1 sola lengua válida")
                    fase3_entries.append({
                        "categoria": cat_name,
                        "concepto": proc_entry.get("concepto", "?"),
                        "kalfirvach": proc_entry.get("kalfirvach", "?"),
                        "razon": f"1 sola lengua válida: {langs}"
                    })
                elif num_langs >= 2 and "Sánscrito Védico" in langs:
                    if num_langs == 2:
                        cat_fase3 += 1
                        entry_changes.append("🟡 FASE 3: 2 lenguas con Skt (50% > 40%)")
                        fase3_entries.append({
                            "categoria": cat_name,
                            "concepto": proc_entry.get("concepto", "?"),
                            "kalfirvach": proc_entry.get("kalfirvach", "?"),
                            "razon": f"Skt + 1 otra lengua = 50% (excede 40%): {langs}"
                        })

                corpus = origen.get("corpus", "")
                if not corpus or corpus.strip() == "":
                    cat_fase2 += 1
                    fase2_entries.append({
                        "categoria": cat_name,
                        "concepto": proc_entry.get("concepto", "?"),
                        "kalfirvach": proc_entry.get("kalfirvach", "?"),
                        "razon": "corpus vacío"
                    })

                raiz = origen.get("raiz_original", "")
                if not raiz or raiz.strip() == "" or re.search(r'\(ra[ií]z', raiz, re.IGNORECASE):
                    if not any(e["kalfirvach"] == proc_entry.get("kalfirvach", "") and e["razon"] == "raíz placeholder o vacía" for e in fase2_entries):
                        fase2_entries.append({
                            "categoria": cat_name,
                            "concepto": proc_entry.get("concepto", "?"),
                            "kalfirvach": proc_entry.get("kalfirvach", "?"),
                            "razon": "raíz placeholder o vacía"
                        })
                    cat_fase2 += 1

            if entry_changes:
                cat_changes.extend(entry_changes)

        cat["entradas"] = new_entries
        total_entries += len(new_entries)
        category_stats[cat_name] = {
            "total": len(new_entries),
            "fase2": cat_fase2,
            "fase3": cat_fase3,
        }
        if cat_changes:
            all_changes.append(f"  {cat_name}: {len(new_entries)} entries — {len(cat_changes)} cambios")

    # ── Actualizar metadata ──
    data["metadata"]["version"] = "1.4"
    data["metadata"]["date_generated"] = "2026-06-16"
    data["metadata"]["normalized"] = True

    # ── Guardar JSON normalizado ──
    # Preservar la estructura exacta
    output_data = lexicon if "kalfirvach_lexicon_v1.3" in lexicon else data
    if "kalfirvach_lexicon_v1.3" in lexicon:
        lexicon["kalfirvach_lexicon_v1.3"] = data
    else:
        output_data = data

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ JSON normalizado guardado: {OUTPUT_PATH}")

    # ── Reporte ──
    # Unificar Fase 2: deduplicar entradas que aparecen por múltiples razones
    fase2_dedup = {}
    for e in fase2_entries:
        key = e["kalfirvach"]
        if key in fase2_dedup:
            fase2_dedup[key]["razones"].append(e["razon"])
        else:
            fase2_dedup[key] = {
                "categoria": e["categoria"],
                "concepto": e["concepto"],
                "kalfirvach": key,
                "razones": [e["razon"]]
            }

    fase3_dedup = {}
    for e in fase3_entries:
        key = e["kalfirvach"]
        if key in fase3_dedup:
            fase3_dedup[key]["razones"].append(e["razon"])
        else:
            fase3_dedup[key] = {
                "categoria": e["categoria"],
                "concepto": e["concepto"],
                "kalfirvach": key,
                "razones": [e["razon"]]
            }

    report = {
        "version_plan": "1.0",
        "fase": "1",
        "fecha": "2026-06-16",
        "resumen": {
            "total_entries": total_entries,
            "categorias": len(cats),
            "fase2_corpus_y_raices": len(fase2_dedup),
            "fase3_reformulacion": len(fase3_dedup),
        },
        "por_categoria": category_stats,
        "fase2_entries": list(fase2_dedup.values()),
        "fase3_entries": list(fase3_dedup.values()),
    }

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"✅ Reporte guardado: {REPORT_PATH}")

    # ── Resumen en pantalla ──
    print("\n" + "=" * 60)
    print("RESUMEN DE NORMALIZACIÓN")
    print("=" * 60)
    print(f"\n📊 Total entradas procesadas: {total_entries}")
    print(f"📂 Categorías: {len(cats)}")
    print(f"\n🔧 Fase 2 (rellenar corpus/raíces): {len(fase2_dedup)} entradas")
    print(f"🔧 Fase 3 (reformular): {len(fase3_dedup)} entradas")
    print(f"\n📁 JSON: {OUTPUT_PATH}")
    print(f"📁 Reporte: {REPORT_PATH}")
    print(f"📁 Backup: {BACKUP_PATH}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Convert Kalfirvach lexicon v1.0 from JSON to Markdown."""

import json, sys, os
from pathlib import Path

BASE = Path(__file__).parent
JSON_PATH = BASE / "kalfirvach_lexicon_v1.0.json"
MD_PATH = BASE / "lexicon_v1.0.md"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

root = data.get("kalfirvach_lexicon_v1.0", data)
meta = root.get("metadata", {})
cats = root.get("categorias", {})

lines = []
lines.append("# Léxico Kalfírvach v1.0")
lines.append("")
lines.append(f"**Versión**: {meta.get('version', '?')}")
lines.append(f"**Entradas**: {meta.get('total_entries', '?')}")
lines.append(f"**Generado**: {meta.get('date_generated', '?')}")
lines.append(f"**Lenguas fuente**: {', '.join(meta.get('languages', []))}")
lines.append(f"**Sistema de escritura**: {meta.get('writing_system', '?')}")
lines.append("")

TITLE_OVERRIDES = {
    "pronombres_y_deicticos": "Pronombres y Deícticos",
    "numeros": "Números",
    "dimensiones_y_adjetivos": "Dimensiones y Adjetivos",
    "personas_y_parentesco": "Personas y Parentesco",
    "animales": "Animales",
    "seres_vivos_plantas": "Seres Vivos — Plantas",
    "anatomia_y_cuerpo": "Anatomía y Cuerpo",
}

cat_order = [
    "pronombres_y_deicticos",
    "numeros",
    "dimensiones_y_adjetivos",
    "personas_y_parentesco",
    "animales",
    "seres_vivos_plantas",
    "anatomia_y_cuerpo",
]
for key in cats:
    if key not in cat_order:
        cat_order.append(key)

for cat_key in cat_order:
    if cat_key not in cats:
        continue
    cat = cats[cat_key]
    title = TITLE_OVERRIDES.get(cat_key, cat_key.replace("_", " ").title())
    desc = cat.get("descripcion", "")
    entries = cat.get("entradas", [])

    lines.append(f"## {title}")
    if desc:
        lines.append("")
        lines.append(f"_{desc}_")
    lines.append("")

    for e in entries:
        conc = e.get("concepto", "?")
        form = e.get("forma_final", "?")
        ipa = e.get("ipa", None)
        origen = e.get("origen", {})
        transf = e.get("transformacion", [])
        deriv = e.get("derivaciones", [])
        notas = e.get("notas", None)

        lines.append(f"### {form}")
        lines.append("")
        lines.append(f"- **Concepto**: {conc}")
        if ipa:
            lines.append(f"- **IPA**: {ipa}")
        lines.append("")
        lines.append("#### Origen")
        lines.append("")
        lines.append(f"- **Lengua**: {origen.get('lengua', '?')}")
        lines.append(f"- **Raíz original**: {origen.get('raiz_original', '?')}")
        corpus = origen.get("corpus", "")
        if corpus:
            lines.append(f"- **Corpus**: {corpus}")

        if transf and len(transf) > 0:
            lines.append("")
            lines.append("#### Transformación")
            lines.append("")
            for t in transf:
                if isinstance(t, str):
                    lines.append(f"- {t}")
                elif isinstance(t, dict):
                    lines.append(f"- {t.get('tipo', '')}: {t.get('descripcion', '')}")

        if isinstance(deriv, list) and len(deriv) > 0:
            lines.append("")
            lines.append("#### Derivaciones")
            lines.append("")
            for d in deriv:
                if isinstance(d, str):
                    lines.append(f"- {d}")
                elif isinstance(d, dict):
                    lines.append(f"- {d.get('forma', '?')} = {d.get('concepto', '?')}")
        elif isinstance(deriv, str) and deriv.strip():
            lines.append("")
            lines.append("#### Derivaciones")
            lines.append("")
            lines.append(f"- {deriv}")

        if notas:
            lines.append("")
            lines.append("#### Notas")
            lines.append("")
            lines.append(notas)

        lines.append("")
        lines.append("---")
        lines.append("")

content = "\n".join(lines)

with open(MD_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Markdown generado: {MD_PATH}")
print(f"   Categorías: {len(cat_order)}")
total_entries = sum(len(cats[k].get("entradas", [])) for k in cat_order if k in cats)
print(f"   Entradas: {total_entries}")

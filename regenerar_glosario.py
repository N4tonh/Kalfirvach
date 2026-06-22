#!/usr/bin/env python3
"""Regenera glosario_v1.5.md desde kalfirvach_lexicon_v1.5.json"""

import json
from datetime import date

BASE = '/var/home/anomxsst17/Escritorio/Kalfirvach_v1.3'

with open(f'{BASE}/kalfirvach_lexicon_v1.5.json') as f:
    data = json.load(f)

lx = data['kalfirvach_lexicon_v1.5']
cats = lx['categorias']
meta = lx['metadata']

total_entries = sum(len(c['entradas']) for c in cats.values())

# Category name display formatting
CATEGORY_LABELS = {
    "pronombres_y_deicticos": "Pronombres y Deícticos",
    "verbos_basicos": "Verbos Básicos",
    "sustantivos_cotidianos": "Sustantivos Cotidianos",
    "numeros": "Números",
    "tiempo_domestico": "Tiempo Doméstico",
    "naturaleza_y_elementos": "Naturaleza y Elementos",
    "anatomia_y_cuerpo": "Anatomía y Cuerpo",
    "comida_y_cocina": "Comida y Cocina",
    "vivienda_y_arquitectura": "Vivienda y Arquitectura",
    "personas_y_parentesco": "Personas y Parentesco",
    "emociones_y_estados_afectivos": "Emociones y Estados Afectivos",
    "dimensiones_y_adjetivos": "Dimensiones y Adjetivos",
    "conceptos_espaciales_y_calidades": "Conceptos Espaciales y Cualidades",
    "conjunciones_y_particulas": "Conjunciones y Partículas",
    "interjecciones_y_exclamaciones": "Interjecciones y Exclamaciones",
    "actitudinales": "Actitudinales",
    "profesiones_y_roles": "Profesiones y Roles",
    "magia_y_mitologia": "Magia y Mitología",
    "tecnologia": "Tecnología",
    "biologia_y_micologia": "Biología y Micología",
    "animales": "Animales",
    "seres_vivos_plantas": "Seres Vivos y Plantas",
    "medicina_y_salud": "Medicina y Salud",
    "gobierno_politica_derecho": "Gobierno, Política y Derecho",
    "onomastica": "Onomástica",
}

lines = []
lines.append("# Léxico Kalfírvach v1.5")
lines.append("")
lines.append(f"**Versión**: 1.5")
lines.append(f"**Entradas**: {total_entries}")
lines.append(f"**Generado**: {date.today().isoformat()}")
lines.append("**Lenguas fuente**: Griego, Sanscrito, Avestan, Persa, Tibetano, Arabe, Egipcio")
lines.append("**Sistema de escritura**: Alfabeto griego politonico con arcaicas")
lines.append("")

CATEGORY_ORDER = sorted(cats.keys(), key=lambda k: (
    # Custom sort order
    {"pronombres_y_deicticos": 0,
     "verbos_basicos": 1,
     "numeros": 2,
     "conjunciones_y_particulas": 3,
     "interjecciones_y_exclamaciones": 4,
     "dimensiones_y_adjetivos": 5,
     "conceptos_espaciales_y_calidades": 6,
     "actitudinales": 7,
     "tiempo_domestico": 8,
     "personas_y_parentesco": 9,
     "profesiones_y_roles": 10,
     "anatomia_y_cuerpo": 11,
     "comida_y_cocina": 12,
     "vivienda_y_arquitectura": 13,
     "naturaleza_y_elementos": 14,
     "animales": 15,
     "seres_vivos_plantas": 16,
     "biologia_y_micologia": 17,
     "medicina_y_salud": 18,
     "emociones_y_estados_afectivos": 19,
     "gobierno_politica_derecho": 20,
     "tecnologia": 21,
     "magia_y_mitologia": 22,
     "onomastica": 23,
    }.get(k, 99), k)
)

for cat_name in CATEGORY_ORDER:
    cat = cats[cat_name]
    label = CATEGORY_LABELS.get(cat_name, cat_name.replace("_", " ").title())
    desc = cat.get("descripcion", "")
    
    lines.append(f"## {label}")
    lines.append("")
    if desc:
        lines.append(f"_{desc}_")
        lines.append("")
    
    entries = cat["entradas"]
    
    for i, e in enumerate(entries):
        word = e["kalfirvach"]
        concepto = e.get("concepto", "")
        ipa = e.get("ipa", "")
        origen = e.get("origen", {})
        trans = e.get("transformacion", [])
        derivs = e.get("derivaciones", [])
        
        lines.append(f"### {word}")
        lines.append("")
        if concepto:
            lines.append(f"- **Concepto**: {concepto}")
        if ipa:
            lines.append(f"- **IPA**: {ipa}")
        lines.append("")
        
        # Origen section (defensive: handle both dict and string)
        if isinstance(origen, dict):
            lengua = origen.get("lengua", "")
            raiz = origen.get("raiz_original", "")
            corpus = origen.get("corpus", "")
        else:
            lengua = str(origen)
            raiz = str(origen)
            corpus = ""
        
        if lengua or raiz or corpus:
            lines.append(f"#### Origen")
            lines.append("")
            if lengua:
                lines.append(f"- **Lengua**: {lengua}")
            if raiz:
                lines.append(f"- **Raíz original**: {raiz}")
            if corpus:
                lines.append(f"- **Corpus**: {corpus}")
            lines.append("")
        
        # Transformacion section
        if trans and len(trans) > 0 and all(t.strip() for t in trans):
            lines.append(f"#### Transformación")
            lines.append("")
            for t in trans:
                lines.append(f"- {t.strip()}")
            lines.append("")
        
        # Derivaciones section
        if derivs and len(derivs) > 0:
            lines.append(f"#### Derivaciones")
            lines.append("")
            for d in derivs:
                lines.append(f"- {d.strip()}")
            lines.append("")
        
        # Separator between entries
        lines.append("---")
        lines.append("")

output = "\n".join(lines).rstrip() + "\n"

with open(f'{BASE}/glosario_v1.5.md', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"✅ glosario_v1.5.md regenerado — {total_entries} entradas, {len(cats)} categorías")
print(f"   Archivo: {len(output)} caracteres, {output.count(chr(10))} líneas")

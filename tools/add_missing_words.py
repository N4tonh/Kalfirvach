#!/usr/bin/env python3
import json, shutil
from pathlib import Path

LEXICON_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v0.4_wip.json"
BACKUP_PATH = LEXICON_PATH.with_suffix(".json.bak2")

WORDS = [
    # (word, category, concepto, pos)
    ("nur", "naturaleza_y_elementos", "luz, claridad, iluminación", "noun"),
    ("ich", "verbos_basicos", "querer, desear, anhelar", "verb"),
    ("dun", "verbos_basicos", "dar, ofrecer, entregar", "verb"),
    ("bhrat", "personas_y_parentesco", "portador, cargador, sustentador", "noun"),
    ("shakti", "conceptos_espaciales_y_calidades", "poder, fuerza, energía dinámica", "noun"),
    ("maya", "conceptos_espaciales_y_calidades", "ilusión, apariencia, manifestación fenoménica", "noun"),
    ("heka", "magia_y_mitologia", "magia, heka, poder mágico primordial", "noun"),
    ("nukh", "conceptos_espaciales_y_calidades", "sabiduría, conocimiento esotérico", "noun"),
    ("thele", "conceptos_espaciales_y_calidades", "voluntad, intención consciente", "noun"),
    ("thes", "conceptos_espaciales_y_calidades", "acto de voluntad, acción volitiva", "noun"),
    ("sadh", "magia_y_mitologia", "práctica espiritual, realización, sadhana", "noun"),
    ("yog", "magia_y_mitologia", "unión, integración, yoga", "noun"),
    ("rat", "verbos_basicos", "brillar, resplandecer, irradiar", "verb"),
    ("chal", "verbos_basicos", "moverse, desplazarse, andar", "verb"),
    ("mar", "verbos_basicos", "morir, extinguirse, cesar", "verb"),
    ("rit", "conceptos_espaciales_y_calidades", "orden cósmico, ciclo, rita", "noun"),
    ("manas", "conceptos_espaciales_y_calidades", "mente, psique, facultad mental", "noun"),
    ("nava", "verbos_basicos", "navegar, cruzar aguas, atravesar", "verb"),
]

def main():
    shutil.copy2(LEXICON_PATH, BACKUP_PATH)
    print(f"Backup: {BACKUP_PATH}")

    with open(LEXICON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    v02 = data["kalfirvach_lexicon_v0.2"]
    cats = v02["categorias"]

    added = 0
    for word, cat_name, concepto, pos in WORDS:
        if cat_name not in cats:
            print(f"  WARN: category '{cat_name}' not found, skipping {word}")
            continue
        cat_data = cats[cat_name]
        entries = cat_data.get("entradas", [])

        existing = any(
            (e.get("kalfirvach") or e.get("forma_final") or "").strip() == word
            for e in entries if isinstance(e, dict)
        )
        if existing:
            print(f"  SKIP: {word} already exists in {cat_name}")
            continue

        entry = {
            "concepto": concepto,
            "kalfirvach": word,
            "forma_final": word,
            "pos": pos,
            "origen": {
                "lengua": "",
                "raiz_original": "",
                "corpus": ""
            },
            "transformacion": [],
            "derivaciones": []
        }
        entries.append(entry)
        added += 1
        print(f"  ADDED: {word} → {cat_name} ({concepto})")

    with open(LEXICON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nTotal added: {added}")

if __name__ == "__main__":
    main()

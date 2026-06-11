#!/usr/bin/env python3
import json, shutil
from pathlib import Path

LEXICON_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v0.4_wip.json"
BACKUP_PATH = LEXICON_PATH.with_suffix(".json.bak.time")

TERMS = [
    {
        "kalfirvach": "sahar",
        "concepto": "madrugada, antes del alba, pre-amanecer",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "سحر (saḥar) 'madrugada, antes del alba' / سحر (sahar) 'amanecer, alba'",
            "corpus": "Corpus coránico (saḥar como tiempo de oración) / Poesía persa (sahar como tiempo místico)"
        },
        "transformacion": ["saḥar → sahar (ḥ → h)", "sahar → sahar (adopción directa) — convergencia panoriental"]
    },
    {
        "kalfirvach": "fajr",
        "concepto": "alba, amanecer, aurora, primera luz del día",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "فجر (fajr) 'alba, amanecer' / سحر (sahar) 'amanecer, alba'",
            "corpus": "Corpus coránico (fajr como tiempo de oración) / Poesía mística persa"
        },
        "transformacion": ["fajr → fajr (adopción directa, CVCC válido)", "sahar → sahr → fajr (convergencia, cambio s→f por énfasis)"]
    },
    {
        "kalfirvach": "shuruk",
        "concepto": "orto, salida del sol, sol naciente",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Griego",
            "raiz_original": "شروق (šurūq) 'salida del sol' / ἀνατολή (anatolē) 'salida del sol, este'",
            "corpus": "Textos astronómicos árabes / Textos de navegación griegos"
        },
        "transformacion": ["šurūq → shurūq → shuruk (š→sh, acortamiento ū→u)", "ἀνατολή → anatolē → anatol → shuruk (convergencia)"]
    },
    {
        "kalfirvach": "duha",
        "concepto": "media mañana, mañana avanzada, horas de luz plena",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Sanscrito",
            "raiz_original": "ضحى (ḍuḥā) 'media mañana, luz matinal' / दिवा (divā) 'de día, durante el día'",
            "corpus": "Corpus coránico (ḍuḥā como juramento) / Ṛgveda (divā)"
        },
        "transformacion": ["ḍuḥā → duha (ḍ→d, ḥ→h, ā→a)", "divā → diva → duha (convergencia vocálica)"]
    },
    {
        "kalfirvach": "ghurub",
        "concepto": "ocaso, puesta del sol, sol poniente, atardecer",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Griego",
            "raiz_original": "غروب (ghurūb) 'puesta del sol' / δυσμή (dysmē) 'ocaso, poniente'",
            "corpus": "Textos astronómicos árabes / Textos de navegación griegos"
        },
        "transformacion": ["ghurūb → ghurub (acortamiento ū→u)", "δυσμή → dysmē → dismē → ghurub (convergencia)"]
    },
    {
        "kalfirvach": "shafak",
        "concepto": "crepúsculo, anochecer, penumbra vespertina",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Griego",
            "raiz_original": "شفق (šafaq) 'crepúsculo, anochecer' / λυκόφως (lykophōs) 'crepúsculo, media luz'",
            "corpus": "Textos astronómicos árabes / PGM (crepúsculo como tiempo liminal)"
        },
        "transformacion": ["šafaq → shafaq → shafak (š→sh, q→k en coda)", "λυκόφως → lykophōs → lykofos → shafak (convergencia)"]
    },
    {
        "kalfirvach": "ghasak",
        "concepto": "oscuridad nocturna, tinieblas, noche cerrada",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Sanscrito",
            "raiz_original": "غسق (ġasaq) 'oscuridad de la noche' / अन्धकार (andhakāra) 'oscuridad, tinieblas'",
            "corpus": "Corpus coránico (ġasaq como tinieblas) / Upaniṣads (tamas, andhakāra)"
        },
        "transformacion": ["ġasaq → ghasaq → ghasak (ġ→gh, q→k en coda)", "andhakāra → andhak → ghasak (convergencia, metátesis)"]
    },
]


def main():
    if not LEXICON_PATH.exists():
        print(f"ERROR: no se encuentra {LEXICON_PATH}")
        return

    shutil.copy2(LEXICON_PATH, BACKUP_PATH)
    print(f"Backup: {BACKUP_PATH}")

    with open(LEXICON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    v02 = data["kalfirvach_lexicon_v0.2"]
    cats = v02["categorias"]
    target = "tiempo_domestico"

    cat_data = cats[target]
    entries = cat_data.setdefault("entradas", [])

    added = 0
    for t in TERMS:
        w = t["kalfirvach"]
        if any((e.get("kalfirvach") or e.get("forma_final") or "").strip() == w for e in entries if isinstance(e, dict)):
            print(f"  SKIP: {w} ya existe")
            continue
        entries.append({
            "kalfirvach": t["kalfirvach"],
            "forma_final": t["kalfirvach"],
            "concepto": t["concepto"],
            "pos": t["pos"],
            "origen": t["origen"],
            "transformacion": t["transformacion"],
            "derivaciones": []
        })
        added += 1
        print(f"  ADDED: {t['kalfirvach']} — {t['concepto']}")

    with open(LEXICON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    skt = sum(1 for t in TERMS if "Sanscrito" in t["origen"]["lengua"])
    total = len(TERMS)
    print(f"\n→ Agregados: {added} | Categoría: {target}")
    print(f"  {total} términos de partes del día | Sánscrito: {skt}/{total} ({100*skt//total}%)")


if __name__ == "__main__":
    main()

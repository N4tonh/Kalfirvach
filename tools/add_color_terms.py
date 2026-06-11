#!/usr/bin/env python3
import json, shutil
from pathlib import Path

LEXICON_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v0.4_wip.json"
BACKUP_PATH = LEXICON_PATH.with_suffix(".json.bak3")

COLORS = [
    {
        "kalfirvach": "shwet",
        "concepto": "blanco, claro, puro",
        "pos": "adjective",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "श्वेत (śveta) 'blanco' / 𐬯𐬞𐬀𐬈𐬙𐬀 (spaeta) 'blanco'",
            "corpus": "Ṛgveda, Upaniṣads / Avesta (Vendidad)"
        },
        "transformacion": ["śveta→shveta (ś→sh por adaptación fonémica §5.2)", "shveta→shwet (elisión de -a final)", "spaeta→speta→shwet (asibilación s→sh por convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "kris",
        "concepto": "negro, oscuro, tenebroso",
        "pos": "adjective",
        "origen": {
            "lengua": "Griego/Sanscrito",
            "raiz_original": "κρῑμα (krīma) 'oscuridad' / कृष्ण (kṛṣṇa) 'negro'",
            "corpus": "Corpus Hermeticum, PGM / Mahābhārata, Purāṇas"
        },
        "transformacion": ["kṛṣṇa→krishna→kris (elisión de -na, simplificación -shn-→-s)", "krīma→kris (elisión de -ma, acortamiento vocálico por influencia sánscrita)"]
    },
    {
        "kalfirvach": "rohik",
        "concepto": "rojo, escarlata, bermellón",
        "pos": "adjective",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "रोहित (rohita) 'rojo' / 𐬭𐬀𐬊𐬜𐬌𐬙𐬀 (raoδita) 'rojo'",
            "corpus": "Ṛgveda, Brāhmaṇas / Avesta (Yashts)"
        },
        "transformacion": ["rohita→rohit→rohik (elisión de -a, ensordecimiento t→k por fonotáctica §3.3)", "raoδita→rodita→rohit (δ→d, convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "nil",
        "concepto": "azul, añil, índigo",
        "pos": "adjective",
        "origen": {
            "lengua": "Sanscrito/Persa/Arabe",
            "raiz_original": "नील (nīla) 'azul' / نیل (nil) 'azul' / نيل (nīl) 'índigo'",
            "corpus": "Ṛgveda / Poesía sufí / Textos de alquimia"
        },
        "transformacion": ["nīla→nil (pérdida de -a final, acortamiento vocálico por influencia persa)", "nil — convergente en las 3 lenguas, forma panetimológica"]
    },
    {
        "kalfirvach": "herit",
        "concepto": "verde, vegetal, viridiano",
        "pos": "adjective",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "हरित (harita) 'verde' / 𐬰𐬀𐬌𐬭𐬌 (zairi) 'amarillo, verde'",
            "corpus": "Ṛgveda / Avesta (Gathas)"
        },
        "transformacion": ["harita→harit→herit (elisión de -a, apertura a→e por influencia avéstica)", "zairi→heri (pérdida de z-, convergencia con harit)"]
    },
    {
        "kalfirvach": "sofar",
        "concepto": "amarillo, dorado, áureo",
        "pos": "adjective",
        "origen": {
            "lengua": "Arabe/Griego",
            "raiz_original": "صفر (ṣafr) 'amarillo' / χλωρός (khlōrós) 'verde claro, amarillo'",
            "corpus": "Textos de alquimia / Corpus Hippocraticum, PGM"
        },
        "transformacion": ["ṣafr→safar→sofar (armonía vocálica)", "khlōrós→kloros→so- (pérdida de kh-, convergencia con la forma árabe)"]
    },
    {
        "kalfirvach": "tamir",
        "concepto": "marrón, pardo, castaño",
        "pos": "adjective",
        "origen": {
            "lengua": "Arabe/Sanscrito",
            "raiz_original": "تمر (tamr) 'dátil, marrón' / ताम्र (tāmra) 'cobre, rojizo'",
            "corpus": "Poesía preislámica / Atharvaveda"
        },
        "transformacion": ["tamr→tamir (vocalización epentética por estructura silábica (C)GVC)", "tāmra→tamir (acortamiento ā→a, convergencia con el árabe)"]
    },
    {
        "kalfirvach": "narin",
        "concepto": "naranja, anaranjado, azafranado",
        "pos": "adjective",
        "origen": {
            "lengua": "Persa/Sanscrito/Arabe",
            "raiz_original": "نارنج (nārenj) 'naranja' / नारङ्ग (nāraṅga) 'naranjo' / نارنج (nāranj)",
            "corpus": "Textos médicos persas / Suśruta Saṃhitā / Farmacopea árabe"
        },
        "transformacion": ["nārenj→naren→narin (cluster final simplificado, acortamiento vocálico)", "Convergencia completas en las 3 lenguas iranias"]
    },
    {
        "kalfirvach": "ward",
        "concepto": "rosa, rosado, rosáceo",
        "pos": "adjective",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "ورد (ward) 'rosa, color rosa' / ورد (ward) 'rosa'",
            "corpus": "Poesía preislámica / Poesía mística persa (Rūmī, Hāfez)"
        },
        "transformacion": ["ward — sin cambios fonotácticos (CVC válida)", "Convergencia completa árabe-persa: misma raíz trilitera w-r-d"]
    },
    {
        "kalfirvach": "palin",
        "concepto": "gris, ceniciento, plomizo",
        "pos": "adjective",
        "origen": {
            "lengua": "Griego/Sanscrito",
            "raiz_original": "πολιός (poliós) 'gris' / पलित (palita) 'gris, canoso'",
            "corpus": "Corpus Hippocraticum / Ṛgveda"
        },
        "transformacion": ["poliós→poli→polin (pérdida de -ós, adición de -n por convergencia con sánscrito)", "palita→palit→palin (elisión de -a, asimilación t→n por influencia griega)"]
    },
    {
        "kalfirvach": "forfir",
        "concepto": "púrpura, violeta, magenta",
        "pos": "adjective",
        "origen": {
            "lengua": "Griego/Arabe",
            "raiz_original": "πορφύρα (porphýra) 'púrpura real' / أرجوان (ʾurjuwān) 'púrpura'",
            "corpus": "PGM, textos alquímicos / Textos de tintorería"
        },
        "transformacion": ["porphýra→porfir→forfir (disimilación p→f por influencia árabe)", "ʾurjuwān→urjuf→urf→forfir (pérdida de vocal inicial, convergencia con el griego)"]
    },
    {
        "kalfirvach": "sarn",
        "concepto": "dorado, áureo, reluciente como el oro",
        "pos": "adjective",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "स्वर्ण (svarṇa) 'oro' / 𐬰𐬀𐬭𐬀𐬥𐬀 (zarana) 'oro, dorado'",
            "corpus": "Ṛgveda (Hiraṇyagarbha) / Avesta (Yasht 5)"
        },
        "transformacion": ["svarṇa→sarna→sarn (simplificación v→Ø, elisión de -a)", "zarana→zarn→sarn (ensordecimiento z→s por fonotáctica, elisión de -ana)"]
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

    cat_name = "colores"
    if cat_name not in cats:
        # Find best category — dimensiones_y_adjetivos is closest for colors
        cat_name = "dimensiones_y_adjetivos"

    cat_data = cats[cat_name]
    if isinstance(cat_data, dict):
        entries = cat_data.setdefault("entradas", [])
    else:
        entries = cat_data
        cats[cat_name] = {"descripcion": "Adjetivos de dimensión, tamaño, cualidad y color", "entradas": entries}

    added = 0
    skipped = 0
    for c in COLORS:
        w = c["kalfirvach"]
        existing = any(
            (e.get("kalfirvach") or e.get("forma_final") or "").strip() == w
            for e in entries if isinstance(e, dict)
        )
        if existing:
            print(f"  SKIP: {w} ya existe")
            skipped += 1
            continue

        entry = {
            "kalfirvach": c["kalfirvach"],
            "forma_final": c["kalfirvach"],
            "concepto": c["concepto"],
            "pos": c["pos"],
            "origen": c["origen"],
            "transformacion": c["transformacion"],
            "derivaciones": []
        }
        entries.append(entry)
        added += 1
        print(f"  ADDED: {c['kalfirvach']} — {c['concepto']} ({c['origen']['lengua']})")

    with open(LEXICON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n→ Agregados: {added} | Omitidos: {skipped}")
    print(f"  Categoría: {cat_name}")

if __name__ == "__main__":
    main()

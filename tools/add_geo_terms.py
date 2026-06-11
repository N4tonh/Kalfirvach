#!/usr/bin/env python3
import json, shutil
from pathlib import Path

LEXICON_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v0.4_wip.json"
BACKUP_PATH = LEXICON_PATH.with_suffix(".json.bak4")

GEO = [
    {
        "kalfirvach": "gir",
        "concepto": "montaña, monte, elevación rocosa",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "गिरि (giri) 'montaña' / 𐬔𐬀𐬌𐬭𐬌 (gairi) 'montaña'",
            "corpus": "Ṛgveda / Avesta (Yasht 10, Mihr Yašt)"
        },
        "transformacion": ["giri→gir (elisión de -i final)", "gairi→giri→gir (acortamiento del diptongo, convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "thil",
        "concepto": "colina, loma, altozano",
        "pos": "noun",
        "origen": {
            "lengua": "Griego/Sanscrito",
            "raiz_original": "θῖλος (thîlos) 'colina, montículo' / स्थल (sthala) 'tierra elevada'",
            "corpus": "Textos geográficos / Ṛgveda"
        },
        "transformacion": ["thîlos→thil (acortamiento, pérdida de -os)", "sthala→sthal→thal→thil (elisión de -a, th- convergente con griego)"]
    },
    {
        "kalfirvach": "ghat",
        "concepto": "valle, cañada, depresión",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Arabe",
            "raiz_original": "घाट (ghāṭa) 'barranco, valle' / غَوْر (ghawr) 'tierra baja, valle'",
            "corpus": "Textos geográficos / Geografía árabe (al-Muqaddasī)"
        },
        "transformacion": ["ghāṭa→ghaṭa→ghat (elisión de -a, coda t válida §3.3)", "ghawr→ghaw→gha→ghat (pérdida de -r, epéntesis de -t por convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "nad",
        "concepto": "río, corriente de agua",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "नदी (nadī) 'río' / 𐬥𐬀𐬜𐬀 (naδa) 'río, corriente'",
            "corpus": "Ṛgveda (nadī-stuti) / Avesta"
        },
        "transformacion": ["nadī→nad (elisión de -ī)", "naδa→nada→nad (elisión de -a)"]
    },
    {
        "kalfirvach": "samud",
        "concepto": "mar, océano, gran masa de agua",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "समुद्र (samudra) 'mar' / 𐬰𐬭𐬀𐬌𐬌𐬀 (zrayah) 'mar, océano'",
            "corpus": "Ṛgveda (samudrá) / Avesta (Yašt 5, Abān Yašt)"
        },
        "transformacion": ["samudra→samud (elisión de -ra, retención de la raíz)", "zrayah→zraya→zra→sra→samud (asimilación inicial, convergencia parcial por posición acentual)"]
    },
    {
        "kalfirvach": "sagar",
        "concepto": "océano profundo, alta mar, abismo marino",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "सागर (sāgara) 'océano' / πέλαγος (pelagos) 'alta mar'",
            "corpus": "Mahābhārata / Homero, PGM"
        },
        "transformacion": ["sāgara→sagara→sagar (elisión de -a final)", "pelagos→pelag→pel→pela→lag→sagar (reducción de π, asimilación fricativa a la forma sánscrita)"]
    },
    {
        "kalfirvach": "sar",
        "concepto": "lago, laguna, espejo de agua",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "सरस् (saras) 'lago, estanque' / ἕλος (helos) 'pantano, lago bajo'",
            "corpus": "Ṛgveda / Homero (Ilíada)"
        },
        "transformacion": ["saras→sar (elisión de -as)", "helos→hel→el→sal→sar (pérdida de h-, asimilación vocálica a sánscrito)"]
    },
    {
        "kalfirvach": "wana",
        "concepto": "bosque, arboleda, floresta",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "वन (vana) 'bosque' / 𐬬𐬀𐬥𐬀 (vana) 'bosque, árbol'",
            "corpus": "Ṛgveda (vana) / Avesta"
        },
        "transformacion": ["vana→wana (v→w por fonética KFA estándar)", "idéntico en ambas lenguas — forma panetimológica"]
    },
    {
        "kalfirvach": "kanan",
        "concepto": "selva, jungla, monte espeso",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Persa",
            "raiz_original": "कानन (kānana) 'bosque denso' / كنار (kanār) 'ribera boscosa, espesura'",
            "corpus": "Kālidāsa / Poesía persa"
        },
        "transformacion": ["kānana→kanan (acortamiento ā→a)", "kanār→kanar→kanan (asibilación r→n por disimilación, convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "sah",
        "concepto": "desierto, yermo, árido",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Griego",
            "raiz_original": "صحراء (ṣaḥrā') 'desierto' / ξηρός (xērós) 'seco, árido'",
            "corpus": "Corán (geografía) / Corpus Hippocraticum"
        },
        "transformacion": ["ṣaḥrā'→sahra→sah (elisión de -ra, pérdida de la enfática)", "xērós→xeros→ser→ser→sah (reducción, convergencia vocálica con el árabe)"]
    },
    {
        "kalfirvach": "pet",
        "concepto": "llanura, planicie, campo abierto",
        "pos": "noun",
        "origen": {
            "lengua": "Griego/Sanscrito",
            "raiz_original": "πεδίον (pedíon) 'llanura' / प्रस्थ (prastha) 'meseta, llano'",
            "corpus": "Heródoto / Mahābhārata"
        },
        "transformacion": ["pedíon→pedi→ped→pet (ensordecimiento d→t en coda §3.3)", "prastha→prastha→prast→prat→pet (simplificación del cluster oncial pr-, convergencia con griego)"]
    },
    {
        "kalfirvach": "kash",
        "concepto": "costa, orilla, litoral",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Persa",
            "raiz_original": "कच्छ (kaccha) 'costa, orilla' / كنان (kanān) 'ribera, costa'",
            "corpus": "Ṛgveda (Sindhu) / Textos geográficos persas"
        },
        "transformacion": ["kaccha→kaccha→kach→kash (palatalización ch→sh por fonotáctica)", "kanān→kana→kan→kash (asibilación n→sh por convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "dip",
        "concepto": "isla, ínsula",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "द्वीप (dvīpa) 'isla' / 𐬛𐬎𐬎𐬀𐬉𐬞𐬀 (duuaēpa) 'isla'",
            "corpus": "Rāmāyaṇa / Avesta (Bundahišn)"
        },
        "transformacion": ["dvīpa→dvipa→dipa→dip (pérdida de v, elisión de -a)", "duuaēpa→dwaēpa→dwipa→dipa→dip (monoptongación, convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "guh",
        "concepto": "cueva, caverna, gruta",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Persa",
            "raiz_original": "गुहा (guhā) 'cueva' / غار (ghār) 'cueva, caverna'",
            "corpus": "Upaniṣads / Poesía mística persa"
        },
        "transformacion": ["guhā→guh (elisión de -ā)", "ghār→ghar→gar→guh (cambio vocálico a→u por influencia sánscrita + epéntesis)"]
    },
    {
        "kalfirvach": "ghas",
        "concepto": "pastizal, sabana, pradera",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "घास (ghāsa) 'pasto, forraje' / 𐬔𐬀𐬯𐬀 (gasa) 'pasto, hierba'",
            "corpus": "Ṛgveda / Avesta"
        },
        "transformacion": ["ghāsa→ghāsa→ghas (elisión de -a)", "gasa→ghas (sonorización de s→sh? No, gasa → gh- por convergencia con sánscrito → ghas)"]
    },
    {
        "kalfirvach": "shikh",
        "concepto": "pico, cumbre, cima",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "शिखर (śikhara) 'cima, pico' / 𐬐𐬀𐬊𐬟𐬀 (kaofa) 'cumbre, pico montañoso'",
            "corpus": "Kālidāsa / Avesta (Yasht 10)"
        },
        "transformacion": ["śikhara→śikhar→shikh (elisión de -ara, ś→sh)", "kaofa→kof→kav→shikh (pérdida de k-, fricativización y convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "shal",
        "concepto": "cascada, salto de agua, catarata",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Sanscrito",
            "raiz_original": "شَلَّال (shallāl) 'cascada' / जल (jala) 'agua'",
            "corpus": "Geografía árabe / Ṛgveda (apāṃ napāt)"
        },
        "transformacion": ["shallāl→shalal→shal (elisión de -lāl)", "jala→jal→shal (palatalización j→sh por asibilación, convergencia con la forma árabe)"]
    },
    {
        "kalfirvach": "khan",
        "concepto": "cañón, garganta, desfiladero",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Arabe",
            "raiz_original": "खण्ड (khaṇḍa) 'barranco, quebrada' / خَنْدَق (khandaq) 'foso, trinchera, cañada'",
            "corpus": "Textos geográficos / Geografía militar árabe"
        },
        "transformacion": ["khaṇḍa→khand→khan (pérdida de -ḍa, simplificación -nd→-n)", "khandaq→khandak→khanaq→khan (elisión de -daq)"]
    },
    {
        "kalfirvach": "sher",
        "concepto": "cordillera, sierra, cadena montañosa",
        "pos": "noun",
        "origen": {
            "lengua": "Griego/Sanscrito",
            "raiz_original": "σειρά (seirá) 'cuerda, hilera' / श्रेणी (śreṇī) 'hilera, serie, fila'",
            "corpus": "Textos geográficos / Kālidāsa (descripción del Himālaya)"
        },
        "transformacion": ["seirá→seir→sér→sher (palatalización s→sh por influencia sánscrita)", "śreṇī→shreni→shren→sher (elisión de -eni y -n, convergencia con griego)"]
    },
    {
        "kalfirvach": "mukh",
        "concepto": "bahía, ensenada, golfo pequeño",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "मुख (mukha) 'boca, entrada' / μυχός (mychós) 'ensenada, recoveco marino'",
            "corpus": "Rāmāyaṇa / Odisea"
        },
        "transformacion": ["mukha→mukh (elisión de -a)", "mychós→mykhós→mikh→mukh (asimilación vocálica i→u por convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "sand",
        "concepto": "estrecho, paso angosto, canal",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "संधि (sandhi) 'unión, estrecho' / στενός (stenós) 'angosto, estrecho'",
            "corpus": "Textos geográficos / Heródoto"
        },
        "transformacion": ["sandhi→sandh→sand (pérdida de -i, sonorización dh→d)", "stenós→sten→sen→sand (pérdida de t-, nasalización, convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "him",
        "concepto": "hielo, nieve, ventisquero",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "हिम (hima) 'hielo, nieve' / χιών (khiōn) 'nieve'",
            "corpus": "Ṛgveda (Himālaya) / Homero"
        },
        "transformacion": ["hima→him (elisión de -a)", "khiōn→khion→khin→hin→him (asibilación velar, convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "burkan",
        "concepto": "volcán, montaña de fuego",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Tibetano",
            "raiz_original": "بُرْكَان (burkān) 'volcán' / འབར་ཁང (bar khang) 'casa de fuego, volcán'",
            "corpus": "Geografía árabe / Textos budistas tibetanos"
        },
        "transformacion": ["burkān→burkan (acortamiento vocálico ā→a)", "bar khang→barkhang→barkhan→burkan (asimilación vocálica a→u, elisión de -kh, -g)"]
    },
    {
        "kalfirvach": "ghor",
        "concepto": "barranco, abismo, precipicio, sima",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Sanscrito",
            "raiz_original": "غَوْر (ghawr) 'profundidad, tierra baja' / गर्त (garta) 'hoyo, abismo'",
            "corpus": "Geografía árabe / Ṛgveda"
        },
        "transformacion": ["ghawr→ghaw→ghor (monoptongación aw→o)", "garta→gart→gar→ghor (sonorización g→gh, cambio vocálico a→o, convergencia con árabe)"]
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
    target = "naturaleza_y_elementos"

    cat_data = cats[target]
    entries = cat_data.setdefault("entradas", [])

    added = 0
    for c in GEO:
        w = c["kalfirvach"]
        if any((e.get("kalfirvach") or e.get("forma_final") or "").strip() == w for e in entries if isinstance(e, dict)):
            print(f"  SKIP: {w} ya existe")
            continue
        entries.append({
            "kalfirvach": c["kalfirvach"],
            "forma_final": c["kalfirvach"],
            "concepto": c["concepto"],
            "pos": c["pos"],
            "origen": c["origen"],
            "transformacion": c["transformacion"],
            "derivaciones": []
        })
        added += 1
        print(f"  ADDED: {c['kalfirvach']} — {c['concepto']}")

    with open(LEXICON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n→ Agregados: {added} | Categoría: {target}")
    print(f"  24 términos de geografía física")

if __name__ == "__main__":
    main()

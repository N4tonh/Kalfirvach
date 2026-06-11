#!/usr/bin/env python3
import json, shutil
from pathlib import Path

LEXICON_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v0.4_wip.json"
BACKUP_PATH = LEXICON_PATH.with_suffix(".json.bak.food")

FOOD = [
    # ── Alimentos básicos ──
    {
        "kalfirvach": "khubz",
        "concepto": "pan, alimento básico de trigo o cereal",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Sanscrito",
            "raiz_original": "خبز (ḫubz) 'pan' / रोटिका (roṭikā) 'pan, torta'",
            "corpus": "Corpus coránico / Textos de alimentación védica"
        },
        "transformacion": ["ḫubz → khubz (ḫ → kh, adopción directa)", "roṭikā → roti → rot → khubz (convergencia con la forma árabe)"]
    },
    {
        "kalfirvach": "bishr",
        "concepto": "carne, vianda, alimento cárnico",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "पिशित (piśita) 'carne' / κρέας (kreas) 'carne'",
            "corpus": "Textos de āyurveda / Textos culinarios griegos"
        },
        "transformacion": ["piśita → pishita → pish → bishr (sonorización p→b)", "kreas → kreas → kris → bishr (convergencia con el sánscrito)"]
    },
    {
        "kalfirvach": "khalib",
        "concepto": "leche, lácteo, producto lácteo",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "حليب (ḥalīb) 'leche' / شیر (šīr) 'leche'",
            "corpus": "Textos de cría de camellos árabes / Poesía pastoral persa"
        },
        "transformacion": ["ḥalīb → halib → khalib (ḥ → kh, refuerzo consonántico)", "šīr → shir → khalib (convergencia con la forma árabe, epéntesis de -ka-)"]
    },
    {
        "kalfirvach": "zayt",
        "concepto": "aceite, grasa vegetal, óleo",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Avestan",
            "raiz_original": "زيت (zayt) 'aceite' / 𐬭𐬀𐬊𐬖𐬀𐬥𐬀 (raoġana) 'aceite, mantequilla'",
            "corpus": "Corpus coránico / Avesta (rituales de fuego)"
        },
        "transformacion": ["zayt → zayt (adopción directa)", "raoġana → raoghan → roghan → zayt (convergencia)"]
    },
    {
        "kalfirvach": "shahd",
        "concepto": "miel, dulce natural, néctar",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Avestan",
            "raiz_original": "شهد (šahd) 'miel' / 𐬨𐬀𐬜𐬎 (maδu) 'miel'",
            "corpus": "Corpus coránico (šahd) / Avesta (haoma con miel)"
        },
        "transformacion": ["šahd → shahd (š → sh, adopción directa)", "maδu → madu → mad → shahd (convergencia)"]
    },
    {
        "kalfirvach": "sabz",
        "concepto": "verdura, vegetal, hortaliza, legumbre verde",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Arabe",
            "raiz_original": "سبزی (sabzī) 'verdura, vegetal' / خضار (ḫuḍār) 'verduras'",
            "corpus": "Textos de gastronomía persa / Textos de agricultura árabes"
        },
        "transformacion": ["sabzī → sabz (pérdida del sufijo -ī)", "ḫuḍār → khuḍār → khuḍ → sabz (convergencia)"]
    },
    {
        "kalfirvach": "oriz",
        "concepto": "arroz, cereal, grano",
        "pos": "noun",
        "origen": {
            "lengua": "Griego/Persa",
            "raiz_original": "ὄρυζα (oryza) 'arroz' / برنج (birinj) 'arroz'",
            "corpus": "Historia Natural (Teofrasto) / Textos de cocina persa"
        },
        "transformacion": ["ὄρυζα → oryza → oriza → oriz (z → s? No, z → z)", "birinj → birinj → binj → oriz (convergencia con el griego)"]
    },
    {
        "kalfirvach": "dal",
        "concepto": "legumbre, lenteja, leguminosa",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Persa",
            "raiz_original": "दाल (dāla) 'lenteja' / دال (dāl) 'lenteja'",
            "corpus": "Textos de āyurveda / Cocina persa tradicional"
        },
        "transformacion": ["dāla → dala → dal (acortamiento ā→a, elisión de -a)", "dāl → dal (acortamiento ā→a) — convergencia panetimológica"]
    },
    {
        "kalfirvach": "tamr",
        "concepto": "dátil, fruta seca, fruto deshidratado",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "تمر (tamr) 'dátil' / خرما (xurmā) 'dátil'",
            "corpus": "Corpus coránico / Poesía persa (dátil como símbolo de hospitalidad)"
        },
        "transformacion": ["tamr → tamr (adopción directa, CVCC válido)", "xurmā → khurma → khur → tamr (convergencia con el árabe)"]
    },
    # ── Bebidas y derivados ──
    {
        "kalfirvach": "mast",
        "concepto": "yogur, leche fermentada, cuajada",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Arabe",
            "raiz_original": "ماست (māst) 'yogur' / زبدي (zabadī) 'yogur'",
            "corpus": "Textos de gastronomía persa / Textos de alimentación árabes"
        },
        "transformacion": ["māst → mast (acortamiento ā→a)", "zabadī → zaba → mast (convergencia)"]
    },
    {
        "kalfirvach": "labn",
        "concepto": "queso, producto lácteo fermentado sólido",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "لبن (laban) 'leche agria, yogur' / پنیر (panīr) 'queso'",
            "corpus": "Textos de beduinos / Textos de gastronomía persa"
        },
        "transformacion": ["laban → labn (elisión de -a)", "panīr → panir → pan → labn (convergencia)"]
    },
    {
        "kalfirvach": "mayn",
        "concepto": "vino, bebida fermentada, licor",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Griego",
            "raiz_original": "می (mey) 'vino' / οἶνος (oinos) 'vino'",
            "corpus": "Poesía persa clásica (Hāfez, Rūmī) / PGM (vino en rituales)"
        },
        "transformacion": ["mey → mayn (epéntesis de -n, refuerzo de coda)", "οἶνος → oinos → oin → mayn (metátesis m-, convergencia)"]
    },
    # ── Cocina y preparación ──
    {
        "kalfirvach": "pakh",
        "concepto": "cocinar, preparar alimentos, guisar",
        "pos": "verb",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "पच् (pac) 'cocinar, cocer' / πέσσω (pessō) 'cocinar, cocer'",
            "corpus": "Ṛgveda (pac) / Homero (pessō, Odisea)"
        },
        "transformacion": ["pac → pak → pakh (oclusiva aspirada por énfasis KFA)", "πέσσω → pessō → pes → pakh (convergencia con el sánscrito)"]
    },
    {
        "kalfirvach": "briz",
        "concepto": "freír, asar, cocinar en grasa o fuego directo",
        "pos": "verb",
        "origen": {
            "lengua": "Sanscrito/Persa",
            "raiz_original": "भृज्ज् (bhṛjj) 'freír, asar' / بریان (biryān) 'asado, frito'",
            "corpus": "Textos de āyurveda / Poesía persa (biryān como banquete)"
        },
        "transformacion": ["bhṛjj → bhrij → briz (elisión de la aspiración, asibilación j→z)", "biryān → biryan → briy → briz (pérdida de -an)"]
    },
    {
        "kalfirvach": "swad",
        "concepto": "sabor, gusto, sabor agradable, condimento",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "स्वाद (svāda) 'sabor, gusto' / γεῦσις (geusis) 'gusto, sentido del gusto'",
            "corpus": "Textos de āyurveda (ṣaḍ-rasa) / Textos filosóficos griegos"
        },
        "transformacion": ["svāda → svada → swad (v → w, acortamiento ā→a)", "γεῦσις → geusis → gheus → swad (convergencia, s- inicial por analogía sánscrita)"]
    },
    {
        "kalfirvach": "khā",
        "concepto": "comida, alimento, vianda, sustento",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Arabe",
            "raiz_original": "खाद (khād) 'comer, masticar' / أكل (akala) 'comer, alimento'",
            "corpus": "Textos de āyurveda / Corpus coránico"
        },
        "transformacion": ["khād → kha → khā (pérdida de -d, alargamiento compensatorio)", "akala → aka → ak → khā (convergencia con el sánscrito)"]
    },
    {
        "kalfirvach": "murak",
        "concepto": "caldo, sopa, cocido, guiso líquido",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Griego",
            "raiz_original": "مرق (maraq) 'caldo' / ζωμός (zōmos) 'caldo, sopa'",
            "corpus": "Textos de gastronomía árabe / Textos culinarios griegos"
        },
        "transformacion": ["maraq → marak → murak (apertura a→u)", "ζωμός → zōmos → zomos → murak (convergencia con el árabe)"]
    },
    {
        "kalfirvach": "tanur",
        "concepto": "horno, fogón, lugar de cocción",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "تنور (tannūr) 'horno' / تنور (tanūr) 'horno' — raíz acadia común",
            "corpus": "Corpus coránico (tannūr del diluvio) / Poesía persa"
        },
        "transformacion": ["tannūr → tanur (geminación simplificada nn→n, ū→u)", "idéntico en ambas — forma panoriental antigua"]
    },
    # ── Utensilios ──
    {
        "kalfirvach": "patr",
        "concepto": "plato, vasija, recipiente, cuenco",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "पात्र (pātra) 'vasija, recipiente' / ποτήρ (potēr) 'copa, vaso'",
            "corpus": "Textos rituales védicos / PGM (vasijas rituales)"
        },
        "transformacion": ["pātra → patra → patr (pérdida de -a)", "ποτήρ → potēr → poter → patr (apertura o→a por convergencia)"]
    },
    {
        "kalfirvach": "chur",
        "concepto": "cuchillo, hoja cortante, cuchilla",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Persa",
            "raiz_original": "छुरिका (churikā) 'cuchillo' / چاقو (čāqū) 'cuchillo'",
            "corpus": "Textos quirúrgicos (Suśruta Saṃhitā) / Textos de cocina persa"
        },
        "transformacion": ["churikā → churi → chur (pérdida de sufijos)", "čāqū → chāqū → chā → chur (convergencia con el sánscrito)"]
    },
    {
        "kalfirvach": "digh",
        "concepto": "olla, caldero, pote, marmita",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Arabe",
            "raiz_original": "دیک (dīg) 'olla, caldero' / قدر (qidr) 'olla'",
            "corpus": "Poesía persa (dīg como símbolo de hogar) / Textos de gastronomía árabes"
        },
        "transformacion": ["dīg → dig → digh (oclusiva sonora aspirada por énfasis KFA)", "qidr → qidr → qid → digh (convergencia, sonorización q→g)"]
    },
    # ── Estados ──
    {
        "kalfirvach": "jos",
        "concepto": "hambre, inanición, apetito intenso",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Sanscrito",
            "raiz_original": "جوع (jūʿ) 'hambre' / क्षुध् (kṣudh) 'hambre'",
            "corpus": "Corpus coránico / Textos budistas (upādāna)"
        },
        "transformacion": ["jūʿ → ju → jos (alargamiento vocálico, adición de coda -os)", "kṣudh → kshudh → kshud → jos (pérdida del cluster ksh-)"]
    },
    {
        "kalfirvach": "tesh",
        "concepto": "sed",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Arabe",
            "raiz_original": "تشنگی (tešnegī) 'sed' / ظمأ (ẓama') 'sed'",
            "corpus": "Poesía persa (tešnegī como metáfora) / Corpus coránico"
        },
        "transformacion": ["tešnegī → tešne → tesh (pérdida de sufijos, š → sh)", "ẓama' → zama → zaa → tesh (convergencia con el persa)"]
    },
    {
        "kalfirvach": "rizq",
        "concepto": "sustento, provisión, alimento diario, pan de cada día",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Griego",
            "raiz_original": "رزق (rizq) 'sustento, provisión' / τροφή (trophē) 'nutrición, alimento'",
            "corpus": "Corpus coránico / Textos filosóficos griegos"
        },
        "transformacion": ["rizq → rizq (adopción directa, CVCC válido)", "τροφή → trophē → trofe → rizq (convergencia)"]
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
    target = "comida_y_cocina"

    if target not in cats:
        cats[target] = {"descripcion": "Alimentos, bebidas, cocina, utensilios y gastronomia", "entradas": []}

    cat_data = cats[target]
    entries = cat_data.setdefault("entradas", [])

    added = 0
    for f in FOOD:
        w = f["kalfirvach"]
        if any((e.get("kalfirvach") or e.get("forma_final") or "").strip() == w for e in entries if isinstance(e, dict)):
            print(f"  SKIP: {w} ya existe")
            continue
        entries.append({
            "kalfirvach": f["kalfirvach"],
            "forma_final": f["kalfirvach"],
            "concepto": f["concepto"],
            "pos": f["pos"],
            "origen": f["origen"],
            "transformacion": f["transformacion"],
            "derivaciones": []
        })
        added += 1
        print(f"  ADDED: {f['kalfirvach']} — {f['concepto']}")

    with open(LEXICON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    skt = sum(1 for a in FOOD if "Sanscrito" in a["origen"]["lengua"])
    total = len(FOOD)
    print(f"\n→ Agregados: {added} | Categoría: {target}")
    print(f"  {total} términos de comida y cocina | Sánscrito: {skt}/{total} ({100*skt//total}%)")


if __name__ == "__main__":
    main()

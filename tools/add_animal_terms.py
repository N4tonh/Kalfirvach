#!/usr/bin/env python3
import json, shutil
from pathlib import Path

LEXICON_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v0.4_wip.json"
BACKUP_PATH = LEXICON_PATH.with_suffix(".json.bak.anim")

ANIMALS = [
    # ── Mamíferos grandes ──
    {
        "kalfirvach": "gav",
        "concepto": "vaca, toro, res, ganado vacuno",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "गो (go) 'vaca, toro' / 𐬔𐬀𐬊 (gao) 'vaca' — raíz PIE *gwou-",
            "corpus": "Ṛgveda (go, gavya) / Avesta (Gathas, Yasna 29)"
        },
        "transformacion": ["go/gav → gav (forma convergente, CVG)", "gao → gav (diptongo ao → a)"]
    },
    {
        "kalfirvach": "ashp",
        "concepto": "caballo",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan/Griego",
            "raiz_original": "अश्व (aśva) 'caballo' / 𐬀𐬯𐬞𐬀 (aspa) 'caballo' / ἵππος (hippos) 'caballo'",
            "corpus": "Ṛgveda (aśva, aśvamedha) / Avesta (Yašt 5, Aredvi Sūra)"
        },
        "transformacion": ["aśva → ashva → ashp (cluster simplificado -śv- → -sh-, pérdida de -a)", "aspa → asp → ashp (convergencia con el cluster śv)", "hippos → hip → ashp (metátesis vocálica)"]
    },
    {
        "kalfirvach": "shir",
        "concepto": "león, fiera, depredador mayor",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Arabe",
            "raiz_original": "شیر (šīr) 'león' / أسد (asad) 'león' (forma dialectal šir)",
            "corpus": "Poesía épica persa (Šāh-nāma) / Bestiarios árabes"
        },
        "transformacion": ["šīr → shir (adopción directa, CVC válido)", "asad → šir → shir (metátesis radical, convergencia con el persa)"]
    },
    {
        "kalfirvach": "hast",
        "concepto": "elefante",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "हस्तिन् (hastin) 'elefante' / ἐλέφας (elephas) 'elefante'",
            "corpus": "Textos épicos (Rāmāyaṇa, guerra de Laṅkā) / Historiografía griega (Heródoto)"
        },
        "transformacion": ["hastin → hast (pérdida del sufijo -in)", "elephas → elef → ele → hast (reducción a primera sílaba + convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "jamal",
        "concepto": "camello",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Avestan",
            "raiz_original": "جمل (jamal) 'camello' / 𐬎𐬱𐬙𐬭𐬀 (uštra) 'camello'",
            "corpus": "Corpus coránico / Avesta (Vendidad, camello como animal valioso)"
        },
        "transformacion": ["jamal → jamal (adopción directa, CVCVC válido)", "uštra → ushtra → ush → jamal (convergencia completa con la forma árabe)"]
    },
    # ── Mamíferos medianos/pequeños ──
    {
        "kalfirvach": "buza",
        "concepto": "cabra",
        "pos": "noun",
        "origen": {
            "lengua": "Avestan/Arabe",
            "raiz_original": "𐬠𐬏𐬰𐬀 (būza) 'cabra' / ماعز (māʿiz) 'cabra'",
            "corpus": "Avesta (Vendidad, sacrificio animal) / Léxico pastoral árabe"
        },
        "transformacion": ["būza → buza (acortamiento vocálico ū → u)", "mā‘iz → maiz → maz → buza (convergencia parcial con el avéstico)"]
    },
    {
        "kalfirvach": "ghanam",
        "concepto": "oveja, carnero, rebaño ovino",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "غنم (ġanam) 'ganado ovino, oveja' / گوسفند (gōsfand) 'oveja'",
            "corpus": "Corpus coránico / Poesía pastoral persa"
        },
        "transformacion": ["ġanam → ghanam (ġ → gh, adaptación KFA)", "gōsfand → gōsfand → gosf → ghanam (reducción a dos primeras sílabas, convergencia)"]
    },
    {
        "kalfirvach": "khinz",
        "concepto": "cerdo, puerco, jabalí",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Griego",
            "raiz_original": "خنزير (ḫinzīr) 'cerdo' / χοῖρος (choiros) 'cerdo, cochinillo'",
            "corpus": "Corpus coránico / Textos de la Antigüedad tardía"
        },
        "transformacion": ["ḫinzīr → khinzīr → khinz (pérdida de -īr)", "choiros → khoiros → khir → khinz (convergencia con el árabe, epéntesis de -n-)"]
    },
    {
        "kalfirvach": "mau",
        "concepto": "gato",
        "pos": "noun",
        "origen": {
            "lengua": "Egipcio/Persa",
            "raiz_original": "mjw (miu) 'gato' / گربه (gurba) 'gato', پشک (pišak) 'gato'",
            "corpus": "Papiros egipcios (adoración de Bastet) / Poesía persa"
        },
        "transformacion": ["mjw → miu → mau (diptongación i → a por onomatopeya)", "gurba → gur → mau (convergencia con la forma egipcia)", "Forma onomatopéyica convergente"]
    },
    {
        "kalfirvach": "mush",
        "concepto": "rata, ratón, roedor",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Griego",
            "raiz_original": "موش (mūš) 'ratón' / μῦς (mȳs) 'ratón, roedor'",
            "corpus": "Literatura persa / Textos de historia natural griega"
        },
        "transformacion": ["mūš → mush (ū → u, š → sh)", "mȳs → mys → mus → mush (y → u por influencia persa, s → sh)"]
    },
    {
        "kalfirvach": "kapi",
        "concepto": "mono, simio, primate",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Egipcio",
            "raiz_original": "कपि (kapi) 'mono' / ky (kī) 'mono' (babuino)",
            "corpus": "Rāmāyaṇa (Hanumān como vanara) / Textos funerarios egipcios"
        },
        "transformacion": ["kapi → kapi (adopción directa, CVCV válido)", "ky → ki → kapi (adición de sílaba final -pi por influencia sánscrita)"]
    },
    # ── Aves ──
    {
        "kalfirvach": "dik",
        "concepto": "gallo, gallina, ave de corral",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "ديك (dīk) 'gallo' / خروس (xorus) 'gallo'",
            "corpus": "Textos de falconería árabe / Poesía persa"
        },
        "transformacion": ["dīk → dik (acortamiento vocálico ī → i)", "xorus → khorus → khor → dik (simplificación del cluster, convergencia con el árabe)"]
    },
    {
        "kalfirvach": "nisr",
        "concepto": "águila, ave rapaz mayor",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "نسر (nasr) 'águila, buitre' / عقاب (ʿuqāb) 'águila'",
            "corpus": "Corpus coránico (nasr como nombre de deidad preislámica) / Poesía épica persa"
        },
        "transformacion": ["nasr → nisr (apertura vocálica a → i por influencia persa)", "ʿuqāb → uqab → ukab → nisr (convergencia, pérdida de ʿ, metátesis)"]
    },
    {
        "kalfirvach": "bum",
        "concepto": "búho, lechuza, ave nocturna",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "بوم (būm) 'búho' / جغد (joġd) 'búho'",
            "corpus": "Textos de augurios árabes / Poesía persa"
        },
        "transformacion": ["būm → bum (acortamiento ū → u)", "joġd → joghd → jod → bum (convergencia con la forma árabe)"]
    },
    {
        "kalfirvach": "korak",
        "concepto": "cuervo, córvido",
        "pos": "noun",
        "origen": {
            "lengua": "Griego/Arabe",
            "raiz_original": "κόραξ (korax) 'cuervo' / غراب (ġurāb) 'cuervo'",
            "corpus": "PGM (advocaciones ctónicas / augurios) / Textos de mal agüero árabes"
        },
        "transformacion": ["κόραξ → korax → korak (x → k en coda §3.3)", "ġurāb → ghurab → ghur → korak (convergencia con el griego, pérdida de la aspiración)"]
    },
    # ── Reptiles y anfibios ──
    {
        "kalfirvach": "kurma",
        "concepto": "tortuga, galápago",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "कूर्म (kūrma) 'tortuga' / χέλυς (chelys) 'tortuga acuática'",
            "corpus": "Purāṇas (Kūrma-avatāra de Viṣṇu) / Textos de historia natural griega"
        },
        "transformacion": ["kūrma → kurma (ū → u)", "chelys → chely → khel → kurma (convergencia con el sánscrito, epéntesis vocálica)"]
    },
    {
        "kalfirvach": "bhek",
        "concepto": "rana, sapo, anfibio",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Arabe",
            "raiz_original": "भेक (bheka) 'rana' / ضفدع (ḍifdaʿ) 'rana'",
            "corpus": "Upaniṣads / Textos de ciencias naturales árabes"
        },
        "transformacion": ["bheka → bhek (elisión de -a)", "ḍifda‘ → difda → dif → bhek (reducción, convergencia con el sánscrito)"]
    },
    {
        "kalfirvach": "tims",
        "concepto": "cocodrilo, lagarto acuático mayor",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Copto",
            "raiz_original": "تمساح (timsāḥ) 'cocodrilo' / ⲙⲥⲁϩ (msah) 'cocodrilo'",
            "corpus": "Textos de navegación árabes / Papiros egipcios (dios Sobek)"
        },
        "transformacion": ["timsāḥ → timsā → tims (pérdida de -āḥ)", "msah → msah → mas → tims (metátesis t-, convergencia con el árabe)"]
    },
    # ── Insectos y arácnidos ──
    {
        "kalfirvach": "bhram",
        "concepto": "abeja",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "भ्रमर (bhramara) 'abeja' / μέλισσα (melissa) 'abeja'",
            "corpus": "Kāma Sūtra (bhramara como metáfora) / PGM (melissa como sacerdotisa)"
        },
        "transformacion": ["bhramara → bhram (elisión de -ara)", "μέλισσα → melissa → melis → bhram (reducción a la consonante inicial, convergencia)"]
    },
    {
        "kalfirvach": "pipil",
        "concepto": "hormiga",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Arabe",
            "raiz_original": "पिपीलिका (pipīlikā) 'hormiga' / نمل (naml) 'hormiga'",
            "corpus": "Textos budistas (upamā) / Corpus coránico (Sūrat an-Naml)"
        },
        "transformacion": ["pipīlikā → pipilī → pipil (elisión del sufijo, acortamiento)", "naml → nam → pipil (convergencia parcial, carácter onomatopéyico)"]
    },
    {
        "kalfirvach": "akrab",
        "concepto": "escorpión, alacrán",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "عقرب (ʿaqrab) 'escorpión' / کژدم (každum) 'escorpión'",
            "corpus": "Textos de venenos árabes / Poesía persa"
        },
        "transformacion": ["ʿaqrab → aqrab → akrab (ʿ → Ø, q → k)", "každum → kazhdum → kazh → akrab (convergencia con el árabe, metátesis)"]
    },
    # ── Acuáticos y otros ──
    {
        "kalfirvach": "delf",
        "concepto": "delfín, cetáceo, mamífero marino",
        "pos": "noun",
        "origen": {
            "lengua": "Griego/Arabe",
            "raiz_original": "δελφίς (delphís) 'delfín' / دلفين (dulfīn) 'delfín'",
            "corpus": "PGM (advocaciones marinas) / Textos de navegación árabes"
        },
        "transformacion": ["δελφίς → delphis → delf (pérdida de -is)", "dulfīn → dulfin → dulf → delf (apertura vocálica u → e)"]
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
    target = "animales"

    cat_data = cats[target]
    entries = cat_data.setdefault("entradas", [])

    added = 0
    for a in ANIMALS:
        w = a["kalfirvach"]
        if any((e.get("kalfirvach") or e.get("forma_final") or "").strip() == w for e in entries if isinstance(e, dict)):
            print(f"  SKIP: {w} ya existe")
            continue
        entries.append({
            "kalfirvach": a["kalfirvach"],
            "forma_final": a["kalfirvach"],
            "concepto": a["concepto"],
            "pos": a["pos"],
            "origen": a["origen"],
            "transformacion": a["transformacion"],
            "derivaciones": []
        })
        added += 1
        print(f"  ADDED: {a['kalfirvach']} — {a['concepto']}")

    with open(LEXICON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Contar Sánscrito
    skt = sum(1 for a in ANIMALS if "Sanscrito" in a["origen"]["lengua"])
    total = len(ANIMALS)
    print(f"\n→ Agregados: {added} | Categoría: {target}")
    print(f"  {total} términos de animales | Sánscrito: {skt}/{total} ({100*skt//total}%)")


if __name__ == "__main__":
    main()

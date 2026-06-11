#!/usr/bin/env python3
import json, shutil
from pathlib import Path

LEXICON_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v0.4_wip.json"
BACKUP_PATH = LEXICON_PATH.with_suffix(".json.bak5")

EMOTIONS = [
    {
        "kalfirvach": "sukha",
        "concepto": "felicidad, dicha, bienestar, júbilo",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "सुख (sukha) 'dicha, felicidad' / 𐬵𐬎𐬑𐬴𐬀𐬚𐬭𐬀 (huxšaθra) 'buen soberano, bienaventuranza'",
            "corpus": "Upaniṣads, Yoga Sūtra / Avesta (Gathas)"
        },
        "transformacion": ["sukha adoptado directamente — CV-CV válido", "huxšaθra→huxša→husha→sukha (simplificación del cluster, convergencia vocálica con sánscrito)"]
    },
    {
        "kalfirvach": "dukh",
        "concepto": "tristeza, aflicción, pesar, sufrimiento",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Persa",
            "raiz_original": "दुःख (duḥkha) 'sufrimiento, dolor' / دق (deq) 'angustia, pesar'",
            "corpus": "Upaniṣads (duḥkha) / Poesía persa clásica"
        },
        "transformacion": ["duḥkha→dukha→dukh (elisión de -a, pérdida de la aspiración)", "deq→dekh→dukh (apertura vocálica e→u por influencia sánscrita, q→kh)"]
    },
    {
        "kalfirvach": "rosh",
        "concepto": "enojo, ira, furia, cólera",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "रोष (roṣa) 'ira, furia' / 𐬀𐬌𐬱𐬨𐬀 (aišma) 'ira, furia' (daevica)",
            "corpus": "Mahābhārata (roṣa) / Avesta (Vendidad, contra los daēva)"
        },
        "transformacion": ["roṣa→rosh (elisión de -a, ṣ→sh)", "aišma→aishma→aish→rosh (metátesis y convergencia con la raíz sánscrita)"]
    },
    {
        "kalfirvach": "prem",
        "concepto": "amor, afecto profundo, devoción amorosa",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Persa",
            "raiz_original": "प्रेमन् (preman) 'amor' / پریم (preym) 'amor, afecto'",
            "corpus": "Bhāgavata Purāṇa (prema-bhakti) / Poesía mística persa (Rūmī)"
        },
        "transformacion": ["preman→prem (elisión de -an)", "preym→prem (monoptongación ey→e)", "Forma convergente indoirania — misma raíz protoindoeuropea *prey-"]
    },
    {
        "kalfirvach": "baya",
        "concepto": "miedo, temor, pavor",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "भय (bhaya) 'miedo' / 𐬠𐬌𐬌𐬁 (biyā) 'miedo'",
            "corpus": "Bhagavad Gītā (bhaya) / Avesta"
        },
        "transformacion": ["bhaya→bhaya→baya (pérdida de la aspiración bh→b por fonética KFA)", "biyā→biya→baya (vowel raising i→a por convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "chint",
        "concepto": "ansiedad, preocupación, inquietud",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Persa",
            "raiz_original": "चिन्ता (cintā) 'ansiedad, preocupación' / چین (chin) 'inquietud'",
            "corpus": "Textos budistas (upacaya) / Poesía persa"
        },
        "transformacion": ["cintā→cinta→chint (pérdida de -ā, c→ch)", "chin→chint (epéntesis de -t por influencia sánscrita)"]
    },
    {
        "kalfirvach": "tham",
        "concepto": "asombro, sorpresa, estupefacción",
        "pos": "noun",
        "origen": {
            "lengua": "Griego/Arabe",
            "raiz_original": "θάμβος (thamvos) 'asombro, estupefacción' / دَهَش (dahash) 'asombro, perplejidad'",
            "corpus": "Homero (Odisea) / Textos árabes (filosofía)"
        },
        "transformacion": ["thamvos→thambos→thamb→tham (elisión de -os, simplificación -mb→-m)", "dahash→dhash→thash→tham (asibilación d→th, convergencia con el griego)"]
    },
    {
        "kalfirvach": "lash",
        "concepto": "vergüenza, pudor, bochorno",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Arabe",
            "raiz_original": "लज्जा (lajjā) 'vergüenza' / خَجَل (khajal) 'vergüenza, turbación'",
            "corpus": "Textos jurídicos (dharmaśāstra) / Textos de adab (etiqueta)"
        },
        "transformacion": ["lajjā→lajja→laj→lash (palatalización j→sh por fonotáctica)", "khajal→khaj→kha→lash (pérdida de kh-, convergencia con sánscrito, l- inicial por analogía)"]
    },
    {
        "kalfirvach": "pap",
        "concepto": "culpa, pecado, transgresión",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "पाप (pāpa) 'pecado, mal' / 𐬞𐬁𐬞𐬀 (pāpa) 'pecado'",
            "corpus": "Manusmṛti / Avesta (Vendidad)"
        },
        "transformacion": ["pāpa→papa→pap (acortamiento vocálico ā→a, elisión de -a)", "idéntico en ambas lenguas — forma panetimológica indoirania"]
    },
    {
        "kalfirvach": "irsh",
        "concepto": "envidia, celos, resentimiento",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Arabe",
            "raiz_original": "ईर्ष्या (īrṣyā) 'envidia' / عِرْش (ʿirš) 'envidia, rivalidad'",
            "corpus": "Textos épicos (Rāmāyaṇa) / Textos de akhlāq (ética)"
        },
        "transformacion": ["īrṣyā→irshya→irsh (pérdida de -ya, simplificación)", "ʿirš→irsh (ʿ → Ø, š → sh) — convergencia completa"]
    },
    {
        "kalfirvach": "garv",
        "concepto": "orgullo, soberbia, dignidad",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "गर्व (garva) 'orgullo, soberbia' / 𐬔𐬀𐬭𐬎𐬎𐬀 (garuua) 'orgullo'",
            "corpus": "Textos de nīti (sabiduría) / Avesta"
        },
        "transformacion": ["garva→garv (elisión de -a)", "garuua→garva→garv (convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "asha",
        "concepto": "esperanza, expectativa, anhelo positivo",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Persa",
            "raiz_original": "आशा (āśā) 'esperanza' / آشا (āšā) 'esperanza'",
            "corpus": "Upaniṣads (āśā) / Poesía persa"
        },
        "transformacion": ["āśā→asha (ś→sh, acortamiento ā→a en sílaba átona)", "āšā→asha (idéntico) — convergencia completa indoirania"]
    },
    {
        "kalfirvach": "daya",
        "concepto": "compasión, piedad, misericordia",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "दया (dayā) 'compasión' / 𐬛𐬀𐬘𐬀𐬌𐬌𐬁 (dajaiiā) 'misericordia'",
            "corpus": "Textos budistas (karuṇā-dayā) / Avesta"
        },
        "transformacion": ["dayā→daya (acortamiento ā→a en sílaba átona)", "dajaiiā→dajai→daja→daya (palatalización j→y, convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "krit",
        "concepto": "gratitud, agradecimiento, reconocimiento",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "कृत (kṛta) 'hecho, ofrenda, gratitud' / χάρις (cháris) 'gracia, gratitud'",
            "corpus": "Ṛgveda (kṛta) / PGM, Homero"
        },
        "transformacion": ["kṛta→krita→krit (vocalización de ṛ→ri, elisión de -a)", "cháris→kharis→kharis→karis→kris→krit (convergencia con sánscrito, s→t por asimilación)"]
    },
    {
        "kalfirvach": "hani",
        "concepto": "nostalgia, melancolía, añoranza",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "حَنِين (ḥanīn) 'nostalgia, anhelo' / هانی (hānī) 'anhelo, deseo'",
            "corpus": "Poesía árabe preislámica / Poesía persa"
        },
        "transformacion": ["ḥanīn→hanin→hani (pérdida de -n final, acortamiento)", "hānī→hani (acortamiento ā→a) — convergencia parcial"]
    },
    {
        "kalfirvach": "kam",
        "concepto": "deseo sexual, pasión, lujuria, excitación erótica",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "काम (kāma) 'deseo sexual, placer' / 𐬐𐬁𐬨𐬀 (kāma) 'deseo'",
            "corpus": "Kāma Sūtra / Avesta"
        },
        "transformacion": ["kāma→kama→kam (acortamiento ā→a, elisión de -a)", "idéntico en ambas lenguas — forma panetimológica indoirania"]
    },
    {
        "kalfirvach": "vish",
        "concepto": "confianza, fe, seguridad interior",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "विश्वास (viśvāsa) 'confianza' / πίστις (pístis) 'fe, confianza'",
            "corpus": "Upaniṣads (viśvāsa) / Corpus Hermeticum, PGM"
        },
        "transformacion": ["viśvāsa→vishvasa→vishvas→vish (simplificación radical)", "pístis→pistis→pist→pish→vish (sonorización p→v por influencia sánscrita)"]
    },
    {
        "kalfirvach": "shak",
        "concepto": "sospecha, duda, desconfianza, recelo",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Arabe",
            "raiz_original": "शङ्का (śaṅkā) 'duda, sospecha' / شَكّ (shakk) 'duda, sospecha'",
            "corpus": "Textos de lógica (Nyāya) / Textos de kalām (teología)"
        },
        "transformacion": ["śaṅkā→shanka→shank→shak (simplificación -nk→-k)", "shakk→shak (geminación simplificada) — convergencia completa"]
    },
    {
        "kalfirvach": "khet",
        "concepto": "aburrimiento, hastío, tedio, desgano",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "खेद (kheda) 'fatiga, aburrimiento' / κῆδος (kēdos) 'cuidado, pesar'",
            "corpus": "Textos de nīti / Homero"
        },
        "transformacion": ["kheda→khed→khet (ensordecimiento d→t en coda §3.3)", "kēdos→kēdos→kedos→ked→khet (convergencia con sánscrito, d→t)"]
    },
    {
        "kalfirvach": "bhat",
        "concepto": "confusión, desconcierto, perplejidad",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Arabe",
            "raiz_original": "भ्रान्ति (bhrānti) 'confusión, error' / بَهَتَ (bahata) 'confundir, desconcertar'",
            "corpus": "Textos de Vedānta (māyā-bhrānti) / Textos de filosofía árabe"
        },
        "transformacion": ["bhrānti→bhanti→bhat (simplificación del cluster bhr→bh, elisión de -nti)", "bahata→baha→bhat (acortamiento, convergencia con sánscrito)"]
    },
    {
        "kalfirvach": "maun",
        "concepto": "soledad, aislamiento, retiro solitario",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "मौन (mauna) 'silencio, soledad' / μόνος (monos) 'solo, solitario'",
            "corpus": "Upaniṣads (mauna, muni) / Textos filosóficos griegos"
        },
        "transformacion": ["mauna→maun (elisión de -a)", "monos→mon→mon→maun (apertura vocálica o→au por influencia sánscrita)"]
    },
    {
        "kalfirvach": "santi",
        "concepto": "paz, serenidad, sosiego, tranquilidad profunda",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "शान्ति (śānti) 'paz' / σάος (saos) 'sano, salvo, seguro'",
            "corpus": "Upaniṣads (śānti pāṭha) / Homero"
        },
        "transformacion": ["śānti→shanti→santi (ś→sh→s por influencia griega, acortamiento ā→a)", "saos→sao→sa→santi (convergencia con sánscrito, adición del sufijo -nti)"]
    },
    {
        "kalfirvach": "vir",
        "concepto": "valentía, coraje, heroicidad, bravura",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Avestan",
            "raiz_original": "वीर (vīra) 'héroe, valiente' / 𐬬𐬍𐬭𐬀 (vīra) 'héroe, guerrero'",
            "corpus": "Ṛgveda (vīrya) / Avesta (Yasht 13, Frawardīn Yašt)"
        },
        "transformacion": ["vīra→vir (acortamiento ī→i, elisión de -a)", "idéntico en ambas lenguas — forma panetimológica indoirania"]
    },
    {
        "kalfirvach": "lal",
        "concepto": "ternura, dulzura, cariño, delicadeza afectiva",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Persa",
            "raiz_original": "लालन (lālana) 'caricia, mimo, ternura' / لال (lāl) 'tierno, querido'",
            "corpus": "Textos de kāmaśāstra / Poesía persa (hijo amado)"
        },
        "transformacion": ["lālana→lalan→lal (elisión de -ana)", "lāl→lal (acortamiento ā→a) — convergencia parcial"]
    },
    {
        "kalfirvach": "ghen",
        "concepto": "repulsión, asco, aversión intensa",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "घृणा (ghṛṇā) 'aversión, disgusto' / χολή (cholē) 'hiel, bilis, amargura'",
            "corpus": "Textos de āyurveda / Corpus Hippocraticum (teoría humoral)"
        },
        "transformacion": ["ghṛṇā→ghrina→ghin→ghen (vocalización de ṛ, apertura i→e)", "χολή→cholē→kholē→kholē→ghol→ghen (sonorización k→g por influencia sánscrita, cambio o→e)"]
    },
    {
        "kalfirvach": "sil",
        "concepto": "calma, tranquilidad, sosiego, placidez",
        "pos": "noun",
        "origen": {
            "lengua": "Griego/Sanscrito",
            "raiz_original": "γαλήνη (galēnē) 'calma, bonanza' / शीतल (śītala) 'fresco, calmado, sereno'",
            "corpus": "Homero / Textos de āyurveda"
        },
        "transformacion": ["γαλήνη→galēnē→galene→gale→sil (reducción extrema, retención de -l- y asimilación vocálica)", "śītala→shital→shil→sil (elisión de -tala, sh→s por convergencia con el griego)"]
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
    target = "emociones_y_estados_afectivos"

    if target not in cats:
        cats[target] = {"descripcion": "Emociones, estados afectivos y sentimientos", "entradas": []}

    cat_data = cats[target]
    entries = cat_data.setdefault("entradas", [])

    added = 0
    for c in EMOTIONS:
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
    print(f"  {len(EMOTIONS)} términos de emociones y estados afectivos")

if __name__ == "__main__":
    main()

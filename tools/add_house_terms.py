#!/usr/bin/env python3
import json, shutil
from pathlib import Path

LEXICON_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v0.4_wip.json"
BACKUP_PATH = LEXICON_PATH.with_suffix(".json.bak.house")

TERMS = [
    # ── Edificios y estructuras ──
    {
        "kalfirvach": "dar",
        "concepto": "casa, hogar, morada, vivienda",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Avestan",
            "raiz_original": "دار (dār) 'casa' / 𐬛𐬀𐬨𐬁𐬥𐬀 (damāna) 'casa, morada'",
            "corpus": "Corpus coránico / Avesta (Gathas)"
        },
        "transformacion": ["dār → dar (acortamiento ā→a)", "damāna → damān → dam → dar (convergencia con el árabe)"]
    },
    {
        "kalfirvach": "shahr",
        "concepto": "ciudad, urbe, poblado grande",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Arabe",
            "raiz_original": "شهر (šahr) 'ciudad' / مدينة (madīna) 'ciudad'",
            "corpus": "Poesía épica persa (Šāh-nāma) / Corpus coránico"
        },
        "transformacion": ["šahr → shahr (š → sh, adopción directa)", "madīna → madina → madī → shahr (convergencia)"]
    },
    {
        "kalfirvach": "qasr",
        "concepto": "fortaleza, castillo, ciudadela, palacio fortificado",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "قصر (qaṣr) 'palacio, fortaleza' / کاخ (kāx) 'palacio'",
            "corpus": "Textos de arquitectura árabes / Šāh-nāma (kāx)"
        },
        "transformacion": ["qaṣr → qasr (ṣ→s, adaptación KFA)", "kāx → kax → qasr (convergencia, énfasis velar q)"]    },
    {
        "kalfirvach": "burj",
        "concepto": "torre, atalaya, fortificación vertical",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Sanscrito",
            "raiz_original": "برج (burj) 'torre' / कूट (kūṭa) 'torre, cumbre'",
            "corpus": "Textos de arquitectura militar árabe / Textos de fortificaciones sánscritos"
        },
        "transformacion": ["burj → burj (adopción directa, CVCC válido)", "kūṭa → kuta → kut → burj (convergencia)"]
    },
    {
        "kalfirvach": "nag",
        "concepto": "edificio, construcción, estructura",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Arabe",
            "raiz_original": "नगर (nagara) 'edificio, ciudad' / بناء (binā') 'edificio, construcción'",
            "corpus": "Arthaśāstra / Textos de arquitectura árabes"
        },
        "transformacion": ["nagara → nagar → nag (pérdida del sufijo -ara)", "binā' → bina → bin → nag (convergencia con el sánscrito)"]
    },
    # ── Partes de la casa ──
    {
        "kalfirvach": "bab",
        "concepto": "puerta, entrada, portal, acceso",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Sanscrito",
            "raiz_original": "باب (bāb) 'puerta' / द्वार (dvāra) 'puerta'",
            "corpus": "Corpus coránico / Ṛgveda (dvāra)"
        },
        "transformacion": ["bāb → bab (acortamiento ā→a)", "dvāra → dvara → dvar → bab (simplificación del cluster dv-, convergencia)"]
    },
    {
        "kalfirvach": "shubak",
        "concepto": "ventana, vano, abertura en muro",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "شباك (šubbāk) 'ventana' / پنجره (panjare) 'ventana'",
            "corpus": "Textos de arquitectura árabes / Poesía persa"
        },
        "transformacion": ["šubbāk → shubbāk → shubak (geminación simplificada bb→b, acortamiento ā→a)", "panjare → panjar → shubak (convergencia con el árabe)"]
    },
    {
        "kalfirvach": "divar",
        "concepto": "muro, pared, muralla, tabique",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Arabe",
            "raiz_original": "دیوار (dīvār) 'muro' / حائط (ḥā'iṭ) 'muro, pared'",
            "corpus": "Šāh-nāma (dīvār) / Textos de construcción árabes"
        },
        "transformacion": ["dīvār → divār → divar (acortamiento ī→i, ā→a)", "ḥā'iṭ → haiṭ → ha → divar (convergencia con el persa)"]
    },
    {
        "kalfirvach": "saqf",
        "concepto": "techo, cubierta, cielo raso",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Griego",
            "raiz_original": "سقف (saqf) 'techo' / στέγη (stegē) 'techo, cubierta'",
            "corpus": "Textos de arquitectura árabes / Textos de construcción griegos"
        },
        "transformacion": ["saqf → saqf (adopción directa, CVCC válido)", "στέγη → stegē → stegi → saqf (convergencia)"]
    },
    {
        "kalfirvach": "bhum",
        "concepto": "piso, suelo, pavimento, base",
        "pos": "noun",
        "origen": {
            "lengua": "Sanscrito/Griego",
            "raiz_original": "भूमि (bhūmi) 'tierra, suelo' / πέδον (pedon) 'suelo, terreno'",
            "corpus": "Upaniṣads (bhūmi) / Textos de arquitectura griega"
        },
        "transformacion": ["bhūmi → bhum (elisión del sufijo -i, acortamiento ū→u)", "πέδον → pedon → ped → bhum (convergencia)"]
    },
    # ── Habitaciones y muebles ──
    {
        "kalfirvach": "otaq",
        "concepto": "habitación, cuarto, aposento, sala",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Arabe",
            "raiz_original": "اتاق (otāq) 'habitación' / غرفة (ġurfa) 'habitación, aposento'",
            "corpus": "Textos de arquitectura persa / Textos de vida cotidiana árabes"
        },
        "transformacion": ["otāq → otaq (acortamiento ā→a, q→q)", "ġurfa → ghurfa → ghur → otaq (convergencia)"]
    },
    {
        "kalfirvach": "firash",
        "concepto": "cama, lecho, yacija, lugar de descanso",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Griego",
            "raiz_original": "فراش (firāš) 'cama, lecho' / κλίνη (klinē) 'cama, lecho'",
            "corpus": "Corpus coránico / PGM"
        },
        "transformacion": ["firāš → firash (ā→a, š→sh)", "κλίνη → klinē → klini → firash (convergencia)"]
    },
    {
        "kalfirvach": "kurs",
        "concepto": "silla, asiento, banco, trono",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Griego",
            "raiz_original": "كرسي (kursī) 'silla' / καθέδρα (kathedra) 'asiento'",
            "corpus": "Corpus coránico / Textos de mobiliario griegos"
        },
        "transformacion": ["kursī → kurs (pérdida del sufijo -ī)", "καθέδρα → kathedra → kathē → kurs (convergencia)"]
    },
    {
        "kalfirvach": "miz",
        "concepto": "mesa, tablero, superficie de apoyo",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "مائدة (mā'ida) 'mesa' / میز (mīz) 'mesa'",
            "corpus": "Corpus coránico / Poesía persa"
        },
        "transformacion": ["mā'ida → maida → mai → miz (convergencia con el persa)", "mīz → miz (acortamiento ī→i)"]
    },
    # ── Elementos arquitectónicos ──
    {
        "kalfirvach": "sutun",
        "concepto": "columna, pilar, poste vertical",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Arabe",
            "raiz_original": "ستون (sutūn) 'columna' / عمود (ʿamūd) 'columna, pilar'",
            "corpus": "Textos de arquitectura persa (Persépolis) / Textos de construcción árabes"
        },
        "transformacion": ["sutūn → sutun (acortamiento ū→u)", "ʿamūd → amūd → amud → sutun (convergencia)"]
    },
    {
        "kalfirvach": "pul",
        "concepto": "puente, paso elevado, conexión",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Arabe",
            "raiz_original": "پل (pul) 'puente' / جسر (jisr) 'puente'",
            "corpus": "Textos de ingeniería persas / Textos de navegación árabes"
        },
        "transformacion": ["pul → pul (adopción directa)", "jisr → jisr → jis → pul (convergencia)"]
    },
    {
        "kalfirvach": "sham",
        "concepto": "lámpara, luminaria, vela, antorcha",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Griego",
            "raiz_original": "شمع (šamʿ) 'vela, candela' / λύχνος (lychnos) 'lámpara'",
            "corpus": "Corpus coránico / PGM (lámparas rituales)"
        },
        "transformacion": ["šamʿ → sham (ʿ → Ø, š → sh)", "λύχνος → lychnos → lykhn → sham (convergencia)"]
    },
    {
        "kalfirvach": "bashk",
        "concepto": "jardín, huerto, vergel, parque",
        "pos": "noun",
        "origen": {
            "lengua": "Persa/Sanscrito",
            "raiz_original": "باغ (bāġ) 'jardín' / वाटिका (vāṭikā) 'jardín'",
            "corpus": "Poesía persa (bāġ como paraíso) / Textos de arquitectura paisajista sánscritos"
        },
        "transformacion": ["bāġ → bāg → bash (con k epentético) → bashk", "vāṭikā → vatika → vatik → bashk (convergencia)"]
    },
    {
        "kalfirvach": "hujr",
        "concepto": "celda, cuarto pequeño, aposento, camarín",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "حجرة (ḥujra) 'habitación pequeña' / حجره (hujre) 'celda'",
            "corpus": "Textos de arquitectura doméstica árabes / Poesía persa"
        },
        "transformacion": ["ḥujra → hujra → hujr (ḥ→h, pérdida de -a)", "hujre → hujr (pérdida de -e) — convergencia panoriental"]
    },
    {
        "kalfirvach": "shar",
        "concepto": "calle, vía, camino urbano, callejuela",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "شارع (šāriʿ) 'calle' / راه (rāh) 'camino, vía'",
            "corpus": "Textos de geografía urbana árabes / Poesía persa"
        },
        "transformacion": ["šāriʿ → shāri → shar (pérdida del sufijo -i)", "rāh → rah → rā → shar (convergencia)"]
    },
    {
        "kalfirvach": "sanduq",
        "concepto": "cofre, caja, arca, baúl",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Persa",
            "raiz_original": "صندوق (ṣundūq) 'cofre' / صندوق (sandūq) 'cofre' — raíz común acadia (tsanduq)",
            "corpus": "Textos de comercio árabes / Poesía persa"
        },
        "transformacion": ["ṣundūq → sunduq → sanduq (asibilación, abertura vocálica)", "sandūq → sanduq (acortamiento ū→u)"]
    },
    {
        "kalfirvach": "khand",
        "concepto": "cimientos, fosa, zanja, excavación basal",
        "pos": "noun",
        "origen": {
            "lengua": "Arabe/Sanscrito",
            "raiz_original": "خندق (ḫandaq) 'foso, trinchera' / खण्ड (khaṇḍa) 'fragmento, división, zanja'",
            "corpus": "Textos de fortificación árabes / Textos de ingeniería sánscritos"
        },
        "transformacion": ["ḫandaq → khandak → khand (pérdida del sufijo -ak)", "khaṇḍa → khanda → khand (elisión de -a)"]
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
    target = "vivienda_y_arquitectura"

    if target not in cats:
        cats[target] = {"descripcion": "Vivienda, edificios, construccion, mobiliario y urbanismo", "entradas": []}

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
    print(f"  {total} términos de vivienda | Sánscrito: {skt}/{total} ({100*skt//total}%)")


if __name__ == "__main__":
    main()

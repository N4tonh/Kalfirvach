#!/usr/bin/env python3
"""
duplicate_checker.py — Busca palabras duplicadas en el léxico Kalfírvach.

Lee kalfirvach_lexicon_v0.4_wip.json, recorre todas las categorías,
y reporta cualquier palabra normalizada que aparezca en más de una entrada
(ya sea en la misma categoría o en distintas).

Distingue entre:
  - Actitudinales (prefijo "-"): son sufijos gramaticales, no palabras léxicas
  - Palabras normales: deben ser únicas en el léxico

Uso:
  python3 duplicate_checker.py
  python3 duplicate_checker.py --verbose
"""

import json, sys
from collections import defaultdict
from pathlib import Path

LEXICON_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v0.4_wip.json"

ACENTOS = str.maketrans({
    "ά": "α", "ὰ": "α", "ἀ": "α", "ἁ": "α", "ἄ": "α", "ἅ": "α", "ᾶ": "α",
    "έ": "ε", "ὲ": "ε", "ἐ": "ε", "ἑ": "ε", "ἔ": "ε", "ἕ": "ε",
    "ή": "η", "ὴ": "η", "ἠ": "η", "ἡ": "η", "ἤ": "η", "ἥ": "η", "ῆ": "η",
    "ί": "ι", "ὶ": "ι", "ἰ": "ι", "ἱ": "ι", "ἴ": "ι", "ἵ": "ι", "ῖ": "ι",
    "ϊ": "ι", "ἳ": "ι",
    "ό": "ο", "ὸ": "ο", "ὀ": "ο", "ὁ": "ο", "ὄ": "ο", "ὅ": "ο",
    "ύ": "υ", "ὺ": "υ", "ὐ": "υ", "ὑ": "υ", "ὔ": "υ", "ὕ": "υ", "ῦ": "υ",
    "ϋ": "υ",
    "ώ": "ω", "ὼ": "ω", "ὠ": "ω", "ὡ": "ω", "ὤ": "ω", "ὥ": "ω", "ῶ": "ω",
    "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
})


def normalize(w: str) -> str:
    """Normaliza: lowercase, sin acentos, sin guión inicial."""
    w = w.strip().lower()
    w = w.lstrip("-")  # actitudinales
    return w.translate(ACENTOS)


def main():
    verbose = "--verbose" in sys.argv

    if not LEXICON_PATH.exists():
        print(f"ERROR: no se encuentra {LEXICON_PATH}")
        sys.exit(1)

    with open(LEXICON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    v02 = data["kalfirvach_lexicon_v0.2"]
    cats = v02["categorias"]

    index = defaultdict(list)
    total = 0

    for cat_name, cat_data in cats.items():
        for entry in cat_data.get("entradas", []):
            if not isinstance(entry, dict):
                continue
            word = entry.get("kalfirvach") or entry.get("forma_final") or ""
            word = word.strip()
            if not word:
                continue

            total += 1
            concepto = entry.get("concepto", "—")
            pos = entry.get("pos", "—")
            is_act = word.startswith("-")
            norm = normalize(word)

            index[norm].append({
                "categoria": cat_name,
                "concepto": concepto,
                "forma": word,
                "pos": pos,
                "actitudinal": is_act,
            })

    print("=" * 70)
    print(f"  VERIFICACION DE DUPLICADOS  —  {total} entradas revisadas")
    print("=" * 70)

    dups = {k: v for k, v in index.items() if len(v) > 1}

    if not dups:
        print("\n  No se encontraron palabras duplicadas.")
        return

    print(f"\n  Se encontraron {len(dups)} palabra(s) con multiples entradas:\n")

    real_dups = 0
    for norm_word in sorted(dups.keys()):
        entries = dups[norm_word]
        lexical = [e for e in entries if not e["actitudinal"]]
        actitudinal = [e for e in entries if e["actitudinal"]]

        is_problem = len(lexical) > 1 or len(actitudinal) > 1

        if is_problem:
            status = " DUPLICADO REAL"
            real_dups += 1
        else:
            status = " LEX + SUFIJO (esperable)"

        if is_problem or verbose:
            print(f"  [{status}]  «{norm_word}»  ({len(entries)} entradas)")
            for e in entries:
                cat_label = e["categoria"]
                if e["actitudinal"]:
                    cat_label += " [ACTITUDINAL]"
                print(f"      {e['forma']:22s} → {cat_label}")
                print(f"      {'':22s}   «{e['concepto']}»")
            print()

    print("=" * 70)
    print(f"  Resumen: {len(dups)} grupos  |  {real_dups} duplicados reales")
    print("=" * 70)


if __name__ == "__main__":
    main()

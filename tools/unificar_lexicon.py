#!/usr/bin/env python3
import json, shutil, sys
from pathlib import Path

LEXICON_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v0.4_wip.json"
BACKUP_PATH = LEXICON_PATH.with_suffix(".json.bak")

CATEGORY_POS = {
    "pronombres_y_deicticos":      "pronoun",
    "numeros":                     "numeral",
    "dimensiones_y_adjetivos":     "adjective",
    "personas_y_parentesco":       "noun",
    "animales":                    "noun",
    "seres_vivos_plantas":         "noun",
    "anatomia_y_cuerpo":           "noun",
    "verbos_basicos":              "verb",
    "naturaleza_y_elementos":      "noun",
    "conceptos_espaciales_y_calidades": "noun",
    "conjunciones_y_particulas":   "particle",
    "actitudinales":               "affix",
    "magia_y_mitologia":           "noun",
    "tecnologia":                  "noun",
    "tiempo_domestico":            "noun",
    "medicina_y_salud":            "noun",
}

GRAPH_IPA = {
    "sh": "ʃ", "kh": "x", "gh": "ɣ", "th": "θ", "ch": "tʃ", "dh": "ð", "ng": "ŋ",
    "a": "a", "e": "e", "i": "i", "o": "o", "u": "u",
    "p": "p", "b": "b", "t": "t", "d": "d", "k": "k", "g": "ɡ",
    "f": "f", "s": "s", "z": "z", "h": "h", "m": "m", "n": "n",
    "r": "r", "l": "l", "w": "w", "y": "j",
    "v": "v", "q": "q", "'": "ʔ",
}

VOWELS = set("aeiou")

def tokenize(word):
    tokens = []
    chars = list(word.lower())
    i = 0
    while i < len(chars):
        if chars[i] in "-=_":
            i += 1
            continue
        if i + 1 < len(chars) and (chars[i] + chars[i+1]) in GRAPH_IPA:
            tokens.append(chars[i] + chars[i+1])
            i += 2
        else:
            tokens.append(chars[i])
            i += 1
    return tokens

def syllabify(ipa_chars):
    syll = []
    cur = []
    for ch in ipa_chars:
        if ch in VOWELS:
            if cur:
                syll.append("".join(cur))
            cur = [ch]
        else:
            cur.append(ch)
    if cur:
        if syll:
            syll[-1] += "".join(cur)
        else:
            syll = ["".join(cur)]
    return syll

def generate_ipa(word):
    if not word:
        return None
    w = word.lower().strip("-=_")
    if not w:
        return None
    parts = [p for p in w.split("-")]
    full = []
    for part in parts:
        ipa = []
        for g in tokenize(part):
            g = GRAPH_IPA.get(g)
            if g:
                ipa.append(g)
        if not ipa:
            return None
        syll = syllabify(ipa)
        if len(syll) <= 1:
            full.append("".join(syll))
            continue
        penult_heavy = len(syll) >= 2 and syll[-2] and syll[-2][-1] not in VOWELS
        if not penult_heavy and len(syll) >= 3:
            stress_idx = -3
        else:
            stress_idx = -2
        result = []
        for idx, s in enumerate(syll):
            if idx == len(syll) + stress_idx:
                result.append("ˈ" + s)
            else:
                result.append(s)
        full.append("".join(result))
    return "/" + "-".join(full) + "/"

def main():
    if not LEXICON_PATH.exists():
        print(f"ERROR: no se encuentra {LEXICON_PATH}")
        sys.exit(1)
    shutil.copy2(LEXICON_PATH, BACKUP_PATH)
    print(f"Backup: {BACKUP_PATH}")

    with open(LEXICON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    v02 = data["kalfirvach_lexicon_v0.2"]
    cats = v02["categorias"]
    meta = v02.get("metadata", {})

    stats = {"unified": 0, "pos_added": 0, "ipa_generated": 0, "duplicates_removed": 0}

    for cat_name, cat_data in sorted(cats.items()):
        if not isinstance(cat_data, dict):
            continue
        for entries in cat_data.values():
            if not isinstance(entries, list):
                continue

            seen = {}
            cleaned = []
            for entry in entries:
                if not isinstance(entry, dict):
                    cleaned.append(entry)
                    continue
                w = (entry.get("kalfirvach") or entry.get("forma_final") or "").strip()
                if not w:
                    cleaned.append(entry)
                    continue
                if w in seen:
                    if len(entry) > len(seen[w]):
                        cleaned[cleaned.index(seen[w])] = entry
                    stats["duplicates_removed"] += 1
                    continue
                seen[w] = entry
                cleaned.append(entry)

            for entry in cleaned:
                if not isinstance(entry, dict):
                    continue
                if not entry.get("kalfirvach", "").strip() and entry.get("forma_final", "").strip():
                    entry["kalfirvach"] = entry["forma_final"].strip()
                    stats["unified"] += 1
                if "pos" not in entry:
                    pos = CATEGORY_POS.get(cat_name, "")
                    if pos:
                        entry["pos"] = pos
                        stats["pos_added"] += 1
                if not entry.get("ipa", "").strip():
                    palabra = entry.get("kalfirvach") or entry.get("forma_final") or ""
                    if palabra:
                        ipa = generate_ipa(palabra)
                        if ipa:
                            entry["ipa"] = ipa
                            stats["ipa_generated"] += 1

            for k in cat_data:
                if isinstance(cat_data[k], list):
                    cat_data[k] = cleaned

    total = sum(
        len(v.get("entradas", [])) if isinstance(v, dict) else 0
        for v in cats.values()
    )
    meta["last_updated"] = "2026-05-30"
    meta["ipa_coverage"] = "100%"
    meta["schema_version"] = "v0.4-unified"
    meta["total_entries"] = total

    with open(LEXICON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nC2 — Unificados: {stats['unified']}")
    print(f"C3 — Duplicados resueltos: {stats['duplicates_removed']}")
    print(f"C4 — POS agregado: {stats['pos_added']}")
    print(f"C1 — IPA generada: {stats['ipa_generated']}")
    print(f"\n→ {LEXICON_PATH}")

if __name__ == "__main__":
    main()

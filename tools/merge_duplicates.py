#!/usr/bin/env python3
"""
merge_duplicates.py — Fusiona entradas duplicadas en el léxico Kalfírvach.

Non-destructivo: crea backup antes de modificar.
"""
import json, shutil
from pathlib import Path

LEXICON_PATH = Path(__file__).parent.parent / "kalfirvach_lexicon_v0.4_wip.json"
BACKUP_PATH = LEXICON_PATH.with_suffix(".json.bak.merge")


def find_entry(cats, category, word_key):
    entries = cats[category].get("entradas", [])
    for i, e in enumerate(entries):
        w = (e.get("kalfirvach") or e.get("forma_final") or "").strip()
        if w == word_key:
            return i, e
    return None, None


def remove_entry(cats, category, index):
    entries = cats[category].get("entradas", [])
    if 0 <= index < len(entries):
        removed = entries.pop(index)
        print(f"  → Eliminada: {removed.get('kalfirvach') or removed.get('forma_final')} de [{category}]")
        return removed
    return None


def main():
    shutil.copy2(LEXICON_PATH, BACKUP_PATH)
    print(f"Backup: {BACKUP_PATH}")

    with open(LEXICON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    cats = data["kalfirvach_lexicon_v0.2"]["categorias"]
    changes = 0

    # ── 1. nur/núr ── ambos en naturaleza_y_elementos ──
    # Keep índice 0 (tiene origen real y derivaciones).
    # Enriquecer con concepto e IPA de índice 47.
    print("\n1. nur/núr → naturaleza_y_elementos")
    idx_keep, e_keep = 0, cats["naturaleza_y_elementos"]["entradas"][0]
    idx_del, e_del = 47, cats["naturaleza_y_elementos"]["entradas"][47]
    e_keep["concepto"] = "luz, claridad, iluminación"
    e_keep["ipa"] = "/nur/"
    e_keep["kalfirvach"] = "nur"
    e_keep["forma_final"] = "nur"
    if not e_keep.get("origen") or not e_keep["origen"].get("lengua"):
        e_keep["origen"] = e_del.get("origen") or e_keep.get("origen", {})
    remove_entry(cats, "naturaleza_y_elementos", idx_del)
    changes += 1

    # ── 2. wana ── naturaleza tiene concepto más rico ──
    print("\n2. wana → naturaleza_y_elementos ← seres_vivos_plantas")
    idx_svp, e_svp = find_entry(cats, "seres_vivos_plantas", "wana")
    idx_nat, e_nat = find_entry(cats, "naturaleza_y_elementos", "wana")
    if e_nat and e_svp is not None:
        if not e_nat.get("ipa") or e_nat["ipa"] in ("/wana/",):
            e_nat["ipa"] = "/ˈwa.na/"
        if not e_nat.get("pos"):
            e_nat["pos"] = "noun"
        remove_entry(cats, "seres_vivos_plantas", idx_svp)
        changes += 1
    else:
        print("  ⚠️  wana no encontrado en ambas categorías")

    # ── 3. maya/máya ── magia tiene origen y derivaciones ──
    print("\n3. maya/máya → magia_y_mitologia ← conceptos_espaciales_y_calidades")
    idx_ce, e_ce = find_entry(cats, "conceptos_espaciales_y_calidades", "maya")
    idx_mag, e_mag = find_entry(cats, "magia_y_mitologia", "máya")
    if e_mag and e_ce is not None:
        if e_ce.get("concepto") and len(e_ce["concepto"]) > len(e_mag.get("concepto", "")):
            e_mag["concepto"] = e_ce["concepto"]
        if e_ce.get("ipa") and e_ce["ipa"] == "/ˈmaja/":
            e_mag["ipa"] = "/ˈma.ja/"
        # Forma unificada sin acento
        e_mag["kalfirvach"] = "maya"
        e_mag["forma_final"] = "maya"
        remove_entry(cats, "conceptos_espaciales_y_calidades", idx_ce)
        changes += 1
    else:
        print("  ⚠️  maya/máya no encontrado en ambas categorías")

    # ── 4. shakti/shákti ── magia tiene origen y derivaciones ──
    print("\n4. shakti/shákti → magia_y_mitologia ← conceptos_espaciales_y_calidades")
    idx_ce, e_ce = find_entry(cats, "conceptos_espaciales_y_calidades", "shakti")
    idx_mag, e_mag = find_entry(cats, "magia_y_mitologia", "shákti")
    if e_mag and e_ce is not None:
        if e_ce.get("concepto") and len(e_ce["concepto"]) > len(e_mag.get("concepto", "")):
            e_mag["concepto"] = e_ce["concepto"]
        if e_ce.get("ipa") and e_ce["ipa"] == "/ˈʃakti/":
            e_mag["ipa"] = "/ˈʃak.ti/"
        e_mag["kalfirvach"] = "shakti"
        e_mag["forma_final"] = "shakti"
        remove_entry(cats, "conceptos_espaciales_y_calidades", idx_ce)
        changes += 1
    else:
        print("  ⚠️  shakti/shákti no encontrado en ambas categorías")

    # ── 5. banda ── verbo primario, sentido médico como derivación ──
    print("\n5. banda → verbos_basicos ← medicina_y_salud")
    idx_vb, e_vb = find_entry(cats, "verbos_basicos", "banda")
    idx_med, e_med = find_entry(cats, "medicina_y_salud", "banda")
    if e_vb and e_med is not None:
        derivs = e_vb.setdefault("derivaciones", [])
        deriv_entry = "vendaje, apósito — extensión médica (Persa band + Árabe ḍimāda)"
        if deriv_entry not in derivs:
            derivs.append(deriv_entry)
        remove_entry(cats, "medicina_y_salud", idx_med)
        changes += 1
    else:
        print("  ⚠️  banda no encontrado en ambas categorías")

    # ── 6. pada/pádá ── anatómico primario, tech como derivación ──
    print("\n6. pada/pádá → anatomia_y_cuerpo ← tecnologia")
    idx_anat, e_anat = find_entry(cats, "anatomia_y_cuerpo", "pada")
    idx_tech, e_tech = find_entry(cats, "tecnologia", "pádá")
    if e_anat and e_tech is not None:
        derivs = e_anat.setdefault("derivaciones", [])
        tech_deriv = "footer, pie de página — extensión tecnológica (informática)"
        if tech_deriv not in derivs:
            derivs.append(tech_deriv)
        remove_entry(cats, "tecnologia", idx_tech)
        changes += 1
    else:
        print("  ⚠️  pada/pádá no encontrado en ambas categorías")

    # ── 7. shita ── frío es semánticamente primario sobre invierno ──
    print("\n7. shita → conceptos_espaciales_y_calidades ← tiempo_domestico")
    idx_ce, e_ce = find_entry(cats, "conceptos_espaciales_y_calidades", "shita")
    idx_tp, e_tp = find_entry(cats, "tiempo_domestico", "shita")
    if e_ce and e_tp is not None:
        e_ce["concepto"] = "frío, invierno"
        origen_ce = e_ce.get("origen", {})
        origen_tp = e_tp.get("origen", {})
        if origen_ce and origen_tp:
            raiz_ce = origen_ce.get("raiz_original", "")
            raiz_tp = origen_tp.get("raiz_original", "")
            if raiz_tp and raiz_tp not in raiz_ce:
                origen_ce["raiz_original"] = f"{raiz_ce} / {raiz_tp}"
                origen_ce["lengua"] = "Sanscrito/Persa/Arabe"
        remove_entry(cats, "tiempo_domestico", idx_tp)
        changes += 1
    else:
        print("  ⚠️  shita no encontrado en ambas categorías")

    # ── 8. hima ── POS merge (noun+verb) en naturaleza ──
    print("\n8. hima → naturaleza_y_elementos ← verbos_basicos")
    idx_nat, e_nat = find_entry(cats, "naturaleza_y_elementos", "hima")
    idx_vb, e_vb = find_entry(cats, "verbos_basicos", "hima")
    if e_nat and e_vb is not None:
        e_nat["concepto"] = "nieve, helar, congelar"
        e_nat["pos"] = "noun, verb"
        origen_nat = e_nat.get("origen", {})
        origen_vb = e_vb.get("origen", {})
        if origen_nat and origen_vb:
            raiz_nat = origen_nat.get("raiz_original", "")
            raiz_vb = origen_vb.get("raiz_original", "")
            if raiz_vb and raiz_vb not in raiz_nat:
                origen_nat["raiz_original"] = f"{raiz_nat} / {raiz_vb}"
                origen_nat["lengua"] = "Sanscrito/Griego/Avestan"
        remove_entry(cats, "verbos_basicos", idx_vb)
        changes += 1
    else:
        print("  ⚠️  hima no encontrado en ambas categorías")

    with open(LEXICON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*50}")
    print(f"Fusiones realizadas: {changes}")
    print(f"Backup: {BACKUP_PATH}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()

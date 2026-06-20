#!/usr/bin/env python3
"""
Forja los 34 conceptos de gobierno/política/derecho.
Usa el motor forja_lexica_kfa.py con batch de múltiples rondas.
"""
import sys
sys.path.insert(0, '/var/home/anomxsst17/Escritorio/Kalfirvach_v1.3')

import json
import random
from forja_lexica_kfa import forjar, ForjaResult

BASE = '/var/home/anomxsst17/Escritorio/Kalfirvach_v1.3'

# =============================================================================
# DATOS DE ENTRADA: cada concepto con IPAs en persa, griego, tibetano
# =============================================================================

CONCEPTOS = [
    # (concepto, pos, ipa_persa, ipa_griego, ipa_tibetano)
    ("gobierno",              "sustantivo", "[dowˈlæt]", "[arˈxeː]", "[ɕuŋ˩˧]"),
    ("gobernar",              "verbo",     "[hoˈkuːmæt]", "[ˈar.xoː]", "[coŋ˥]"),
    ("estado / nación",       "sustantivo", "[keʃˈvæɾ]", "[po.liˈti.a]", "[cɛ˩˧ kʰap˥]"),
    ("autoridad",             "sustantivo", "[eɢteˈdɒːɾ]", "[ek.suːˈsi.a]", "[waŋ˩˧ tɕʰa˥]"),
    ("líder",                 "sustantivo", "[ɾæhˈbæɾ]", "[eː.ɣeˈmoːn]", "[ɡo˩˧ ʈʰi˥]"),
    ("rey / soberano",        "sustantivo", "[ʃɒːh]", "[ba.siˈleβs]", "[cɛ˩˧ po˥]"),
    ("consejo",               "sustantivo", "[ʃuːˈɾɒː]", "[βuːˈleː]", "[ka˥ ɕak˥]"),
    ("jefe / cabeza",         "sustantivo", "[ɾæˈʔiːs]", "[ˈar.xoːn]", "[tsʰo˥ tsin˩˧]"),
    ("política",              "sustantivo", "[siːjɒːˈsæt]", "[po.li.tiˈkeː]", "[tɕʰap˥ si˥]"),
    ("comunidad",             "sustantivo", "[dʒɒːmeˈʔe]", "[kyː.noːˈni.a]", "[tɕi˥ tsʰok˥]"),
    ("pueblo / gente",        "sustantivo", "[mæɾˈdom]", "[ˈdeː.mos]", "[mi˩˧ maŋ˥]"),
    ("ciudadano",             "sustantivo", "[ʃæhɾˈvænd]", "[poˈli.teːs]", "[mi˩˧ ke˥]"),
    ("derecho (civil)",       "sustantivo", "[hæɢɢ]", "[ˈði.kɛ.on]", "[tʰop˥ tʰaŋ˥]"),
    ("deber / obligación",    "sustantivo", "[væˈziːfe]", "[o.ɸiːˈleː]", "[ɡɛ̃˩˧ tʂʰi˥]"),
    ("libertad",              "sustantivo", "[ɒːzɒːˈdiː]", "[e.leβ.θeˈri.a]", "[raŋ˩˧ waŋ˥]"),
    ("decisión",              "sustantivo", "[tæsˈmiːm]", "[ˈkri.sis]", "[tʰak˥ tɕø˥]"),
    ("ley",                   "sustantivo", "[ɢɒːˈnuːn]", "[ˈno.mos]", "[ʈʰim˥]"),
    ("justicia",              "sustantivo", "[edɒːˈlæt]", "[ði.kɛ.oˈsyː.neː]", "[ʈʂaŋ˩˧ tẽ˥]"),
    ("juez",                  "sustantivo", "[ɢɒːˈziː]", "[kriˈteːs]", "[ʈʰim˥ pø̃˥]"),
    ("juzgar",                "verbo",     "[ɢæzɒːˈvæt]", "[ˈkri.noː]", "[ʈʰim˥ ʈʂʰi˩˧]"),
    ("culpa",                 "sustantivo", "[ɡoˈnɒːh]", "[ɛˈti.a]", "[ti˩˧ ka˥]"),
    ("sentencia / veredicto", "sustantivo", "[hokm]", "[aˈpo.ɸa.sis]", "[ʈʰim˥ tʰak˥]"),
    ("castigo",               "sustantivo", "[modʒɒːˈzɒːt]", "[ti.moːˈri.a]", "[ɲe˩˧ tɕʰɛ˥]"),
    ("crimen / delito",       "sustantivo", "[dʒoɾm]", "[ˈeŋ.kleː.ma]", "[ɲe˩˧ mi˥]"),
    ("multa",                 "sustantivo", "[dʒæˈɾiːme]", "[zeːˈmi.a]", "[tɕʰɛ˩˧ pa˥]"),
    ("prueba / evidencia",    "sustantivo", "[mædˈɾæk]", "[tekˈmeː.ri.on]", "[paŋ˥ tak˥]"),
    ("testigo",               "sustantivo", "[ʃɒːˈhed]", "[ˈmar.tys]", "[paŋ˥ po˥]"),
    ("votar",                 "verbo",     "[ɾæʔj dɒːˈdæn]", "[pseːˈɸi.zo.mɛ]", "[ø˩˧ tep˥]"),
    ("aprobar",               "verbo",     "[tæsˈviːb]", "[ðo.kiˈma.zoː]", "[tɕʰok˥ tɕʰa˥]"),
    ("prohibir",              "verbo",     "[mænʔ]", "[koːˈly.oː]", "[kak˥ tsu˩˧]"),
    ("permitir",              "verbo",     "[edʒɒːˈze]", "[e.piˈtre.poː]", "[tɕʰok˥ tʂø˥]"),
    ("acusar",                "verbo",     "[motaˈhæm]", "[ka.teː.ɣoˈre.oː]", "[cø̃˥ tsuk˩˧]"),
    ("defender / abogar",     "verbo",     "[deˈfɒːʔ]", "[a.po.loˈɣe.o.mɛ]", "[suŋ˩˧ cop˥]"),
    ("acuerdo / pacto",       "sustantivo", "[tævɒːˈfoɢ]", "[syɱ.foːˈni.a]", "[tʰỹ˩˧ pa˥]"),
]

# Lenguas fuente para la etimología
FUENTES = ["persa moderno", "griego koiné", "tibetano"]

def forjar_concepto(ipa_persa, ipa_griego, ipa_tibetano, concepto, rondas=8):
    """Forja un concepto: múltiples rondas, elige el mejor."""
    ipas = [ipa_persa, ipa_griego, ipa_tibetano]
    
    seen = {}
    for r in range(rondas):
        random.seed(random.randint(0, 2**32))
        results = forjar(ipas, concepto, num_candidates=600, top_n=8)
        for res in results:
            w = res.word
            if w not in seen or res.score > seen[w].score:
                seen[w] = res
    
    # Ordenar por score descendente
    sorted_words = sorted(seen.values(), key=lambda r: -r.score)
    return sorted_words[0] if sorted_words else None


def main():
    print("=" * 70)
    print("  FORJA LÉXICA — gobierno / política / derecho (34 conceptos)")
    print("=" * 70)
    
    resultados = []
    
    for i, (concepto, pos, ipa_p, ipa_g, ipa_t) in enumerate(CONCEPTOS, 1):
        best = forjar_concepto(ipa_p, ipa_g, ipa_t, concepto, rondas=8)
        
        if best:
            print(f"\n  [{i:2d}/34] {concepto:25s} → \033[1;36m{best.word:12s}\033[0m  "
                  f"(score: {best.score:.1f})  IPA: {best.prosody.get('ipa_estimate', '—')}")
            
            resultados.append({
                "kalfirvach": best.word,
                "concepto": concepto,
                "pos": pos,
                "ipa": best.prosody.get("ipa_estimate", ""),
                "origen": f"forjado desde {FUENTES[0]}, {FUENTES[1]}, {FUENTES[2]}",
                "transformacion": f"score {best.score:.1f} — silabeo: {best.prosody.get('syllabified', '—')}",
                "derivaciones": []
            })
        else:
            print(f"\n  ✗ [{i:2d}/34] {concepto:25s} → SIN RESULTADO")
    
    # Guardar resultados como JSON
    with open(f"{BASE}/resultados_gobierno.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'=' * 70}")
    print(f"  ✅ {len(resultados)}/{len(CONCEPTOS)} conceptos forjados")
    print(f"  Resultados guardados en resultados_gobierno.json")
    print(f"{'=' * 70}")

if __name__ == "__main__":
    main()

# Code Context

## Files Retrieved
1. `fonologia.md` (lines 226-268, 360-414) - stress rule (penultimate/retroceso) and writing system declared as Coptic.
2. `presentacion_v0.4.md` (lines 46-88) - writing system declared as Greek; summary of postpositions/evidentials.
3. `gramatica_v0.4.md` (lines 161-173, 283-302, 455-460) - evidential set, postpositions list, and number form for “3”.
4. `guia_aprendizaje_v0.4.md` (lines 33-80, 820-887, 924-936) - learner pronunciation/orthography, /dh/ pronunciation, and numerals/ordinals using “tri”.
5. `lexicon_v0.4.md` (lines 125-188) - numerals section with “tri”.
6. `kalfirvach_lexicon_v0.4_wip.json` (lines 1-17) - JSON root key “v0.2” vs metadata v0.4 and writing system.
7. `sephirot_v0.4.md` (entire file reviewed) - Sephirot naming rules and composition consistency check; no direct conflicts found.

## Key Code
**Writing system conflict**
- Phonology declares Coptic: `Kalfírvach se escribe con el **alfabeto copto**...` (`fonologia.md` 360-361).
- Presentation declares Greek: `Usamos el **alfabeto griego politónico**...` (`presentacion_v0.4.md` 46-47).
- Guide also declares Greek: `Kalfírvach usa el **alfabeto griego politónico**...` (`guia_aprendizaje_v0.4.md` 33-35).

**Evidential set conflict**
- Grammar evidentials: `-e, -on, -anu, -wah, -Ø` (`gramatica_v0.4.md` 161-173).
- Presentation evidentials: `-e, -o, -i, -a, -u` (`presentacion_v0.4.md` 81-82) → different forms and meanings.

**Postposition list conflict**
- Grammar postpositions: `-na, -te, -ra, -sya (gen), -ka (inst), -muk (dir)` (`gramatica_v0.4.md` 283-292).
- Presentation postpositions: `-na, -te, -ra, -sya (instrumental), -kar (causal)` (`presentacion_v0.4.md` 79-80) → roles and inventory differ.

**Numeral “3” inconsistency**
- Grammar uses **tiri**: `| 3 | tiri | /ˈti.ri/ | ...` (`gramatica_v0.4.md` 455-460).
- Guide uses **tri** in numerals/ordinals and examples (`guia_aprendizaje_v0.4.md` 820-887, 924-936).
- Lexicon uses **tri** (`lexicon_v0.4.md` 171-188).

**/dh/ pronunciation mismatch**
- Guide: `dh /dʱ/` (`guia_aprendizaje_v0.4.md` 69).
- Phonology: optional /ð/ phoneme and /dʱ/ appears only in loan adaptation (treated as /d/) (`fonologia.md` 395-399, 288-290).

**JSON metadata mismatch**
- JSON top-level key: `kalfirvach_lexicon_v0.2` while metadata says version `0.4` (`kalfirvach_lexicon_v0.4_wip.json` 1-5).

**Stress rule clarity**
- Phonology defines penultimate with retroceso if light syllable (`fonologia.md` 230-248).
- Guide says “acento siempre se marca con tilde aguda” without explaining retroceso or exceptions (`guia_aprendizaje_v0.4.md` 71-78).

## Architecture
- **Phonology (v0.2)** defines the phoneme inventory, phonotactics, stress, and writing system. It is the authoritative source for sound patterns.
- **Grammar (v0.4)** defines syntax, morphology, particles, and numerals; intended as the definitive structural spec.
- **Guide (v0.4)** is a didactic layer for learners; it should mirror phonology/grammar decisions but currently diverges in orthography, numerals, and phoneme descriptions.
- **Presentation (v0.4)** is a high-level overview and marketing doc; it must align with grammar/phonology but currently includes older or simplified rules (evidentials, postpositions).
- **Lexicon (md/json, v0.4)** provides lexical inventory and should be consistent with grammar numerals and writing system.
- **Sephirot document** is a thematic application of the lexicon and morphology; it appears consistent but depends on stable orthography and phonology.

## Findings & Improvement Suggestions
1. **Unify writing system (Greek vs Coptic).** Decide one canonical script or define two explicit orthographies with conversion rules. Update `fonologia.md`, `presentacion_v0.4.md`, and `guia_aprendizaje_v0.4.md` to match. If dual, add a dedicated “Ortografías” section explaining when each is used.
2. **Fix evidential inventory mismatch.** Presentation uses an outdated 5-vowel evidential set; align it with grammar’s `-e/-on/-anu/-wah/-Ø` or clearly mark as historical. Add a quick reference table in `presentacion_v0.4.md` matching grammar.
3. **Normalize postpositions.** Presentation claims `-sya` instrumental and `-kar` causal; grammar says `-sya` genitive and `-ka` instrumental, with causality handled by `kar` conjunction. Update presentation and guide to match grammar, and consider adding a causal postposition only if intended.
4. **Resolve numeral “3” form.** Choose **tri** or **tiri**; then update grammar numerals, guide exercises, and lexicon entries accordingly. If both are allowed (colloquial vs ritual), document the register split and add derivation rules.
5. **Clarify /dh/ phoneme.** Guide describes /dʱ/ while phonology uses /ð/ and treats /dʱ/ as a loan simplification. Pick one: if /ð/ is the optional phoneme, rename the digraph or clarify allophones and update examples.
6. **Stress rule consistency.** Guide should include the penultimate/retroceso rule and clarify when stress is marked. Consider a brief “stress exceptions” box referencing phonology and a minimal set of marked examples.
7. **JSON metadata cleanup.** Rename the JSON root key to `kalfirvach_lexicon_v0.4` or add a `schema_version` field explaining the mismatch. Ensure docs consume the same key.
8. **Missing sections for completeness.**
   - Add a short “Registro ceremonial” section in grammar/guide explaining optional phonemes and ritual phonetics (phonology hints at it).
   - Provide a canonical “Morphophonemics” mini-section (assimilation, elision) in grammar or link to phonology.
   - Add a “Versioning and compatibility” note in presentation to clarify that phonology is v0.2 while grammar/lexicon are v0.4.

## Start Here
Open `presentacion_v0.4.md` first. It contains the highest-level summary and currently diverges from grammar/phonology on writing system, evidentials, and postpositions, so fixing it will cascade into consistent public-facing docs.

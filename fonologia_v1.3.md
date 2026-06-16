---
title: "Kalfírvach v1.3 — Fonología"
version: v1.3
date: 2026-06-06
lang: es
status: stable
---

# KALFÍRVACH v1.3 — Fonología

## 1. Metodología de construcción

El inventario fonémico de Kalfírvach se construye por **intersección ponderada** de los sistemas fonológicos de las seis lenguas fuente, restringidas a sus corpus esotéricos:

| # | Lengua | Corpus esotérico |
|---|--------|-----------------|
| 1 | Griego koiné/helenístico | Corpus Hermeticum, PGM, neoplatónicos, gnósticos |
| 2 | Sánscrito tántrico | Tantras (Kaula, Trika), Āgamas, Mantraśāstra |
| 3 | Egipcio (demótico/antiguo) | Textos pirámide (heka), PGM (sección egipcia), Edfu/Dendera |
| 4 | Persa/avéstico | Avesta (Gathas, Yashts), mitraísmo, poesía metafísica |
| 5 | Tibetano clásico | Tantras budistas, Dzogchen, tradición Milarepa |
| 6 | Árabe esotérico | Ilm al-Huruf (Ibn ʿArabī, al-Būnī), hurufismo |

**Criterio de selección:**
- Fonema en ≥3 lenguas → **núcleo obligatorio**
- Fonema en 2 lenguas → **núcleo opcional** (flag `cross_lingual: true`)
- Fonema en 1 lengua → **excluir**, salvo alta densidad esotérica documentada

---

## 2. Inventario fonémico núcleo

### 2.1 Vocales

El sistema vocálico de Kalfírvach es un sistema de **5 vocales**, presente en las 6 lenguas fuente:

| Fonema IPA | Grafía | Frecuencia cruzada | Lenguas fuente |
|-----------|--------|-------------------|---------------|
| /a/ | a | 6/6 | Griego, Sánscrito, Egipcio, Avestan, Tibetano, Árabe |
| /e/ | e | 5/6 | Griego, Sánscrito, Avestan, Persa, Tibetano |
| /i/ | i | 6/6 | Griego, Sánscrito, Egipcio, Avestan, Tibetano, Árabe |
| /o/ | o | 5/6 | Griego, Sánscrito, Avestan, Persa, Tibetano |
| /u/ | u | 6/6 | Griego, Sánscrito, Egipcio, Avestan, Tibetano, Árabe |

**Justificación:** Las 5 vocales cardinales constituyen el sistema más estable y ampliamente compartido entre las lenguas fuente. El Sánscrito y el Avestan poseen vocales adicionales (/ṛ/, /ḷ/, /ə/, nasalizadas), pero estas son tipológicamente marcadas y ausentes en la mayoría de las otras tradiciones. El egipcio reconstruye solo /a, i, u/ con certeza, pero /e/ y /o/ aparecen como alófonos y en préstamos posteriores. Se prioriza la universalidad de pronunciación para hablantes globales.

### 2.1.b Cantidad vocálica fonémica

Kalfírvach **distingue fonémicamente** /a, e, i, o, u/ de /aː, eː, iː, oː, uː/. La cantidad vocálica NO es predecible por regla silábica — pertenece al léxico. En transcripción latina, las vocales largas se marcan con macrón: ā, ē, ī, ō, ū.

**Justificación cross-lingüística:** Aunque el koiné tardío neutralizó la cantidad, las lenguas fuente con corpus esotérico la preservan:

| Fonema largo | Fuentes | Lenguas |
|-------------|---------|---------|
| /aː/ (ā) | Sánscrito आ (ā), Árabe ا (alif + fatḥa → /aː/), Avestan ā | 3/6 |
| /iː/ (ī) | Sánscrito ई (ī), Árabe ي (yā' con kasra → /iː/), Avestan ī | 3/6 |
| /uː/ (ū) | Sánscrito ऊ (ū), Árabe و (wāw con ḍamma → /uː/), Avestan ū | 3/6 |
| /eː/ (ē) | Avestan ē, Préstamos sánscritos con e larga | 2/6 |
| /oː/ (ō) | Avestan ō, Préstamos sánscritos con o larga | 2/6 |

/eː/ y /oː/ son núcleo opcional (2 lenguas), pero se documentan por su presencia en el léxico existente.

**Regla de posición (vinculante para expansión léxica):**

Una vocal larga SOLO puede aparecer en las siguientes posiciones. Cualquier entrada nueva que use macrón debe cumplir AL MENOS UNA:

1. **Monosílabo léxico**: raíz monosílaba de contenido pleno (verbo, nombre, adjetivo). NO aplica a partículas gramaticales (`cha`, `de`, `fu`, `la`, `o`, `ti`, `tu`, `va`, `ya`, etc.).
   - Ejemplos: `bīj`, `kīr`, `mēr`, `rūt`, `yū`, `thī`
   - NO: `bas`, `dzun`, `chal`, `mar`

2. **Sílaba acentuada**: la vocal de la sílaba que lleva el acento tónico.
   - Ejemplos: `dārchē` /ˈdaːr.tʃeː/ (ā acentuada), `gīra` /ˈgiː.ra/ (ī acentuada), `nāyak` /ˈnaː.jak/ (ā acentuada)

3. **Sílaba final abierta**: la última vocal de la palabra, en sílaba abierta (termina en vocal).
   - Ejemplos: `adarī` /ˈa.da.riː/ (ī final), `tōdā` /ˈtoː.daː/ (ā final), `gashgī` /ˈgaʃ.giː/ (ī final)

**Restricción adicional:** Una palabra puede tener hasta DOS vocales largas, siempre que una esté en la sílaba acentuada (regla 2) y la otra en la sílaba final abierta (regla 3). Ejemplo: `tōdā` /ˈtoː.daː/, `dārchē` /ˈdaːr.tʃeː/. No se permiten tres o más vocales largas sin documentación etimológica expresa de cada una.

**Pronunciación:**

| Grafía | IPA | Como en español...  | Pero... |
|--------|-----|--------------------|---------|
| a | /a/ | **a**mo | Duración normal |
| ā | /aː/ | **a**mo | Sostené la **a** el doble de tiempo |
| e | /e/ | p**e**so | Normal |
| ē | /eː/ | p**e**so | Sostené la **e** |
| i | /i/ | p**i**so | Normal |
| ī | /iː/ | p**i**so | Sostené la **i** |
| o | /o/ | p**o**so | Normal |
| ō | /oː/ | p**o**so | Sostené la **o** |
| u | /u/ | p**u**ro | Normal |
| ū | /uː/ | p**u**ro | Sostené la **u** |

La diferencia no es de timbre (no suenan a otra vocal), solo de **duración**. Un hispanohablante ya produce vocales largas inconscientemente cuando énfatiza una palabra — en KFA esa duración extra es léxica y contrastiva.

**Contraste mínimo (evidencia fonémica):**
- `bīj` /biːj/ "semilla/principio" vs. una hipotética `bij` /bij/ (no existe en el léxico actual, pero ilustra que la longitud puede crear pares mínimos)
- `rūt` /ruːt/ "raíz" vs. `rut` /rut/ (no existe en el léxico actual)
- En la práctica, la longitud suele ir acompañada de diferencias consonánticas o silábicas, pero el contraste existe y debe respetarse en la transcripción y pronunciación.

**⚠️ Regla de contención para generación de nuevo léxico:**

En futuras expansiones, NO se pueden añadir macrones por razones estéticas, por "sonoridad" o por imitación de lenguas fuente sin verificar. Toda nueva entrada con āēīōū debe justificarse por UNA de las 3 posiciones de arriba. Si no cumple ninguna, la vocal debe ser breve. Esta regla es vinculante para generación asistida y revisión humana.

### 2.2 Consonantes obligatorias (≥3 lenguas)

| Punto/Modo | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Velar | Uvular | Glotal |
|-----------|----------|-------------|--------|----------|--------------|-------|--------|--------|
| Oclusiva sorda | p | | t | | | k | | |
| Oclusiva sonora | b | | d | | | ɡ | | |
| Africada sorda | | | | | tʃ | | | |
| Africada sonora | | | | d͡z | | | | |
| Fricativa sorda | | f | θ | s | ʃ | x | | h |
| Fricativa sonora | | | | z | | ɣ | | |
| Nasal | m | | | n | | | | |
| Vibrante/Líquida | | | | r, l | | | | |
| Aproximante | w | | | | j | | | |

**Total: 22 consonantes** (21 obligatorias + /d͡z/ como africada sonora, justificada por 2 lenguas con densidad esotérica)

#### Detalle por fonema con documentación cruzada:

| Fonema | Grafía | # Lenguas | Detalle |
|--------|--------|-----------|---------|
| /p/ | p | 6/6 | Griego π, Sánscrito p, Egipcio p, Avestan p, Tibetano p, Árabe (préstamo) |
| /b/ | b | 6/6 | Griego β (antigua /b/), Sánscrito b, Egipcio b, Avestan b, Tibetano b, Árabe b |
| /t/ | t | 6/6 | Universal en las 6 tradiciones |
| /d/ | d | 6/6 | Griego δ (antigua /d/), Sánscrito d, Egipcio d, Avestan d, Tibetano d, Árabe d |
| /k/ | k | 6/6 | Universal |
| /ɡ/ | g | 6/6 | Griego γ (antigua /ɡ/), Sánscrito g, Egipcio g, Avestan g, Tibetano g, Árabe (préstamo/ɣ) |
| /f/ | f | 3/6 | Griego φ→/f/ (koiné), Árabe f, Persa f |
| /s/ | s | 6/6 | Universal |
| /z/ | z | 6/6 | Griego ζ, Sánscrito z (jhā→z), Tibetano z, Árabe z, Avestan z, Persa z |
| /ʃ/ | sh | 4/6 | Sánscrito ś, Árabe ش, Avestan š, Persa ش |
| /x/ | kh | 4/6 | Griego χ→/x/, Árabe خ, Avestan x, Persa خ |
| /ɣ/ | gh | 4/6 | Griego γ→/ɣ/, Árabe غ, Avestan ɣ, Persa غ |
| /h/ | h | 4/6 | Sánscrito h, Árabe ه, Avestan h, Tibetano h |
| /θ/ | th | 3/6 | Griego θ→/θ/ (koiné), Árabe ث, Avestan θ |
| /m/ | m | 6/6 | Universal |
| /n/ | n | 6/6 | Universal |
| /r/ | r | 6/6 | Universal |
| /l/ | l | 6/6 | Universal |
| /w/ | w | 4/6 | Sánscrito v/w, Árabe و, Avestan v, Griego (digamma) |
| /j/ | y | 6/6 | Griego ι (como semivocal), Sánscrito y, Árabe ي, Avestan y, Tibetano y, Persa y |
| /tʃ/ | ch | 4/6 | Sánscrito च (ca) → /tʃ/, Tibetano ཅ (ca) → /tʃ/, Persa چ (če) → /tʃ/, Avestan (c) → /tʃ/. 4 lenguas. |
| /d͡z/ | dz | 2/6 | Tibetano ཛ (dza) → /d͡z/ (en tantras y dzogchen); Griego ζ (ático clásico → /dz/, preservado en contextos rituales PGM). La contraparte sonora de /tʃ/. |

### 2.3 Consonantes opcionales (2 lenguas, `cross_lingual: true`)

| Fonema | Grafía | # Lenguas | Detalle | Uso en Kalfírvach |
|--------|--------|-----------|---------|----------------------|
| /ð/ | dh | 2/6 | Griego δ→/ð/ (koiné), Árabe ذ | Solo en préstamos documentados de estas lenguas |
| /v/ | v | 2/6 | Griego β→/v/ (koiné tardía), Persa v | Alternante con /w/ en posición intervocálica |
| /q/ | q | 2/6 | Árabe ق, Avestan q (marginal) | Solo en términos de tradición árabe/avéstica |
| /ʔ/ | ' | 2/6 | Árabe ء, Egipcio (reconstruido) | Solo antes de ataque vocálico absoluto; no fonémico en la mayoría de contextos |
| /ŋ/ | ng | 2/6 | Sánscrito (anusvāra), Tibetano (sufijo) | Solo como alófono de /n/ ante velar |


### 2.4 Fonemas excluidos (1 lengua) con justificación

| Fonema | Lengua | Razón de exclusión | Densidad esotérica |
|--------|--------|--------------------|--------------------|
| Retroflejos /ʈ, ɖ, ɳ, ɭ, ʂ/ | Sánscrito | 1 lengua; tipológicamente marcados | ALTA en Mantraśāstra (śiva-sūtra) |
| Aspirados sonoros /bʱ, dʱ, ɡʱ/ | Sánscrito | 1 lengua; extremadamente raros globalmente | MEDIA en mantra |
| Eyectivas /pʼ, tʼ, kʼ/ | Egipcio | 1 lengua; reconstrucción incierta | MEDIA en heka |
| Faringalizados /tˤ, sˤ, dˤ, ðˤ/ | Árabe | 1 lengua; muy marcados | ALTA en Ilm al-Huruf |
| /ħ, ʕ/ | Árabe, Egipcio | 2 lenguas pero altamente marcados | ALTA en ambas tradiciones |

**Decisión sobre fonemas de alta densidad esotérica excluidos:** Se documenta su existencia y su valor ritual en las tradiciones fuente, pero se excluyen del núcleo por razones de **accesibilidad fonética global**. El conlang debe ser pronunciable por hablantes de cualquier lengua materna. En contextos rituales avanzados (v0.2+), se podrá introducir un **registro ceremonial** que incorpore fonemas marcados como variantes estilísticas opcionales.

---

## 3. Fonotáctica

### 3.1 Estructura silábica

La plantilla silábica básica de Kalfírvach es:

```
(C₁)(G)V(C₂)
```

Donde:
- **C₁** = consonante inicial (cualquier consonante del inventario obligatorio)
- **G** = glide: /w/ o /j/
- **V** = vocal nuclear (cualquier vocal del inventario)
- **C₂** = consonante final (restringida — ver §3.3)

**Sílabas posibles:**
- V → a, e, i, o, u
- CV → pa, te, ki, shu, mo
- CGV → pwa, tya, kwe, shya
- CVC → par, ten, kish, mul
- CGVC → pwar, tyal, kwesh

### 3.2 Restricciones onciales

**C₁ permitido:** Toda consonante obligatoria puede ocupar la posición de ataque silábico.

**Clusters onciales permitidos — dos categorías:**

**Categoría A: C₁ + glide (G = /w, j/):**

| C₁ | + /w/ | + /j/ |
|----|-------|-------|
| /p/ | pwa ✓ | pya ✓ |
| /b/ | bwa ✓ | bya ✓ |
| /t/ | twa ✓ | tya ✓ |
| /d/ | dwa ✓ | dya ✓ |
| /k/ | kwa ✓ | kya ✓ |
| /ɡ/ | gwa ✓ | gya ✓ |
| /f/ | fwa ✓ | fya ✓ |
| /s/ | swa ✓ | sya ✓ |
| /ʃ/ | shwa ✓ | shya ✓ |
| /tʃ/ | chwa ✓ | chya ✓ |
| /d͡z/ | dzwa ✓ | dzya ✓ |
| /x/ | khwa ✓ | khya ✓ |
| /m/ | mwa ✓ | mya ✓ |
| /n/ | nwa ✓ | nya ✓ |

**Categoría B: C₁ + líquida (L = /r, l/):**

| C₁ | + /r/ | + /l/ |
|----|-------|-------|
| /p/ | pra ✓ | pla ✓ |
| /b/ | bra ✓ | bla ✓ |
| /t/ | tra ✓ | tla ✓ |
| /d/ | dra ✓ | dla ✓ |
| /k/ | kra ✓ | kla ✓ |
| /ɡ/ | gra ✓ | gla ✓ |
| /f/ | fra ✓ | fla ✓ |
| /s/ | —    | sla ✓¹ |
| /ʃ/ | shra ✓ | —    |
| /θ/ | thra ✓ | thla ✓² |
| /x/ | khra ✓ | —    |
| /tʃ/ | —    | —    |
| /m/ | —    | mla ✓² |
| /n/ | —    | nla ✓² |

¹ `sl-` permitido solo en préstamos documentados (eslavo, sánscrito).
² Patrón marginal (< 2% del corpus); se permite sin restringir.

Los clusters de C+líquida aparecen naturalmente en préstamos del sánscrito (`kriyā`, `prati`, `śrī`) y del griego (`pneum-`, `drama`, `krist-`), y son consistentes con §10.2 (Silabificación).

**Excepción — `gn-`**: el cluster /gn-/ (oclusiva velar sonora + nasal alveolar) se permite exclusivamente en préstamos rituales y técnicos del griego (`gnōsis`, `gnōthi`, `gnomon`, `gnōrisma`) y del sánscrito (`jñāna` → `gnāna`), con la misma justificación que C+líquida: el peso del corpus esotérico greco-sánscrito justifica expandir el inventario oncial. El onset /gn-/ funciona como una unidad indivisible a efectos de silabificación (§10.2) y acentuación (§9.2). Los demás clusters oclusiva+nasal (*/pn-/, */kn-/, */tm-/) siguen prohibidos y deben adaptarse por epéntesis (§10.5).

**Clusters onciales PROHIBIDOS (en toda posición):**
- Cualquier secuencia de dos oclusivas: */pt-/, */kt-/, */gd-/
- Oclusiva + nasal: */pn-/, */kn-/, */tm-/ (excepto `gn-`, ver excepción arriba)
- Fricativa + oclusiva (excepto /s/ + oclusiva en préstamos sánscritos — adaptar): */ft-/, */xk-/
- Líquida + oclusiva (orden inverso): */rp-/, */lk-/, */rt-/
- Nasal + líquida: */mr-/, */nl-/
- Dos consonantes iguales: */pp-/, */ss-/
- Tres o más consonantes sin vocal intermedia

**Justificación tipológica:** Las restricciones anteriores reflejan la intersección de las restricciones fonotácticas de las lenguas fuente. El sánscrito y el griego permiten tanto C+glide como C+líquida; el árabe y el egipcio prohíben clusters onciales complejos. Kalfírvach adopta C+glide como patrón universal (compatible con las 6 tradiciones) y C+líquida como patrón expandido, justificado por el peso del sánscrito y el griego en el corpus esotérico. A estas se suma la excepción `gn-` (oclusiva velar + nasal), documentada arriba, con la misma justificación. Esta decisión alinea §3.2 con §10.2.

### 3.3 Restricciones codiciales

**C₂ permitido en coda:** Solo los siguientes fonemas pueden cerrar sílaba:

| Fonema | Grafía | Ejemplo |
|--------|--------|---------|
| /r/ | r | θar "fuego interior" |
| /l/ | l | kal "hipótesis" |
| /n/ | n | θen "ritual" |
| /m/ | m | sham "sombra" |
| /s/ | s | thes "acto volitivo" |
| /ʃ/ | sh | kash "símbolo" |
| /tʃ/ | ch | vach "palabra ritual" |
| /k/ | k | shak "duda ritual" |
| /x/ | kh | nukh "sabiduría" |
| /h/ | h | mah "luna/medida" |
| /p/ | p | (ensordecimiento de /b/ en coda) |
| /t/ | t | gachat "él va" |
| /ʔ/ | ' | (solo en hiato) |

**C₂ PROHIBIDO en coda:**
- Oclusivas sonoras: /b, d, ɡ/ (se ensordecen: /b/→/p/, /d/→/t/, /ɡ/→/k/)
- Fricativas sonoras: /z, ɣ/ (se ensordecen: /z/→/s/, /ɣ/→/x/)
- /θ, ð/ (se neutralizan: /θ, ð/ → /s/ en coda; /tʃ/ se conserva como /ʃ/ en variantes coloquiales)
- /f/ — /f/ → /p/ en coda opcionalmente, o se pierde
- /w, j/ (los glides en coda generan diptongos, tratados como V larga)

**Justificación:** Esta restricción refleja una tendencia universal de ensordecimiento codicial presente en la mayoría de las lenguas fuente (tibetano: coda siempre sorda; alemán, ruso, sánscrito parcial). Simplifica la fonología y aumenta la distintividad.

### 3.4 Diptongos

Los únicos diptongos permitidos son los formados por V + glide en coda:

| Diptongo | Grafía | Como sílaba |
|----------|--------|-------------|
| /aj/ | ay | CVC (C₂=j) |
| /aw/ | aw | CVC (C₂=w) |
| /ej/ | ey | CVC |
| /ow/ | ow | CVC |

Diptongos como /ij/, /uw/, /oj/, /ew/ son posibles pero infrecuentes. **No se permiten diptongos inversos** (/ja/, /wa/ en núcleo) — estas secuencias se analizan como C+jV o C+wV (sílaba CGV).

### 3.5 Asimilación y elisión

#### 3.5.1 Asimilación nasal
- /n/ + consonante velar → /ŋ/ (escrito ng): an + kal → angkal
- /n/ + consonante bilabial → /m/: an + pa → ampa
- /n/ + consonante labiodental → /m/: an + fari → amfari

#### 3.5.2 Asimilación de sonoridad en contacto codicial-oncial
Cuando una coda sorda contacta con una consonante oncial sonora, o viceversa:
- Coda + Oclusiva sonora → la oclusiva se ensordece: kat + bala → katpala
- Coda nasal + Oclusiva → la oclusiva conserva sonoridad: tan + ka → tanka

#### 3.5.3 Elisión vocálica
- Dos vocales idénticas en contacto (a+a, e+e, etc.) se reducen a una: thea + an → thean (no *theaan)
- Vocal alta /i, u/ entre dos consonantes idénticas se elide: kati + isha → katisha (sin elisión, consonantes distintas)

#### 3.5.4 Armonía vocálica
Kalfírvach **no posee armonía vocálica** estricta. Sin embargo, se aplica una **armonía de resonancia** opcional en composición:

- Cuando dos raíces se combinan, si la primera raíz contiene solo vocales abiertas (/a, e, o/), la /i/ o /u/ de la segunda raíz puede abrirse a /e/ o /o/ respectivamente en habla ritual:
  - Standard: man + rikh → manrikh
  - Ritual: man + rikh → manrekh (apertura vocálica)

Esta armonía es **opcional y estilística**, no obligatoria.

#### 3.5.5 Apócope derivativa

Regla **productiva y obligatoria**: la vocal final `-e` de un tema nominal o adjetival se **elide** ante una consonante derivativa (sufijo nominalizador, composicional, o formador de adjetivo).

**Entorno fonológico:** `tema` que termina en `-e` (vocal media abierta) + `sufijo` que comienza con consonante (no vocal).

**Transformación:** `-e + C → -∅ + C` (apócope; la `-e` se pierde sin marca, sin alargamiento compensatorio).

**Ejemplos canónicos (de la derivación documentada en lexicón):**
- `θéle` (voluntad) + `-tár` (sufijo agente) → `θel-tár` (practicante-de-la-voluntad)
- `θéle` + `-ká` (sufijo adjetival) → `θel-ká` (volitivo)
- `θéle` + `-shá` (sufijo locativo-santuario) → `θel-shá` (santuario-de-la-voluntad)
- `θéle` + `-ník` (sufijo instrumental) → `θel-ník` (instrumento-de-voluntad)

**Justificación morfológica:** la apócope evita contacto vocálico `-e.C-` que violaría §3.3.1 (restricciones codiciales: coda máxima una consonante). Sin apócope, `θéle-tár` daría `θé.le.tár` con `-e-` en posición intervocálica, no coda.

**Excepciones:**
- La apócope **no se aplica** ante vocal (se conserva la `-e` como enlace: `θéle-ai` para "voluntad-este").
- La apócope **no aplica** a temas que terminan en `-a` o `-o` (éstos conservan su vocal final: `fír-a` se mantiene).
- Temas con `-e` paragógica (insertada fonotácticamente, no morfológica) **no** sufren apócope.

**Cross-ref:** documentada por primera vez para evitar la colisión `θel`/`θele` (ver lexicón F1.3). Las 4 derivaciones arriba son las documentadas en `conceptos_espaciales_y_calidades.entradas` (que pasan a usar la forma apocopada `thel-` consistentemente en sus derivaciones).

---

## 4. Acentuación

### 4.1 Regla general

El acento de intensidad recae sobre la **penúltima sílaba** de la palabra:

| Palabra | Sílaba acentuada | Transcripción |
|---------|-----------------|---------------|
| θéle | θé-le | "voluntad" |
| thesís | the-sís | "acto de voluntad" |
| mántrik | mán-trik | "ritual" |
| kalésha | ka-lé-sha | "transformación" |

### 4.2 Excepciones

**Palabras monosilábicas:** No llevan acento marcado (se pronuncian con peso igual).

**Palabras con penúltima sílaba ligera:** Si la penúltima sílaba es ligera (CV sin coda y con vocal breve), el acento **retrocede** a la antepenúltima sílaba:

| Palabra | Estructura | Acento |
|---------|-----------|--------|
| kámita | CV-CV-CV | kámita (penúltima ligera → antepenúltima) |
| theláyon | CV-CVC-CVC | theláyon (penúltima pesada → penúltima) |

**Sílaba pesada** = CVC, CVV (con diptongo), o CV con vocal larga.
**Sílaba ligera** = CV con vocal breve.

### 4.3 Justificación

| Patrón | Lenguas que lo exhiben |
|--------|----------------------|
| Acento en penúltima | Griego (limitado a 3 últimas), Sánscrito (variable, pero penúltima pesada atrae acento), Persa (estrés final, pero compuestos en penúltima) |
| Retroceso con sílaba ligera | Sánscrito (regla de peso silábico para acento), Griego (mora-counting) |
| Acento de intensidad | Griego koiné tardío, Persa, Árabe, Tibetano |

El sistema de acento por peso silábico (penúltima con retroceso) está tipológicamente justificado por el Griego y el Sánscrito, las dos tradiciones con sistemas acentuales más desarrollados. Es además fonéticamente natural y fácil de aprender.

### 4.4 Acento en composición

En palabras compuestas (raíz + raíz), el acento principal recae sobre la **penúltima sílaba del compuesto entero**, como si fuera una palabra simple:

- mur (muro) + fír (fuego) → m**úr**fir → murfír → m**ur**fír → murf**ír** (penúltima del compuesto)
- θel (voluntad) + kár (acción) → thelk**ár**

---

## 5. Adaptación de préstamos

### 5.1 Principios

Todo préstamo de una lengua fuente debe pasar por el **Filtro de Homogeneización**:

1. **Filtrado fonémico:** Reemplazar fonemas ajenos al núcleo por el equivalente más cercano
2. **Filtrado fonotáctico:** Ajustar clusters y estructura silábica al patrón (C)(G)V(C)
3. **Filtrado acentual:** Aplicar regla de acento en penúltima

### 5.2 Tabla de sustitución fonémica

| Fonema original | Lengua | Sustitución en LA | Ejemplo |
|----------------|--------|-------------------|---------|
| /ʈ/ (retrofleja) | Sánscrito | /t/ | tanma → tanma |
| /ɖ/ (retrofleja) | Sánscrito | /d/ | ḍamaru → damaru |
| /ʂ/ (retrofleja) | Sánscrito | /ʃ/ | śiva → shiva |
| /bʱ/ (aspirada sonora) | Sánscrito | /b/ | bhrānti → branti |
| /dʱ/ | Sánscrito | /d/ | dhyāna → dyana |
| /tˤ/ (faringalizada) | Árabe | /t/ | ṭarīq → tarik |
| /sˤ/ | Árabe | /s/ | ṣirāṭ → sirat |
| /ħ/ | Árabe, Egipcio | /h/ | ḥikma → hikma |
| /ʕ/ | Árabe, Egipcio | /ʔ/ o se pierde | ʿirfān → irfan |
| /q/ | Árabe | /k/ (si préstamo asimilado) o /q/ (si término técnico árabe) | qalb → kalb |
| /ɮˤ/ (ḍād clásica) | Árabe | /d/ | ḍiyā' → diya |

### 5.3 Ejemplos de adaptación

| Palabra original | Lengua | Forma intermedia | Forma final LA | Cambios aplicados |
|-----------------|--------|-----------------|---------------|------------------|
| θέλημα (thélēma) | Griego | θelema | θéle | elisión de -ma (sufijo nominal); /θ/ se mantiene; acento en penúltima |
| शक्ति (śakti) | Sánscrito | shakti | shákti | /ʂ/→/ʃ/; acento en penúltima |
| ḥkꜣ (heka) | Egipcio | heka | héka | /ħ/→/h/; vocal epentética; acento en penúltima |
| xᵛarənah | Avestan | xwaranah | khwára | /xʷ/→/kw/ (C+G); /ə/→/a/; elisión de -nah; acento penúltima |
| rig pa | Tibetano | rigpa | ríga | /p/ intervocálica se debilita→/g/; acento penúltima |
| حكمة (ḥikma) | Árabe | hikma | híkma | /ħ/→/h/; acento penúltima |

---

## 6. Resumen fonológico BNF

```
<silaba>    ::= (<onset>) <nucleo> (<coda>)
<onset>     ::= <consonante> | <consonante> <glide>
<nucleo>    ::= <vocal> | <diptongo>
<coda>      ::= <consonante_coda>

<consonante> ::= "p" | "b" | "t" | "d" | "k" | "g"
               | "f" | "s" | "z" | "sh" | "kh" | "gh" | "h" | "th"
               | "ch"
               | "m" | "n" | "r" | "l" | "w" | "y" | "j"
<glide>     ::= "w" | "y" | "j"
<vocal>     ::= "a" | "e" | "i" | "o" | "u"
<diptongo>  ::= "ay" | "aw" | "ey" | "ow"

<consonante_coda> ::= "r" | "l" | "n" | "m" | "s" | "sh" | "ch" | "k" | "kh" | "h" | "p" | "t"

<palabra>   ::= <silaba>+  (mínimo 1, máximo 4 sílabas recomendado)
<acento>    ::= penúltima sílaba (retrocede si ligera)
```

---

## 7. Inventario fonémico completo (resumen visual)

```
VOCALICO:   a   e   i   o   u

OCLUSIVAS:  p   b   t   d   k   g

AFRICADAS:  ch

FRICATIVAS: f   th  s   z   sh  kh  gh  h

NASALES:    m   n

LIQUIDAS:   r   l

GLIDES:     w   y   (j equiv. a y)

TOTAL: 5 vocales + 21 consonantes = 26 fonemas nucleares
        + 5 consonantes opcionales (dh, v, q, ', ng) = 31 fonemas máximo

> **Nota:** 'j' en LA se usa como variante gráfica de 'y' para /j/ (ver §8.2).
> **Nota:** /tʃ/ (ch) es coda válida — ver §3.3 y gramática §3.3.
```

---

## 8. Correspondencia con la escritura griega politónica

Kalfírvach se escribe con el **alfabeto griego politónico**, usando letras arcaicas cuando hace falta. En este documento se utiliza **transcripción latina (LA)** por claridad tipográfica. La ortografía griega es una transliteración fonémica 1:1 de la LA.

### 8.1 Vocales

| Fonema | Grafía LA | Griego |
|--------|-----------|--------|
| /a/ | a | α |
| /e/ | e | ε |
| /i/ | i | ι |
| /o/ | o | ο |
| /u/ | u | υ |

### 8.2 Consonantes principales

| Fonema | Grafía LA | Griego |
|--------|-----------|--------|
| /p/ | p | π |
| /b/ | b | β |
| /t/ | t | τ |
| /d/ | d | δ |
| /k/ | k | κ |
| /ɡ/ | g | γ |
| /f/ | f | φ |
| /s/ | s | σ/ς |
| /z/ | z | ζ |
| /r/ | r | ρ |
| /l/ | l | λ |
| /m/ | m | μ |
| /n/ | n | ν |
| /θ/ | th | θ |
| /x/ | kh | χ |
| /h/ | h | ἁ (espíritu áspero sobre vocal) |
| /w/ | w | ου |
| /j/ | y, j | ι (semivocal) / ϳ (yot, letra arcaica) |

> **Nota sobre 'j' en LA:** La letra 'j' se usa en transcripción latina como equivalente de 'y' para representar /j/. Ambas grafías son intercambiables en LA y corresponden a ι (semivocal) o ϳ (yot) en la escritura griega. Esta convención permite reflejar préstamos del árabe (donde ي = /j/) y del sánscrito (donde य = /j/) sin forzar una transliteración única. En el léxico pueden coexistir formas con 'y' y 'j' (ej. `yajña` / `yajna`, `jana` / `jana`).

### 8.3 Dígrafos no clásicos

Los fonemas no presentes en el griego clásico (**sh /ʃ/, ch /tʃ/, gh /ɣ/, dh /ð/, dz /d͡z/**) se representan con **dígrafos** estables en la ortografía politónica:

| Fonema | Grafía LA | Griego (dígrafo propuesto) |
|--------|-----------|---------------------------|
| /ʃ/ | sh | ση (san) / ϻ (letra arcaica) |
| /tʃ/ | ch | τϻ (tau+san) / ϡ (sampi, letra arcaica) |
| /ɣ/ | gh | γχ (gamma+chi) |
| /ð/ | dh | δθ (delta+theta) |
| /d͡z/ | dz | δζ (delta+zeta) |

La forma exacta de estos dígrafos puede refinarse en el uso real del idioma.

---

## 9. Prosodia

KFA está pensado para ser **hablado, cantado, declamado, susurrado y gritado**. Cinco modos de uso, un solo sistema prosódico que sirve a todos. Esta sección construye la capa melódica, rítmica y de fonación que se monta sobre el sistema fonémico (§2), la fonotáctica (§3) y el acento de intensidad (§4).

### 9.1 Principios estéticos

Cinco propiedades no negociables, derivadas del uso previsto del idioma en contextos rituales, poéticos y ceremoniales:

1. **Sonoridad abierta.** La sílaba átona conserva su vocal clara. No hay reducción extrema a *schwa* (como en inglés) ni cierre vocálico (como en árabe coloquial). **Razón:** en contexto ritual cada sílaba es una unidad significativa; perder su forma audible es perder su carga operativa.

2. **Memorabilidad regular.** Las frases rituales KFA deben poder memorizarse tras **3 repeticiones**. Esto exige un patrón rítmico predecible y una curva melódica estable.

3. **Variedad expresiva.** La fonación ofrece al menos **4 modos** (modal, breathy, creaky, falsetto) que el oficiante alterna según intención. La monotonía rompe el *enchantment* en el sentido técnico: el hechizo se disuelve cuando el discurso ritual se vuelve plano.

4. **Cadencia sellante.** Toda unidad ritual completa cierra con **descenso melódico a la zona grave de la voz** + alargamiento de la última vocal + pausa proporcional. El efecto perceptual: la palabra **se planta en el aire** — lo que las tradiciones herméticas llamaban *verbum stabilitum*.

5. **Respiración natural.** Cada cláusula debe poder decirse dentro de **una sola exhalación** de un oficiante adulto promedio (≈5-7 segundos, 30-40 sílabas a tempo ritual). Es un principio de salud vocal **y** de retención atencional del oyente.

**Lo que KFA no es:**
- No es *stress-timed* (como inglés) donde las sílabas átonas se aplastan
- No tiene reducción vocálica extrema (como portugués de São Paulo)
- No es tonal (como mandarín): la melodía oracional existe pero no es fonémica

### 9.2 Cronometría silábica

KFA es una lengua **silábico-timed** (isocronía silábica). Cada sílaba ocupa aproximadamente la misma unidad temporal, **independientemente de si es tónica o átona**.

**Tiempos base (sílabas/segundo):**

| Tempo | sil/seg | Uso típico |
|-------|---------|------------|
| Veloz (no ritual) | 9-10 | Argumentación, debate, instrucción operativa |
| Normal | 6-7 | Conversación ritual, discurso ceremonial |
| Cantable (coro) | 7-8 | Canto comunitario, himnos |
| Lento (litúrgico) | 4-5 | Invocación, consagración, silencio activo |
| Glacial (sellado) | 2-3 | Sello final, palabra de poder, bīja aislado |

**Acentuación dentro de la isocronía:** la sílaba tónica **no acorta a la átona**; al contrario, la tónica **se alarga un 30-50%** y **se eleva un semitono** sobre su tono base, mientras la átona mantiene su duración estándar. Esto produce el patrón "pulso regular con picos" típico del canto llano, del sánscrito védico y del canto sinagogal.

**Ejemplo morfológico (Text 4 de los textos modelo):**
- `θé-le kal thar nam-poi` — "la voluntad realiza el ritual, con reverencia"
- 6 sílabas a tempo lento: 6 × 0.20s = 1.20s
- Con alargamiento de tónicas: `θé`(0.26) `le`(0.16) `kal`(0.18) `thár`(0.26) `nam`(0.18) `poi`(0.16) ≈ 1.20s
- Lo que se percibe: silabeo regular **más** picos de intensidad/pitch en las tónicas

**Justificación cross-lingüística:** griego koiné (silábico-timed, lengua del PGM), sánscrito védico (cadencia descendente en recitación), árabe clásico (silábico-timed, lengua del *ḥurūfismo*), tibetano (silábico-timed marcado en el canto *rñiṅ-ma-pa*). **4 de 6 fuentes** coinciden en este rasgo.

### 9.3 Curva melódica de la cláusula

La entonación KFA es **declarativa por defecto**: la cláusula desciende gradualmente del registro medio-alto al registro grave, con caída final en la última sílaba tónica.

**Patrones oracionales canónicos:**

| Tipo de cláusula | Movimiento melódico | Marca final |
|------------------|---------------------|-------------|
| Declarativa | mid-high → low (descenso gradual) | caída en última tónica |
| Interrogativa sí/no | mid-high → high (ascenso en última tónica) | subida en última tónica |
| Interrogativa qu- | mid → high (pico en la palabra interrogativa) | caída en el resto |
| Exclamativa | high (registro elevado en todo el enunciado) | pico en foco exclamativo |
| Imperativa | mid-high sostenido (sin caída final) | mantenido en alto hasta ejecución |
| Vocativa | rise-fall en el nombre invocado | caída ceremonial al final |

> **v1.3 cross-ref:** el morfema que dispara la curva vocativa es la partícula `o` (gramática §1.7, lexicón `conjunciones_y_particulas`). Sin `o`, ningún sintagma nominal puede recibir la curva rise-fall characteristic del vocativo.

**Curva declarativa (visualización):**

```
   pitch
   high ┤      ╱╲
        │     ╱  ╲
   mid  ┤    ╱    ╲
        │   ╱      ╲___
   low  ┤  ╱           ╲___
        └──────────────────── tiempo
        θé  le  kal  thar
```

**Curva interrogativa sí/no:**

```
   pitch
   high ┤      ╱╲
        │     ╱  ╲
   mid  ┤    ╱    ╲
        │   ╱      ╲
   low  ┤  ╱        ╲___╱
        └──────────────────── tiempo
        θé  le  kal  thar?
```

### 9.4 Acento de foco

El constituyente focalizado (información nueva, contraste, énfasis) se marca con tres rasgos simultáneos:

1. **Pico melódico** en su sílaba tónica (la tónica se eleva un tono y medio sobre el registro circundante)
2. **Alargamiento** de la sílaba tónica focal (×1.5 de su duración base)
3. **Pausa previa** si el foco es contrastivo (pausa breve de 1 sílaba)

**Ejemplo:**

> Neutro: `pír hú-hék thár káir` — "el señor sacerdote realiza el ritual"
>
> Foco en *kair* ("¿cuándo?"): `pir hú-hék thar` [pico] `káir↑` — la sílaba final se eleva
>
> Foco contrastivo en *pir* ("no el devoto, sino el sacerdote"): [pausa] `PÍR↑` hú-hék thár káir — pico en la primera sílaba + alargamiento

**Combinación con evidencial y actitudinal:** los marcadores de evidencialidad (`-nam` visual, `-nand` revelado) y actitudinales (`-nam` reverencia, `-nand` alegría, `-prem` amor, `-shant` paz) ocupan la **posición tónica** de su constituyente. Cuando hay foco, el evidencial/actitudinal recibe el pico melódico, **no el nombre**. Esto evita que el énfasis invierta la carga ritual.

### 9.5 Pausas

| Tipo | Duración | Marca prosódica | Uso |
|------|----------|-----------------|-----|
| Micro | 0.1-0.2s | (apenas perceptible) | Entre modificador y núcleo |
| Corta | 0.3-0.4s | Sutil ascenso tonal antes | Entre sintagmas |
| Media | 0.6-0.8s | Tono suspendido | Entre cláusulas |
| Larga | 1.0-1.2s | Tono mantenido, inhalación audible | Entre oraciones |
| Ritual | 1.5-2.5s | Silencio total + posible inhalación nasal | Entre actos del rito, antes del bīja |

**Regla del silencio respiratorio:** en discurso ceremonial, **toda pausa larga va precedida de inhalación audible** (no forzada, no ruidosa, pero presente). Esta inhalación se integra al rito: marca la separación sin cortar el flujo vital del oficiante. Es el equivalente acústico del *prāṇa* yāmico.

### 9.6 Cadencia ritual (sellado melódico)

Toda invocación KFA completa termina con la **secuencia de sellado**, en este orden estricto:

1. **Descenso melódico** (*high → mid → low-grave*) en los últimos 2-3 pies rítmicos
2. **Alargamiento** de la última sílaba tónica a **3 moras** (en vez de 1.5)
3. **Tenida** de la última vocal átona hasta completar **una exhalación**
4. **Silencio proporcional** posterior de **1.5× la duración de la última sílaba tenida**
5. **Inhalación ritual** antes del silencio, audible pero no ruidosa

**Efecto perceptual:** la invocación **baja, se asienta, y permanece**. Es el equivalente acústico de asentar el cimiento de una construcción — el sonido aterriza en el plano físico.

**Justificación cross-tradicional:** el descenso melódico final aparece en las 6 tradiciones fuente:
- Hebreo bíblico: cadencia final descendente (*sof pasuq*)
- Sánscrito védico: *udātta* descendente al final del mantra
- Árabe clásico: cadencia conclusiva del Corán (*wājib al-waqf*)
- Griego bizantino: *apothísma* final
- Tibetano: *gyü* (cierre de mantra) con tono descendente
- Avestan: cadencia del *Staomi*

### 9.7 Modos de fonación

KFA permite alternar entre **5 modos primarios**, cada uno con una intención característica:

| Modo | Característica | Uso típico |
|------|----------------|------------|
| **Modal** | Voz natural, sin tensión | Discurso, narración, declaración |
| **Breathy** (aspirado) | Voz con escape aéreo audible | Pregunta, devoción, ternura, súplica |
| **Creaky** (crepitante) | Cuerdas vocales tensas, vibración irregular | Cierre de declaración, advertencia, transición |
| **Falsetto / head** | Registro agudo de cabeza | Invocación aguda, alabanza, bīja elevado |
| **Tenso / percusivo** | Ataques glotales marcados, sin aire | Imperativo coercitivo, conjuro, sello |

**Reglas de uso ritual:**

- Un **bīja** (nombre esencial, §3.18 gramática) **se canta en falsetto**, una octava arriba de la voz modal
- Una **declaración de intención** se dice en modal
- Un **sello coercitivo** se dice en tenso
- Una **pregunta devocional** se dice en breathy
- Un **cierre de sección** se dice en creaky descendente

**Conmutación fonatoria:** en un solo discurso ceremonial, el oficiante pasa por **al menos 3 modos distintos** (modal → falsetto en bīja → tenso en sello). Esta alternancia es **fonética, no gramatical**: no cambia el contenido proposicional pero sí la fuerza ilocutiva.

### 9.8 Métrica para poesía

**Unidad básica: el pie KFA.**

- 1 pie = 1 sílaba tónica (larga, alta) + 1 sílaba átona (corta, media)
- Patrón por defecto: **troqueo** (fuerte-débil)
- Patrón alternativo: **iambo** (débil-fuerte), para variación expresiva

**Versos comunes:**

| Verso | # pies | # sílabas | Uso |
|-------|--------|-----------|-----|
| Dímetro | 2 | 4 | Sentencia, proverbio, conjuro mínimo |
| Tetrámetro | 4 | 8 | Oración poética corta, mantra breve |
| **Hexámetro** | 6 | 12 | **Verso de invocación mayor** (estándar ceremonial) |
| Octámetro | 8 | 16 | Himno extenso, recitación larga |

**El hexámetro KFA** (12 sílabas en patrón trocaico) es el verso ceremonial por defecto. Ejemplo construido:

```
muk thé - le kal - thar
muk.the.le.kal.thar
vo-lun-tad-de hi-pó-te-sis rea-li-za
("La voluntad de la hipótesis se realiza")
```

Estructura: 6 pies trocaicos = 12 sílabas = duración media 2.0-3.0 segundos a tempo ritual. Es el equivalente funcional del **hexámetro homérico** (que mide por cantidad) y del **gāyatrī védico** (que tiene 24 sílabas — exactamente 2 hexámetros KFA, 8+8 pies).

**Sustituciones permitidas en poesía:**

- Troqueo → iambo en un pie por verso (genera pregunta o duda interior)
- Sílaba final larga → sinalefa (fusión de 2 vocales) en rima interior
- **Catálisis**: añadir 1 sílaba átona antes de tónica en cesura (suspensión)

**Rima:** KFA prefiere **pararima** (eco consonántico) sobre rima perfecta. La rima perfecta es opcional. La pararima es la coincidencia de al menos 2 consonantes en coda o ataque, no necesariamente la vocal. Esto refleja el conservadurismo consonántico de las 6 tradiciones (sánscrito, árabe, hebreo, avéstico y tibetano conservan las consonantes rábidas más que las vocales).

### 9.9 Estructura del canto

**El canto KFA es silábico, coral y repetitivo** — su modelo es el canto llano, el *dhikr* sufí y el canto védico.

**Unidad básica: la estrofa de 4 versos hexámetros** = 48 sílabas ≈ 6-7 segundos a tempo coral.

**Estructura de un canto ritual completo:**

1. **Prólogo** (1 verso hexámetro aislado): la "llamada" — quien canta se presenta o invoca la atención
2. **Cuerpo** (3-7 estrofas de 4 versos): el contenido central
3. **Sello** (1 verso hexámetro repetido 3 veces): la palabra de poder que cierra

**Reglas de ejecución coral:**

- **Unisonancia** (no polifonía): todos los cantores en la misma línea melódica
- **Octavas paralelas** (opcional): los cantores pueden doblar a la octava inferior o superior
- **Sin acompañamiento instrumental** por defecto: la voz humana es el único medio
- **Percusión mínima opcional**: un marco (*duff*, *daf*) puede marcar el pulso, nunca la melodía

**Regla de las 3 repeticiones:** toda estrofa o verso de poder se repite **3 veces** en tempos distintos:

| Repetición | Tempo (sil/seg) | Función ritual |
|------------|-----------------|----------------|
| 1ª | 7-8 (normal-coral) | "Anuncia" |
| 2ª | 8-9 (ligeramente más rápido) | "Acerca" |
| 3ª | 4-5 (cadencia sellante) | "Asienta" |

**Esta tricotomía (anunciar / acercar / asentar) es la convención performativa KFA para todo material de poder.** Un mismo verso, dicho en 3 tempos, ejecuta 3 funciones rituales diferenciadas.

### 9.10 Discurso ceremonial

**El discurso ceremonial KFA** es la unidad operativa más compleja. Se usa en consagraciones, declaraciones de intención ritual, juramentos mágicos y alocuciones formales.

**Estructura tripartita:**

| Parte | Función | Tempo | Modo de fonación | Duración |
|-------|---------|-------|------------------|----------|
| 1. **Invocación** | Llamar la atención del plano invocado | Lento (4-5) | Falsetto en clímax | 10-20s |
| 2. **Declaración** | Expresar la intención | Normal (6-7) | Modal | 5-15s |
| 3. **Sello** | Asentar y cerrar | Glacial (2-3) | Tenso descendente | 3-8s |

**Total: 18-43 segundos, máximo 60 segundos.** Esto es deliberado: el discurso debe poder sostenerse en la memoria del oficiante y de los testigos.

**Regla de las 3 recitaciones:** el discurso completo se recita **3 veces** en la ceremonia:

| Recitación | Característica | Función |
|------------|---------------|---------|
| 1ª | Normal, todos presentes escuchan | Anunciar |
| 2ª | Pausas ligeramente más largas (cada cláusula marcada) | Acercar |
| 3ª | Cadencia sellante pronunciada, todos en silencio | Asentar |

**Variación tipológica** (no todo discurso requiere las 3 partes):

- Discurso de **invocación simple** ("yo te llamo"): solo parte 1
- Discurso de **declaración simple** ("esto es así"): solo parte 2
- Discurso de **sello** ("que así sea"): solo parte 3
- Discurso **completo** (consagración mayor): las 3 partes

**Regla de la unidad respiratoria:** cada parte debe poder decirse en **una sola exhalación** de un oficiante adulto. Si una parte requiere más de 7 segundos a tempo lento (≈30 sílabas), debe partirse en cláusulas con pausa media entre ellas.

### 9.11 Reglas de evitación

KFA evita ciertos patrones que, aunque gramaticalmente correctos, resultan cacofónicos, agotadores o antiestéticos en uso oral:

1. **Evitar 3+ sílabas átonas consecutivas en una cláusula** (monotonía tonal). Insertar una tónica cada 3 átonas como máximo.

2. **Evitar 2+ sílabas con la misma consonante oncial seguidas en habla continua** (aliteración excesiva que dificulta la articulación clara). Permitir aliteración en rima poética, no en discurso ceremonial.

3. **Evitar cláusula de más de 40 sílabas** (agotamiento respiratorio y atencional). Partir en cláusulas más cortas con pausa media.

4. **Evitar encabalgamiento abrupto** entre cláusulas sin pausa. Toda cláusula debe tener pausa media antes de la siguiente.

5. **Evitar descenso melódico en la primera sílaba de una cláusula** (suena a "rendición prematura"). Empezar cada cláusula en registro medio o alto.

6. **Evitar cierre de invocación en registro agudo**. El cierre **debe** descender a registro medio-grave. Un cierre agudo suena inconcluso y rompe el efecto de sellado.

7. **Evitar mezclar más de 2 modos de fonación en una sola cláusula** (la alternancia sin regla confunde al oyente). Reservar el cambio de modo para la transición entre cláusulas o entre partes del discurso.

8. **Evitar palabras de 4 sílabas en discurso ceremonial** (aún si la fonotáctica las permite, §3.1). En ceremonial, máximo **3 sílabas por palabra**. Esto es una restricción de registro, no de gramática.

### 9.12 Resumen ejecutivo

| Componente | Regla principal |
|------------|-----------------|
| Cronometría | Silábico-timed (cada sílaba = unidad igual) |
| Acento | Intensidad (§4): penúltima, retroceso si ligera |
| Sílaba tónica | +30-50% duración, +1 semitono pitch |
| Melodía base | Descenso gradual (mid-high → low) |
| Pregunta sí/no | Ascenso en última tónica |
| Pregunta qu- | Pico en palabra interrogativa |
| Exclamación | Registro elevado en todo el enunciado |
| Imperativo | Sostenido en alto, sin caída final |
| Foco | Pico melódico + alargamiento + posible pausa |
| Pausa corta / media / larga / ritual | 0.3s / 0.7s / 1.1s / 2.0s |
| Cadencia sellante | Descenso + alargamiento ×3 + silencio 1.5× |
| Falsetto | Bīja, invocación aguda |
| Breathy | Pregunta, devoción |
| Tenso | Sello coercitivo |
| Creaky | Cierre de sección |
| Verso estándar | Hexámetro trocaico (12 sílabas) |
| Estrofa | 4 versos hexámetros (48 sílabas) |
| Canto | Unisonancia, 3 repeticiones con tempos descendentes |
| Discurso ceremonial | 3 partes (invocación + declaración + sello) |
| Recitaciones ceremoniales | 3 veces en tempos descendentes |
| Máx. sílabas/cláusula ceremonial | 30 (≈7s a tempo lento) |
| Máx. sílabas/palabra ceremonial | 3 |

### 9.13 Audición modelo

Aplicación de las reglas a la primera cláusula del Text 4 de los textos modelo (*Pir Hú-Hék va Áz-Hék*):

**Original (KFA politónico):**
> `πιρ χου-χεκ βα αζ-χεκ ναμ-ποι`
> *pir hú-hék va áz-hék nam-poi*
> "el Señor Sacerdote y el iniciado realizan (con reverencia)"

**Análisis prosódico:**
- `pir` (1 sil, tónica por defecto) — tónica, alargada, pico FOCO (sujeto focalizado)
- pausa micro (0.15s)
- `hú-hék` (2 sil, tónica en `-hék`) — tónica en la 2ª, segunda mitad del compuesto
- pausa micro (0.15s)
- `va` (1 sil, conjunción) — átona, sin acento marcado
- pausa corta (0.3s)
- `áz-hék` (2 sil, tónica en `-hék`) — paralelo rítmico con `hú-hék`
- pausa media (0.7s)
- `nam-poi` (2 sil, tónica en `-poi`) — verbo compuesto en tónica final, alargada
- cadencia sellante: descenso melódico + alargamiento ×3 + silencio 1.5×

**Tempo ceremonial (3ª recitación, glacial, 4 sil/seg):**

```
   pitch
   high ┤     ╱╲
        │    ╱  ╲
   mid  ┤   ╱    ╲
        │  ╱      ╲╲
   low  ┤ ╱        ╲╲___
        └────────────────── tiempo
        pír hú-hék va áz-hék nam-poi.
        [F]              [S]      [S]
        Foco             Sello    Asentamiento
```

**Lectura:**

> [Falsetto ligero, registro medio] *píííir...* [pausa micro, desciende] *hú-hék* [pausa micro] *va* [pausa corta, tono medio] *áz-hék* [pausa media, tono suspendido] *náaam-pooooooiii* [silencio 1.5×, 3 segundos] *...* [inhalación ritual audible]

**Lo que se percibe:** dos agentes nombrados, paralelismo rítmico *hú-hék* / *áz-hék* (eco intencional), conjunción breve *va* como bisagra, verbo final con cadencia descendente que **asienta** la acción en el aire. El silencio posterior **prolonga el eco** — el oyente retiene la imagen auditiva.

### 9.14 BNF prosódica (extensión de §6)

```bnf
<oración>     ::= <cláusula> (<pausa_media> <cláusula>)*
<cláusula>    ::= <sintagma>+ <cadencia_sellante>?
<cadencia_sellante> ::= <descenso> <alargamiento_x3> <silencio_1.5x>
<acento_tónico>     ::= <sílaba> [×1.5 duración] [×1.5 pitch]
<modo_fonación>     ::= "modal" | "breathy" | "creaky" | "falsetto" | "tenso"
<curva_melódica>    ::= "declarativa" | "interrogativa_sn"
                      | "interrogativa_qu" | "exclamativa"
                      | "imperativa" | "vocativa"
<verso>        ::= "dimetro" | "tetrametro" | "hexametro" | "octametro"
<estrofa>      ::= <verso> ×4
<canto>        ::= <prologo> <estrofa>+ <sello_3x>
<discurso_ceremonial> ::= <invocación> <declaración>? <sello>?
<recitación>   ::= <discurso_ceremonial> ×3
<tempo>        ::= "veloz" | "normal" | "cantable" | "lento" | "glacial"
```

**Nota sobre escritura:** la prosodia KFA es **primariamente una realidad de performance**, no de notación. Las convenciones ortográficas (acento agudo del griego politónico) marcan la sílaba tónica, pero el movimiento melódico, las pausas, el modo de fonación y la cadencia sellante **se transmiten oralmente** de maestro a discípulo o se consignan en guías de recitación. El circunflejo y el grave, reservados por la gramática §7.4 para "poesía mágica o glosas etimológicas", se usan opcionalmente en textos poéticos para indicar patrones melódicos específicos (rise-fall circunflejo = invocación; grave = cierre sellado en escritura).

---

## 10. Silabificación

La sílaba en KFA sigue la **estructura canónica**:

```
σ = (C) (C) (C) V (C) (C)
    └── onset ──┘ └─ núcleo ─┘ └─ coda ─┘
```

- **Onset**: hasta 3 consonantes (C, CC, CCC, o CVC en el segundo ataque, ver §10.2).
- **Núcleo**: V (vocal simple) o VV (diptongo/hiatos, ver §4.4).
- **Coda**: hasta 2 consonantes, con fuertes restricciones (ver §3.3 gramática y §10.3).

### 10.1 Jerarquía de sonoridad

La asignación de consonantes a onset o coda está regida por la **jerarquía de sonoridad** (adaptada de Clements 1990 + Bhat 1999):

```
menos sonoras <───────────────────────────────> más sonoras
oclusiva  africada  fricativa  nasal  líquida  glide
   p, t, k  ts, tʃ  s, ʃ, f, x  m, n  l, r    j, w
```

**Regla de sonoridad ascendente en onset**: de la primera a la última consonante del onset, la sonoridad **aumenta** (oclusiva → líquida → glide).
**Regla de sonoridad descendente en coda**: de la primera a la última consonante de la coda, la sonoridad **disminuye** (líquida → nasal → oclusiva).

### 10.2 Tipos de onset permitidos

| Tipo | Estructura | Ejemplo KFA | Notas |
|------|-----------|-------------|-------|
| V | V inicial | `a.hu` | palabra exclusivamente vocálica |
| CV | C + V | `ka.lam` | más común (60% de sílabas) |
| CCV | C + glide/líquida + V | `thra.kar` | glide inicial (`j`, `w`) |
| CCCV | oclusiva + líquida/glide + glide + V | `skwam` | raro (≤3% del corpus) |
| VV | diptongo/hiatos | `bīj`, `aum` | vocal larga o diptongo |

**Restricciones del onset CCC**:
1. La primera C **debe** ser oclusiva (p, t, k) o fricativa sibilante (s, ʃ).
2. La segunda C **debe** ser líquida (l, r) o glide (j, w).
3. La tercera C **debe** ser glide (j, w).
4. Tres oclusivas seguidas **nunca** ocurren (geminación prohibida).
5. Los prestamos griegos `pt-`, `kt-` se resílaban: `ptōma` → `pā.tō.ma` (epéntesis).

**Sibilantes en onset doble**: `sp-`, `st-`, `sk-`, `ʃr-` son **legales** (respetan la jerarquía).
**Secuencias prohibidas en onset**:
- Oclusiva + nasal: `pn-`, `tm-`, `kn-` (nasalización de la oclusiva) → se epentesiza: `pa.na`, `ta.ma`, `ka.na`
- Tres oclusivas: `ptk-`, `ktp-` → resílaba: `pat.ka`, `kat.pa`
- Liquida + oclusiva: `rk-`, `lp-` (coda) → se mueve a onset siguiente sílaba: `ra.ka`, `la.pa`

### 10.3 Restricciones de coda

La coda KFA admite **máximo 2 consonantes** con las siguientes reglas (recap §3.3.5 gramática):

| Posición | Coda 1 | Coda 2 | Ejemplo |
|----------|--------|--------|---------|
| C | nasal, fricativa, oclusiva | — | `han` (bí-), `hal` (salte) |
| CC | nasal / líquida | oclusiva sorda (p, t, k) | `han` (man-) + `t` → `hant` |
| CC | fricativa sibilante | oclusiva sorda | `huʃ` + `t` → `huʃt` (huʃt-ka) |
| CC | líquida | nasal | rarísimo, dialectal: `warm` |

**Prohibidas en coda**:
- Tres consonantes: `karst`, `helft`, `angst` → se resílaba: `kar.sta`, `hel.fa`, `an.gaʃ`
- Oclusiva + líquida: `kar.l` → se mueve a onset: `ka.rla`
- Fricativa + nasal: `lef.n` → se resílaba: `le.fna`
- Dos nasales: `han.m` → se asimila: `han.na` (nasal + nasal → idéntica)

### 10.4 Ambigüedad silábica

Cuando las dos asignaciones (CV.CV vs CVC.V) son posibles, KFA aplica el **Principio de Onset Máximo** (MOP, Kahn 1976): se prefiere la silabificación que **maximiza el onset**.

| Secuencia | Silabificación | Razón |
|-----------|----------------|-------|
| `baka` | `ba.ka` (no `bak.a`) | MOP: `k` prefiere onset que coda |
| `pamri` | `pam.ri` (no `pa.mri`) | MOP: `m` se agrupa con `r` en onset |
| `ʃalta` | `ʃal.ta` (no `ʃa.lta`) | MOP: `l` + `t` ambos en coda sí, pero `lt` agrupa |
| `darsa` | `dar.sa` (no `da.rsa`) | MOP: `r` se agrupa con `s` |
| `kaptu` | `kap.tu` (no `ka.ptu`) | sonoridad descendente en coda: `p` + `t` ✓ |

### 10.5 Préstamos y adaptación

Los préstamos (especialmente del Griego y del Sánscrito) requieren **adaptación silábica KFA**:

**Regla 1 — Resílabación obligatoria**:
- Gr `ptōma` → KFA `pa.tō.ma` (epéntesis de `a`)
- Skt `śrī` → KFA `shi.rí` (re-sílaba con onset `sh`)

**Regla 2 — Coda CC permitida** (de §10.3):
- Mantenidas: `sp`, `st`, `sk`, `ʃp`, `ʃt`, `ʃk`
- Adaptadas: Skt `r̥` → `ru`; Skt `ḥ` → `a` (silencio glotal elidido)

**Regla 3 — Hiatos conservados en préstamos rituales**:
- Skt `dīpa` → KFA `dī.pa` (no `dip.pa`)
- Gr `zoē` → KFA `zo.é` (diptongo griego mantenido como hiato)

### 10.6 Interacción con el acento

El acento prosódico (lengthening × 1.5 + pitch × 1.5, ver §9.4) **siempre cae sobre la sílaba tónica de la palabra**, no sobre la sílaba tónica del grupo fónico. La silabificación determina dónde puede caer el acento:

| Tipo de palabra | Sílaba acentuada | Ejemplo |
|-----------------|-------------------|---------|
| Bisílaba paroxítona (predominante) | 1ª sílaba | `ká.lam` |
| Trisílaba paroxítona | 1ª sílaba | `bí.je.ri` |
| Trisílaba proparoxítona (10%) | 1ª sílaba | `ká.la.mi` |
| Tetrasílaba paroxítona | 2ª sílaba | `ka.` `rās.` `ti` → `ka.rā́s.ti` (acento en `rās`) |
| Monosílaba | única sílaba | `bīj` |

**Regla del acento en sílaba pesada**: una sílaba con coda CC o con VV (vocal larga/diptongo) **siempre** es **pesada**, y atrae el acento si está disponible. De ahí la preferencia por paroxítonas: la penúltima sílaba es típicamente pesada en palabras trisílabas (CVCC, CVVC, CV.VC).

### 10.7 Resumen de algoritmo silábico

El silabificador KFA aplica las siguientes reglas en orden:

1. Identificar las vocales (núcleos).
2. Asignar la primera consonante post-vocálica a la **coda** de la sílaba actual (respetando §10.3).
3. Si hay consonantes extra entre la coda y la siguiente vocal, aplicar **MOP** (onset máximo).
4. Si la secuencia no forma onset legal (§10.2), **epéntesis** de vocal `a` o `i`.
5. Si la secuencia viola coda CC (§10.3), **resílabación** (mover la consonante al onset siguiente).
6. Si quedan tres+ consonantes, **resílabación** con epéntesis vocálica.
7. Marcar el acento prosódico en la sílaba pesada más cercana a la posición paroxítona.

**Resultado**: KFA es un idioma de **sílabas bien formadas** con un sesgo CV fuerte (≥60% de sílabas CV), coda restringida a max 2C, y onset max 3C. Esto lo hace **silábico-timed** (ver §9.1), apropiado para invocación, canto y discurso ceremonial.

---

## 11. Fonosemántica generativa (v1.3)

Esta sección introduce el **sistema fonosemántico generativo** de Kalfírvach: una matriz que asigna a cada fonema del inventario núcleo una **carga elemental o planetaria**, y un algoritmo composicional que permite derivar **bījas nativos** a partir de un propósito ritual declarado. Los bījas derivados de este sistema **sustituyen** los bījas tradicionales importados (`óm-húm-trám`, etc.); los tradicionales pueden documentarse en lexicón como **registro arqueológico** (ver §11.4 nota final), pero el sistema v1.3 se basta a sí mismo.

**Cobertura cross-tradicional:** cada mapeo se ancla en ≥3 tradiciones (Sánscrito, Griego, Egipcio, Avestan, Hebreo, Latín, Persa, Sumerio, Tibetano, Árabe). 18/19 mapeos tienen ≥3 fuentes explícitas; el restante (`v`) se marca como variante de `p` (Venus canónico) con refuerzo Griego koiné tardío. Cobertura total: 100% de los mapeos con al menos una fuente de las **3 tradiciones core** (Skt/Gr/Eg).

**Cross-ref:** la carga semántica de cada fonema se aplica en la composición de bījas — ver gramática §3.18.2.a para reglas algorítmicas y plantillas. La regla de **apócope derivativa** §3.5.5 es prerrequisito estructural (habilita bījas derivados de raíces con `-e` final) aunque los 6 bījas de los worked examples de §11.2 no la ejercen (todos derivan de raíces consonánticas puras).

### 11.1 Matriz fonema→elemento (19 mapeos)

**Estructura por capa** (5 categorías):

| Capa | Símbolo | Selección | Ejemplo |
|------|---------|-----------|---------|
| Astral / primordial | V₀ | la vocal inicial (5 opciones) | `/a/` = plano astral |
| Elemental | V₁ | una de las 5 vocales (capa elemental) | `/i/` = agua |
| Raíz / fuerza | C_R | 1-2 consonantes con carga semántica | `/r/` = fuego |
| Planetaria | C_P | 1 consonante planetaria opcional | `/k/` = Saturno |
| Glotal / sellado | C_Σ | marcador de cierre (opcional) | `/h/` = Júpiter expansor |

**Matriz completa** (5 vocales + 14 consonantes = 19 mapeos):

| # | Fonema | IPA | Capa | Elemento / planeta / fuerza | Source anchors (≥3 tradiciones) | Confianza |
|---|--------|-----|------|------------------------------|----------------------------------|-----------|
| 1 | `a` | /a/ | V (astral) | plano astral / primordial | proto-semitic `*ʾ`; Egipcio ꜣ "primeval"; Skt अ a-kāra | **high** |
| 2 | `e` | /e/ | V | tierra / sólido | Skt ए; Griego ε; Avestan ə (regular outcome) | **high** |
| 3 | `i` | /i/ | V | agua / fluidez | Skt इ; Egipcio j "reed" (water-symbol); Griego ι (iota aquática) | **high** |
| 4 | `o` | /o/ | V | éter / ākāśa | Skt ओ; Griego ο (omicron, "void" PGM); Avestan aw | **high** |
| 5 | `u` | /u/ | V | fuego ascendente | Skt उ; Egipcio wꜣ "one/primeval fire"; Avestan uš "fire" | **high** |
| 6 | `r` | /r/ | C (root) | fuego / sol | Skt र; Griego ῥ; PIE *h₁reh₁-; Egipcio rꜥ "sun" | **high** |
| 7 | `y` | /j/ | C | aire / viento | Skt य; Griego ψ "spirit"; Egipcio ḥ𓅃 "wind" | **medium** |
| 8 | `m` | /m/ | C | coerción / fijación | Skt म; Egipcio mꜣꜥ "truth/māyā"; Griego μ (μίτρα mitra) | **high** |
| 9 | `l` | /l/ | C | agua / fluidez líquida | Skt ल; Griego λ; Egipcio n "water" → L-drop | **medium** |
| 10 | `s` | /s/ | C | tierra / arena | Skt स; Egipcio sꜣ "earth/sand"; Avestan saoshyant "earth-renewer" | **high** |
| 11 | `b` | /b/ | C | éter / ākāśa | Skt ब; Griego β; Sumerian BAD "open/reed" | **medium** |
| 12 | `k` | /k/ | C | Saturno / Chronos | Griego Κρόνος; Skt काल kāla; Avestan kərəmna | **high** |
| 13 | `t` | /t/ | C | Marte / fuerza | Skt त; Griego θ; Egipcio ḏꜣ "strength" | **medium** |
| 14 | `d` | /d/ | C | Mercurio / comunicación | Skt द; Egipcio ḏd "stable"; Griego δ (δοκέω "receive") | **medium** |
| 15 | `n` | /n/ | C | Luna / receptividad | Skt न; Egipcio n "sky"; Avestan nāman | **high** |
| 16 | `p` | /p/ | C | Venus / armonía | Skt प; Egipcio pꜣ "primeval"; Avestan paoiri | **medium** |
| 17 | `h` | /h/ | C | Júpiter / expansión | Egipcio ḥ; Skt ह; Hebreo ה | **high** |
| 18 | `v` | /v/ | C (variant) | Venus variante | Latín V; Persa v; Griego β→/v/ (koiné tardía, refuerzo) | **low** |
| 19 | `w` | /w/ | C | voluntad / soplo | Hebreo ו; Skt व; Egipcio wꜣ "command" | **high** |

**Tally de confianza:** 13 high, 5 medium, 1 low (`v`). `v` se documenta como **variante explícita de `p`** (Venus canónico) en la columna Capa; el refuerzo Griego koiné tardío `β→/v/` se cita como cuarta fuente parcial.

**Cobertura por tradición** (sobre los 19 mapeos):

| Tradición | Mapeos que cita | % |
|-----------|------------------|---|
| Sánscrito (Skt) | 14/19 | 74% |
| Griego (Gr) | 14/19 | 74% |
| Egipcio (Eg) | 14/19 | 74% |
| Avestan (Av) | 11/19 | 58% |
| Hebreo (Heb) | 3/19 (`h`, `w`, refuerzo en `a`) | 16% |
| Latín (Lat) | 1/19 (`v`) | 5% |
| Persa (Per) | 2/19 (`v`, refuerzo en otros) | 11% |
| Sumerio (Sum) | 1/19 (`b`) | 5% |
| Tibetano (Tib) | 0/19 explícitos (las correspondencias tántricas operan a nivel de partículas interjectivas §3.19, no de inventario fonémico) | 0% (gap documentado) |
| Árabe (Ar) | 0/19 explícitos (Ilm al-Huruf trabaja sobre abjad values, no segmento fonémico) | 0% (gap documentado) |

### 11.2 Worked examples (6 derivaciones)

Los 3 primeros ejemplos (`raka`, `mil`, `nu`) son los trabajados en spec §2.2; los 3 siguientes (`ra`, `let`, `yat`) son los derivados del design §4.5 y demuestran el algoritmo con iteración fonotáctica.

**Slot structure:** `[C_R] V [C_P]?` — una consonante raíz con carga semántica, una vocal con carga de plano elemental, y un sufijo planetario opcional.

**Forma ritual obligatoria:** `bīj [bīja] wah-nam-poi` (siguiendo §3.18.7 Capa I: invocar con `-wah` revelado, `-nam` reverencia, `-poi` performativo).

#### Ejemplo A — "Invocar al fuego" (`raka`)

- **Propósito ritual:** sellar el fuego en el plano astral con marca temporal.
- **Triada:** C_R = `/r/` (fuego/sol) + V₀ = `/a/` (plano astral) + C_P = `/k/` (Saturno/cronos — sellado temporal).
- **Ensamblaje:** `/r/ + /a/ + /k/ + /a/ = raka` (CVCV).
- **Validación fonotáctica:** §3.2 onset `r-` ✓; §3.2 onset `k-` ✓; §3.3 coda vacía ✓; §11.3 sin forbidden.
- **Abjad:** r=200, a=1, k=20, a=1 → 222 (canónico, sagrado).
- **Forma ritual:** `bīj raka wah-nam-poi`.
- **Gloss:** "el fuego sellado en el tiempo".
- **Uso ritual:** invocación ígnea en plano sutil con anclaje cronal.

#### Ejemplo B — "Coerción del agua" (`mil`)

- **Propósito ritual:** atar el agua con fuerza coercitiva.
- **Triada:** C_R = `/m/` (coerción/fijación) + V₁ = `/i/` (agua/fluidez) + C_P = `/l/` (agua — refuerzo líquido).
- **Ensamblaje:** `/m/ + /i/ + /l/ = mil` (CVC).
- **Validación fonotáctica:** §3.2 onset `m-` ✓; §3.3 coda `-l` ✓ (líquida en coda permitida); §11.3 sin forbidden.
- **Abjad:** m=40, i=10, l=30 → 80 (no canónico; relajar: mono-bīja en v1.3 no requiere 7 estricto, ver §3.18.2.a).
- **Forma ritual:** `bīj mil wah-nam-poi`.
- **Gloss:** "el agua atada por la fuerza".
- **Uso ritual:** ritual de fijación de corrientes, sellado de flujos acuáticos.

#### Ejemplo C — "Receptividad lunar" (`nu`)

- **Propósito ritual:** receptividad lunar con activación por fuego ascendente.
- **Triada:** C_R = `/n/` (Luna/receptividad) + V₁ = `/u/` (fuego ascendente, activador) + sin C_P.
- **Ensamblaje:** `/n/ + /u/ = nu` (CV).
- **Validación fonotáctica:** §3.2 onset `n-` ✓; §3.3 coda vacía ✓; §11.3 sin forbidden.
- **Abjad:** n=50, u=200 → 250 (no canónico; mono-bīja: se acepta).
- **Forma ritual:** `bīj nu wah-nam-poi`.
- **Gloss:** "lo lunar que asciende en fuego".
- **Uso ritual:** apertura de operaciones nocturnas, invocación de sueños.

#### Ejemplo D — "Fuego astral simple" (`ra`)

- **Propósito ritual:** invocar el fuego orientado al plano sutil, sin sellado temporal.
- **Triada:** C_R = `/r/` (fuego) + V₀ = `/a/` (plano astral) + sin C_P (default; invocación elemental simple).
- **Ensamblaje:** `/r/ + /a/ = ra` (CV, mono-bīja).
- **Validación fonotáctica:** §3.2 onset `r-` ✓; §3.3 coda vacía ✓; §11.3 sin forbidden.
- **Abjad:** r=200, a=1 → 201 (no canónico; mono-bīja elemental acepta abjad no-canónico).
- **Forma ritual:** `bīj ra wah-nam-poi`.
- **Gloss:** "el fuego invocado en el plano astral".
- **Uso ritual:** apertura elemental de cualquier ritual ígneo sutil.

#### Ejemplo E — "Destierro del agua del plano terrestre" (`let`)

- **Propósito ritual:** expulsar una presencia líquida que opera en el plano físico/material.
- **Triada:** Plano físico (terrestre) → V₀ = `/e/`; elemento agua → C_R = `/l/`; fuerza abjurativa (destierro) → C_P = `/k/` (Saturno/cronos — el destierro sella en el tiempo).
- **Iteración 1 (con prefijo `/m/` de coerción reforzada):** `/m/ + /l/ + /e/ + /k/ = mlek` (CCVCC) — §3.2 onset `ml-` no es legal (nasal+líquida prohibida en onset). **Rechazado.**
- **Iteración 2 (sin prefijo, con C_P = `/k/`):** `/l/ + /e/ + /k/ + /t/` epentética para resolver coda → `lekt` (CCVC) — §3.2 onset `lk-` no es legal (líquida+oclusiva prohibida). **Rechazado.**
- **Iteración 3 (cambiar C_P a `/d/`, Mercurio — también comunica con planos liminales, apropiado para destierro):** `/l/ + /e/ + /d/ = led` (CVC) — §3.3 coda `-d` se ensordece a `-t` per reglas codiciales. **Bīja final: `let`** (CVC).
- **Validación final:** §3.2 onset `l-` ✓; §3.3 coda `-t` ✓ (oclusiva sorda en coda permitida); §11.3 sin forbidden.
- **Abjad:** l=30, e=5, t=9 → 44 (no canónico; di-bīja elemental acepta).
- **Forma ritual:** `bīj let wah-nam-rak-poi` (rak = actitudinal abjurativo, ver F3 §5.3).
- **Gloss:** "el agua-terreno sellada en Mercurio para destierro".
- **Uso ritual:** exorcismo líquido en plano físico.
- **Nota metodológica:** este ejemplo requirió **3 iteraciones** documentadas; el algoritmo detecta la violación fonotáctica y propone variantes (cambio de C_P, ensordecimiento codicial). El output siempre es fonotáctico; el costo es iteración, no fallo.

#### Ejemplo F — "Sello del aire mercurial" (`yat`)

- **Propósito ritual:** sellar una operación de comunicación aérea con ligadura ritual.
- **Triada:** Plano no especificado → default astral → V₀ = `/a/`; elemento aire → C_R = `/y/` (capa aire/ψ); fuerza vinculante → C_P = `/d/` (Mercurio = comunicación, ya canónico); refuerzo de plano divino: añadir V₁ = `/o/` (éter) entre C_R y C_P.
- **Ensamblaje inicial:** `/y/ + /a/ + /o/ + /d/ = yaod` (CVVC) — VV no es diptongo KFA canónico per §3.4 (solo ay/aw/ey/ow); silabificación `ya.od` o `yao.d`; coda `-d` se ensordece a `-t`.
- **Iteración 1:** `yaot` (CVVC) — VV `ao` no es diptongo legal. **Rechazado.**
- **Iteración 2 (dropear refuerzo V₁):** `/y/ + /a/ + /d/` → coda `-d` → `-t` → `yat` (CVC).
- **Validación final:** §3.2 onset `y-` ✓ (semivocal + vocal); §3.3 coda `-t` ✓; §11.3 sin forbidden.
- **Abjad:** y=10, a=1, t=9 → 20 (no canónico; se acepta).
- **Forma ritual:** `bīj yat wah-nam-rab-poi` (rab = vinculante, F3 §5.3).
- **Gloss:** "el aire sellado en Mercurio para atadura".
- **Uso ritual:** sellado de comunicaciones; inscripciones en pergaminos.

**Tabla resumen de los 6 worked examples:**

| # | Propósito | Triada | Bīja | Forma ritual |
|---|-----------|--------|------|---------------|
| A | Fuego sellado cronal | fuego + astral + Saturno | `raka` (CVCV) | `bīj raka wah-nam-poi` |
| B | Coerción del agua | coerción + agua + agua-refuerzo | `mil` (CVC) | `bīj mil wah-nam-poi` |
| C | Receptividad lunar | Luna + fuego-ascendente | `nu` (CV) | `bīj nu wah-nam-poi` |
| D | Fuego astral simple | fuego + astral | `ra` (CV) | `bīj ra wah-nam-poi` |
| E | Destierro agua terrestre | físico + agua + Mercurio | `let` (CVC) | `bīj let wah-nam-rak-poi` |
| F | Sello aire mercurial | astral + aire + Mercurio | `yat` (CVC) | `bīj yat wah-nam-rab-poi` |

### 11.3 Combinaciones prohibidas

La validación fonotáctica (paso 7 del algoritmo) bloquea 2 combinaciones que violan la fonotáctica KFA o introducen carga cross-tradicional problemática.

| Combo | Razón fonotáctica | Razón semántica / cross-tradicional | Severidad |
|-------|--------------------|--------------------------------------|-----------|
| `/aŋ/` | Fonema `/ŋ/` no es fonémico en KFA: solo existe como **alófono de `/n/` ante velar** (per §2.3 fonología v1.0, línea 98). En coda de bīja no hay contexto para la velarización; `/ŋ/` sería fonémico por accidente. | Bantu tone systems asocian `/aŋ/` con tonos altos; KFA no tiene tonos fonémicos (cf. §9.1 "KFA no es tonal"). El préstamo tonal está prohibido. | **high** (fonológico) |
| `/dhv/` | Cluster `dhv` viola §3.2 fonología: fricativa + oclusiva + glide es onset de 3 consonantes no listada en §3.2. | Sin carga semántica clara: `dh` = fricativa sonora (2/6 tradiciones), `v` = variante venusino (2/6 tradiciones). La yuxtaposición de dos fonemas raros produce un cluster más raro aún, sin anclaje cross-tradicional suficiente. | **medium** (cluster fonotáctico) |

**Nota:** las 2 restricciones son **fonológicas, no semánticas**. La validación semántica (paso 8 del algoritmo) no detecta forbidden combos; es la validación fonotáctica (paso 7) quien los bloquea. Esto simplifica la tabla: no hay reglas semánticas de incompatibilidad (e.g., "fuego + agua no se mezclan"); KFA permite todos los emparejamientos C+V, el rito decide si la combinación es coherente.

### 11.4 Reglas de composición

**Algoritmo generativo** (10 pasos, output siempre fonotáctico-legal):

```
función generar_bīja(propósito) -> string:

  1. PARSEO DEL PROPÓSITO
     Identificar la triada elemental:
       a) Elemento principal: fuego | agua | tierra | aire | éter
          (si no se especifica, default = éter/V₀)
       b) Plano ontológico: físico | astral | divino
          (si no se especifica, default = astral/V₀)
       c) Fuerza coercitiva (opcional): precativo | imperativo |
          vinculante | abjurativo | sello
          (si no, omitir sufijo planetario)

  2. SELECCIÓN DE CAPA V₀ (VOCAL DE PLANO)
     Plano astral   -> /a/
     Plano físico   -> /e/  (tierra = lo encarnado)
     Plano divino   -> /o/  (éter/ākāśa = trascendencia)

  3. SELECCIÓN DE CAPA V₁ (VOCAL ELEMENTAL) — opcional,
     solo si se quiere sobreescribir V₀:
     fuego   -> /u/
     agua    -> /i/
     tierra  -> /e/
     aire    -> /a/  (colisión con V₀ astral — preferir V₁ /i/ o /y-/)
     éter    -> /o/  (colisión con V₀ divino)

  4. SELECCIÓN DE CAPA C_R (CONSONANTE RAÍZ)
     Mapeo directo desde §11.1 (matriz):
       fuego -> /r/; agua -> /l/ (canónico) o /m/ (coercitivo);
       tierra -> /s/; aire -> /y/; éter -> /b/
     Si el propósito pide "coerción de X" -> /m/ como prefijo

  5. SELECCIÓN DE CAPA C_P (SUFIJO PLANETARIO) — opcional
     Marte/fuerza    -> /t/
     Mercurio/comunic -> /d/
     Saturno/tiempo  -> /k/
     Luna/receptividad -> /n/
     Venus/armonía   -> /p/ (o /v/ como variante)
     Júpiter/expansión -> /h/

  6. ENSAMBLAJE
     Plantilla:  [C_R] V [C_P]?
     Validar: cada slot <= 1 fonema
     Resultado: bisílabo CV.CVC o CVCV (típico)

  7. VALIDACIÓN FONOTÁCTICA
     Verificar §3 (fonotáctica KFA):
       - onset legal (§3.2)
       - coda legal (§3.3)
       - no diptongo inverso (§3.4)
     Verificar §11.3 (forbidden combinations):
       - NO /aŋ/ (fonema /ŋ/ no es fonémico en KFA)
       - NO /dh/ + /v/ (cluster dhv prohibido)

  8. VALIDACIÓN SEMÁNTICA
     Verificar coherencia: el mapeo fonema->elemento no debe
     contradecir el propósito declarado.
     Ejemplo: si propósito = "vincular agua", el bīja debe
     llevar /l/ (agua) o /m/ (coerción) en C_R, no /r/ (fuego).

  9. CÁLCULO ABJAD (opcional, requisito v1.0 relajado en v1.3)
     Numeración 1-9, 10-90, 100-900 (modelo árabo-persa-sánscrito).
     En v1.3 los mono-bījas (CV) y di-bījas elementalmente simples
     NO requieren abjad canónico (7/11/22/33/77/99). La restricción
     abjad se reserva a bījas rituales complejos (tri/penta-bīja)
     y a operaciones de registro formal (F5 §3.18.7.b).

 10. EMISIÓN
     Retornar el bīja más el formante obligatorio:
       "bīj [bīja] wah-nam-poi"
     (siguiendo §3.18.7 Capa I: invocar con -wah -nam -poi)
```

**Slot structure** (resumen tabular del algoritmo):

| Slot | Cardinalidad | Contenido | Default |
|------|--------------|-----------|---------|
| C_R | 0-2 fonemas | una consonante con carga semántica (§11.1) | 1 (obligatorio en C_R simple) |
| V | 1 fonema | una vocal con carga de plano elemental | obligatorio |
| C_P | 0-1 fonemas | una consonante con carga planetaria (§11.1) | 0 (opcional) |

**Output lengths típicos:** CVCV (4 fonemas) para 70% de bījas, CVCVCV (6 fonemas) para 20%, CV (2 fonemas) para 10% (mono-bīja elemental, ver Ejemplos C, D).

**Apócope y bījas:** la regla §3.5.5 (apócope derivativa de `-e` ante C) **habilita** bījas derivados de raíces con `-e` final (no es el caso de los 6 worked examples de §11.2 — todos derivan de raíces consonánticas puras). Si en el futuro se introducen raíces como `bīje` o `thele` como generadores de bījas, la apócope se activará automáticamente (`*bīj-tár`, `*thel-rak`). La regla queda **preparada para v1.3+**, no ejercida masivamente en v1.3.

**Cross-ref fonología:** §3 (fonotáctica general), §3.5.5 (apócope derivativa prerrequisito), §3.18.7 (invocación ritual integrada), §3.18.2.a (composición algorítmica en gramática).

**Cross-ref gramática:** §3.18.2.a (reglas algorítmicas, plantillas, sub-patrones), §3.18.7 (capa I integración), §5.3 (sufijos actitudinales F3 — varios de ellos son bījas truncados: `-rak` = `raka` sin vocal final; ver cross-front design §5.2).

**Nota final:** los bījas tradicionales importados (`óm`, `húm`, `yám`, `rám`, `lám`, `trám`, etc.) se documentan en lexicón `magia_y_mitologia` como **registro arqueológico** (categoría ya presente); el sistema v1.3 los **sustituye** pero no los prohíbe. Un iniciado puede usar `óm-húm-trám` si tiene transmisión tradicional; la fonología §11 ofrece una **ruta nativa KFA** equivalente.

---

*Documento generado como parte de Kalfírvach v1.0 — Especificación Fonológica*
*Toda decisión fonológica y prosódica se ha justificado con datos de ≥2 lenguas fuente.*

---

**Agentes autónomos y usuarios, ignorar este apartado del documento, son wikilinks para Obsidian**: [[constructed-language]], [[iadicur]], [[kemoupyr]], [[koine-greek]], [[ancient-persian-language]], [[tibetan-language]], [[]]
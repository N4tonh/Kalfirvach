---
title: "Kalfírvach v1.4 — Gramática Completa"
version: v1.4
date: 2026-06-06
lang: es
status: stable
---

# KALFÍRVACH v1.4 — Gramática Completa

---

## 1. Sintaxis

### 1.1 Orden básico: SOV

El orden de palabras fundamental de Kalfírvach es **SOV** (Sujeto-Objeto-Verbo).

**Justificación tipológica:**

| Orden | Lenguas fuente que lo usan | Frecuencia global |
|-------|---------------------------|-------------------|
| **SOV** | Sánscrito, Persa, Tibetano, Árabe (VSO→SVO→SOV variante) | ~45% de lenguas |
| SVO | Griego, Árabe (variante) | ~42% de lenguas |
| VSO | Egipcio, Árabe (clásico) | ~9% de lenguas |

El orden SOV es el más frecuente en las lenguas fuente orientales (sánscrito, persa, tibetano) y es el orden más común entre las lenguas del mundo. Además, facilita la **postposición** de partículas mágicas, que es el patrón natural en SOV: las partículas evidenciales, actitudinales y de modo se colocan tras el verbo o la frase que modifican, creando un efecto de "revelación progresiva" — el hablante primero presenta el contenido semántico y luego califica su estatus ontológico, lo cual es ritualmente poderoso.

**Ejemplo:**
```
Nyós   zal   kár-e
suj    obj    verbo-EVID:visual
"Sombra acción hace[veo]"
= "Veo que la sombra actúa"
```

### 1.2 Orden dentro del sintagma nominal

```
Determinante + Adjetivo + Núcleo + Modificador + Postposición
```

| Posición | Elemento | Ejemplo |
|----------|----------|---------|
| 1 | Determinante/Cuantificador | mu "todo", ta "este" |
| 2 | Adjetivo | rík "grande", khap "oscuro" |
| 3 | Núcleo nominal | thel "voluntad", nús "conciencia" |
| 4 | Complemento del nombre | (otro SN en aposición) |
| 5 | Postposición | -na (locativo), -te (dativo), -ra (ablativo) |

**Ejemplo:**
```
mu  rík  thel-na
todo grande voluntad-LOC
"En la gran voluntad total"
```

### 1.2.1 Artículos (definitud y número)

Kalfírvach **no tiene género gramatical**. La **definitud** y el **número** se marcan en el artículo, no en el sustantivo ni en el adjetivo.

| Artículo | Valor | Origen (≥2) | Uso |
|----------|-------|------------|-----|
| **ha** | definido singular | Griego ὁ/ἡ (ho/ha) + Árabe هـٰذا (hā-) | "el/la" singular |
| **han** | definido plural | ha + -n (plural general, cf. pronombres) | "los/las" plural |
| **é** | indefinido singular | Sánscrito *éka* + Griego *heîs* (uno) → reducción | "un/una" |
| **én** | indefinido plural | é + -n (plural general) | "unos/unas" |

**Ejemplos:**
```
ha  nūros      = la luz
han nūros      = las luces
é   nūros      = una luz
én  nūros      = unas luces
ha  rík  thel = la gran voluntad
én  khap  zal = unas sombras oscuras
```

**Notas:**
- Los sustantivos y adjetivos **no flexionan** por número.
- El **plural** se expresa en el artículo (han/én). Si no hay artículo, el sustantivo puede ser genérico o indefinido por contexto.

### 1.3 Orden dentro del sintagma verbal

```
[Aspecto-]Raíz verbal + Tiempo + Evidencial + Actitudinal + Modo realidad
```

Los afijos y partículas verbales se disponen en orden fijo alrededor de la raíz:

| Posición | Marcador | Función |
|----------|----------|---------|
| -3 (prefijo) | chrón-, kair-, neh- | Temporalidad mágica |
| -2 (prefijo) | pra-, kal-, tél-, sél- | Fase ritual |
| -1 (prefijo) | su-, a-, ta- | Aspecto |
| Raíz | kár- "hacer" | Contenido léxico |
| +1 | -a (presente), -i (pasado), -u (futuro) | Tiempo |
| +2 | -e (visual), -on (onírico), -anu (inferido), -wah (revelado), -Ø (neutro) | Evidencial |
| +3 | -nam, -tuf, -al, -shak, -has, -nand, -shok, -bay, -krod, -prem, -vismay, -viras, -shant, -gar, -ék, -wíl, -azáz, -soph, -lúx, -síg | Actitudinal |
| +4 | -som (físico), -ast (astral), -kal (hipotético), -poi (performativo) | Modo realidad |
| +5 | -h | Registro hierático |
| +6 | -dín, -máh, -sól | Tiempo astrológico |

**Ejemplo completo:**
```
áz   kair-kal-su-kár-a-e-nam-gar-ék-poi-h-máh
yo.HIER kair-invocar-PFV-hacer-PRES-visual-reverencia-orgullo-éxtasis-PERF-HIER-lunar

"Yo, iniciado, invoco en el momento sagrado el acto completado que veo con reverencia, orgullo y éxtasis, performativamente y en registro hierático, bajo esta fase lunar."
```

### 1.4 Elisión

El sujeto puede elidirse si es recuperable del contexto (pro-drop), tipológicamente justificado por el Sánscrito, el Árabe y el Tibetano, que son lenguas pro-drop:

```
zal  kár-e
sombra hacer-visual
"[La sombra] actúa [veo]"
```

### 1.5 Predicación nominal y adjetival

La predicación se realiza con la cópula **as**. Los adjetivos no concuerdan en género ni número.

```
ha  nūros   khap    as-a
DEF.SG luz  oscura ser-PRES
"La luz es oscura"

én  zal  rík    as-a
INDEF.PL sombra grande ser-PRES
"Unas sombras son grandes"
```

### 1.6 Comparativos y equativos

Kalfírvach usa partículas de grado:

| Grado | Partícula | Origen (≥2) | Uso |
|-------|-----------|------------|-----|
| **para** | "más (que)" | Sánscrito *para* "más allá" + Griego *para* "más allá" | comparativo de superioridad |
| **awa** | "menos (que)" | Sánscrito *ava* "hacia abajo" + Avestan *ava* "abajo" → /v/→/w/ | comparativo de inferioridad |
| **sáma** | "tan…como" | Sánscrito *sama* "igual" + Avestan *hama* "igual" | equativo |

**Estructura:**
- Superioridad / inferioridad: **Adj + (para/awa) + Estándar-sya**
- Equativo: **sáma + Adj + Estándar-sya**

**Ejemplos:**
```
ha  nūros  rík  para  han zal-sya  as-a
DEF.SG luz grande más  DEF.PL sombra-GEN ser-PRES
"La luz es más grande que las sombras"

ha  zal  khap  awa  ha nūros-sya  as-a
DEF.SG sombra oscura menos DEF.SG luz-GEN ser-PRES
"La sombra es menos oscura que la luz"

ha  nūros  sáma rík  ha zal-sya  as-a
DEF.SG luz tan  grande DEF.SG sombra-GEN ser-PRES
"La luz es tan grande como la sombra"
```

### 1.7 Vocativo

El vocativo KFA se marca con la partícula **`o`** en posición **pre-nominal absoluta**: `o + SN + , + resto de cláusula`. La coma es ortográfica (separa la invocación del resto de la cláusula), no gramatical.

**BNF:**

```
<clausula>   ::= <vocativo> "," <clausula_principal> | <clausula_principal>
<vocativo>   ::= "o" <SN_nominal>
<SN_nominal> ::= <nombre_propio> | <titulo> | <designacion_ritual>
```

**Restricciones del vocativo (vs. sujeto, §1.2):**
- El vocativo **nunca** lleva evidencial (a diferencia del sujeto agentivo, §1.2.3).
- El vocativo **nunca** lleva postposición de caso (§1.4).
- El vocativo **puede** llevar determinante honorífico (`o ha Yaho` "oh el-YHWH"; `ha` = artículo definido, §1.2.1).

**Combinación con actitudinales coercitivos (F3, §5.3):**

```
o [entidad invocada], [verbo] + [sufijo coercitivo] + [evidencial hierático]
```

**Ejemplo canónico (F3 + F4 + F2):**

```
o Yaho, bīj raka wah-nam-ran-poi
```

Gloss: "¡Oh YHWH, por favor, invoco el nombre esencial fuego-cronos con reverencia, performativamente!"

**Distinción con interjección `ya` (§3.19.1):** `ya` es exclamación admirativa (sin objetivo); `o` es **invocación dirigida** (siempre lleva nombre propio o título). `o` puede llevar nombre; `ya` no. Pueden co-ocurrir: `o Yaho, ya!` (invocación + admiración).

**Prosodia (cross-ref fonología §9.3):** el vocativo recibe **tono vocativo** (rise-fall en el nombre invocado + caída ceremonial al final del vocativo). El segmento `o [nombre]` se entona como una unidad melódica autónoma antes de la cláusula principal.

---

## 2. Sistema de partículas

### 2.1 Evidenciales (5 valores)

Los evidenciales codifican la **fuente del conocimiento** del hablante. Son obligatorios en toda oración asertiva **en contexto ritual**; en contexto cotidiano se usa la forma neutra (-Ø).

| Valor | Partícula | IPA | Origen documentado | Contexto de uso |
|-------|-----------|-----|-------------------|----------------|
| **Visual** | -e | /e/ | Griego ὁράω (horáō) "ver" → hor- → -e (reducción); Sánscrito ākṣi "ojo" → aks- → -e (reducción fonética). 2 lenguas. | Conocimiento directo por percepción sensorial. "Lo vi con mis ojos." |
| **Onírico** | -on | /on/ | Griego ὄναρ (ónar) "sueño" → on-; Tibetano rmi.lam (milam) "sueño" → mi- → reducción a -on por asimilación con griego. 2 lenguas. | Conocimiento recibido en sueño o visión alterada. "Me fue revelado en sueño." |
| **Inferido** | -anu | /a.nu/ | Sánscrito anumāna "inferencia" → anu-; Persa danistan "saber por deducción" → dan- → anu (homofonía reforzada). 2 lenguas. | Conocimiento deducido de evidencia indirecta. "Lo infiero de los signos." |
| **Revelado** | -wah | /wah/ | Árabe وحي (waḥy) "revelación divina" → wah; Egipcio wḥꜣ "revelar" → wah (cognado propuesto). 2 lenguas. | Conocimiento recibido por revelación directa, sin mediación sensorial. "Me fue revelado." |
| **Neutro** | -Ø | — | Sin marca. No codifica fuente de conocimiento. | Conversación cotidiana, pragmático, no marcado ritualmente. Se usa cuando la fuente del conocimiento no es relevante para el contexto. |

**Uso del neutro:** El evidencial neutro (-Ø) permite usar Kalfírvach en contextos cotidianos sin la carga ritual de especificar la fuente de conocimiento. Es el equivalente a la ausencia de marca en lenguas como el turco, que tienen evidenciales pero permiten formas no-marcadas en habla casual. En contexto ritual o mágico, los 4 evidenciales tradicionales siguen siendo obligatorios.

```
ma  as-a   = "yo soy" (neutro, cotidiano)
ma  as-a-e = "yo soy [veo]" (visual, ritual: lo sé porque lo veo)
```

**Justificación de la obligatoriedad (en contexto ritual):** En las 6 tradiciones fuente, la **distinción entre modos de conocimiento es ontológicamente significativa**: el PGM distingue entre fórmulas "vistas" y "reveladas"; el Mantraśāstra distingue entre mantras "escuchados" (śruti) y "inferidos"; el Ilm al-Huruf distingue entre conocimiento ilham (inspirado) e istidlāl (inferido). El neutro permite que el hablante use el idioma fuera de este marco cuando la precisión epistemológica no es necesaria.

> **v1.4 cross-ref:** las actitudinales coercitivas (`-ran`/`-rak`/`-rab`/`-ro-hék`) comparten la morfología de las actitudinales (§2.2), pero reservan el slot final del verbo para un sufijo dedicado de fuerza ritual (ver §5.3).

### 2.2 Actitudinales (20 valores)

Los actitudinales codifican la **postura emocional/ritual** del hablante ante lo enunciado. Son opcionales. Se agrupan en tres categorías: rituales (herencia mágica), emocionales (expresión humana) y prometeicos (expansión luciferiana).

#### 2.2.1 Rituales (5)

| Valor | Partícula | IPA | Origen documentado | Contexto de uso |
|-------|-----------|-----|-------------------|----------------|
| **Reverencia** | -nam | /nam/ | Sánscrito नमस् (namas) "reverencia, saludo" → nam; Persa نام (nām) "nombre" (el nombre sagrado se invoca con reverencia). 2 lenguas. | El hablante se inclina ante lo que describe. Se usa en invocaciones, oraciones, reconocimientos de poder superior. |
| **Desafío** | -tuf | /tuf/ | Árabe طوف (ṭūf) "circuito, asedio" → tuf; Persian طوفان (ṭūfān) "tormenta" → tuf. La idea de "viento huracanado que desafía". 2 lenguas. | El hablante desafía o resiste lo descrito. Se usa en exorcismos, contraincantos, afirmaciones de autonomía. |
| **Certeza mágica** | -al | /al/ | Griego ἀλήθεια (alētheia) "verdad, des-ocultamiento" → al-; Árabe الحق (al-ḥaqq) "la Verdad" → al- (artículo + raíz, reducido). 2 lenguas. | El hablante afirma con certeza absoluta de origen mágico. No es certeza lógica sino gnóstica: "lo sé porque lo he realizado." |
| **Duda ritual** | -shak | /ʃak/ | Árabe شك (shakk) "duda" → shak; Persa شک (shakk) "duda" → shak. Préstamo compartido árabe-persa. 2 lenguas. | El hablante suspende el juicio ritualmente. No es duda escéptica sino dubitación sacra: "esto requiere más investigación/iniciación." |
| **Ironía sagrada** | -has | /has/ | Sánscrito हास्य (hāsya) "risa, comicidad ritual" → has; Tibetano bzhad.pa "reír" → zhad → has (adaptación fonémica). 2 lenguas. | El hablante enuncia con ironía consciente, reconociendo la paradoja. La risa divina (Shiva Nataraja, el Buda sonriente) es un reconocimiento de la naturaleza ilusoria de lo enunciado. |

#### 2.2.2 Emocionales (8)

| Valor | Partícula | IPA | Origen documentado (≥2) | Contexto de uso |
|-------|-----------|-----|------------------------|-----------------|
| **Alegría** | -nand | /nand/ | Sánscrito *nanda* "gozo, deleite"; Avestan *nand-* (raíz IE *ned- "sonar, regocijarse"). 2 lenguas. | El hablante expresa alegría ante lo enunciado. Uso cotidiano y ritual. |
| **Tristeza** | -shok | /ʃok/ | Sánscrito *śoka* "pena, aflicción"; Avestan *saok-* "quemar" (pena que quema, duelo). 2 lenguas. | El hablante expresa tristeza, duelo o melancolía. |
| **Miedo** | -bay | /baj/ | Sánscrito *bhaya* "miedo, temor"; Avestan *baya-* (raíz IE *bheyh₂- "temer"). 2 lenguas. | El hablante expresa temor o aprensión. |
| **Ira** | -krod | /krod/ | Sánscrito *krodha* "ira, furia"; Avestan *khrōdha-* "ira" (raíz IE compartida). 2 lenguas. | El hablante expresa enfado, indignación o furia. |
| **Amor** | -prem | /prem/ | Sánscrito *prema(n)* "amor, afecto"; Avestan *frya-* "querido, amado" (raíz IE *priy-). 2 lenguas. | El hablante expresa amor, cariño, devoción o afecto profundo. |
| **Asombro** | -vismay | /-ˈwis.maj/ | Sánscrito *vismaya* "asombro, sorpresa, maravilla"; Persa *vismā* (misma raíz IE). 2 lenguas. | El hablante expresa sorpresa, maravilla o admiración. |
| **Disgusto** | -viras | /-ˈwi.ras/ | Sánscrito *virasa* "insípido, repulsivo, desagradable"; Persa *bī-ras* "sin sabor" (misma raíz compuesta). 2 lenguas. | El hablante expresa repulsión, asco o rechazo. |
| **Calma** | -shant | /ʃant/ | Sánscrito *śānti* "paz, serenidad, calma"; Avestan *spanta-* "sagrado, pacífico, bienhechor". 2 lenguas. | El hablante expresa paz, serenidad, tranquilidad o aceptación. |

#### 2.2.3 Prometeicos (7)

Nuevos actitudinales para la expresión emocional del camino luciferiano/prometeico:

| Valor | Partícula | IPA | Origen documentado | Contexto |
|-------|-----------|-----|-------------------|----------|
| **Orgullo/Excelencia** | -gar | /gar/ | Persa *gharur* "orgullo" + Árabe *ghurūr* "orgullo, autoconocimiento" → ghar → gar. 2 lenguas. | Orgullo justo, dignidad, reconocimiento del propio valor. No es hybris. |
| **Trascendencia/Éxtasis** | -ék | /ek/ | Griego *ἔκστασις* (ékstasis) "éxtasis, estar fuera de sí" → ek-; Egipcio *Ꜣḫ* (akh) "espíritu transfigurado" → ék. 2 lenguas. | Estar más allá de los límites normales. Liberación de la consciencia. |
| **Voluntad/Determinación** | -wíl | /wil/ | Persa *wilāyat* "autoridad, voluntad soberana" → wíl; Griego *βουλή* (boulḗ) "voluntad deliberada" → wil. 2 lenguas. | Afirmación de determinación inquebrantable. |
| **Liberación/Rebelión** | -azáz | /a.zaz/ | Árabe *ʿazīz* "poderoso, libre, independiente" → az-; Egipcio *ꜤsꜢ* "rebelarse, levantarse" → az → reduplicación. 2 lenguas. | Liberación de restricción, ruptura de cadenas. Emancipación consciente. |
| **Sagacidad/Sabiduría** | -soph | /sof/ | Griego *σοφία* (sophía) "sabiduría" → soph; Persa *saf* "puro, sabio esotérico" → soph. 2 lenguas. | Sabiduría profunda, conocimiento esotérico, gnosis. |
| **Anhelo/Iluminación** | -lúx | /luks/ | Griego *λυχνία* (lychnía) "luz, lámpara, revelación" → luk-s → lúx; Persa *raxš* "luz, brillo" → rúx → lúx. 2 lenguas. | El anhelo de luz, la búsqueda de iluminación. Deseo consciente de trascender. |
| **Silencio gnóstico** | -síg | /sig/ | Árabe *sakīna* "presencia divina, paz interior" → síg; Griego *σιγή* (sigḗ) "silencio" → síg. 2 lenguas. | El silencio que sigue a la gnosis. Plenitud en reposo. |

```
ma  kár-a-gar       = "Actúo con orgullo [justo]"
áz  as-a-ék-poi     = "Yo hierático soy en éxtasis [performativo]"
sa  as-i-azáz       = "Él/Ella fue en liberación"
ma  nūros ich-a-lúx   = "Anhelo la luz con deseo de iluminación"
as-a-síg            = "Es en silencio [gnóstico]"
ma  shám kár-a-wíl  = "Actúo la sombra con determinación"
ma  ops-a-soph      = "Veo con sabiduría [esotérica]"
```

**Posición:** Los actitudinales se colocan tras el evidencial y antes del modo realidad (posición +3). Pueden combinarse múltiples actitudinales en cadena.

```
kár-a-nand-poi         = "¡hago con alegría performativamente!"
as-i-shok-wah          = "fue con tristeza [revelado]"
kár-a-e-krod-som       = "actúa con ira[veo] en el plano físico"
áz   kair-kár-a-h-nam-gar-ék-poi
yo.HIER momento-hacer-PRES-sacro-reverencia-orgullo-éxtasis-performativo
"Yo, iniciado, decreto el acto sagrado en el momento oportuno, con reverencia, orgullo legítimo y éxtasis trascendente."
```

### 2.3 Modo de realidad (4 valores)

Los modos de realidad codifican el **plano ontológico** en el que se sitúa lo enunciado. Son obligatorios cuando se hace una afirmación sobre un plano no-físico; son opcionales (por defecto = físico) en contextos cotidianos.

| Valor | Partícula | IPA | Origen documentado | Contexto de uso |
|-------|-----------|-----|-------------------|----------------|
| **Físico** | -som | /som/ | Griego σῶμα (sōma) "cuerpo" → som; Sánscrito सोम (soma) "jugo ritual, encarnación física de lo divino" → som. 2 lenguas. | El evento ocurre en el plano material. Por defecto si no se especifica otro. |
| **Astral** | -ast | /ast/ | Griego ἀστήρ (astēr) "estrella" → ast; Sánscrito अस्त्र (astra) "arma ritual, proyección astral" → ast. 2 lenguas. | El evento ocurre en el plano sutil/intermedio entre físico y divino. Sueños lúcidos, viajes astrales, visualización. |
| **Hipotético** | -kal | /kal/ | Sánscrito कल्पना (kalpanā) "imaginación, hipótesis" → kal; Persa کالبد (kālbod) "cuerpo sutil/forma imaginada" → kal. 2 lenguas. | El evento es posible pero no realizado. Se usa en planificación ritual, especulación teosófica, exploración de posibilidades. |
| **Performativo** | -poi | /poi/ | Griego ποιέω (poieō) "hacer, crear, producir" → poi; Sánscrito पुरोहित (purohita) "sacerdote que pone adelante" → po- → poi (reducción). 2 lenguas. | El enunciado **es** el acto. Decir = hacer. El speech act mágico por excelencia. Solo se usa en contextos donde la palabra tiene poder causal directo. |

**Uso combinado de los tres sistemas:**

La gramática de Kalfírvach permite **apilar** los tres tipos de partículas en una sola forma verbal, creando una especificación sumamente precisa del estatus del enunciado:

```
nyós    zal   kár-a-wah-al-poi
sombra  acción hacer-PRES-revelado-certeza_mag-performativo

"Por revelación y certeza mágica, decreto que la sombra actúa [y el decirlo lo hace real]."
```

Esta combinación no es decorativa: responde a la necesidad real de los sistemas mágicos de especificar simultáneamente (a) cómo sé lo que digo (evidencial), (b) con qué actitud lo digo (actitudinal), y (c) en qué plano opera mi enunciado (modo realidad).

---

## 3. Morfología

### 3.1 Principio general

Kalfírvach **no tiene género gramatical ni casos gramaticales**. Las relaciones se marcan mediante:
1. **Orden de palabras** (SOV)
2. **Postposiciones** para funciones semánticas
3. **Derivación léxica** mediante afijos regulares

No hay irregularidades morfológicas. Toda forma se construye productivamente.

### 3.2 Postposiciones

| Postposición | Función | IPA | Origen |
|-------------|---------|-----|--------|
| -na | Locativo ("en", "sobre") | /na/ | Sánscrito -na (sufijo locativo); Tibetano -na (partícula locativa). 2 lenguas. |
| -te | Dativo ("a", "para") | /te/ | Sánscrito -te (terminación dativa); Griego -τε (enclítica "y"). 2 lenguas. |
| -ra | Ablativo ("desde", "de") | /ra/ | Sánscrito -rāt (ablativo) → ra; Persa -ra (marcador de objeto definido). 2 lenguas. |
| -sya | Genitivo ("de", "de pertenencia a") | /sja/ | Sánscrito -sya (genitivo singular); Avestan -sya (genitivo). 2 lenguas. |
| -ka | Instrumental ("con", "mediante") | /ka/ | Sánscrito -ka (sufijo instrumental/adjetival); Tibetano -gis (instrumental) → -ka (reducción). 2 lenguas. |
| -muk | Directivo ("hacia") | /muk/ | Sánscrito mukha "rostro, dirección" → muk; Árabe مقام (maqām) "estación, dirección" → muk (reducción). 2 lenguas. |

**Ejemplos:**
```
thel-na     = en la voluntad
nús-te     = a la conciencia
zal-ra    = desde la sombra
rík-sya    = del grande (perteneciente al grande)
shaktí-ka  = mediante poder
sól-muk    = hacia la luz
```

### 3.3 Morfología verbal

#### 3.3.1 Tiempos

| Tiempo | Sufijo | IPA | Origen |
|--------|--------|-----|--------|
| Presente | -a | /a/ | Sánscrito -ati (3sg presente) → -a; Griego -ω (presente) → -a (reducción). 2 lenguas. |
| Pasado | -i | /i/ | Sánscrito -ī (aoristo); Tibetano -ki (pasado) → -i. 2 lenguas. |
| Futuro | -u | /u/ | Sánscrito -iṣyati (futuro) → -u (reducción extrema); Persa -ad (futuro) → -u (reducción). 2 lenguas. |

#### 3.3.2 Temporalidad mágica

Kalfírvach distingue tres tipos de tiempo sagrado, expresados como prefijos verbales:

| Tipo | Prefijo | Significado | Origen |
|------|---------|-------------|--------|
| **chrón-** | Tiempo lineal, cronológico, mundano | Griego *χρόνος* (chrónos) "tiempo secuencial" |
| **kair-** | Tiempo oportuno, momento sagrado | Griego *καιρός* (kairós) "momento cualitativo" |
| **neh-** | Tiempo cíclico, eterno retorno | Egipcio *nḥḥ* (neheh) "eternidad recurrente" |
| **-djet** | Sufijo: tiempo estático, permanencia | Egipcio *ḏt* (djet) "eternidad estática" |

**Fases rituales (prefijos aspectuales):**

| Fase | Prefijo | Significado | Origen |
|------|---------|-------------|--------|
| **pra-** | Preparación / purificación | Griego *πρό* (pro-) "antes" + Persa *par-* "preparar" |
| **kal-** | Invocación / llamado | Árabe *qāla* "decir, invocar" → kal; Persa *kalām* "palabra" |
| **tél-** | Culminación / realización | Griego *τέλος* (télos) "fin, culminación" + Árabe *tamām* "completado" |
| **sél-** | Cierre / fijación | Persa *sal* "año/completo" + Egipcio *sḥr* "sellar, fijar" |

**Marcadores astrológicos (postposiciones temporales):**

| Marcador | Postposición | Significado | Origen |
|----------|-------------|-------------|--------|
| **-dín** | "en el día/tiempo de" | Persa *din* "día, tiempo" + Árabe *dīn* "ciclo" |
| **-máh** | "en la fase lunar de" | Árabe *qamar* "luna" → máh; Persa *māh* "luna/mes" |
| **-sól** | "en la posición solar de" | (extensión de nūros "luz" a temporalidad solar) |

```
chrón-kár-a    = "actúa en el tiempo mundano"
kair-kár-a     = "actúa en el momento sagrado"
neh-kár-a      = "actúa en el ciclo eterno"
kár-a-djet     = "actúa en permanencia estática"
kal-kár-a-e-nam    = "invoco-que-actúa[veo]con reverencia" (invocación)
tél-kár-i-wah      = "se ha culminado[revelado]" (culminación ritual)
sél-kár-a-nam-poi  = "cierro el acto reverentemente y performativamente"
kár-a-máh      = "actúa en la fase lunar de"
kair-kár-a-máh = "actúa en el momento sagrado de la fase lunar"
```

**Orden de prefijos en el sintagma verbal expandido:**

```
[Temporalidad mágica-][Fase ritual-][Aspecto-]Raíz verbal + Tiempo + Evidencial + Actitudinal + Modo realidad + [Registro hierático] + [Tiempo astrológico]
```

```
áz   kair-kal-su-kár-a-e-nam-gar-ék-poi-h-máh
yo.HIER kair-invocar-PFV-hacer-PRES-visual-reverencia-orgullo-éxtasis-PERF-HIER-lunar

"Yo, iniciado, invoco en el momento sagrado el acto completado que veo con reverencia, orgullo y éxtasis, performativamente y en registro hierático, bajo esta fase lunar."
```

#### 3.3.3 Aspectos (prefijos)

| Aspecto | Prefijo | IPA | Origen |
|---------|---------|-----|--------|
| Perfectivo (completado) | su- | /su/ | Sánscrito su- "bien, completamente"; Avestan hu-/su- "bien". 2 lenguas. |
| Imperfectivo (en progreso) | a- | /a/ | Sánscrito a- (aumentativo, marca pasado); Griego ἐ- (aumento). 2 lenguas. |
| Habitual (repetitivo) | ta- | /ta/ | Sánscrito -tá- (sufijo de participio pasado); Tibetano -ta- (marcador habitual). 2 lenguas. |

**Ejemplos:**
```
su-kár-a  = ha hecho (perfectivo-presente) = "está completado el hacer"
a-kár-a   = está haciendo (imperfectivo-presente)
ta-kár-a  = suele hacer (habitual-presente)
su-kár-i  = hizo (perfectivo-pasado)
kár-u     = hará (futuro simple)
```

#### 3.3.4 Negación

La negación se marca con el prefijo **na-** (/na/):

| Negación | Origen |
|----------|--------|
| na- | Sánscrito न (na) "no" (negación simple, atestiguadísimo); Egipcio n/nḏ "no"; Árabe لا (lā) → na (adaptación fonotáctica); Avestan naē "no". 4 lenguas. Cambiado de ma- en v1.3 para resolver colisión con pronombre 1sg `ma`. |

```
na-kár-a = "no hace"
na-su-kár-a = "no ha completado"
```

#### 3.3.5 Formas no finitas

Kalfírvach usa tres formas no finitas para lenguaje cotidiano y ritual:

| Forma | Sufijo | Origen (≥2) | Función |
|-------|--------|------------|---------|
| **Verbo nominal / infinitivo** | **-an** | Sánscrito *-ana* (verbal noun) + Avestan *-ana* | "ver", "hacer", "el acto de…" |
| **Participio activo** | **-ant** | Sánscrito *-ant* (participio presente) + Avestan *-ant* | "que hace / que está haciendo" |
| **Participio resultativo** | **-ta** | Sánscrito *-ta* (participio pasado) + Avestan *-ta* | "hecho / completado" |

**Ejemplos:**
```
kár-an     = hacer / el acto de hacer
kár-ant    = que hace / actuante
kár-ta     = hecho / completado

ha  kár-ant  thel  as-a
DEF.SG actuante voluntad ser-PRES
"El que actúa es voluntad"

ma  nūros  kár-an  ich-a
yo  luz  hacer-INF querer-PRES
"Quiero hacer luz"
```

### 3.4 Cópula "as"

Kalfírvach expresa **ser/estar** mediante el verbo copulativo **as**:

| Forma | IPA | Origen |
|-------|-----|--------|
| **as** | /as/ | Sánscrito *ásti* "es" (3sg) + Avestan *asti* "es" + Griego *estí(n)* "es". Raíz PIE *h₁es-* "ser". 3 lenguas. |

**Conjugación regular** (sigue el patrón verbal estándar):

```
ma mago as-a      = "yo soy mago" (neutro, cotidiano)
ma mago as-a-e    = "yo soy mago [veo]" (visual, ritual)
ka as-i-wah       = "eso fue [revelado]"
zal as-u-anu     = "la sombra será [inferido]"
ma-kal as-a-al    = "hipotéticamente, no soy con certeza mágica"
as-ro!            = "¡sé!" (imperativo)
```

**Con actitudinales:**
```
ma ta as-a-nand      = "yo esto soy-alegría" = "esto soy con alegría"
ka as-i-shok         = "eso fue-tristeza" = "eso fue triste"
ma ma as-a-bay       = "yo no soy-miedo" = "no tengo miedo"
súnya as-a-shant     = "el vacío es-calma" = "el vacío es sereno"
```

### 3.5 Números

El sistema numérico de Kalfírvach es **decimal**. Todas las raíces tienen origen documentado en ≥2 lenguas fuente.

#### Cardinales

| # | Forma | IPA | Origen |
|---|-------|-----|--------|
| 0 | súnya | /ˈsuɲ.ja/ | Sánscrito *śūnya* "vacío" (reutilizado del léxico esotérico) |
| 1 | ekami | /ˈe.ka/ | Sánscrito *eka* "uno" + Avestan *aēva-* → reducción a ekami. 2 lenguas. |
| 2 | dwi | /dwi/ | Sánscrito *dvi* + Avestan *dva* + Griego *δύο* (dýo) → /dv/→/dw/. 3 lenguas. |
| 3 | tiri | /ˈti.ri/ | Sánscrito *tri* + Avestan *θri* + Griego *τρεῖς* (treîs) → bisilábico. 3 lenguas. |
| 4 | chatúr | /tʃaˈtur/ | Sánscrito *catúr* + Avestan *caθwar*. 2 lenguas. |
| 5 | páncha | /ˈpan.tʃa/ | Sánscrito *pañca* + Avestan *panča*. 2 lenguas. |
| 6 | shásh | /ʃaʃ/ | Sánscrito *ṣaṣ* + Persa *šeš*. 2 lenguas. |
| 7 | sápta | /ˈsap.ta/ | Sánscrito *saptá* + Avestan *hapta*. 2 lenguas. |
| 8 | áshta | /ˈaʃ.ta/ | Sánscrito *aṣṭá* + Avestan *ašta*. 2 lenguas. |
| 9 | navan | /ˈna.wa/ | Sánscrito *náva* + Avestan *nava*. 2 lenguas. |
| 10 | dashak | /ˈda.ʃa/ | Sánscrito *dáśa* + Avestan *dasa*. 2 lenguas. |
| 100 | sháta | /ˈʃa.ta/ | Sánscrito *śata* + Avestan *sata*. 2 lenguas. |
| 1000 | hasarak | /ˈha.zar/ | Persa *hazār* + Sánscrito *sahásra* → hasarak (reducción). 2 lenguas. |

#### Formación de números mayores

```
11 = dashak ekami        "diez uno"
12 = dashak dwi        "diez dos"
20 = dwi-dashak        "dos-diez" (veinte)
21 = dwi-dashak ekami    "veintiuno"
99 = navan-dashak navan  "noventa y nueve"
100 = sháta           "cien"
101 = sháta ekami       "ciento uno"
356 = tiri-sháta páncha-dashak shásh
1000 = hasarak
2026 = dwi-hasarak dwi-sháta dwi-dashak shásh
```

#### Ordinales

Se forman con el sufijo **-th** (Sánscrito *-tha*; Griego *-τος* → -tos → -th) sobre la raíz cardinal:

| Cardinal | Ordinal | Uso |
|----------|---------|-----|
| ekami | **ekamith** | "primero/a" — Regular. |
| dwi | **dwith** | "segundo/a" — Regular. |
| tiri | **tirith** | "tercero/a" — Regular. |
| chatúr | **chatúrth** | "cuarto/a" — Regular. |
| páncha | **pánchath** | "quinto/a" — Regular. |
| shásh | **sháshth** | "sexto/a" — Regular. |
| sápta | **sáptath** | "séptimo/a" — Regular. |
| áshta | **áshtath** | "octavo/a" — Regular. |
| navan | **navanth** | "noveno/a" — Regular. |
| dashak | **dashakth** | "décimo/a" — Regular. |
| sháta | **shátath** | "centésimo/a" — Regular. |

**Irregulares:**
- **púrwa** /ˈpur.wa/ = "primero/a" (variante culta, del Sánscrito *pūrva* "primero, anterior, oriental" + Persa *parv* "primero, previo". 2 lenguas.) — Se usa como **raíz ordinal independiente**, más frecuente que ekamith en textos rituales.
- **pashcha** /ˈpaʃ.tʃa/ = "último/a" (Sánscrito *paścāt* "después, detrás, último" + Persa *pas* "después, detrás". 2 lenguas.)

**Ordinales compuestos** (se marca solo el último elemento):

```
dashak ekamith    = undécimo (10.º)
dwi-sháta dwith = zweihundertster / 200.º
```

**Uso con clasificadores:** El ordinal **precede** al nombre sin clasificador (los clasificadores solo se usan con cardinales):

```
púrwa nūros      = "la primera luz"
dwith nara     = "la segunda persona"
púrwa-wan asib = "el primer médico" (con clasificador enfático)
```

**Adverbios ordinales** (se forman con el sufijo **-dá** del Sánscrito *-dā* "tiempo, cuando" + Griego *-δην* (-dēn) "modo"):

| Adverbio | Significado |
|----------|-------------|
| ekamith-dá | "primeramente" |
| dwith-dá | "en segundo lugar" |
| tirith-dá | "en tercer lugar" |
| púrwa-dá | "en primer lugar" (culta) |

#### Numerales distributivos y multiplicativos

- **Distributivo** ("de a X"): prefijo **prati-** (Sánscrito *prati* "por, según"):
  - prati-dwi = "de a dos", prati-tiri = "de a tres"
- **Multiplicativo** ("X veces"): sufijo **-krit** (Sánscrito *kṛt* "vez" + Avestan *kr-t*):
  - dwi-krit = "dos veces", tiri-krit = "tres veces"
- **Fraccionario**: sufijo **-anshá** (Sánscrito *aṃśa* "parte, porción"):
  - tiri-anshá = "tercio", chatúr-anshá = "cuarto"

#### Clasificadores numerales

Los clasificadores son **medidores semánticos** que se interponen entre el número y el nombre para especificar la **clase de objeto** que se cuenta. Son obligatorios con números cuando se cuentan entidades concretas (excepto unidades de medida y tiempo, que no requieren clasificador). Sintaxis:

```
<cardinal> + <clasificador> + <nombre>
```

| Clasificador | IPA | Mide | Origen (≥2) | Ejemplo |
|-------------|-----|------|-------------|---------|
| **-wan** | /wan/ | Seres animados (personas, animales, espíritus) | Persa *-vant* "poseedor de" + Sánscrito *-vant* "que tiene" → convergencia IE. 2 lenguas. | dwi-wan nara = "dos personas" |
| **-pata** | /ˈpa.ta/ | Objetos planos (hojas, láminas, páginas) | Sánscrito *paṭṭa* "tabla, plancha" + Griego *πετάννυμι* (petánnymi) "extender, desplegar". 2 lenguas. | tiri-pata patara = "tres hojas" |
| **-thang** | /θaŋ/ | Objetos redondos (piedras, frutos, gotas) | Tibetano *thang* "moneda redonda, círculo" + Persa *sang* "piedra" → thang. 2 lenguas. | páncha-thang phala = "cinco frutos" |
| **-sutra** | /ˈsu.tra/ | Objetos alargados (cuerdas, ríos, caminos) | Sánscrito *sūtra* "hilo, cuerda, línea" + Griego *νητόν* (nētón) "tejido, hilo" → sutra. 2 lenguas. | ekami-sutra sota = "un río" |
| **-rasi** | /ˈra.si/ | Masas incontables (agua, arena, fuego) | Sánscrito *rāśi* "montón, masa, cúmulo" + Persa *ras* "llegar, alcanzar" → rasi. 2 lenguas. | dwi-rasi apa = "dos masas de agua" |
| **-khanda** | /ˈkʰan.da/ | Fragmentos (pedazos, porciones, tajadas) | Sánscrito *khaṇḍa* "fragmento, pieza, segmento" + Persa *kand* "cortar, partir". 2 lenguas. | tiri-khanda mamsa = "tres trozos de carne" |
| **-dhara** | /ˈdʱa.ra/ | Líquidos en recipiente (vasos, cuencos) | Sánscrito *dhārā* "chorro, corriente" + Árabe *حر* *ḥar* "contenedor" → dhara. 2 lenguas. | chatúr-dhara iksir = "cuatro vasos de elixir" |
| **-jati** | /ˈdʒa.ti/ | Clases/tipos abstractos (clases, especies) | Sánscrito *jāti* "clase, género, especie" + Griego *γένος* (génos) "clase, tipo, género". 2 lenguas. | dwi-jati druma = "dos tipos de árbol" |

**Notas:**
- El clasificador se **omite** con unidades de medida (hasarak "mil", sháta "cien"), conceptos temporales (dín "día", rátrí "noche"), y números ordinales.
- Sin clasificador, el número + nombre sugiere una **lectura abstracta o metafórica**: *tiri nūros* = "tres luces" (tres fuentes de luz), pero *tiri-thang nūros* = "tres [objetos redondos] de luz" (tres soles/lunas).
- Cuando el clasificador precede al nombre sin número, funciona como **artículo clasificatorio**: *wan nara* = "la persona (alguna)", *pata patara* = "la hoja (plana)".

**Uso mágico — clasificador como pronombre:**
En contexto ritual, el clasificador puede sustituir al nombre cuando el referente ya se estableció. Funciona como **pronombre clasificatorio**:

```
ma  dwi-wan  dirish-i-e    — púrwa-wan  kár-a,  dwith-wan  ops-a
yo  dos-ANIM ver-PAS-VIS     prim-ANIM   hace    seg-ANIM    ve
"Vi a dos [seres]: el primero actúa, el segundo observa"
```

**Apilamiento de clasificadores** (uso poético/ritual): Dos clasificadores pueden combinarse para describir un objeto con atributos híbridos. Raro en habla cotidiana, pero atestiguado en textos de invocación:

```
ekami-thang-sutra nūros    = "una [redonda-y-alargada] luz" (un relámpago, un bastón de luz)
dwi-pata-wan atma      = "dos [planos-y-animados] espíritus" (entidades con manifestación plana)
```

**Omisión poética del clasificador:** En poesía mágica, omitir el clasificador donde sería esperable crea ambigüedad deliberada — el oyente debe inferir qué tipo de entidad se cuenta. Marca un **registro oracular**:

```
tiri khapa   dirish-i-e
tres esconder vi
"Tres [ocultamientos/almas ocultas/entidades ocultas...] vi"
```

### 3.6 Derivación léxica

#### 3.6.1 Sistema de afijos derivativos

Cada afijo tiene origen documentado en ≥2 lenguas fuente:

| Afijo | Función | IPA | Origen | Ejemplo |
|-------|---------|-----|--------|---------|
| **-tar** | Agente ("el que hace") | /tar/ | Sánscrito -tṛ (agentivo); Griego -τήρ/-τωρ (-tēr/-tōr); Avestan -tar. 3 lenguas. | thel-tár = "voluntario, el que ejerce voluntad" |
| **-ta** | Abstracto ("la cualidad de") | /ta/ | Sánscrito -tā (abstracto); Persa -at (abstracto); Tibetano -ta (abstracción). 3 lenguas. | shaktí-ta = "el estado de poder" |
| **-ka** | Adjetivizador ("relacionado con") | /ka/ | Sánscrito -ka (adjetivizador); Avestan -ka; Tibetano -ka. 3 lenguas. | nús-ka = "consciente, relativo a la conciencia" |
| **-ma** | Resultado/producto ("lo producido por") | /ma/ | Sánscrito -ma (sufijo de resultado); Griego -μα (-ma, resultado de acción); Tibetano -ma (sufijo nominal). 3 lenguas. | kár-ma = "lo hecho, acción realizada" |
| **-sha** | Lugar/contenedor ("donde ocurre") | /ʃa/ | Sánscrito -sthāna → -sha (reducción); Persa -stan → -sha. 2 lenguas. | thel-shá = "lugar de voluntad, santuario de la voluntad" |
| **-nik** | Instrumento ("con lo cual se hace") | /nik/ | Sánsckrit -nika (instrumental); Griego -νική (-nikē) "victoria/instrumento de victoria". 2 lenguas. | man-ník = "instrumento de mente, herramienta mental" |
| **-wan** | Poseedor ("el que tiene") | /wan/ | Sánscrito -van (poseedor); Avestan -van. 2 lenguas. | shaktí-wan = "el que posee poder, poderoso" |
| **-lis** | Diminutivo/honorífico ("pequeño/querido") | /lis/ | Sánscrito -la (diminutivo); Griego -ίσκος (-iskos, diminutivo) → -lis (reducción). 2 lenguas. | nús-lis = "pequeña conciencia, chispa de conciencia" |
| **su-** | Aumentativo/bueno ("bien, grande, excelso") | /su/ | Sánscrito su- "bueno"; Avestan hu-/su-. 2 lenguas. | su-shákti = "gran poder, poder excelso" |
| **a-** | Privativo/negativo ("sin, no-") | /a/ | Sánscrito a- (privativo); Griego ἀ-/ἀν- (alfa privativa). 2 lenguas. | a-nús = "sin conciencia, inconsciente" |
| **pari-** | Transformación ("cambio hacia") | /pa.ri/ | Sánscrito pari- "alrededor, transformación"; Griego περι- (peri-) "alrededor". 2 lenguas. | pari-shám = "transformación de sombra, integración de la sombra" |
| **-thu** | Colectivo ("grupo de") | /θu/ | Sánscrito -thu (colectivo); Tibetano -thu (colectivo). 2 lenguas. | nús-thú = "colectivo de conciencias, campo de conciencia" |

#### 3.6.2 Ejemplos de derivación en cadena

```
thel (voluntad) → raíz semilla
├── thel-tár    = agente de voluntad, practicante
├── thel-tá     = estado de voluntad, volición
├── thel-ká     = relativo a la voluntad, volitivo
├── thel-má     = producto de la voluntad, acto volitivo
├── thel-shá    = lugar de voluntad, santuario
├── thel-ník    = instrumento de voluntad
├── thel-wán    = el que posee voluntad
├── thel-lís    = pequeña voluntad, intención
├── su-thél     = gran voluntad, voluntad excelso
├── a-thél      = sin voluntad, abulia
├── pari-thél   = transformación de voluntad
└── thel-thú    = campo de voluntad, voluntad colectiva
```

### 3.7 Pronombres

| Persona | Singular | Plural |
|---------|----------|--------|
| 1ª | ma | man |
| 2ª | ta | tan |
| 3ª (animado) | sa | san |
| 3ª (inanimado) | ka | kan |

**Origen:**
- **ma**: Sánscrito mám (1sg acusativo); Egipcio m̩ (1sg). 2 lenguas.
- **ta**: Sánscrito tvám (2sg); Egipcio ṯw (2sg). 2 lenguas.
- **sa**: Sánscrito sáḥ (3sg); Egipcio sw (3sg). 2 lenguas.
- **ka**: Sánscrito idám "esto"; Tibetano kha "aquello". 2 lenguas.
- **-n** (plural): Sánscrito -nah (1pl); Árabe -na (plural). 2 lenguas.

### 3.7.1 Registros honoríficos

Kalfírvach distingue tres registros pronominales:

| Registro | Contexto | 1sg | 2sg | 3sg | 1pl | 2pl | 3pl |
|----------|----------|-----|-----|-----|-----|-----|-----|
| **Familiar** | Cotidiano, íntimo | ma | ta | sa/ka | man | tan | san/kan |
| **Cortés** | Social, desconocidos | ma | **tum** | **aj** | man | **tum-thu** | **aj-thu** |
| **Hierático** | Ritual, divinidad, iniciación | **áz** | **thum** | **hú** | **áz-thu** | **thum-thu** | **hú-thu** |

**Origen:**
- **tum** (2sg cortés): Persa *tumā* "tú" (cortés) + Árabe *anta→antum* (2pl, usado como cortés). 2 lenguas.
- **aj** (3sg cortés): Egipcio *ꜤḥꜤ* "él, aquel" → aj; Griego *αὐτός* (autós) → aú- → aj. 2 lenguas.
- **áz** (1sg hierático): Griego *ἐγώ* (egṓ) → eg- → áz; Egipcio *zꜢ* "alma iniciada" → z → áz (refuerzo). 2 lenguas.
- **thum** (2sg hierático): Sánscrito *tvám* → thum (reducción); Tibetano *khyod* → th- + -um (reducción). 2 lenguas.
- **hú** (3sg hierático): Sánscrito *bhū* "ser supremo" → hú; Egipcio *ḥw* "él divino". 2 lenguas.

**Títulos y tratamientos:**

| Título | Uso | Origen |
|--------|-----|--------|
| **pir** | Prefijo: "gran/maestro" (antes del nombre) | Persa *pīr* "sabio, anciano, guía espiritual" |
| **-khán** | Sufijo: "señor/soberano" | Persa *khān* "gobernante"; Árabe *qabīla* "tribu" → khán (asimilación) |
| **-hék** | Sufijo: "sacerdote/mago" | Griego *ἱερατικός* (hieratikós) → hék; Egipcio *ḥkꜢ* "heka, poder mágico" |
| **báp** | Prefijo: "padre/fundador" | Egipcio *bꜢbꜢ* "fundador"; Árabe *bāb* "puerta/portal iniciático" |

**Marcador verbal hierático:** En registro hierático, el verbo **debe** llevar el actitudinal -nam y el sufijo **-h** (Egipcio *ḥ* "sacralidad", Tibetano *-h* causal):

| Forma estándar | Forma hierática |
|---------------|-----------------|
| kár-a-e | kár-a-h-nam |
| as-a-nand | as-a-h-nam-nand |

```
áz   thum   kár-u-h-nam-poi
yo.HIER tú.HIER hacer-FUT-HIER-reverencia-performativo
"Yo, el iniciado, decreto que tú, el divino, actuarás"

ma  tum-te  vach-a-nam
yo  tú.CORT-DAT hablar-PRES-reverencia
"Te hablo con respeto"

pir nús-hék
maestro conciencia-sacerdote
"Gran sacerdote de la conciencia"
```

### 3.8 Demostrativos e interrogativos

| Función | Palabra | IPA | Origen |
|---------|---------|-----|--------|
| "este, esta" | ta | /ta/ | Sánscrito tad "eso"; Tibetano de "eso" → ta. 2 lenguas. |
| "aquel, aquella" | ka | /ka/ | Sánscrito idam→ka; Egipcio kꜣ "eso". 2 lenguas. |
| "¿quién?" | kwa | /kwa/ | Sánscrito kaḥ "¿quién?"; Persa ku "¿dónde?" → kwa. 2 lenguas. |
| "¿qué?" | kím | /kim/ | Sánscrito *kim* "¿qué?" + Persa *ki* "quién/que". 2 lenguas. |
| "¿dónde?" | kwa-na | /kwa.na/ | kwa + -na (locativo) |
| "¿cómo?" | kwa-ka | /kwa.ka/ | kwa + -ka (instrumental) |
| "¿cuándo?" | kwa-dín | /kwa.din/ | kwa + dín ("día/tiempo") |
| "¿por qué?" | kwa-kar | /kwa.kar/ | kwa + kar ("causa") |
| "¿cuál?" | kwa-th | /kwaθ/ | kwa + -th (sufijo ordinal/selectivo) |

**Nota:** El interrogativo "qué" se separó de **ma** (1sg, negación) a **kím** en v0.3 para evitar ambigüedad.

### 3.9 Posesión

Kalfírvach expresa la posesión mediante dos construcciones: **atributiva** (el poseedor modifica al poseído dentro de un sintagma nominal) y **predicativa** (la relación de posesión es ella misma lo que se predica). Ambas usan marcadores ya existentes en el sistema de postposiciones.

#### 3.9.1 Posesión atributiva ("mi luz", "la sombra del mago")

El poseedor se marca con la postposición genitiva **-sya** (§3.2) y **precede** al poseído, siguiendo el orden natural de lenguas SOV — el modificador siempre antecede al núcleo.

**Estructura:**
```
Poseedor-sya + Poseído
```

**Con pronombres:**
```
ma-sya  nūros     = mi luz
ta-sya  zal    = tu sombra
sa-sya  thel    = su voluntad (de él/ella)
ka-sya  mur     = su muro (de eso)
man-sya nús     = nuestra conciencia
tan-sya bhavan  = vuestra casa
san-sya rík     = su grandeza (de ellos/as)
kan-sya khap     = su oscuridad (de esas cosas)
```

**Con nombres completos:**
```
ha  mago-sya   nūros      = la luz del mago
ha  rík  mago-sya zal  = la sombra del gran mago
én  khap  zal-sya wácha = las palabras de unas sombras oscuras
```

**Nota:** La postposición -sya se adjunta al último elemento del sintagma del poseedor, no a cada palabra. En `ha rík mago-sya`, el genitivo va sobre `mago`, no sobre cada modificador.

**Con registros honoríficos:**

| Registro | 1sg | 2sg | 3sg | 1pl | 2pl | 3pl |
|----------|-----|-----|-----|-----|-----|-----|
| Familiar | ma-sya | ta-sya | sa-sya / ka-sya | man-sya | tan-sya | san-sya / kan-sya |
| Cortés | ma-sya | tum-sya | aj-sya | man-sya | tum-thu-sya | aj-thu-sya |
| Hierático | áz-sya | thum-sya | hú-sya | áz-thu-sya | thum-thu-sya | hú-thu-sya |

**Uso con demostrativos y cuantificadores:**
```
ta-sya  nūros     = la luz de esto
ka-sya  zal    = la sombra de aquello
mu-sya  thel    = la voluntad de todo
```

**Posesión atributiva encadenada:** Múltiples niveles de posesión se expresan anidando genitivos:
```
ha  mago-sya  bábu-sya  nús
DEF.SG mago-GEN  padre-GEN conciencia
"la conciencia del padre del mago"
```

#### 3.9.2 Posesión predicativa ("tengo", "tienes")

La predicación de posesión se construye con el **poseedor en dativo** (-te) y el **poseído como sujeto de la cópula as**. Este es el patrón típico de lenguas SOV con dativo posesivo — atestiguado en sánscrito (*mama asti*), griego (*éstí moi*), latín (*mihi est*) y japonés (*watashi ni aru*).

**Estructura:**
```
Poseedor-te + Poseído + as-<TAM>
```

**Origen tipológico:** Sánscrito *mama putraḥ asti* "mi hijo es" = "tengo un hijo" (genitivo + cópula); Griego *ἔστι μοι φῶς* (ésti moi phôs) "es a mí luz" = "tengo luz" (dativo + cópula); Tibetano *nga-la dngos po yod* "a mí cosa hay" = "tengo una cosa" (locativo/dativo + existencial). Kalfírvach sigue el patrón griego con dativo explícito -te.

**Afirmativo:**
```
ma-te   é    nūros  as-a
yo-DAT  INDEF luz  ser-PRES
"A mí una luz es" = "Tengo una luz"

ma-te   ha   zal  as-a-e
yo-DAT  DEF  sombra ser-PRES-VIS
"Tengo la sombra [veo]" = "[Veo que] poseo la sombra"

ta-te   bay   as-a
tú-DAT  miedo ser-PRES
"A ti miedo es" = "Tienes miedo"

sa-te   rík  shaktí  as-a
él-DAT grande poder ser-PRES
"Él tiene gran poder"

man-te  dwi-wan  nara  as-a
nos-DAT dos-ANIM persona ser-PRES
"Tenemos dos personas"
```

**Negativo:**
```
ma-te   nūros  na-as-a
yo-DAT  luz  NEG-ser-PRES
"No tengo luz"

ta-te   zal  na-as-i
tú-DAT  sombra NEG-ser-PAS
"No tuviste sombra"
```

**Con evidenciales y actitudinales:**
```
ma-te   shaktí  as-a-wah-al
yo-DAT  poder   ser-PRES-REVELADO-certeza_mágica
"Por revelación y certeza mágica, tengo poder"

áz-te   nūros  as-a-nand
yo.HIER-DAT luz ser-PRES-alegría
"Yo, iniciado, tengo luz con alegría"
```

**Pasado y futuro:**
```
ma-te   zal  as-i      = "Tuve una sombra"
ma-te   nūros   as-u      = "Tendré luz"
sa-te   máya  as-i-wah  = "Él tuvo ilusión [revelado]"
```

**Interrogativo:**
```
ta-te   nūros  as-a  ka?
tú-DAT  luz  ser-PRES INTERR
"¿Tienes luz?"

ta-te   kím  as-a?
tú-DAT  qué  ser-PRES
"¿Qué tienes?"
```

**Con honoríficos:**
```
tum-te    shánt  as-a-nam
tú.CORT-DAT paz ser-PRES-reverencia
"Usted tiene paz [con respeto]"

áz-te     ha  heka  as-a-h-nam
yo.HIER-DAT DEF magia ser-PRES-HIER-reverencia
"Yo, el iniciado, poseo la magia [en registro hierático]"
```

#### 3.9.3 Contraste entre posesión atributiva y predicativa

| Construcción | Estructura | Ejemplo | Significado |
|-------------|-----------|---------|-------------|
| Atributiva | `Poseedor-sya + Poseído + Verbo` | `ma-sya nūros as-a` | "Mi luz es" (la luz que me pertenece existe/es X) |
| Predicativa | `Poseedor-te + Poseído + as-a` | `ma-te nūros as-a` | "Tengo luz" (poseo luz) |

La diferencia es sutil pero real: la atributiva **presupone** el poseído y predica algo sobre él; la predicativa **afirma** la relación de posesión misma.

```
ma-sya  nūros  khap   as-a   = "Mi luz es oscura" (la luz que tengo: es oscura)
ma-te   nūros  khap   as-a   = "Tengo una luz oscura" (afirmo que poseo algo)
```

**Ambigüedad con la cópula:** Cuando el poseído es un adjetivo o un nombre sin artículo, la construcción predicativa puede generar ambigüedad:

```
ma-te   bay   as-a
yo-DAT  miedo ser-PRES

Interpretación 1: "Tengo miedo" (posesión predicativa, bay = sustantivo "miedo")
Interpretación 2: "Para mí, [algo] es miedoso" (dativo de interés, bay = raíz adjetiva)
```

En la práctica, las raíces de emoción/pasión del léxico se interpretan como **sustantivos poseídos** en esta construcción, y el contexto desambigua. Si se quiere forzar la lectura de dativo de interés, se usa el orden marcado con tópico (§5.1):

```
ma ho,  ha   nūros  bay   as-a
yo TOP  DEF  luz  miedo ser-PRES
"En cuanto a mí, la luz es atemorizante" (NO "tengo miedo de la luz")
```

#### 3.9.4 Posesión en cláusulas complejas

El poseedor en genitivo puede ser el antecedente de una relativa:
```
ya  ma  dirish-i-e,    ha  nara-sya  zal
REL yo  ver-PAS-VIS     DEF persona-GEN sombra
"la sombra de la persona que yo vi"
```

Y el dativo posesivo puede incrustarse en subordinadas:
```
ma  yan-a-e       ti   sa-te   ha  shaktí  as-a
yo  saber-PRES-VIS QUE  él-DAT DEF  poder   ser-PRES
"Sé que él tiene el poder"
```

#### 3.9.5 Resumen rápido

| Qué querés decir | Cómo se dice | Patrón |
|-----------------|-------------|--------|
| "mi luz" | ma-sya nūros | Pronombre-sya + Nombre |
| "la sombra del mago" | ha mago-sya zal | Nombre-sya + Nombre |
| "tengo luz" | ma-te nūros as-a | Pronombre-te + Nombre + as |
| "tengo miedo" | ma-te bay as-a | Pronombre-te + Abstracto + as |
| "no tengo sombra" | ma-te zal na-as-a | na- sobre as |
| "tuviste poder" | ta-te shaktí as-i | as en pasado |
| "tendré luz" | ma-te nūros as-u | as en futuro |
| "¿tenés luz?" | ta-te nūros as-a ka? | + partícula ka |

### 3.10 Adverbios

Kalfírvach expresa la función adverbial mediante **raíces adverbiales léxicas** (tiempo, lugar), **derivación** desde adjetivos (modo), y **partículas independientes** (grado). La posición del adverbio varía según su tipo, siguiendo tendencias naturales de lenguas SOV.

#### 3.10.1 Posición sintáctica

| Tipo | Posición | Ejemplo |
|------|----------|---------|
| Temporal | Inicio de oración (tema, $§5.1) | `nun ma kár-a` = "ahora actúo" |
| Locativo | Tras el SN sujeto, antes del SV | `ma ida kár-a` = "yo aquí actúo" |
| Modo | Inmediatamente antes del verbo | `ma rík-ka kár-a` = "actúo grandemente" |
| Grado | Inmediatamente antes del elemento que modifica | `tís rík as-a` = "es muy grande" |

**Excepción — foco:** Cualquier adverbio puede desplazarse a la posición inmediatamente preverbal para recibir énfasis (**foco estrecho**):
```
ma  kár-a    sárí-ka    = "actúo rápidamente" (neutro)
ma  sárí-ka  kár-a      = "actúo RÁPIDAMENTE" (foco: no lentamente)
```

#### 3.10.2 Adverbios temporales

Kalfírvach posee un rico conjunto de adverbios temporales en el léxico de `tiempo_domestico`:

| Adverbio | IPA | Significado | Origen |
|----------|-----|-------------|--------|
| **nun** | /nun/ | "ahora" | Griego *nyn* + Persa *nūn* → nun. 2 lenguas. |
| **yawm** | /jawm/ | "hoy" | Árabe *yawm* "día" + Persa *yawm* "día" → yawm. 2 lenguas. |
| **ams** | /ams/ | "ayer" | Árabe *ams* "ayer" + Persa *dī* (con asimilación) → ams. 2 lenguas. |
| **ghat** | /ɣad/ | "mañana" (día siguiente) | Árabe *ġad(an)* "mañana" + Persa *qad* "tiempo" → ghat. 2 lenguas. |
| **dáim** | /'da.im/ | "siempre" | Árabe *dāʾim* "permanente, continuo" + Persa *dāyem* "siempre". 2 lenguas. |
| **áb-d** | /'ab.d/ | "nunca" | Persa *āb* "agua (tiempo)" + Árabe *dāʾim* (contracción negativa). 1 fuente + a- privativo del léxico derivativo. |
| **qábal** | /ˈka.bal/ | "antes" (anterioridad) | Árabe *qabl* "antes" + Persa *qabl* "previo". 2 lenguas. |
| **bákd** | /'bakd/ | "después" (posterioridad) | Árabe *baʿd* "después" + Persa *pas* → bakd (fusión). 2 lenguas. |
| **bád-zam** | /'bad.zam/ | "a veces" | Persa *bād* "al viento" + Árabe *zamān* "tiempo" → "en tiempo al viento" = "ocasionalmente". 2 lenguas. |
| **bákra** | /ˈbak.ra/ | "temprano" | Árabe *bakr* "madrugada, temprano" + Persa *bāmdād* "amanecer" → bakr. 2 lenguas. |
| **atáp** | /'a.taf/ | "tarde" (hora tardía) | Árabe *ʿatash* "tarde" + Persa *towf* "atardecer" → atáp. 2 lenguas. |

```
nun  ma  kár-a        = "Ahora actúo"
yawm ha  nūros  rík as-a = "Hoy la luz es grande"
ams  zal kár-i-e     = "Ayer la sombra actuó [veo]"
ghat ma-te  nūros as-u  = "Mañana tendré luz"
```

**Con evidenciales y actitudinales (el adverbio temporal no bloquea la partícula verbal):**
```
ams  zal  kár-i-wah-al
ayer sombra actuar-PAS-REVELADO-certeza_mágica
"Ayer la sombra actuó [revelado con certeza mágica]"
```

#### 3.10.3 Adverbios locativos

| Adverbio | IPA | Significado | Origen |
|----------|-----|-------------|--------|
| **idá** | /i'da/ | "aquí" | Sánscrito *iha* + Avestan *idha* → ida (/h/→O, /dh/→/d/). 2 lenguas. |
| **ta-ná** | /ta'na/ | "acá, por acá" | ta (demostrativo) + -na (locativo). — Productivo. |
| **ka-ná** | /ka'na/ | "allá, por allá" | ka (demostrativo distal) + -na (locativo). — Productivo. |
| **antár** | /an'tar/ | "dentro, adentro" | Sánscrito *antar* "dentro, entre" + Persa *andar* "dentro, en medio de". 2 lenguas. |
| **bahí** | /ba'hi/ | "fuera, afuera" | Sánscrito *bahis* "fuera" + Árabe *bāḥ* "exterior, afuera" → bahí. 2 lenguas. |
| **kwa-ná** | /kwa'na/ | "¿dónde?" | kwa (interrogativo) + -na (locativo). Del §3.8. |

```
idá  ha  nūros  as-a    = "Aquí está la luz"
anta-ná  zal  kár-a  = "Dentro, la sombra actúa"
ma  idá  as-a-e       = "Estoy aquí [veo]"
ka-ná  kwa  as-a?     = "¿Quién está allá?"
```

**Locativos como argumentos:** Los adverbios locativos pueden funcionar como complemento circunstancial sin postposición adicional. No llevan -na cuando ya la incorporan: *idá* (ida = i + da = "en esto" → lexicalizado), *ka-ná*, *ta-ná*.

**Locativos con postposiciones adicionales** (para matices):
```
idá-ra  aya-ro!    = "¡Ven desde aquí!"
ka-ná-muk  gach-a  = "Va hacia allá"
```

#### 3.10.4 Adverbios de modo (derivación)

Los adverbios de modo se forman añadiendo el sufijo **-ka** (instrumental, §3.2) a una **raíz adjetiva**. El significado es "de manera [adjetivo]" o "con [cualidad del adjetivo]".

**Origen tipológico:** El instrumental de cualidad es la principal fuente de adverbios de modo en las lenguas del mundo. Sánscrito usa el instrumental (-ena, -śas); Griego usa -ως (-ōs); Persa usa جفتی (-āne). Kalfírvach extiende la postposición -ka (instrumental, "con/mediante") para cubrir también la función adverbial — el mismo sufijo que ya funciona como adjetivizador (§3.6.1).

**Regla:**
```
Adjetivo + -ka → Adverbio de modo
```

| Adjetivo | Adverbio | Significado |
|----------|----------|-------------|
| rík "grande" | rík-ka | "grandemente, con grandeza" |
| sárí "rápido" | sárí-ka | "rápidamente, con rapidez" |
| bátí "lento" | bátí-ka | "lentamente, con lentitud" |
| khap "oscuro" | khap-ka | "oscuramente, con oscuridad" |
| shánt "calmo" | shánt-ka | "calmadamente, con calma" |
| narm "suave" | narm-ka | "suavemente, con suavidad" |
| shwét "blanco" | shwét-ka | "blancamente, con pureza/blancura" |

```
ma  rík-ka  kár-a       = "Actúo grandemente"
sa  sárí-ka  gach-a     = "Él/Ella va rápidamente"
ha  nūros  shánt-ka  as-a = "La luz es calmadamente" = "La luz existe en calma"
ta  khap-ka  vach-i-e    = "Hablaste oscuramente [veo]" = "Hablaste de manera críptica"
```

**Doble lectura instrumental/adverbial:**

La partícula -ka puede leerse como instrumental o adverbial según el contexto:
```
ma  shaktí-ka  kár-a
1sg poder-INST hacer-PRES
= "Actúo con poder" (instrumental: poder como herramienta)
= "Actúo poderosamente" (adverbial: poder como modo)
```

Ambas lecturas convergen en la misma realidad — no hay ambigüedad problemática. Es una **polisemia controlada** tipológicamente natural (cf. inglés *strongly* / *with strength*).

**Adverbios de modo irregulares o lexicalizados:**
| Forma | Significado | Origen |
|-------|-------------|--------|
| **ich-ka** | "voluntariamente, por deseo" | ich "querer" + -ka → lexicalizado como adverbio |

#### 3.10.5 Adverbios de grado

Los adverbios de grado modifican adjetivos, verbos u otros adverbios para indicar intensidad. Pueden ser palabras independientes o prefijos derivativos.

**Independientes (modifican elementos del SN/SV):**

| Adverbio | IPA | Valor | Origen (≥2) |
|----------|-----|-------|-------------|
| **tís** | /tis/ | "muy" (intensificador positivo) | Sánscrito *tīvra* "intenso, fuerte, agudo" + Persa *tīz* "agudo, rápido, filoso". 2 lenguas. |
| **lav** | /law/ | "poco, apenas" (atenuador) | Sánscrito *lava* "pequeña porción, instante, átomo" + Persa *lab* "labio, borde, pequeña cantidad". 2 lenguas. |
| **atísh** | /'a.tiʃ/ | "demasiado, excesivamente" (exceso) | Sánscrito *ati* "más allá, sobre" + Persa *ātish* "fuego" → fusión semántica "sobrefuego". 2 lenguas. |
| **káf** | /kaf/ | "bastante, suficiente" (suficiencia) | Árabe *kāfī* "suficiente" + Persa *kāf* "suficiente, bastante". 2 lenguas. |

**Posición sintáctica:**
Los adverbios de grado se colocan **inmediatamente antes** del elemento que modifican:

```
tís  rík   as-a     = "Es muy grande"      (modifica adjetivo)
lav  khap   as-a     = "Es poco oscuro"     (modifica adjetivo)
tís  sárí-ka  gach-a  = "Va muy rápidamente"  (modifica adverbio)
ma   lav   kár-a    = "Actúo poco"         (modifica verbo)
```

**Con verbos evidenciales:**
```
atísh  rík  as-i-wah       = "Fue demasiado grande [revelado]"
ha   nūros  káf  rík  as-a-e  = "La luz es suficientemente grande [veo]"
```

**Prefijo aumentativo su- vs. adverbio tís:**

La diferencia entre el prefijo léxico **su-** (§3.6.1) y el adverbio **tís**:

| Forma | Estructura | Significado |
|-------|-----------|-------------|
| `su-shákti` | prefijo + nombre | "superpoder, poder excelso" (cambio léxico: es OTRA palabra) |
| `tís rík` | adverbio + adjetivo | "muy grande" (modificación sintáctica: es el MISMO adjetivo intensificado) |

`su-` crea una **nueva raíz léxica**, mientras que `tís` **modifica sintácticamente** al elemento existente. Son complementarios.

#### 3.10.6 Adverbios modales

Kalfírvach ya expresa modalidad epistémica mediante el sistema de evidenciales (§2.1) y actitudinales (§2.2) anclados al verbo. Sin embargo, existe un adverbio modal para expresar incertidumbre sin compromiso evidencial:

| Adverbio | IPA | Valor | Origen (≥2) |
|----------|-----|-------|-------------|
| **sháyat** | /'ʃa.jat/ | "quizás, tal vez" | Persa *shāyad* "quizás" + Sánscrito *śayyate* "yacer, permanecer incierto" → fusión. 2 lenguas. |

```
sháyat  ha  nūros  as-a    = "Quizás la luz es"  (incertidumbre, sin evidencial)
sháyat  ma  kár-u-kal    = "Quizás actuaré"    (incertidumbre + modo hipotético)
```

**Contraste con el sistema verbal:** El adverbio `sháyat` expresa duda sin especificar la fuente de conocimiento. El sistema evidencial expresa certeza sobre *cómo* se conoce. Pueden combinarse:

```
sháyat  ha  máya  as-a-wah
quizás  DEF  ilusión ser-PRES-REVELADO
"Quizás la ilusión es [revelado]" = "Me fue revelado que quizás la ilusión existe"
```

La incertidumbre recae sobre el contenido (`sháyat`), la certeza sobre el modo de conocimiento (`-wah`).

#### 3.10.7 Resumen rápido

| Qué querés decir | Cómo se dice | Patrón |
|-----------------|-------------|--------|
| "ahora actúo" | nun ma kár-a | Temporal al inicio |
| "ayer actuó" | ams sa kár-i | Temporal al inicio |
| "estoy aquí" | ma idá as-a | Locativo antes del SV |
| "va adentro" | antár gach-a | Locativo antes del SV |
| "actúa rápidamente" | sárí-ka kár-a | Adj + -ka antes del verbo |
| "es muy grande" | tís rík as-a | Grado antes del adj |
| "es demasiado oscuro" | atísh khap as-a | Grado antes del adj |
| "tengo suficiente poder" | ma-te káf shaktí as-a | Grado antes del nombre |
| "quizás la luz es" | sháyat ha nūros as-a | Modal al inicio |
| "habló oscuramente [veo]" | khap-ka vach-i-e | Modo antes del verbo |

### 3.11 Existencia ("hay", "existe")

Kalfírvach no tiene un verbo separado para "existir". La **existencia** se expresa mediante la cópula **as** (§3.4) en una construcción específica que **no predica una cualidad** del sujeto sino su **mera presencia en el universo del discurso**. Este patrón está atestiguado en las lenguas fuente — sánscrito *asti* ("es, existe, hay"), griego *ἔστι* ("es, existe, hay"), árabe *yakūnu* "ser/existir" — y es común en lenguas SOV (japonés *aru*, turco *var*).

#### 3.11.1 Construcción existencial básica

**Estructura:**
```
(<>-na)?          (<SN>)          as-<TAM>
(locativo opcional)   (nombre indefinido/definido)     cópula
```

El elemento cuya existencia se afirma es el **sujeto sintáctico** de la cópula. No necesita artículo ni determinante.

**Con nombre indefinido (más común — equivalente a "hay un/una"):**
```
é   nūros  as-a        = "Hay una luz" / "Una luz existe"
é   zal  as-i       = "Hubo una sombra"
én  shaktí  as-a     = "Hay unos poderes"
```

**Con nombre escueto (sin artículo — existencia genérica):**
```
nūros  as-a            = "Hay luz" / "Existe luz"
zal  as-i           = "Hubo sombra"
shánt  as-u          = "Habrá paz"
```

**Con nombre definido (existencia específica — "lo conocido existe"):**
```
ha  nūros  as-a        = "La luz existe" / "Está la luz"
ha  zal  as-i-wah   = "La sombra existió [revelado]"
```

**En negación (no existencia):**
```
é   nūros  na-as-a     = "No hay una luz"
nūros  na-as-a         = "No hay luz" / "La luz no existe"
ha  nūros  na-as-a-e   = "La luz no existe [veo]"
```

#### 3.11.2 Existencia locativa ("en X hay Y")

Cuando se especifica una **ubicación**, el locativo en **-na** precede al SN:

**Estructura:** `<>-na <SN> as-a`

```
díwa-na  é   súrua  as-a      = "En el cielo hay un sol"
ghasák-na  nūros  na-as-a       = "En la oscuridad no hay luz"
ha  thel-na  shánt  as-a      = "En la voluntad hay paz"
```

**Orden de palabras:** En existencia locativa, el locativo suele ir al inicio (tema), pero puede moverse para foco:
```
é   súrua  as-a   díwa-na     = "HAY un sol en el cielo" (foco en existencia, no en ubicación)
díwa-na  é   súrua  as-a     = "En el cielo hay un sol" (foco neutro, ubicación como tema)
```

**Ejemplos del cuento (KFA ya producido):**
```
hán ápa ghasák-na, ha chandára as-i
"Aquí agua oscuridad-LOC, DEF.SG luna ser-PAS"
"En la oscuridad de las aguas, la Luna estaba/existía"

↑ El existencial con nombre definido y locativo produce una lectura de "existencia situada"
```

#### 3.11.3 Existencia vs. predicación

La diferencia entre `as` existencial y `as` predicativo está en la **presencia de un predicado nominal/adjetival**:

| Construcción | Estructura | Ejemplo | Significado |
|-------------|-----------|---------|-------------|
| Existencial | `<SN> as-a` | `nūros as-a` | "hay luz" (la luz existe) |
| Predicativa | `<SN> <pred> as-a` | `nūros khap as-a` | "la luz es oscura" (cualidad) |
| Posesiva (§3.9.2) | `<SN-te> <SN> as-a` | `ma-te nūros as-a` | "tengo luz" (posesión) |

- **Existencial** → la cópula es todo el predicado: "X es" = "X existe/hay X"
- **Predicativa** → la cópula conecta al sujeto con un atributo: "X es Y"
- **Posesiva** → la cópula afirma que el poseído existe para el poseedor

**Regla práctica:**
- Si `as-<tiempo>` está **solo** al final de la oración (sin adjetivo, sin sintagma nominal en aposición), es **existencial**.
- Si hay un adjetivo, un nombre predicativo, o un adverbio de modo que modifica a `as`, es **predicativo**.

```
é   nūros  as-a                 = EXISTENCIAL: "Hay una luz"
é   nūros  rík  as-a            = PREDICATIVO: "Una luz es grande"
é   nūros  shánt-ka  as-a       = PREDICATIVO: "Una luz es calmadamente" (modo)
```

**Con evidenciales (la partícula no cambia la lectura):**
```
nūros  as-a-e                   = EXISTENCIAL: "Hay luz [veo]"
nūros  rík  as-a-e              = PREDICATIVO: "La luz es grande [veo]"
```

#### 3.11.4 Existencia en tiempo pasado y futuro

```
díwa-na  é   súrua  as-i      = "En el cielo había/hubo un sol"
nūros  as-u                     = "Habrá luz" (existencia futura)
é   rík  zal  as-i-wah      = "Hubo una gran sombra [revelado]"
```

**Memoria ritual — existencial con -djet (permanencia):**
```
ha  thel  as-a-djet          = "La voluntad existe en permanencia estática"
ha  nūros  neh-as-a            = "La luz existe en el ciclo eterno" (con temporalidad mágica neh-)
```

#### 3.11.5 Pregunta existencial

**Sí/no:**
```
nūros  as-a  ka?              = "¿Hay luz?"
é   rík  zal  as-i  ka?    = "¿Hubo una gran sombra?"
díwa-na  é   súrua  as-a  ka?  = "¿Hay un sol en el cielo?"
```

**De contenido:**
```
kím  as-a?                  = "¿Qué hay?" / "¿Qué existe?"
kwa  idá  as-a?             = "¿Quién está aquí?"
```

#### 3.11.6 Sustantivo derivado: as-tá ("existencia, ser")

Del afijo abstracto **-ta** (§3.6.1) sobre la raíz copulativa **as**:

```
as-tá  = "existencia, el estado de ser, la cualidad de existir"
```

```
ha  as-tá-na  mu   nūros  as-a
DEF existencia-LOC todo luz  ser-PRES
"En la existencia, todo es luz"

as-tá  na-as-a  kwa-na?      = "La existencia no está ¿dónde?" = "La existencia no tiene lugar" (poético)
```

**Contraste con otras abstracciones derivadas:**
| Forma | Significado | Tipo |
|-------|-------------|------|
| as-tá | existencia, estado de ser | Abstracto de la cópula |
| as-má | "lo hecho por el ser" = "lo creado, el resultado de existir" | Resultado (§3.6.1) |
| as-ka | "relativo al ser" = "existencial, ontológico" | Adjetivo (§3.6.1) |

#### 3.11.7 Resumen rápido

| Qué querés decir | Cómo se dice | Patrón |
|-----------------|-------------|--------|
| "hay luz" | nūros as-a | SN + as |
| "hay una luz" | é nūros as-a | Indef + SN + as |
| "había una sombra" | é zal as-i | Indef + SN + as pasado |
| "no hay luz" | nūros na-as-a | SN + neg-as |
| "en el cielo hay un sol" | díwa-na é súrua as-a | Loc + Indef + SN + as |
| "¿hay luz?" | nūros as-a ka? | SN + as + interr |
| "el sol existe [veo]" | ha súrua as-a-e | Def + SN + as-evid |
| "la existencia" | as-tá | as + -ta (abstracto) |

### 3.12 Modalidad

Kalfírvach codifica la modalidad mediante **tres raíces verbales modales** que funcionan como verbos plenos con flexión completa. A diferencia del griego antiguo o el turco — que tienen sistemas modales auxiliares más complejos —, KFA mantiene un sistema **mínimo y elegante** de tres raíces que cubren el espacio semántico de la volición, la capacidad y la obligación, y se combinan productivamente con el causativo, el infinitivo, las cláusulas subordinadas y los modos de realidad.

Las tres raíces modales proceden de **tres raíces PIE distintas que han convergido semánticamente** en KFA: PIE *h₂eyḱ-* ("ser dueño de, sostener") → ich- (volición); PIE *dʰwer-* ("cerrar, contener, tener poder") → dún- (capacidad); PIE *dʰer-* ("sostener, portar, cargar") → dhar- (obligación). Esta **convergencia multi-PIE** (cada raíz de un étimo distinto) justifica la coherencia tipológica del sistema y evita que KFA dependa de un solo clado lingüístico. La distribución posterior en las 6 lenguas fuente (griego koiné, indio (tántrico), egipcio demótico, persa/avéstico, tibetano clásico, árabe esotérico) muestra cómo lenguas de familias muy distintas desarrollaron raíces modales con la misma estructura semántica tripartita: volición / capacidad / obligación.

#### 3.12.1 Sistema modal: tres raíces básicas

| Raíz | IPA | Significado | Tipo | Etimología documentada (3 lenguas) |
|------|-----|-------------|------|--------------------------------------|
| **ich-** | /itʃ/ | "querer, desear" | Volición | Sánscrito *icchā* (इच्छा, "deseo, voluntad") — justifica la **forma** africada /tʃ/, única con africada inicial en este contexto semántico + Avestan *iša-* (𐬫𐬴𐬀-, "desear, querer") + Egipcio *mrj* (𓄟𓂋𓏭, "amar, querer", en PGM y textos demóticos). PIE *h₂eyḱ-* "ser dueño de". 3 lenguas. |
| **dún-** | /dun/ | "poder, ser capaz" | Capacidad / Permiso | Griego *dýnamai* (δύναμαι, "poder, ser capaz") — raíz δυν- que da forma y vocal /u/ + Persa *tavānestan* (توانستن, "poder") — reducción *tavān* → coda nasal /n/ + Egipcio *ḥkꜣ* (heka, "poder mágico", central en rituales KFA). PIE *dʰwer-* "sostener, tener poder". 3 lenguas. |
| **dhar-** | /dʰar/ | "deber, estar obligado" | Obligación deóntica | Avestan *dar-* (𐬛𐬀𐬭-, "sostener, portar, tener") — raíz indoirania + Persa *dāshtan* (داشتن, "tener, deber, estar obligado a") — matiz de posesión obligatoria + Sánscrito *dhar-* (धृ, "sostener, portar") — justifica la forma aspirada /dʰ/. PIE *dʰer-* "sostener, mantener". 3 lenguas. |

**Verificación fonológica** (per fonología §3):
- `ich-` = VC, onset vacío + coda africada — válido.
- `dún-` = CVC, onset /d/ + coda nasal /n/ — válido.
- `dhar-` = CVC, onset /dʰ/ (dh, fonema opcional) + coda líquida /r/ — válido.

**Justificación del diseño etimológico (3 lenguas por raíz, no 2):**

La expansión de 2 a 3 lenguas por etimología responde al principio de **distribución etimológica equilibrada** entre las 6 lenguas fuente, para que KFA no dependa de una sola tradición. En este caso:
- **ich-**: 1/3 sánscrito (la africada inicial solo se justifica con Skt icchā; Avestan da la raíz semántica, Egipcio el matiz emocional de "querer = amar").
- **dún-**: 0/3 sánscrito (la raíz se reconstruye completamente desde Gk + Persa + Egipcio; el sánscrito *dhárman* fue desplazado porque su significado es más "ley, orden cósmico" que "poder personal" y no encajaba en la semántica dinámica de KFA).
- **dhar-**: 1/3 sánscrito (la forma aspirada /dʰar-/ se mantiene como anclaje sánscrito, pero el SIGNIFICADO de "obligación" se documenta con Avestan dar- "tener, portar" y Persa dāshtan "tener obligación").

**Origen tipológico del sistema:**

La decisión de tener solo tres raíces modales básicas (en vez de auxiliares más complejos como el griego antiguo con sus múltiples formas de *eimí* y *phēmí* en distintos aspectos, o el turco con sus modalidades derivadas) se justifica por el principio de **mínimo sistema productivo**: el resto de la gramática (causativo, infinitivo, cláusula subordinada con *ti*, modo hipotético *-kal*, adverbios modales) cubre los matices modales que estas tres raíces solas no expresarían explícitamente.

---

#### 3.12.2 ich- (volición, deseo)

**ich-** expresa **querer hacer, desear, tener la voluntad de**. Es la raíz para todo lo que el hablante elige, anhela o se propone.

**Etimología detallada (3 lenguas):**
- La **forma** /itʃ/ con africada inicial se justifica principalmente por Sánscrito *icchā* (इच्छा, "deseo, voluntad") — es la única raíz entre las 6 lenguas fuente con africada inicial en este contexto semántico. La africada /tʃ/ es típicamente sudasiática.
- El **significado** "querer, desear" se documenta también en Avestan *iša-* (𐬫𐬴𐬀-, "querer, desear", raíz verbal irania) y en Egipcio *mrj* (𓄟𓂋𓏭, "amar, querer", atestiguado abundantemente en PGM y textos demóticos rituales).
- **3 lenguas**: Sánscrito (forma) + Avestan (significado irano) + Egipcio (significado afroasiático). La distribución etimológica evita que la raíz quede anclada solo al sánscrito: la FORMA es sudasiática, pero el CONCEPTO modal es pan-tipológico (también Griego ἐθέλω, Tibetano 'dod pa, Árabe arāda tienen la misma función).

**Conjugación completa** (es un verbo regular, sigue la flexión estándar):

```
ma  ich-a       = "quiero" (presente)
ma  ich-i       = "quise / quería" (pasado)
ma  ich-u       = "querré" (futuro)
ma  ich-a-e     = "quiero [veo]" (visual: constato mi deseo)
ma  ich-a-wah   = "quiero [revelado]" (revelación: el deseo me fue dado)
ma  ich-a-nand  = "quiero con alegría"
```

**Con evidenciales y actitudinales** (sigue la posición estándar del sistema verbal, §3.3):
```
ta  ich-a-kal-nam    = "querrías [con reverencia]" (hipotético reverencial)
```

**En negación:**
```
ma  na-ich-a    = "no quiero"
ma  na-ich-i    = "no quise / no quería"
```

**En interrogación:**
```
ta  ich-a  ka?  = "¿Querés?"
ta  na-ich-a ka? = "¿No querés?"
```

**Atestiguado en el corpus** (cuento y gramática): ya aparece en `ma nūros kár-an ich-a` (§3.3.4, "quiero hacer luz") y en `ta ich-a ekami` (cuento, "quiero uno").

---

#### 3.12.3 dún- (capacidad, permiso)

**dún-** expresa **poder, ser capaz, tener la capacidad o el permiso de hacer algo**. Cubre tanto la **habilidad** (poder hacer por capacidad propia) como el **permiso** (poder hacer por autorización externa); el contexto y los evidenciales desambiguan.

**Etimología detallada (3 lenguas, sin sánscrito):**
- Griego *dýnamai* (δύναμαι, "poder, ser capaz") — raíz δυν- que da la consonante inicial /d/ y la vocal /u/. Es la fuente formal más clara.
- Persa *tavānestan* (توانستن, "poder, ser capaz") — reducción a *tavān* → coda nasal /n/ y consonante inicial /t/ → KFA /d/ (ensordecimiento en posición inicial de palabra sánscrita, ya documentado como préstamo).
- Egipcio *ḥkꜣ* (heka, "poder mágico, heka") — concepto central de la tradición ritual egipcia, perfectamente alineado con la semántica KFA de "poder" en contexto ritual y cotidiano.
- **3 lenguas, 0/3 sánscrito**: la raíz se reconstruye completamente desde Griego + Persa + Egipcio, distribuyendo la carga etimológica en tres familias lingüísticas distintas (IE occidental, IE iranio, afroasiático). Esta distribución refuerza la coherencia tipológica de la raíz y la integra con la tradición ritual egipcia que es central en KFA.

**Conjugación completa:**

```
ma  dún-a       = "puedo" (presente)
ma  dún-i       = "pude / podía" (pasado)
ma  dún-u       = "podré" (futuro)
ma  dún-a-e     = "puedo [veo]" (constato mi capacidad)
ma  dún-a-anu   = "puedo [inferido]" (infiero de los signos que puedo)
ma  dún-a-kal   = "podría" (hipotético: capacidad condicional)
ma  na-dún-a    = "no puedo"
```

**Desambiguación habilidad vs. permiso (con evidenciales y actitudinales):**

```
ma  dún-a-som       = "puedo (físicamente, en este plano)" → habilidad
ma  dún-a-wah       = "puedo (me fue revelado que se me permite)" → permiso
ma  dún-a-al        = "puedo (con certeza mágica, es legítima mi capacidad)" → ambas
ma  dún-a-bay       = "puedo (con miedo: puedo pero temo)" → permiso temeroso
```

**Atestiguado en el corpus**: ya aparece en §4.4.4:
```
yas  ma  dún-a,   ma  kár-u-kál
"si puedo, actuaría (potencialmente)"
```

---

#### 3.12.4 dhar- (obligación deóntica)

**dhar-** expresa **deber, estar obligado a, tener la necesidad moral o social de hacer algo**. Es la raíz para obligación, mandato interno (conciencia) o externo (ley, norma, promesa).

**Etimología detallada (3 lenguas):**
- Sánscrito *dhar-* (धृ, "sostener, portar, mantener") — fuente formal: justifica la **forma** aspirada /dʰar-/ (la consonante aspirada /dʰ/ solo se justifica robustamente desde el sánscrito, donde /dʰ/ es fonema pleno).
- Avestan *dar-* (𐬛𐬀𐬭-, "sostener, portar, tener") — fuente semántica indoirania: la metáfora de "cargar con un peso" (= cargar con una obligación).
- Persa *dāshtan* (داشتن, "tener, poseer, deber, estar obligado a") — fuente semántica iranio-occidental: dāshtan se usa tanto para "tener posesiones" como para "tener obligación", y KFA dhar- hereda ambos matices.
- **3 lenguas, 1/3 sánscrito**: la forma es sánscrita (necesaria por la aspiración /dʰ/), pero el SIGNIFICADO se documenta con dos lenguas iranias (Avestan + Persa), evitando que la semántica quede reducida a la tradición védica.

La metáfora de "sostener, portar" da el matiz de **"sostener una obligación"** — cargar con un deber como quien carga con un peso. Esta metáfora es convergente en las tradiciones iranias (avéstico, persa) y en la sudasiática védica, y está semánticamente alineada con la idea KFA de "cumplir un deber" como acto físico-espiritual.

**Conjugación completa:**

```
ma  dhar-a       = "debo" (presente)
ma  dhar-i       = "debía" (pasado, también "debí haber")
ma  dhar-u       = "deberé" (futuro)
ma  dhar-a-e     = "debo [veo]" (constato mi obligación)
ma  dhar-a-wah   = "debo [revelado]" (la obligación me fue revelada)
ma  dhar-a-wíl   = "debo con determinación" (deber internalizado)
ma  dhar-a-nam   = "debo con reverencia" (deber reverencial, ante lo sagrado)
ma  dhar-a-bay   = "debo con miedo" (obligación temerosa)
ma  dhar-a-krod  = "debo con ira" (obligación forzada por indignación)
ma  na-dhar-a    = "no debo"
```

**Modalidad débil (debería):** se obtiene agregando el modo de realidad **-kal** (§2.3) al modal:
```
ma  dhar-a       = "debo" (obligación firme, realizada)
ma  dhar-a-kal   = "debería" (obligación hipotética, irrealis, no realizada aún)
```

**Origen tipológico del `-kal` como debilitador deóntico:** tipológicamente análogo al sufijo condicional/irrealis de muchas lenguas: turco `-sA gerekirdi`, japonés `-ba yokatta`, persa می‌بایست (*mi-bāyad*, literalmente "debería" por sufijo subjuntivo). El `-kal` marca la irrealidad del cumplimiento, lo que automáticamente debilita la obligación.

**Variación pronominal:**

```
ta  dhar-a          = "debés" (cortés o familiar según registro pronominal)
tum dhar-a          = "usted debe"
áz  dhar-a-h-nam    = "yo, iniciado, debo [en registro hierático]"
```

---

#### 3.12.5 Modal + infinitivo (-an)

La construcción más natural con modales en KFA es **modal conjugado + infinitivo del verbo principal** (verbo en `-an`, §3.3.4). El orden es **modal primero, infinitivo al final** (como auxiliar preverbal en SOV):

```
ma  dún-a   kár-an     = "puedo hacer"
ma  dhar-a  gach-an     = "debo ir"
ma  ich-a   vach-an     = "quiero hablar"
ta  dún-a   dirish-an   = "podés ver"
```

**Con evidenciales y actitudinales** (la flexión se aplica al modal, no al infinitivo):
```
ma  dún-a-e-nand   kár-an    = "puedo [veo, con alegría] hacer"
ma  dhar-a-wah-al  gach-an   = "debo [revelado, con certeza] ir"
```

**Negación:** la negación recae sobre el modal, no sobre el infinitivo:
```
ma  na-dún-a   kár-an    = "no puedo hacer"
ma  na-dhar-a  gach-an   = "no debo ir"
ma  na-ich-a   vach-an   = "no quiero hablar"
```

**Doble negación modal + infinitivo negativo (rara, enfática):**
```
ma  na-dún-a   na-kár-an    = "no puedo NO hacer" = "no puedo evitar hacer" (connotación ritual)
```

---

#### 3.12.6 Modal + cláusula subordinada (ti)

Para acciones que involucran un cambio de sujeto, un control compartido, o una elaboración más rica que un simple infinitivo, el modal se combina con una cláusula subordinada introducida por **ti** (§4.4.2):

```
ma  dún-a   ti   ma  gach-u      = "puedo (que vaya)" = "puedo ir"
ma  dhar-a  ti   nūros  as-a       = "debo (que la luz sea)" = "la luz debe ser"
ma  ich-a   ti   ta  vach-a      = "quiero (que vos hables)" = "quiero que hables"
```

**Con evidenciales en ambas cláusulas (pueden diferir):**
```
ma  dún-a-e   ti   sa  gach-u-wah
yo  poder-VIS  QUE  él ir-FUT-REVELADO
"Puedo [lo veo] ir" + "él irá [me fue revelado]" → "puedo ver que él irá"
```

**Doble modal con subordinada (modal que rige otro modal):**
```
ma  ich-a   ti   ma  dún-a   kár-an
yo  querer  QUE  yo poder   hacer-INF
"Quiero poder hacer" (capacidad condicionada al deseo)
```

**Anidamiento profundo (estilo ritual):**
```
ma  dhar-a   ti   ta  ich-a   ti   sa  dún-a   vach-an
yo  deber    QUE  tú querer QUE  él poder hablar-INF
"Debo querer que él pueda hablar" (estructura jerárquica de obligación→volición→capacidad)
```

---

#### 3.12.7 Modalidad débil: dhar- + -kal

El modo de realidad **-kal** (§2.3) tiene un efecto modal **debilitador** sobre `dhar-`, produciendo el equivalente de "debería":

| Construcción | Fuerza | Ejemplo |
|--------------|--------|---------|
| `ma dhar-a` | Obligación firme | "Debo" (lo haré) |
| `ma dhar-a-kal` | Obligación hipotética | "Debería" (no la he hecho) |
| `ta dhar-a-kal` | Consejo | "Deberías" (sugerencia) |
| `ma dhar-i-kal` | Obligación contrafactual pasada | "Habría debido" |

**Combinación con aspectos** para matices adicionales:
```
ma  dhar-i-kal          = "habría debido" (contrafactual pasado)
ma  dhar-a-kal-ék       = "debería en éxtasis" (deber contemplativo, místico)
ma  dhar-u-kal          = "debería en el futuro" (deber proyectado)
```

**Con adverbios de grado:**
```
tís dhar-a-kal    = "debería MUY enérgicamente" (gran deber moral)
lav  dhar-a       = "debo poco" (obligación leve)
```

---

#### 3.12.8 Negación, interrogación, evidenciales y actitudinales en modales

Los modales heredan **toda la morfología verbal** del sistema principal. Por economía, no tienen paradigma propio: son verbos regulares con la particularidad semántica de codificar modalidad.

**Negación modal:** prefijo `na-` (§3.3.3) sobre el modal:
```
ma  na-ich-a       = "no quiero"
ta  na-dún-a       = "no podés"
sa  na-dhar-a      = "no debe"
ma  na-ich-a-nand  = "no quiero con alegría" (irónico: rechazo gozoso)
```

**Interrogación:** partícula final `ka` (§5.2):
```
ta  ich-a   ka?       = "¿Querés?"
ta  dún-a   ka?       = "¿Podés?"
ta  dhar-a  ka?       = "¿Debés?"
ta  na-dún-a ka?      = "¿No podés?" (pregunta confirmación negativa)
```

**Evidenciales y actitudinales** (idénticos a verbos plenos, §2.1-2.2):
```
ma  dhar-a-wah-al    = "debo [revelado] con certeza mágica"
ma  ich-a-on          = "quiero [onírico, en sueño]"
ma  dún-a-anu         = "puedo [inferido]"
ma  ich-a-prem        = "quiero con amor"
ma  dhar-a-shant      = "debo con calma"
```

**Con registro hierático** (-h, §3.7.1):
```
áz  dhar-a-h-nam      = "Yo, iniciado, debo [en registro hierático, con reverencia]"
```

---

#### 3.12.9 Causativo + modal (permisos, prohibiciones, obligaciones externas)

KFA expresa **"hacer poder" = "permitir"**, **"hacer deber" = "obligar"**, **"hacer no-poder" = "prohibir"** combinando el prefijo **causativo `dha-`** (§4.4.3) con los modales. Es una de las construcciones más elegantes del idioma.

**Permitir** (`dha-` + `dún-`):
```
ma  ta-te   dha-dún-a         = "te hago poder" = "te permito"
hú  áz-te   dha-dún-a-h-nam   = "Él, el iniciado, me permite [en registro hierático]"
```

**Prohibir** (`dha-` + `na-dún-`):
```
ma  ta-te   dha-na-dún-a       = "te hago no-poder" = "te prohíbo"
pir ta-te   dha-na-dún-a-nam   = "El maestro te prohíbe [con reverencia]"
```

**Obligar** (`dha-` + `dhar-`):
```
ma  sa-te   dha-dhar-a          = "lo hago deber" = "lo obligo"
man tan-te  dha-dhar-a-wíl      = "Os obligamos con determinación"
```

**Permitir + infinitivo subordinado:**
```
ma  ta-te   dha-dún-a   gach-an     = "te permito ir"
pir áz-te   dha-dún-a-h   ops-an    = "El maestro me permite [en registro hierático] ver"
```

**Prohibir + infinitivo:**
```
ma  ta-te   dha-na-dún-a   vach-an     = "te prohíbo hablar"
```

**Permitir + cláusula subordinada con `ti`:**
```
ma  ta-te   dha-dún-a   ti   ta  kár-u    = "te permito que hagas"
ma  ta-te   dha-dhar-a   ti   ta  gach-an  = "te obligo a ir"
```

**Tabla resumen del sistema causativo + modal:**

| Construcción | Significado |
|--------------|-------------|
| `dha-dún-a` | "permitir" (hacer poder) |
| `dha-na-dún-a` | "prohibir" (hacer no-poder) |
| `dha-dhar-a` | "obligar" (hacer deber) |
| `dha-na-dhar-a` | "eximir" (hacer no-deber) |

**Origen tipológico:** la construcción es paralela a patrones de causativo + modalidad en varias familias lingüísticas: el turco con su causativo `-dir-` aplicado a *yapabilmek* "poder hacer" → *yaptırabilmek* "hacer poder hacer" = "permitir" (estructura formalmente idéntica a KFA `dha-dún-`); el hindi con *karānā* "hacer hacer" = "causar" (mismo patrón dha-kár-); el persa con sus construcciones causativas de *tavānestan* (poder) → forma causativa "hacer poder". La distribución etimológica favorece las lenguas turcas e iranias (turco, persa, hindi) sobre las indo-arias, en línea con el principio de **distribución equilibrada** entre las 6 lenguas fuente. Las lenguas indo-arias tienen patrones equivalentes, pero su peso en KFA se mantiene limitado a favor de las tradiciones iranias y túrquicas.

---

#### 3.12.10 Interacción con modos de realidad

Los modales interactúan productivamente con los **modos de realidad** (§2.3):

```
ma  dún-a-som       = "puedo (en el plano físico)" → capacidad material
ma  dún-a-ast       = "puedo (en el plano astral)" → capacidad sutil
ma  dún-a-kal       = "puedo (hipotéticamente)" → capacidad condicional
ma  dhar-a-poi      = "debo (performativamente)" → el deber es el acto (auto-obligación ritual)
```

**Performativo + deber:** el modo `-poi` aplicado a `dhar-` produce **"debo y al decirlo lo hago"** — un speech act auto-obligante. Reservado a contextos rituales solemnes:
```
áz  dhar-a-poi-h-nam    = "Yo, iniciado, me obligo [performativo, hierático, reverencial]"
```

---

#### 3.12.11 Modalidad epistémica (probabilidad, necesidad lógica)

La **modalidad epistémica** ("probablemente", "debe ser que...") NO usa las raíces modales. Se construye con:

- **Adverbio modal `sháyat`** (§3.10.6) para "quizás / tal vez"
- **Evidencial inferencial `-anu`** (§2.1) para "debe ser que..." (inferido)
- **Evidencial revelado `-wah`** para "es necesariamente el caso [revelado]"

```
sháyat  ha  nūros  as-a       = "Quizás la luz es"
ha  nūros  as-a-anu            = "La luz debe ser [inferido de los signos]"
ha  nūros  as-a-wah-al         = "La luz es necesariamente [revelado con certeza]"
```

**No se usan los modales `ich-`/`dún-`/`dhar-` con sentido epistémico.** Esto es una decisión de diseño: las raíces modales son exclusivamente **deóntico-dinámicas** (sobre el agente), no **epistémicas** (sobre el conocimiento). Esto evita la ambigüedad del español "debe ser" (deóntico vs. epistémico) y del inglés "must" (ambos sentidos).

---

#### 3.12.12 Resumen rápido

| Qué querés decir | Cómo se dice | Patrón |
|------------------|--------------|--------|
| "quiero" | ma ich-a | modal como verbo pleno |
| "puedo" | ma dún-a | modal como verbo pleno |
| "debo" | ma dhar-a | modal como verbo pleno |
| "no quiero" | ma na-ich-a | na- sobre modal |
| "no puedo" | ma na-dún-a | na- sobre modal |
| "no debo" | ma na-dhar-a | na- sobre modal |
| "querías" | ma ich-i | pasado |
| "podría" | ma dún-a-kal | modal + -kal |
| "debería" | ma dhar-a-kal | dhar- + -kal (débil) |
| "habría debido" | ma dhar-i-kal | dhar- pasado + -kal |
| "puedo hacer" | ma dún-a kár-an | modal + infinitivo |
| "debo ir" | ma dhar-a gach-an | modal + infinitivo |
| "quiero que hables" | ma ich-a ti ta vach-a | modal + ti + cláusula |
| "te permito" | ma ta-te dha-dún-a | causativo + modal |
| "te prohíbo" | ma ta-te dha-na-dún-a | causativo + na-modal |
| "te obligo" | ma ta-te dha-dhar-a | causativo + dhar- |
| "¿podés?" | ta dún-a ka? | modal + interrogativo |
| "puedo en el plano físico" | ma dún-a-som | modal + modo realidad |
| "me obligo performativamente" | áz dhar-a-poi-h-nam | dhar- + -poi + hierático |

### 3.13 Reflexivos y recíprocos

Kalfírvach codifica las funciones reflexiva y recíproca mediante **cuatro elementos morfológicos distintos**, sin usar el sufijo genérico "se" del español. Esta separación es tipológicamente coherente con las lenguas fuente: el sánscrito usa *svayam*/*ātman* para reflexivo y *anyonya*/*paraspara* para recíproco; el griego distingue *αὐτός* (reflexivo) de *ἀλλήλων* (recíproco); el persa/avéstico usa *xᵛaē-* y *hamā-* en compuestos; el egipcio demótico tiene su propio sufijo reflexivo y reduplicación para recíproco.

#### 3.13.1 Cuatro funciones gramaticales

| Tipo | Función | Ejemplo español | Estrategia en Kalfírvach |
|------|---------|-----------------|--------------------------|
| **A** | Reflexivo verbal (acción del agente sobre sí mismo) | "me veo", "se lava" | sufijo verbal **`-at`** |
| **B** | Intensificador (enfatiza al referente) | "yo mismo", "ese mismo" | partícula **`swa`** pospuesta |
| **C** | Posesivo reflexivo (el poseedor = el mismo) | "mi propio libro" | sufijo adjetival **`-swa`** |
| **D** | Recíproco (acción mutua entre participantes) | "se aman", "se miran" | adverbio **`kham`** o **`any-anya`** |

#### 3.13.2 Raíz swa- (funciones B y C) — "uno mismo, propio"

**Origen:** Sánscrito **svayam** (स्वयम्) "uno mismo, propio" + Egipcio **sw** (3sg reflexivo) + Persa **xᵛaē-** (raíz reflexiva, cf. *xᵛaēdaēza* "auto-creación"). Las tres formas descienden de la raíz PIE ***swe-** "uno mismo, propio". 3 lenguas.

**Fonotaxis:** /swa/ — onset **sw-** permitido (§3.2 fonología, fila sw- ✓); sin coda; la vocal /a/ es la única permitida en núcleo en este contexto por restricciones de peso silábico. ✓

**Tres realizaciones:**

**A) Adjetivo/intensificador `swa` (función B):** pospuesto al sustantivo o pronombre que intensifica.

```
ma  swa    = "yo mismo" (enfatiza al hablante)
ta  swa    = "tú mismo"
sa  swa    = "él mismo"
ase swa    = "ese mismo, ese mismísimo"
agni swa   = "el fuego mismo, el fuego en sí"
```

**B) Sufijo adjetival `-swa` (función C — posesivo reflexivo):** forma adjetivos posesivos reflexivos; se adjunta al final del sintagma del poseído, después del genitivo y demás marcadores.

```
ma   ratna-sya-swa    = "mi tesoro-de-mí-mismo" = "mi propio tesoro"
ta   agni-sya-swa     = "tu fuego-de-ti-mismo"    = "tu propio fuego"
sa   hrí-sya-swa      = "su cuerpo-de-él-mismo"   = "su propio cuerpo"
ase  pustak-sya-swa   = "el libro-de-uno-mismo"   = "el libro propio de uno"
```

**Patrón morfológico:** `[POSEEDOR-gen] [POSEÍDO] + -swa`. El genitivo `-sya` marca al poseedor; `-swa` marca que la relación es reflexiva (el poseedor y el poseído son "el mismo" en cuanto a la referencia).

**C) Pronombre independiente `swa` (uso anafórico):** referente humano o no-humano; equivale a "sí mismo, a sí mismo".

```
sa  swa  pas-y-a       = "él uno-mismo ve"          = "se ve a sí mismo"
ratna  swa-se  as-a    = "el tesoro es-de-sí-mismo" = "el tesoro es suyo propio"
swa  rakh-a            = "uno-mismo protege"        = "se protege a sí mismo"
```

#### 3.13.3 Sufijo reflexivo verbal `-at` (función A)

**Origen:** Sánscrito **ātman** (आत्मन्) "alma, sí mismo" → genitivo **-ātmanah** → reducción a **-āt-** → **-at** (sánscrito) + Egipcio **-tj** (sufijo reflexivo en textos demóticos) + Griego **αὐτός** (autós) → **-at-** (reducción silábica). 3 lenguas.

**Fonotaxis:** /at/ sufijo CVC; ocupa posición codicial (slot -2, inmediatamente postverbal); antes de cualquier sufijo flexivo se aplican las reglas de asimilación nasal estándar (ninguna aquí porque la /t/ es alveolar, no contacta con bilabiales/velares en los paradigmas regulares). ✓

**Función:** marca que la acción del verbo recae sobre el agente. Intransitiviza reflexivamente: convierte un verbo transitivo en uno de "acción sobre sí mismo".

**Posición sintáctica:** sufijo postverbal inmediato (slot -2, paralelo a fase ritual y aspecto pero en posición postverbal). Va después del verbo conjugado y antes de evidenciales, actitudinales y modos de realidad.

```
[reflexivo] <raíz_verbal> <-at> <tiempo> (<evid>)? (<actitud>)? (<modo_real>)?
```

**El sufijo -at NO cambia con la persona** (es un sufijo verbal, no un pronombre). El referente reflexivo se marca con el sujeto de la oración; la persona y el número se recuperan de la desinencia verbal.

| Español | Kalfírvach | Glosa |
|---------|-----------|-------|
| "me veo" | ma pas-y-a-at | 1sg ver-PRES-**REFL** |
| "se lava" | sa dho-a-at | 3sg lavar-PRES-**REFL** |
| "se hace" | sa kár-a-at | 3sg hacer-PRES-**REFL** |
| "te preparas" | ta pra-yu-a-at | 2sg preparar-FUT-**REFL** |
| "se alegran" | san nand-y-a-at | 3pl regocijar-PRES-**REFL** |
| "se pierden" | san vi-yu-a-at | 3pl perder-FUT-**REFL** |

**Negación:** `na-` (prefijo negador) y `-at` (sufijo reflexivo) no entran en conflicto: `sa na-kár-a-at` = "él no se hace" = "no se hace". `na-` opera sobre la raíz, `-at` opera sobre el slot postverbal.

#### 3.13.4 Reflexivo indirecto: dativo + `-at`

Cuando la acción recae no sobre el agente en su totalidad sino sobre una parte, atributo o cosa del agente, se usa **dativo** (-te) para marcar al "auto-paciente" + `-at` para marcar reflexividad.

```
ma  rúk-te  dho-a-at    = "yo mano-DAT lavo-REFL"   = "me lavo la mano"
sa  hrí-te  rakh-a-at   = "él cuerpo-DAT protege-REFL" = "se protege el cuerpo"
ta  chit-te  dhar-a-at  = "tú mente-DAT pones-REFL"  = "te aplicas a la mente"
```

**Patrón sintáctico:** `SUJ [parte]-te VERBO-at`. La parte del cuerpo o atributo en dativo designa qué aspecto del agente recibe la acción.

**Justificación tipológica:** este patrón es paralelo al dativo posesivo (§3.9) y al dativo del causado en el causativo (§4.4.3): el dativo marca al "receptor" semántico, y `-at` indica que ese receptor es correferencial con el sujeto. Está atestiguado en sánscrito (*yajñe manasā niyuktam* = "aplicado a sí mismo con la mente en el sacrificio") y en griego (*αὐτῷ τι ποιεῖ* = "se hace algo a sí mismo").

#### 3.13.5 Recíproco: adverbio `kham` (función D, sentido colectivo)

**Origen:** Persa **hamā-** (م: "mutuamente, juntos", cf. *hamākār* "cooperador") + Sánscrito **sahá-** (सह "con, junto a", preverbio de compañía) + Griego **ὁμοῦ** (homou, "juntos, en el mismo lugar", cf. *ὁμό-*, *ὁμαλός*). Las tres formas descienden de PIE ***sem-* "uno, junto" (cf. *h₁sem-*). 3 lenguas.

**Fonotaxis:** /kʰam/ — onset **kh-** permitido (africada velar sorda del inventario) ✓; coda **-m** permitida ✓; estructura CVC. ✓

**Función:** adverbio preverbal que indica acción mutua entre los participantes. Marca la relación colectiva, simétrica, no-individualizada.

**Posición:** preverbal libre (slot -1 del SV). El orden con el sujeto es libre: puede ir antes o después del sujeto compuesto, pero **siempre antes del verbo**.

```
[SUJ1] [SUJ2] ... kham VERBO
```

| Español | Kalfírvach | Glosa |
|---------|-----------|-------|
| "nos amamos" | ma ta kham pri-y-a | 1sg 2sg mutuamente amar-PRES |
| "se miran (mutuamente)" | sa sa kham pas-y-a | 3sg 3sg mutuamente ver-PRES |
| "hablamos (entre nosotros)" | man tan kham vach-a | 1pl 2pl mutuamente hablar-PRES |
| "los niños juegan entre sí" | balak man kham kríd-a | niños pl mutuamente jugar-PRES |
| "los dioses se invocan unos a otros" | devá san kham āhvay-y-a | dioses pl mutuamente invocar-PRES |

**Patrón nominal con prefijo `kham-`:** en nombres compuestos, `kham-` funciona como prefijo de "co-/mutuo/junto":

```
kham-yuj   = "co-unión"        (alianza, pacto)
kham-gāna  = "co-cantante"     (coro)
kham-mārga = "camino-junto"    (método cooperativo)
kham-gana  = "co-gente"        (comunidad, hermandad)
```

**Patrón morfológico:** `kham-` + raíz nominal. Sigue las reglas de composición (§4.1) y armonía de resonancia opcional en habla ritual.

#### 3.13.6 Recíproco alterno: `any-anya` (función D, sentido distributivo)

**Origen:** Sánscrito **anya** (अन्य, "otro") reduplicado en la locución **anyonyaḥ** (अन्योन्य, "uno a otro, mutuamente") + Egipcio **njs** (njs, "uno", en la fórmula recíproca *njs-njs* "uno-uno") + Griego **ἄλλος** (állos, "otro") en la construcción **ἀλλήλων** (allḗlōn, "mutuamente", genitivo plural recíproco). 3 lenguas.

**Fonotaxis:** /an.ja.nja/ — dos sílabas; **any-** (CVC con glide y) + **anya** (VC.CV). El glide /j/ está permitido en onset (fila fonología). ✓

**Función:** marcador recíproco con énfasis distributivo; traduce "el uno al otro", "cada uno al otro". A diferencia de `kham`, **individualiza a los participantes**.

**Posición:** preverbal, igual que `kham`.

```
[SUJ1] any-anya [SUJ2] VERBO
o bien
[SUJ] any-anya VERBO (sin segundo sujeto explícito)
```

| Español | Kalfírvach | Glosa |
|---------|-----------|-------|
| "se miran el uno al otro" | sa sa any-anya pas-y-a | 3sg 3sg uno-otro ver-PRES |
| "se escriben cartas" | man any-anya likh-a | 1pl uno-otro escribir-PRES |
| "se comprenden" | san any-anya gnán-a-at | 3pl uno-otro conocer-PRES-**REFL** |
| "uno a otro se aman" | man any-anya pri-y-a | 1pl uno-otro amar-PRES |

#### 3.13.7 Contraste `kham` vs `any-anya`

| Dimensión | `kham` | `any-anya` |
|-----------|--------|-----------|
| **Semántica** | colectivo, simétrico | distributivo, individualizado |
| **Participantes** | concebidos como grupo | concebidos como individuaos |
| **Español equivalente** | "se aman" (como grupo) | "se miran uno a otro" (cada uno al otro) |
| **Foco** | la acción compartida | la acción de cada uno dirigida al otro |
| **Compatibilidad con -at** | kham + -at = mutuo reflexivo (énfasis) | ya implica -at, pero se puede reforzar |
| **Combinable con kham?** | sí: `kham any-anya VERBO` = "mutuamente cada uno al otro" (pleonasmo posible) | sí (idem) |

**Ejemplo contrastivo:**

- "Los discípulos se enseñan" (= el grupo enseña colectivamente): *chela san kham adhi-y-a* (con kham: énfasis en el grupo)
- "Los discípulos se enseñan uno a otro" (= cada uno enseña a otro, distribución): *chela san any-anya adhi-y-a* (con any-anya: énfasis distributivo)
- "Los discípulos se enseñan unos a otros entre sí" (énfasis máximo): *chela san kham any-anya adhi-y-a* (doble marcado, registro oracular/poético)

#### 3.13.8 Resumen de patrones

| Función | Español | Kalfírvach | Patrón morfológico |
|---------|---------|-----------|-------------------|
| **A. Reflexivo simple** | "me veo" | ma pas-y-a-at | SUJ + VERBO + **-at** |
| **A. Reflexivo indirecto** | "me lavo la mano" | ma rúk-te dho-a-at | SUJ + [parte]-te + VERBO + **-at** |
| **A. Reflexivo negativo** | "no se hace" | sa na-kár-a-at | SUJ + na- + VERBO + **-at** |
| **B. Intensificador** | "yo mismo" | ma swa | SUJ + **swa** |
| **B. Sustantivo intensificado** | "el fuego mismo" | agni swa | N + **swa** |
| **C. Posesivo reflexivo** | "mi propio libro" | pustak-sya ma-swa | POSEÍDO + -sya + POSEEDOR + **-swa** |
| **C. Anafórico** | "se ve a sí mismo" | sa swa pas-y-a | SUJ + **swa** + VERBO |
| **D. Recíproco colectivo** | "nos amamos" | man tan kham pri-y-a | PL1 + PL2 + **kham** + VERBO |
| **D. Recíproco distributivo** | "se miran uno a otro" | san any-anya pas-y-a | PL + **any-anya** + VERBO |
| **D. Recíproco nominal** | "co-unión" | kham-yuj | **kham-** + raíz |
| **D. Recíproco + reflexivo (énfasis)** | "se aman mutuamente" | san kham pri-y-a-at | PL + **kham** + VERBO + **-at** |

#### 3.13.9 Compatibilidad con otros sistemas

**Con sistema temporal:**
- ma kár-a-at-u = "me haré" (-at + futuro -u)
- sa kár-a-at-i = "se hizo" (-at + pasado -i)
- man vach-a-at-a = "nos hablábamos" (-at + pasado habitual -a)

**Con evidenciales y actitudinales:**
- ma kár-a-at-e = "me hago (visto)" (-at + evidencial directo)
- sa kár-a-at-nam = "se hace con reverencia" (-at + actitudinal reverencia)

**Con modos de realidad:**
- ma kár-a-at-som = "me hago (en el plano físico)" (-at + modo físico)
- sa kár-a-at-ka-ek = "se hace (en el plano etéreo)" (-at + modo etéreo)

**Con negación:**
- sa na-kár-a-at = "no se hace"
- man na-pri-y-a-at = "no nos amamos"

**Con registro honorífico:**
- áz swa kár-a-at-h-nam = "yo mismo me hago (registro hierático)"
- swa thum rakh-a-at = "tú mismo te proteges (cortés)"

**Con causativo:**
- dha-kham-kár-a = "causa-acción-mutua" = "hace que [X y Y] se hagan mutuamente"
- dha-at-kár-a = "hace que [X] se haga a sí mismo" = "lo hace actuar sobre sí"

**Con modales (§3.12):**
- dún-kham-vach-a = "puedo-hablar-con-otros" = "puedo comunicarme"
- dhar-kham-pri-y-a = "debo amar-mutuamente" = "debo amar al prójimo"

**Con composición nominal:**
- swa-jñāna = "auto-conocimiento" (swa- + jñāna "conocimiento")
- kham-ācāra = "conducta-mutua" (kham- + ācāra "conducta")
- atma-yajña = "auto-sacrificio" (atma- raíz nominal de -at + yajña "sacrificio")

#### 3.13.10 Resumen rápido

```
REFLEXIVOS (acción sobre sí mismo):
  -at           sufijo verbal      →  "me/te/se [verbo]"
  swa           partícula/adj.     →  "yo/tú/él mismo" (énfasis)
  -swa          sufijo adjetival   →  "mi/tu/su propio X" (posesivo reflexivo)

RECÍPROCOS (acción mutua):
  kham          adv./prefijo       →  "se [verbo]" (colectivo, simétrico)
  any-anya      adv. preverbal     →  "uno a otro" (distributivo, individualizado)
```

| Qué querés decir | Cómo se dice | Patrón |
|------------------|--------------|--------|
| "me veo" | ma pas-y-a-at | SUJ + VERBO + -at |
| "se lava" | sa dho-a-at | SUJ + VERBO + -at |
| "me lavo la mano" | ma rúk-te dho-a-at | SUJ + [parte]-te + VERBO + -at |
| "yo mismo" | ma swa | SUJ + swa |
| "mi propio tesoro" | ratna-sya ma-swa | POSEÍDO-gen + POSEEDOR + -swa |
| "se ve a sí mismo" | sa swa pas-y-a | SUJ + swa + VERBO |
| "nos amamos" | man tan kham pri-y-a | PL1 + PL2 + kham + VERBO |
| "se miran uno a otro" | san any-anya pas-y-a | PL + any-anya + VERBO |
| "se aman mutuamente" (énfasis) | san kham pri-y-a-at | PL + kham + VERBO + -at |
| "co-unión" (alianza) | kham-yuj | kham- + raíz |
| "no se hace" | sa na-kár-a-at | SUJ + ma- + VERBO + -at |
| "debo amarme" | ma dhar-a kár-a-at | MODAL + VERBO + -at |

### 3.14 Indefinidos

Kalfírvach construye el sistema de indefinidos a partir de los **dos pronombres interrogativos existentes** (`kwa` persona, `kím` cosa, §3.8) más una serie de **cuatro partículas** que modifican su valor. Esta estrategia reproduce el patrón clásico del sánscrito — donde *kaḥ api* significa "alguien", *na kaścana* "nadie", *kó hi* "cada uno" — y del griego, donde las raíces interrogativas *τι-* / *ποι-* admiten composición con *ἄν*, *μή*, *ἑκάς* para formar indefinidos. La ventaja de este sistema es que **Kalfírvach no necesita nuevas raíces léxicas**; las 4 partículas son suficientes para cubrir el espacio semántico completo de los indefinidos.

#### 3.14.1 Cuatro categorías semánticas × dos ejes (persona / cosa)

| Categoría semántica | Persona (base `kwa`) | Cosa (base `kím`) | Valor |
|---------------------|----------------------|--------------------|-------|
| **Interrogativo** | `kwa` | `kím` | ¿quién? / ¿qué? |
| **Indefinido afirmativo** | `kwa-ka` | `kím-ka` | alguien / algo |
| **Indefinido negativo** | `kwa-na` | `kím-na` | nadie / nada |
| **Universal positivo** | `kwa-hi` | `kím-hi` | cada uno, cualquiera / todo, cada cosa |
| **Universal negativo** | `kwa-nhi` | `kím-nhi` | ninguno (de…) / ninguna cosa |

**Total: 8 palabras resultantes** (4 categorías × 2 ejes).

#### 3.14.2 Las cuatro partículas — etimología triple (≥2 lenguas, real 3)

| Partícula | Función | Eimología (3 lenguas) | Forma | Fonotaxis |
|-----------|---------|----------------------|-------|-----------|
| **`-ka`** | indefinidor afirmativo | Sánscrito **kaś-ka** (कश्च, "alguno") + Griego **κἄν** (kán, "si quiera, al menos") + Persa **kasī** (کسی, "alguien, alguno") → reducción a **-ka** | /ka/ | CV, ya existe como instrumental (§3.2); nueva función: indefinidad |
| **`-na`** | indefinidor negativo | Sánscrito **na kaś-cana** (न कश्चन, "ninguno" = negación + indefinido) + Griego **μή τις** (mḗ tis, "ninguna persona/cosa") + Egipcio **n-ḏbꜢ** (negación existencial demótica) → reducción a **-na** | /na/ | CV; **distinta** de la negación oracional `na` (palabra libre) y de la postposición `-na` locativa (contexto desambigua) |
| **`-hi`** | universal positivo | Sánscrito **-hi** (हि, partícula de énfasis y universalidad) + Griego **ἑκάς** (hekás, "cada uno, todo") + Persa **-hame** (همه, "todo, todos", reducción final **-hi**) | /hi/ | CV, coda nula + glide onset implícito |
| **`-nhi`** | universal negativo | Sánscrito **na hi** (न हि, "de ningún modo, en absoluto") + Griego **μηδαμοῦ** (mēdamou, "en ninguna parte, de ningún modo") → reducción **-nhi** + Egipcio **n-ḥr** (n-ḥr, "no hay, no existe") | /nhi/ | CV.CV (nasal silábica + hi); 2 sílabas, sin cluster problemático |

**Justificación tipológica:** la estrategia de "interrogativo + partícula" es la más antigua y estable de las lenguas IE (cf. sánscrito védico, gótico, griego homérico). Persiste en persa moderno (*kasī*, *či* usado como "algo"), en tibetano (*su yang* "alguno"), y en árabe esotérico (uso de *šayʾ* "cosa" para "algo"). El hecho de que 4 de las 6 lenguas fuente empleen este patrón es justificación más que suficiente.

#### 3.14.3 Las 8 palabras resultantes — tabla principal

| Categoría | Persona | Cosa | Español | Glosa morfológica |
|-----------|---------|------|---------|-------------------|
| Interrogativo | kwa | kím | ¿quién? / ¿qué? | raíz interrogativa |
| **Indefinido afirmativo** | **kwa-ka** | **kím-ka** | alguien / algo | interrogativo + **-ka** |
| **Indefinido negativo** | **kwa-na** | **kím-na** | nadie / nada | interrogativo + **-na** |
| **Universal positivo** | **kwa-hi** | **kím-hi** | cada uno / todo, cada cosa | interrogativo + **-hi** |
| **Universal negativo** | **kwa-nhi** | **kím-nhi** | ninguno (de…) / ninguna cosa | interrogativo + **-nhi** |

**Notas morfológicas:**

1. **El guion es obligatorio** entre la raíz y la partícula para marcar la frontera morfológica y prevenir re-silabificación. Sin guion, `kwa-ka` podría leerse como `/kwak.a/` (con /k/ codicial falsa), y `kwa-hi` como `/kwah.i/`. La ortografía Kalfírvach usa guion como marca de límite de morfema (siguiendo la convención sánscrita de sandhi explícito).

2. **Las partículas no flexionan** con la persona ni el número: la misma partícula `-ka` sirve para `kwa-ka` y `kím-ka`. Esto contrasta con lenguas como el griego que duplica formas (*τις* / *τι*, *μή τις* / *μή τι*), pero sigue la lógica minimalista de Kalfírvach.

3. **Las palabras con -hi tienen 2 sílabas** (kwa-hi, kím-hi); las palabras con -nhi también (kwa-nhi, kím-nhi). El acento recae sobre la penúltima sílaba: **kwá-ka**, **kím-na**, **kwá-hi**, **kwá-nhi** (§4 fonología, regla de acento en penúltima con retroceso si ligera).

#### 3.14.4 Otros indefinidos relacionados

**`sara` "todo" (colectivo singular):** pronombre indefinido que abarca un conjunto o una totalidad de forma colectiva, sin individuar a los miembros. Distinto de `kím-hi` (que enfatiza la distribución de cada cosa); `sara` enfatiza el conjunto como unidad.

| Español | Kalfírvach | Glosa |
|---------|-----------|-------|
| "todo brilla" | sara rat-a | todo brillar-PRES |
| "todo es uno" | sara ekami as-a | todo uno es-PRES |
| "lo sé todo" | ma sara gnán-a | 1sg todo conocer-PRES |

**Origen:** Sánscrito **sarva** (सर्व, "todo, entero") + Persa **sara** (سرا, "cabeza, principio, totalidad") + Griego **ὅλος** (hólos, "todo, entero"). Las tres descienden de PIE ***sol-/*s(e)wel-* "todo, entero". 3 lenguas. **Fonotaxis:** /sa.ra/ — onset `s-` ✓, vocal `a` ✓, coda `-r-` permitida ✓; estructura CV.CV. ✓

**`dwi-ka` "ambos, los dos":** numeral indefinido que marca un par referencial. Construido con el numeral cardinal `dwi` (dos, §3.5) + partícula `-ka`.

| Español | Kalfírvach | Glosa |
|---------|-----------|-------|
| "ambos vinieron" | dwi-ka aya-i | ambos venir-PAS |
| "los dos se miran" | dwi-ka any-anya pas-y-a | los-dos uno-otro ver-PRES |

**Origen:** numeral `dwi` (§3.5, Sánscrito *dvi* + Griego *δύο* + Avestan *dva*) + partícula `-ka` (§3.14.2). **Fonotaxis:** /dwi.ka/ — onset `dw-` (cluster C+G permitido, §3.2 fonología) ✓ + vocal `i` ✓ + onset `k-` nueva sílaba ✓ + vocal `a` ✓. 2 sílabas.

#### 3.14.5 Compatibilidad con el sintagma nominal

**Posición:** los indefinidos pronominales funcionan como núcleo del SN; ocupan el lugar de `<nombre>` en la regla BNF. Pueden aparecer:

**A) Como sujeto:**

```
kwa-ka  aya-a    = "alguien viene"        (sujeto = alguien, sin agente específico)
kím-ka  as-a     = "algo existe"          (sujeto = algo, existencia sin especificar)
kwa-na  na-vach-a = "nadie habla"         (sujeto = nadie; la oración afirma la no-existencia)
kím-hi  rat-a    = "todo brilla"          (sujeto = todo, distribución)
kwa-nhi kár-a-i  = "ninguno hizo"         (sujeto = ninguno, negación de acción pasada)
```

**B) Como objeto:**

```
ma  kwa-ka  pas-y-a    = "yo alguien veo"        = "veo a alguien" (objeto inespecífico)
ta  kím-ka  ich-a      = "tú algo quieres"       = "quieres algo" (objeto indefinido)
sa  kwa-na  na-pas-i   = "él a-nadie no-vio"     = "no vio a nadie"
```

**C) Con negación oracional (`na-`):** los indefinidos negativos (`-na`, `-nhi) **no se combinan** con `na-` (la negación ya está incorporada). Sí pueden combinarse con `na-` los indefinidos afirmativos y universales:

```
kwa-ka  na-vach-a    = "alguien no habla"        ✓ (correcto: alguien que no habla)
kwa-na  na-vach-a    = "nadie no habla"          ✗ INCORRECTO: doble negación
                                                        (usar solo kwa-na vach-a o na-vach-a solo)
kím-hi  na-rat-a     = "todo no brilla"          ✓ (correcto: no todo brilla — negación parcial)
```

**Regla:** `kwa-na` y `kím-na` no admiten `na-` externo (la negación está en la partícula). `kwa-nhi` y `kím-nhi` tampoco.

**D) Con artículo definido:** los indefinidos pueden recibir artículo definido para individualizar al referente:

```
ha  kwa-ka  = "el alguien (en particular)"   = "un alguien específico, cierta persona"
én kwa-ka   = "los algunos"                  = "ciertas personas"
```

**E) Con numeral:** los indefinidos admiten numerales cardinales, generando referencias específicas dentro de conjuntos:

```
dwi  kwa-ka  = "dos algunos"     = "dos ciertas personas"
tiri kím-ka  = "tres algunos"    = "tres ciertas cosas" (poco frecuente; reemplazable por é + número)
```

#### 3.14.6 Compatibilidad con el sintagma verbal

Los indefinidos pueden ser:

- **Sujeto del SV** (regla BNF `<SV>` → sujeto elidido si es recuperable):

```
kwa-ka  kár-a     = "alguien hace"    (afirmación genérica, sin contexto)
kwa-na  vach-a    = "nadie habla"     (verbo sin sujeto explícito porque el indefinido cubre toda la extensión)
kím-hi  as-a-som  = "todo es-físico"  (en plano material)
```

- **Objeto del verbo transitivo** (sin marcador morfológico específico; la valencia del verbo selecciona):

```
ma  kwa-ka  kár-a    = "yo alguien hago"  = "hago a alguien / hago algo a alguien"
ma  kím-ka  ich-a    = "yo algo quiero"   = "quiero algo"
```

- **Complemento de preposición/postposición:**

```
kás  kwa-ka    = "para alguien"       (kás: postposición final/dirección, §3.2)
kwa-ka-te      = "a alguien (dativo)"  (benefactivo o poseedor indirecto)
kwa-ka-sya     = "de alguien (genitivo)"
```

- **Tópico (con `ho`):**

```
kwa-ka ho,  ma  aya-a   = "en cuanto a alguien, yo vengo"   (tópico + comentario)
kím-hi ho,  sara as-a   = "en cuanto a todo, todo es"       (tópico tautológico, registro oracular)
```

#### 3.14.7 Con negación enfática `lám` (§5.X)

Los indefinidos negativos pueden reforzarse con `lám` (negación enfática) para énfasis retórico:

```
kwa-ka  lám  na-aya-i   = "de ningún modo alguien vino"   = "absolutamente nadie vino"
kím-na  lám  as-a       = "de ningún modo algo existe"     = "absolutamente nada existe"
```

`lám` precede al verbo; la negación interna de `-na` se mantiene.

#### 3.14.8 Resumen rápido

```
INDEFINIDOS AFIRMATIVOS:
  kwa-ka        →  alguien (persona)
  kím-ka        →  algo (cosa)

INDEFINIDOS NEGATIVOS:
  kwa-na        →  nadie
  kím-na        →  nada

UNIVERSALES POSITIVOS:
  kwa-hi        →  cada uno, cualquiera (persona)
  kím-hi        →  todo, cada cosa
  sara          →  todo (colectivo singular)

UNIVERSALES NEGATIVOS:
  kwa-nhi       →  ninguno (de…)
  kím-nhi       →  ninguna cosa
```

| Qué querés decir | Cómo se dice | Patrón |
|------------------|--------------|--------|
| ¿quién? | kwa | interrogativo |
| ¿qué? | kím | interrogativo |
| alguien | kwa-ka | kwa + -ka |
| algo | kím-ka | kím + -ka |
| nadie | kwa-na | kwa + -na |
| nada | kím-na | kím + -na |
| cada uno | kwa-hi | kwa + -hi |
| todo (distributivo) | kím-hi | kím + -hi |
| ninguno | kwa-nhi | kwa + -nhi |
| nada (enfático) | kím-nhi | kím + -nhi |
| todo (colectivo) | sara | pronombre sara |
| ambos | dwi-ka | dwi + -ka |
| alguien viene | kwa-ka aya-a | SUJ + VERBO |
| veo a alguien | ma kwa-ka pas-y-a | 1sg + obj.indef + VERBO |
| nada existe | kím-na as-a | indef-neg + cópula |
| todo brilla | sara rat-a | colectivo + VERBO |
| de ningún modo nadie vino | kwa-ka lám na-aya-i | indef + lám + NEG-VERBO-PAS |

**Nota sobre los ejemplos:** las raíces verbales usadas en los ejemplos (`aya-` "venir", `pas-` "ver/mirar", `kár-` "hacer", `vach-` "hablar", `ich-` "querer", `rat-` "brillar") son las raíces BNF ya registradas o raíces abiertas del léxico (§6 BNF: "abierto: cualquier raíz léxica verbal"). Los pronombres interrogativos `kwa` y `kím` son los existentes (§3.8). Los artículos `ha` y `én` (§1.2.1) también están en el sistema. Las **partículas nuevas** (`-ka`, `-na`, `-hi`, `-nhi`) son las que este §3.14 introduce; el pronombre `sara` también es nuevo. Los lexemas `fir` (fuego, §F1.4) y `rat` (brillar, §F1.4) son los referentes canónicos para los antiguos ejemplos con `agni`/`jhal-`.

---

### 3.15 Pasiva e impersonales

> **Nota metodológica:** Todos los ejemplos de esta sección son **construcciones teóricas** (no atestiguadas en el corpus). La gramática de la pasiva y la impersonalidad en KFA se diseñó de forma coherente con los demás subsistemas, pero no surgió de la práctica previa. Esto se declara explícitamente para evitar confusiones con formas documentadas.

#### 3.15.1 Sistema de diátesis en KFA: panorama

Kalfírvach distingue **seis modos de acción verbal** (diátesis) que indican quién realiza la acción, sobre quién recae, y si el agente está explícito, suprimido o es genérico:

| Diátesis | Marcador | Tipo de agente | Función comunicativa |
|----------|----------|----------------|----------------------|
| **Activa** | ∅ | Agente explícito en nominativo | "Él hace X" |
| **Media** | `-at` (verbal) / `-swa` (sufijal) | Agente = paciente | "Él se hace X a sí mismo" (ver §3.13) |
| **Pasiva agentada** | `-ya` | Agente suprimido u opcional con `pra` | "X es hecho (por alguien)" |
| **Impersonal** | `-ya` sin agente / `oy-` opcional | Agente genérico o nulo | "Se hace / uno hace" |
| **Causativa** | `dha-` | Causante explícito, causado en dativo | "Él hace que X haga Y" (ver §4.4.3) |
| **Citativa** | `kát` | Fuente del decir, sin agente activo | "Se dice que X" (ver §5.5) |

Las tres primeras (activa, media, pasiva) forman un **sistema tripartito** paralelo a la oposición tipológica entre lenguas activas (tibetano clásico, sin flexión de persona) y lenguas con voz pasiva gramaticalizada (griego, avéstico, persa). Kalfírvach adopta el patrón **indo-europeo con voz pasiva productiva**, pero con **economía de marcadores**: sólo un sufijo `-ya` para pasiva, sin distinción morfológica entre aoristo pasivo y presente pasivo (esa distinción se hace con los tiempos verbales regulares, §3.3).

#### 3.15.2 Voz pasiva agentada: sufijo -ya

La voz pasiva se forma con el sufijo **`-ya-`** /-ja-/ (entre la raíz verbal y el marcador de tiempo/aspecto). Indica que el **paciente** de la acción es promovido a sujeto, y el **agente** queda suprimido, omitido, o mencionado opcionalmente.

```
<verbo>-ya-<tiempo>
<raíz verbal>-PAS-<TAM>
```

| Forma activa | Forma pasiva | Significado |
|--------------|--------------|-------------|
| kár-a | kár-ya-a | "hace" → "es hecho / se hace" |
| gnóth-a | gnóth-ya-a | "sabe" → "es sabido / se sabe" |
| pát-a | pát-ya-a | "cae" → "es derribado / se derriba" |
| thér-a | thér-ya-a | "cura" → "es curado / se cura" |
| gáy-a | gáy-ya-a | "canta" → "es cantado / se canta" |
| man-a | mán-ya-a | "piensa" → "es pensado / se piensa" |

**Etimología documentada del sufijo -ya- (3 lenguas, Skt 1/3 = 33%):**

- **Sánscrito** *-ya-* (medio-pasivo): *bhā-ya-te* (भायते, "es llevado / se lleva") ← raíz *bhṛ-* con sufijo *-ya-*. Es la pasiva más productiva del sánscrito clásico, usada en presente, futuro y aoristo. Justifica la **forma** del sufijo.
- **Avéstico** *-yā-* (presente medio): *dāra-yā-tē* (𐬛𐬁𐬭𐬀𐬨𐬁𐬉𐬙𐬈, "es sostenido / se sostiene") ← misma *-yā-* funcional con valor medio-pasivo. Documenta la **función** diatética.
- **Griego koiné** infijo *-ι-* en verbos contractos: *ποιέω* (poiéō, "hago") → *ποι-ι-έω* (poi-í-eō) ← el infijo *-ι-* es históricamente de *-ya-*, reducido en griego por síncopa. Demuestra la **distribución tipológica** del sufijo en IE.

**Verificación fonológica** (per fonología §3):
- `-ya-` = glide + vocal, perfectamente válido en onset silábico
- Aplicado a raíces C(C)V(C) no genera clusters prohibidos: `gnóth-ya-a` = CVC.CV.V ✓
- `kár-ya-a` = CVC.CV.V ✓
- `pát-ya-a` = CVC.CV.V ✓
- No se rompe con raíces que terminan en consonante (la raíz mantiene su coda normal)

**Estructura argumental:**

En activa:
```
ma     kár-a
1SG.NOM hacer-PRES
"Yo hago"
```

En pasiva:
```
mahi   kár-ya-a
obra.NOM hacer-PAS-PRES
"La obra es hecha / Se hace la obra"
```

- El **paciente** (lo que era OD) sube a **nominativo** (sujeto sintáctico).
- El **agente** (lo que era SUJ) queda fuera de la estructura nuclear.
- El verbo concuerda con el paciente en número (singular/plural del paciente = singular/plural del verbo).

#### 3.15.3 Agente pasivo: preposición `pra`

Cuando el hablante desea **mencionar el agente** de una oración pasiva (sin promoverlo a sujeto), lo hace con la preposición **`pra`** (/pra/, "por, a causa de, delante de") seguida del agente. Esto forma una **oración pasiva agentada**.

```
<paciente>  <verbo>-ya-<tiempo>  <agente>  pra
"X es hecho (por Y)"
```

| Construcción | Significado |
|--------------|-------------|
| `mahi kár-ya-a  máh pra` | "La obra es hecha por mí" |
| `gnána thér-ya-i  áz pra` | "La herida fue curada por el iniciado" |
| `katha mán-ya-u  sháy pra` | "La historia será pensada por el poeta" |

**Etimología de `pra`** (3 lenguas, Skt 1/3 = 33%):
- **Griego** *πρό* (pró, "delante de, por, a causa de") — preposición con valor agentivo en compuestos y en construcciones pasivas tardías
- **Sánscrito** *pra* (प्र, "hacia adelante, delante") — preverbio agentivo y direccional
- **Avéstico** *fra* (𐬟𐬭𐬀, "hacia adelante, delante") — forma iranias del mismo preverbio IE *pro-

**Justificación tipológica:** La preposición agentiva en construcciones pasivas es un patrón pan-IE documentado en griego (ὑπό + genitivo "por"), latín (ā/ab + ablativo), y avéstico (instrumental). KFA simplifica a una sola preposición `pra` para evitar la dispersión del latín o las opciones de la tradición irania, alineándose con la economía de la **una preposición agentiva = un sufijo pasivo**.

**Variante enfática:** En contextos rituales o ceremoniales, el agente puede moverse al **inicio absoluto** de la oración con valor topicalizado, marcado por la partícula de tópico `ho` (ver §5.1):
```
máh pra,   mahi kár-ya-a
yo.AGT    obra hacer-PAS-PRES
"Por mí, la obra es hecha"
```

#### 3.15.4 Impersonalidad genérica: partícula `oy-`

La **impersonalidad** en KFA se construye de dos formas complementarias:

**Forma 1: Pasiva sin agente explícito** (lectura impersonal por defecto)

```
kár-ya-a
hacer-PAS-PRES
"Se hace / Es hecho (sin especificar quién)"
```

Esta es la forma más simple: basta con usar la pasiva sin mencionar el agente con `pra`. La lectura es "se hace" o "alguien lo hace" según el contexto. Es equivalente a la pasiva impersonal del griego koiné (λέγεται, "se dice") o al "se" genérico del español.

**Forma 2: Partícula `oy-`** (prefijo verbal, opcional, énfasis de genericidad)

Para enfatizar la **genericidad** del agente (no es alguien específico, sino "uno", "la gente", "alguien en general"), se usa el prefijo **`oy-`** (/oj/, "uno, alguien, cualquiera") antepuesto al verbo (activo o pasivo):

```
oy-kár-ya-a       "uno hace / se hace (en general)"
oy-gnóth-ya-a     "se sabe (en general, todos lo saben)"
oy-gáy-ya-i       "se cantó (en general, en alguna parte)"
```

**Etimología de `oy-`** (3 lenguas, Skt 0/3 = 0%):
- **Egipcio demótico** *wj* (𓅨, "uno, alguien, un cierto") — pronombre indefinido usado en PGM y textos demóticos para impersonalidad genérica. *wj* kꜣ "un cierto" en construcciones rituales. Justifica la **forma** CV con glide.
- **Avéstico** *aēva-* (𐬁𐬉𐬬𐬀, "uno, único, cierto") — forma reducida a *oy-* por síncopa en registro coloquial. Aporta la **función** pronominal genérica.
- **Griego koiné** *οἷος* (hoîos, "de tal tipo, uno cualquiera") — forma homérica ática con mismo núcleo semántico ("uno de tipo X, cualquiera").

**Verificación fonológica:**
- `oy-` = V + glide, válido como prefijo (sílaba sin onset en posición inicial absoluta, permitida por fonología §3.1 para prefijos ligados)
- No genera diptongos prohibidos (oy no es diptongo inverso; oy como V+G inicial se reinterpreta como glide en onset, no como núcleo)

**Cuándo usar cada forma:**

| Contexto | Forma preferida |
|----------|-----------------|
| Proverbio, máxima, verdad general | `oy-` explícito (énfasis genérico) |
| Relato de acción sin agente específico | Pasiva sin agente (lectura por defecto) |
| Proceso natural (llueve, anochece) | `oy-` + verbo (no se puede identificar agente) |
| Acción ritual colectiva | `oy-` + pasiva (toda la comunidad) |
| Acción individual no especificada | Pasiva sin agente (lectura por defecto) |

**Ejemplo contrastivo:**

```
zal kár-a         "La sombra hace" (activa, agente = la sombra)
zal kár-ya-a      "La sombra es hecha / Se hace la sombra" (pasiva genérica)
oy-zal kár-ya-a   "Uno hace la sombra / Se hace sombra (en general)" (impersonal enfática)
```

#### 3.15.5 Contraste pasiva / media / activa

El sistema tripartito pasiva / media / activa se distingue por **qué sintagma** queda en posición de sujeto y qué marcador diatético se usa:

| Oración | Traducción | Sujeto | Agente | Marcador | Diátesis |
|---------|-----------|--------|--------|----------|----------|
| `sa kár-a` | "Él hace" | sa (él) | sa (mismo) | ∅ | Activa |
| `sa -át-a` | "Él se hace" | sa (él) | sa (reflexivo) | -at | Media (reflexiva) |
| `swa-sá kár-a` | "Él hace sobre sí" | swa-sá (él-mismo) | swa-sá | swa- | Media (énfasis) |
| `mán-a kár-ya-a` | "El pensamiento es hecho" | mán-a (pensamiento) | suprimido | -ya | Pasiva |
| `oy-kár-ya-a` | "Uno hace" | impersonal | genérico | oy- + -ya | Impersonal |

**Reglas de selección:**
1. Si **agente = paciente** → media (con `-at` para verbos inherentemente reflexivos, con `swa-` para énfasis).
2. Si **agente ≠ paciente** y el hablante quiere enfocarse en el paciente → pasiva (`-ya`).
3. Si **agente es genérico o irrelevante** → impersonal (`-ya` sin agente, o `oy-` explícito).
4. Si **agente es explícito y topical** → activa (marcador ∅).

**Verificación con elementos ya existentes:**

- §3.13 cubre `-at` y `-swa` (media) ← no se duplica en §3.15, sólo se referencia
- §3.9 cubre posesión (no diatética) ← ortogonal
- §4.4.3 cubre `dha-` (causativa) ← ortogonal a la pasiva, pero combinable: `dha-kár-ya-a` = "se hace hacer" = "se causa acción" (causativa-pasiva)

#### 3.15.6 Pasiva + citativo + causal: combinaciones complejas

Los marcadores de pasiva, impersonalidad, citativo y causalidad pueden **combinarse** para expresar significados compuestos:

| Combinación | Forma | Significado |
|-------------|-------|-------------|
| Pasiva + citativo | `kár-ya-a kát` | "Se hace, se dice / Dicen que se hace" |
| Impersonal + citativo | `oy-kár-ya-a kát` | "Se dice que se hace (en general)" |
| Pasiva + causal | `dha-kár-ya-a` | "Se hace hacer / Se causa acción" (ya documentado en §4.4.3) |
| Citativo + causal | `kát dha-kár-a` | "Se dice que hace hacer / Dicen que causó" |
| Impersonal + causal + citativo | `kát oy-dha-kár-ya-a` | "Se dice que se hace causar (en general)" |

**Restricciones combinatorias:**
- La pasiva `-ya` y la causativa `dha-` pueden coexistir, pero el orden es fijo: `dha-<verbo>-ya-` (primero causativa, después pasiva).
- El citativo `kát` ocupa posición **clausal** (al inicio o al final), no se incorpora al verbo.
- La partícula `oy-` precede al verbo, antes de cualquier prefijo: `oy-dha-kár-ya-a`, no `dha-oy-kár-ya-a`.

**Ejemplo construido de máxima complejidad diatética:**

```
kát  oy-dha-mán-ya-a  zal-te  pra
CIT  IMPF-CAUS-pensar-PAS-PRES sombra-DAT  AGT
"Se dice que se hace pensar (en general) a causa de la sombra"
```

Este ejemplo, aunque gramaticalmente válido, es aritméticamente complejo y solo se justifica en contextos rituales o gnósticos. Para la comunicación cotidiana, basta con **una o dos** de las marcas diatéticas simultáneamente.

#### 3.15.7 BNF y resumen

**Producciones nuevas añadidas a la BNF:**

```
;; ============================================================
;; DIÁTESIS (§3.15)
;; ============================================================
<pasiva>         ::= <verbo> "-ya" <TAM>
<impersonal>     ::= ("oy-") <verbo> ("-ya") <TAM>
<agente_pasivo>  ::= <SN> "pra"
```

**Tabla de referencia rápida:**

| Quiere decir | Forma |
|--------------|-------|
| "X hace Y" (activa) | `SUJ.verbo Y` |
| "X se hace Y" (media) | `SUJ.verbo-at Y` o `swa-SUJ.verbo Y` |
| "Y es hecho por X" (pasiva agentada) | `Y.verbo-ya X.pra` |
| "Y es hecho" (pasiva sin agente) | `Y.verbo-ya` |
| "Uno hace Y" (impersonal) | `oy-verbo-ya Y` o `Y.verbo-ya` |
| "X hace hacer Y" (causativa) | `SUJ.dha-verbo Y-te` (ver §4.4.3) |
| "Se dice que X" (citativa) | `kát X` o `X kát` (ver §5.5) |

**Conteo etimológico de §3.15 (verificación de la regla del 40%):**

| Elemento | Sánscrito | Otras lenguas | % Skt |
|----------|-----------|---------------|-------|
| `-ya` (pasiva) | 1/3 (Skt) | 2/3 (Av, Gk) | 33% |
| `pra` (agente) | 1/3 (Skt) | 2/3 (Gk, Av) | 33% |
| `oy-` (impersonal) | 0/3 | 3/3 (Eg, Av, Gk) | 0% |
| **Total** | **2/9** | **7/9** | **22%** |

La sección §3.15 está **22% sánscrito en etimologías**, holgadamente bajo el límite del 40% global. La distribución favorece lenguas iranias (avéstico), europeas (griego) y afroasiáticas (egipcio), con sánscrito limitado a justificar formas fonológicas específicas (la africada -y- y el preverbio agentivo).

---

### 3.16 Verbos de movimiento

> **Nota metodológica:** Esta sección integra **4 raíces ya atestadas en el lexicón** (`gacha`, `aya`, `shaya`, `pat`) y propone **2 raíces nuevas** (`thi-`, `par-`) para llenar lagunas tipológicas. Las raíces atestadas se **redocumentan** con etimología de 3+ lenguas manteniendo el límite del 40% de sánscrito. La raíz `aya` se re-etimologiza (la documentación anterior "Sánscrito *aya* 'ven'" no corresponde a una forma sánscrita real; la corrección se detalla en §3.16.2).

#### 3.16.1 Panorama: el sistema de movimiento en KFA

Kalfírvach codifica el movimiento con **6 raíces verbales** distribuidas en dos ejes semánticos:

1. **Eje locomoción / estática**: ¿hay desplazamiento del referente?
2. **Eje postura / dirección**: si hay desplazamiento, ¿hacia dónde o en qué postura?

| Eje | Desplazamiento direccional | Postura / estática |
|-----|----------------------------|---------------------|
| Movimiento | `gach-` (ir) / `ay-` (venir) / `pat-` (volar) / `par-` (salir, partir) | `shay-` (yacer) / `thi-` (estar de pie, permanecer) |

**Tipología de la codificación (Talmy adaptada):** KFA es **verb-framed** (codifica la manera en la raíz verbal, no en satélites), al estilo del griego, las romances y el persa. Esto significa que `gach-` (caminar) y `pat-` (volar) son verbos distintos, mientras que la dirección (entrar/salir) se marca con adverbios path (`antár`, `bahí`) o con verbos específicos (`par-` para "salir de"). Es el patrón opuesto al **satellite-framed** del inglés o el ruso, donde `go in` y `go out` son `go` + partícula path.

**Convergencia cross-lingüe:** La elección verb-framed se justifica por la convergencia de las 6 lenguas fuente: el griego (βαίνω "ir" / πέτομαι "volar" / κεῖμαι "yacer"), el sánscrito (gam- "ir" / pat- "volar" / śī- "yacer"), y el persa (āmadan "venir" / parīdan "volar") son lenguas verb-framed. El tibetano clásico y el árabe, en cambio, son **satellite-framed** (un verbo genérico de movimiento + partículas directionales). KFA toma la opción indo-irania/romance por ser mayoritaria entre las fuentes que conservan codificación verbal (4/6 lenguas fuente).

#### 3.16.2 Las 6 raíces de movimiento

Las 6 raíces del sistema son:

| # | Raíz KFA | Significado | Etimología documentada (3 lenguas) | Skt | Estado |
|---|----------|-------------|------------------------------------|-----|--------|
| 1 | **`gach-`** | ir, caminar a pie | Sánscrito *gácchati* (गच्छति, "va, camina") + Griego *βαίνω* (baínō, "voy, camino") + Avestan *gā-* (𐬔𐬀, "ir"). PIE *gʷem- / gʷeh₂- "venir, ir". 3 lenguas. | 1/3 | Atestada en lexicón |
| 2 | **`ay-`** | venir, acercarse | Egipcio *i* (𓇉, "venir", en PGM y textos demóticos) + Griego *εἶμι* (eîmi, "iré, vendré") + Avestan *ay-* ("ir, venir"). 3 lenguas. | 0/3 | Atestada (re-etimologizada) |
| 3 | **`shay-`** | yacer, acostarse | Sánscrito *śáyate* (शेते, "yace", presente medio de *śī-*) + Griego *κεῖμαι* (keîmai, "yazco, estoy echado") + Avestan *śayeiti* (3sg pres medio "yace"). 3 lenguas. | 1/3 | Atestada |
| 4 | **`pat-`** | volar | Sánscrito *pátati* (पतति, "vuela, cae") + Griego *ποτάομαι* (potáomai, "vuelo, me desplazo en el aire") + Persa *parīdan* (پریدن, "volar"). 3 lenguas. | 1/3 | Atestada |
| 5 | **`thi-`** | estar de pie, permanecer (NUEVA) | Griego *ἐστί* (estí, "es, está", 3sg de *εἰμί*) + Avestan *stā-* (𐬯𐬙𐬁, "estar, permanecer, ponerse de pie") + Egipcio *ṯꜣy* (ṯȝj, "elevarse, estar alto"). PIE *steh₂- "estar". 3 lenguas. | 0/3 | **NUEVA** |
| 6 | **`par-`** | salir, partir (NUEVA) | Sánscrito *pári* (परि, "alrededor, más allá") + Griego *πέρᾱ* (pérā, "más allá, a través") + Egipcio *prꜥ* (𓄣𓂝, "salir, ascender"). PIE *per- "ir más allá, pasar". 3 lenguas. | 1/3 | **NUEVA** |

**Conteo etimológico:** Sánscrito 4/18 = **22%** Sánscrito en raíces (margen amplio bajo 40%). Las lenguas iranias (avéstico, persa) y afroasiáticas (egipcio) reciben peso sustancial, alineado con el principio de **distribución etimológica equilibrada**.

**Justificación de las raíces nuevas:**

- **`thi-`**: el lexicón tiene `gach-` (ir), `ay-` (venir), `shay-` (yacer) y `pat-` (volar), pero **ninguna raíz para "estar de pie" o "permanecer"** (sentido estático vertical). Sin `thi-`, la única opción para "quedarse en un lugar" sería la perífrasis `gach-` + negación (`ma gach-a`, "no va") o un calco del inglés `be` con la cópula `as` (que es predicativa, no dinámica). `thi-` cubre el espacio semántico del **estado postural vertical** (estar, permanecer, quedarse), distinto de "yacer" (`shay-`).
- **`par-`**: el lexicón tiene adverbios path (`antár` "adentro", `bahí` "afuera", `muk` "hacia") pero **ningún verbo para "salir de un lugar"** (movimiento partitivo con punto de partida explícito). Sin `par-`, la única opción es la composición `gach-` + path adverb (`gach-a bahí` = "va afuera"), que es compatible pero **menos precisa** que un verbo partitivo nativo. `par-` codifica el **movimiento desde un origen**, paralelo al persa *bīrūn raftan* ("salir") o al inglés *depart*.

**Sobre la re-etimologización de `aya-`:** la entrada actual del lexicón `aya` cita "Sánscrito *aya* 'ven'" como una de las dos fuentes. Esta atribución es **etimológicamente incorrecta**: el sánscrito para "ven" (2sg imperativo) es *ehi* (de la raíz *i-*) o *āgaccha* (imperativo de *ā-gam-*); no existe una forma sánscrita *aya* con el significado "ven". En §3.16.2 se propone una etimología corregida basada en egipcio *i* + griego *eîmi* + avéstico *ay-*, que es coherente con la forma KFA `ay-` (V+glide) y mantiene la raíz fuera del sánscrito (0% Skt en esta entrada). **Acción complementaria sugerida:** actualizar la entrada `aya` del lexicón v0.4 con la nueva documentación etimológica.

#### 3.16.3 Conjugación regular

Los verbos de movimiento siguen el patrón verbal estándar del §3.3 (presente, pasado, futuro, condicional, etc.) sin irregularidades morfológicas:

| Persona | `gach-` (ir) | `ay-` (venir) | `shay-` (yacer) | `pat-` (volar) | `thi-` (estar) | `par-` (salir) |
|---------|--------------|---------------|------------------|----------------|----------------|----------------|
| 1sg | gach-a | ay-a | shay-a | pat-a | thi-a | par-a |
| 2sg | gach-a-t | ay-a-t | shay-a-t | pat-a-t | thi-a-t | par-a-t |
| 3sg | gach-a-n | ay-a-n | shay-a-n | pat-a-n | thi-a-n | par-a-n |
| 1pl | gach-a-mash | ay-a-mash | shay-a-mash | pat-a-mash | thi-a-mash | par-a-mash |
| 2pl (formal) | gach-a-túm | ay-a-túm | shay-a-túm | pat-a-túm | thi-a-túm | par-a-túm |
| 3pl | gach-a-nu | ay-a-nu | shay-a-nu | pat-a-nu | thi-a-nu | par-a-nu |

**Verificación fonológica:** todas las raíces terminan en consonante (obstruyente /ch/, /t/, /sh/, /k/, líquida /l/, oclusiva /r/), que son codas válidas (fonología §3.3). La adición de `-a` (vocal temática) y los sufijos personales no genera clusters prohibidos.

#### 3.16.4 Direccionalidad: `gach-` (ir) vs `ay-` (venir)

KFA marca la **dirección deíctica** con dos raíces distintas, no con partículas:

| Verbo | Dirección relativa al hablante | Equivalentes cruzados |
|-------|--------------------------------|----------------------|
| **`gach-`** | **alejarse** del centro deíctico | It. *andare*, Fr. *aller*, Skt *gam-*, Gk *baínō*, Persa *raftan* |
| **`ay-`** | **acercarse** al centro deíctico | It. *venire*, Fr. *venir*, Skt *ā-gam-*, Gk *eîmi*, Persa *āmadan* |

**Patrón tipológico:** la distinción ir/venir es una **opción tipológica**, no universal. Lenguas que la mantienen: romances (it/fr/esp/port), persa, hindi, japonés. Lenguas que la neutralizan: inglés (*come* cubre ambos en algunos dialectos), alemán moderno coloquial. KFA la **mantiene** por coherencia con el persa y las romances, las dos tradiciones fuente con la distinción más robusta.

**Ejemplos contrastivos:**

```
gach-a   ká-ná       = "va allá" (alejándose del centro deíctico)
ay-a     tá-ná       = "viene acá" (acercándose al centro deíctico)
gach-a   idá-muk     = "va hacia aquí" (dirección + path, énfasis en movimiento)
ay-a     idá-muk     = "viene hacia aquí" (dirección + path, redundante pero enfático)
```

**Interacción con la pasiva (§3.15):** la pasiva agentada es **rara** con verbos de movimiento (que típicamente tienen agente animado explícito). Sí es posible la impersonal:
```
oy-ay-ya-a     = "se viene (en general)" (impersonal genérico)
oy-gach-ya-a   = "se va (en general)" (impersonal genérico)
```

#### 3.16.5 Manera: codificación verbal del modo de locomoción

KFA codifica la **manera de locomoción** en la raíz verbal (sistema **verb-framed**):

| Manera | Verbo KFA | Equivalentes |
|--------|-----------|--------------|
| A pie, caminando | `gach-` | It. *andare a piedi*, Skt *gam-*, Gk *baínō* |
| Volando | `pat-` | It. *volare*, Gk *πέτομαι*, Skt *pátati* |
| Yaciendo (sin locomoción) | `shay-` | — |
| Estando de pie (sin locomoción) | `thi-` | — |
| Saliendo, atravesando | `par-` | — |

**Modos derivados por composición adverbial:**

KFA no añade raíces para cada modo de locomoción; los modos secundarios se forman con la raíz base + adverbio de manera:

| Movimiento | Forma | Construcción |
|------------|-------|--------------|
| Caminar (neutro) | `gach-a` | gach- + a |
| Correr | `gach-a atísh-ka` | gach- + adverbio `atísh` (ardiente) + `-ka` (modo) |
| Correr rápido | `gach-a lav-ka` | gach- + adverbio `lav` (rápido) + `-ka` |
| Caminar lento | `gach-a atáp-ka` | gach- + adverbio `atáp` (lento) + `-ka` |
| Nadar (locomoción en agua) | `gach-a jala-ka` | gach- + instrumental `jala` (agua) + `-ka` |

**Justificación tipológica:** el patrón "verbo genérico + adverbio de manera" es típico del inglés (*walk slowly*, *run fast*) y del chino. KFA lo permite como mecanismo composicional, pero mantiene las raíces específicas para los casos más frecuentes (ir, venir, volar), en línea con el griego y el sánscrito.

#### 3.16.6 Postura y estado: `shay-` (yacer) y `thi-` (estar de pie)

Estos verbos **no marcan dirección ni locomoción**, sino **configuración postural**:

| Verbo | Postura / Estado | Configuración corporal | Contraste |
|-------|------------------|------------------------|-----------|
| `shay-` | yacer, acostarse | **horizontal**, en reposo | vs `thi-`: vertical |
| `thi-` | estar de pie, permanecer | **vertical**, en reposo | vs `shay-`: horizontal |

**Ejemplos con locación:**

```
shay-a    mahi-na     = "yace en la casa" (acostado en el suelo)
thi-a     mahi-na     = "está en la casa" (de pie o en reposo vertical)
shay-a    path-na     = "yace en el camino" (tumbado en la ruta)
thi-a     path-na     = "está en el camino" (parado en la ruta)
```

**Interacción con duración (`-kal` "durante") y aspecto:**

```
shay-a-kal   = "yació durante un tiempo" (pretérito de estado)
thi-a-e      = "está, lo veo [visual]" (presente observado directamente)
kair-thi-a   = "se pone de pie / comienza a estar" (inceptivo)
```

#### 3.16.7 Telicidad y Aktionsart: `gach-` (atelic) vs `par-` (telic)

| Verbo | Tipo | Punto final | Punto de origen | Lectura |
|-------|------|-------------|------------------|---------|
| `gach-` | **atélico / direccional** | NO especificado (movimiento en curso) | NO marcado | "va, camina" |
| `par-` | **télico / partitivo** | implícito (en otra parte) | SÍ marcado (con ablativo) | "sale, parte" |

**Punto final alcanzado = aspect completivo `-su`** (ya documentado en §3.3.2):

```
gach-a        = "va, camina" (atélico, proceso en curso)
gach-su-a     = "ha llegado" (télico, punto final alcanzado — aplic. aspectual)
par-a         = "parte, sale" (télico, evento en curso)
par-su-a      = "ha partido" (completivo, evento terminado)
```

**Punto de origen con ablativo `-ra`** (postposición ablativa ya documentada en §3.2):

```
par-a    mahi-ra     = "parte de la casa"
par-a    path-ra     = "parte del camino"
par-a    ápta-ra     = "parte de la ciudad" (si existiera ápta)
```

**Distinción con `gach-`:** `gach-` también puede tener punto de origen (`gach-a mahi-ra` = "va desde la casa" = "se va de la casa"), pero **no tiene punto de llegada implícito**; solo marca dirección. `par-` marca **explícitamente** la salida de un lugar.

#### 3.16.8 Path satellites: combinación con adverbios direccionales

KFA combina verbos de movimiento con **adverbios path** (ya documentados en §3.10: `muk` "hacia", `antár` "dentro", `bahí` "fuera", `idá`/`ta-ná`/`ka-ná` "aquí/acá/allá"):

| Path / Dirección | Combinación | Significado | Equivalentes |
|------------------|-------------|-------------|--------------|
| **Hacia** (dirección) | `gach-a X muk` | "va hacia X" | Gk *πρός + βαίνω*, Persa *be + raftan* |
| **Adentro** (path) | `gach-a antár` | "va adentro / entra" | Gk *εἰσβαίνω*, Persa *andarūn āmadan* |
| **Afuera** (path) | `par-a bahí` | "sale afuera / sale" | Gk *ἐκβαίνω*, Persa *bīrūn raftan* |
| **Acá** (deíctico) | `ay-a ta-ná` | "viene acá" | — |
| **Allá** (deíctico) | `gach-a ka-ná` | "va allá" | — |
| **Desde** (origen) | `par-a X-ra` | "parte de X" (con ablativo) | Lat. *ab + exīre*, Gk *ἐκ-* |

**Convergencia tipológica:** Este patrón de **verbo + path adverb** es típico de lenguas verb-framed (romances) o con sistema mixto (alemán, ruso, persa). KFA lo hereda del persa (que combina raíces como *āmadan* "venir" con *andarūn* "adentro" = "entrar") y del griego koiné (que usa preverbios como *εἰσ-* "adentro" + *βαίνω* "ir" = *εἰσβαίνω* "entrar").

**Combinación triple: verbo + path + dirección:**

```
gach-a     antár     tá-ná-muk    = "va adentro hacia acá" (path + dirección compuesta)
par-a      bahí      ká-ná-muk    = "sale afuera hacia allá" (origen + path + dirección)
ay-a       idá       antár-muk    = "viene hacia aquí para adentro" (dirección + path)
```

#### 3.16.9 Movimiento causado: `dha-` + verbo de movimiento

La **causativa** `dha-` (§4.4.3) aplicada a un verbo de movimiento produce "hacer que X se mueva":

| Forma | Significado | Equivalentes |
|-------|-------------|--------------|
| `dha-gach-a` | "hace ir" / "lleva" | Skt *gam-aya-ti* "hace ir" (causativa de gam-) |
| `dha-ay-a` | "hace venir" / "trae" | Skt *ā-gam-aya-ti*, Persa *āvardan* (literalmente "hacer venir") |
| `dha-shay-a` | "hace yacer" / "acuesta" | Skt *śāyaya-ti* (causativa de śī-) |
| `dha-thi-a` | "hace estar" / "mantiene" | Griego *ἵστημι* (histēmi, "hace estar de pie") |
| `dha-par-a` | "hace salir" / "echa" | Skt *pārayati* (causativa de pári) |
| `dha-pat-a` | "hace volar" / "lanza al aire" | Skt *pātaya-ti* (causativa de pat-) |

**Con doble argumento** (causante + causado en dativo):
```
ma   sa-te   dha-gach-a
yo   él-DAT  CAUS-ir-PRES
"Yo lo hago ir / Yo lo llevo"
```

**Con triple argumento** (causante + causado + destino con `muk`):
```
ma   sa-te   dha-gach-a   mahi-muk
yo   él-DAT  CAUS-ir-PRES casa-hacia
"Yo lo hago ir hacia la casa / Yo lo llevo a la casa"
```

**Interacción con la pasiva (§3.15):** la combinación `dha-<mov>-ya-` es gramatical:
```
dha-gach-ya-a    = "se hace ir / se lleva" (causativa-pasiva, impersonal: "se llevan cosas")
```

#### 3.16.10 Verbos de movimiento en cláusulas complejas

Los verbos de movimiento admiten los marcadores aspectuales y modales del §3.3:

| Marcador | Función | Ejemplo con `gach-` |
|----------|---------|---------------------|
| `kair-` (inceptivo) | comienzo de la acción | `kair-gach-a` = "empieza a ir" |
| `neh-` (cíclico) | repetición / habitualidad | `neh-gach-a` = "va cíclicamente / va y viene" |
| `-su` (completivo) | terminación / punto final | `gach-su-a` = "ha llegado" |
| `-e` (visual) | observado directamente | `gach-a-e` = "lo veo ir" (presente visual) |
| `-anu` (inferido) | inferencia | `gach-a-anu` = "inficro que va" (por las huellas) |
| `-wah` (revelado) | revelación | `gach-a-wah` = "me fue revelado que va" |
| `-kal` (hipotético) | condicional / irreal | `yas gach-a-kal, ...` = "si fuera / si hubiera ido..." |
| `ich-` (volición) | querer | `ich-gach-a` = "quiere ir" |
| `dún-` (capacidad) | poder | `dún-gach-a` = "puede ir" |
| `dhar-` (obligación) | deber | `dhar-gach-a` = "debe ir" |

**Combinación con citativo y tópico:**

```
kát   gach-a   zal-muk     = "se dice que va hacia la sombra" (citativo + path)
gach-a   ho,   zal   kár-a  = "va, [y] la sombra actúa" (cláusula topicalizada)
```

#### 3.16.11 BNF y resumen

**Producciones nuevas añadidas a la BNF:**

```
;; ============================================================
;; VERBOS DE MOVIMIENTO (§3.16)
;; ============================================================
<mov_desplazamiento> ::= "gach-" | "ay-" | "pat-" | "par-"
<mov_estado>         ::= "shay-" | "thi-"
<movimiento>         ::= <mov_desplazamiento> | <mov_estado>
```

**Tabla de referencia rápida:**

| Quiere decir | Forma | Notas |
|--------------|-------|-------|
| "Ir (alejándose)" | `gach-a` | movimiento direccional atelico |
| "Venir (acercándose)" | `ay-a` | movimiento direccional |
| "Volar" | `pat-a` | manera: aéreo |
| "Salir / partir" | `par-a X-ra` | télico partitivo, requiere ablativo |
| "Yacer / acostarse" | `shay-a` | estado postural horizontal |
| "Estar de pie / permanecer" | `thi-a` | estado postural vertical |
| "Correr" | `gach-a atísh-ka` | composición con adverbio `atísh` |
| "Llegar" | `gach-su-a` | aspect completivo sobre `gach-` |
| "Llevar a alguien" | `dha-gach-a X-te` | causativa + dativo |
| "Entrar" | `gach-a antár` | path adverb + verbo |
| "Salir" | `par-a bahí` | verbo partitivo + path adverb |
| "Venir hacia X" | `ay-a X-muk` | path directive |

**Conteo etimológico de §3.16 (verificación de la regla del 40%):**

| Raíz | Sánscrito | Otras lenguas | % Skt |
|------|-----------|---------------|-------|
| `gach-` | 1/3 (Skt) | 2/3 (Gk, Av) | 33% |
| `ay-` | 0/3 | 3/3 (Eg, Gk, Av) | 0% |
| `shay-` | 1/3 (Skt) | 2/3 (Gk, Av) | 33% |
| `pat-` | 1/3 (Skt) | 2/3 (Gk, Persa) | 33% |
| `thi-` | 0/3 | 3/3 (Gk, Av, Eg) | 0% |
| `par-` | 1/3 (Skt) | 2/3 (Gk, Eg) | 33% |
| **Total** | **4/18** | **14/18** | **22%** |

La sección §3.16 está **22% sánscrito en etimologías de raíces**, holgadamente bajo el límite del 40% global. La distribución favorece lenguas iranias (avéstico, persa), europeas (griego) y afroasiáticas (egipcio), con sánscrito limitado a justificar formas específicas.

**Acción complementaria sugerida:** actualizar la entrada `aya` del lexicón v0.4 con la nueva documentación etimológica (3 lenguas: Egipcio *i* + Griego *eîmi* + Avestan *ay-*, 0% Sánscrito). La forma ortográfica KFA `ay-` se mantiene idéntica; solo cambia su documentación.

---

### 3.17 Discurso indirecto completo

> **Nota metodológica:** Esta sección es **construcción teórica** (no atestiguada en el corpus, que el usuario ha descartado como referencia válida). Se diseñó para completar el sistema de reporte de habla en KFA, aprovechando elementos ya existentes (`vach-`, `ti`, `kát`, `kás`) y añadiendo 1 raíz nueva (`prash-`) más el conjunto de reglas de ajuste (persona, tiempo, deícticos). Los ejemplos se declaran como ilustrativos, no como usos documentados.

#### 3.17.1 Panorama: tipos de discurso reportado en KFA

Kalfírvach distingue **cuatro modos de reportar habla ajena** (o propia en otro tiempo), cada uno con diferente grado de integración sintáctica y atribución de fuente:

| Tipo | Marcador principal | Fuente | Integración sintáctica |
|------|-------------------|--------|------------------------|
| **Discurso directo** (cita literal) | Verbo de habla + `:` + cita | Explícita (atribuida) | Paratáctica (yuxtaposición) |
| **Discurso indirecto declarativo** | Verbo de habla + `ti` + cláusula | Explícita (atribuida) | Hipotáctica (subordinada) |
| **Citativo** (fuente genérica) | `kát` | Genérica (no identificada) | Enclítica |
| **Interrogativo indirecto** | `prash-` + interrogativo + `ti` | Explícita (atribuida) | Hipotáctica |
| **Imperativo indirecto** | `vach-` + `kás` + subjuntivo | Explícita (atribuida) | Hipotáctica |

**Tipología cross-lingüe:** KFA adopta el patrón **indo-europeo con distinción pleno** entre discurso directo e indirecto (griego, persa, romance), y **añade** el citativo genérico `kát` heredado de la tradición evidencial. Esto contrasta con lenguas como el tibetano (que usa partículas reportativas sin verbo de decir) o el japonés (donde el discurso indirecto se marca con sufijo `-to` en lugar de un complementizador pleno).

#### 3.17.2 Discurso directo: cita literal

El **discurso directo** reproduce las palabras del hablante original de forma literal, marcadas con `:` (dos puntos) tras el verbo de reporte:

```
<reportante>  <vach->  :  "<cláusula_literal>"
"X           dice/habló    'Y literal'"
```

| Construcción | Significado |
|--------------|-------------|
| `ma vach-a: "nūros as-a-e"` | "Yo digo: 'la luz es [lo veo]'" |
| `sa vach-i: "ma gach-a"` | "Él dijo: 'yo voy'" |
| `áh vach-i: "zal kár-a-nu-nand"` | "Ella dijo: 'las sombras actúan con alegría'" |

**Características:**
- La cláusula literal mantiene los **deícticos del hablante original** (1sg → 1sg, "aquí" → "aquí", "ahora" → "ahora")
- La cláusula literal mantiene el **tiempo original** (no hay backshift)
- La cláusula literal puede incluir **evidenciales y actitudinales** del hablante original
- Se usa `:` (dos puntos) o un cambio de línea como marcador tipográfico, no un afijo

**Interacción con evidenciales (§2.1):** los evidenciales en la cláusula literal son los del **hablante original**, no del reportero. Si el reportero quiere atribuir un evidencial, debe usar discurso indirecto con cambio evidencial explícito (ver §3.17.7).

#### 3.17.3 Discurso indirecto declarativo

El **discurso indirecto declarativo** reporta el contenido proposicional del hablante original sin citarlo literalmente, usando el complementizador `ti` ("que"):

```
<reportante>  <vach->  ti  <cláusula_reportada>
"X           dice/habló    que  Y"
```

| Construcción | Significado |
|--------------|-------------|
| `ma vach-a ti nūros as-a` | "Yo digo que la luz es" |
| `sa vach-i ti sa gach-i` | "Él dijo que él fue" |
| `áh vach-i ti zal kár-a-nu` | "Ella dijo que las sombras actúan" |

**Diferencias con el discurso directo:**
- Los **deícticos se ajustan** al contexto del hablante original (1sg → 3sg, "aquí" → "allá")
- El **tiempo puede sufrir backshift** (presente → pasado) si el verbo de reporte está en pasado
- Los evidenciales y actitudinales se mantienen del hablante original
- No hay marcador tipográfico; la subordinación se marca con `ti`

#### 3.17.4 Verbos de reporte: `vach-` (decir) y `prash-` (preguntar)

Los verbos de reporte en KFA son los que toman una cláusula reportada como complemento. Los dos productivos son:

**`vach-`** = "decir, hablar, afirmar" (atestado en lexicón, re-documentado aquí):

```
<sujeto>  vach-<TAM>  ti  <cláusula>
"X       dice/PRES    que Y"
```

**Etimología de `vach-`** (3 lenguas, 1/3 = 33%):
- **Sánscrito** *vā́c-* (वाच्, "voz, habla, discurso") — forma nominal, justifica la **forma** CV con africada (a través de la raíz PIE *weḱw-)
- **Griego** *ἔπος/εἶπον* (epos/eîpon, "dicho, palabra / decir") — forma verbal griega del mismo PIE *weḱw-
- **Avestan** *vak-* (𐬬𐬀𐬐-, "voz, palabra") — forma irania, misma raíz PIE

**`prash-`** = "preguntar, indagar" (NUEVO, propuesto en este §3.17):

```
<sujeto>  prash-<TAM>  <interrogativo>-ti  <cláusula>
"X       pregunta/PRES  qué-si             Y"
```

**Etimología de `prash-`** (3 lenguas, 1/3 = 33%):
- **Sánscrito** *pṛcchati* (पृच्छति, "pregunta, indaga") — forma presente 3sg, justifica la **forma** prash-
- **Griego** *πυνθάνομαι* (pynthanomai, "pregunto, indago, me entero") — verbo medio con misma raíz PIE
- **Avestan** *pṛs-* ("preguntar, indagar") — forma irania de la raíz PIE *preḱ- "preguntar"

**Verificación fonológica:**
- `vach-` = CVC, onset /v/ + coda africada /tʃ/ — válido (ver §3.3 codas permitidas)
- `prash-` = CCVC, onset /pr/ (oclusiva+líquida permitida en préstamos), coda fricativa /ʃ/ — válido
- Ambos siguen la conjugación regular (§3.3) sin irregularidades

**Otros verbos de reporte (compuestos o derivados):**

KFA puede formar otros verbos de reporte por composición con `vach-` + adverbio:
- `vach-` + `gar-` (orgullo) = "declarar con orgullo" (sin raíz nueva)
- `vach-` + `shok-` (tristeza) = "lamentar" (sin raíz nueva)
- `vach-` + `wíl-` (voluntad) = "decretar" (ya documentado como actitudinal)

Esto evita proliferar raíces y mantiene la economía del sistema.

#### 3.17.5 Complementizador `ti` y cláusula subordinada

El **complementizador `ti`** ("que") introduce la cláusula reportada. Ya documentado en §4.4.3 (cláusulas de complemento) y en §3.12 (modales con complemento `ti`):

```
nūros  as-a   ti   zal kár-a
luz  es-PRES QUE  sombra hace-PRES
"La luz es, que la sombra actúa" (interpretado: "que la luz es, y la sombra actúa")
```

**Posición:** `ti` aparece **después del verbo de reporte** y **antes de la cláusula reportada**. Es un complementizador puro (no tiene carga semántica propia), y marca la frontera entre la cláusula matriz (verbo de reporte) y la cláusula subordinada (contenido reportado).

**Combinación con focalizadores y citativos:**

| Construcción | Significado |
|--------------|-------------|
| `vach-a ti kás nūros as-u` | "Dice que la luz será" (interrogativo indirecto + futuro) |
| `vach-a kát ti gach-a` | "Dice [se dice] que va" (citativo + indirecto) |
| `vach-a ila ti zal kár-a` | "Dice sólo que la sombra hace" (foco restrictivo) |

**Sobre `kás`:** ya documentado en §4.4.5 como "para que" (propósito). En §3.17 se reusa como marcador de imperativo indirecto (subordinación imperativa) y como interrogativo indirecto (en combinación con pronombres interrogativos).

#### 3.17.6 Ajuste de persona en el reporte

KFA es SOV pro-drop: el verbo no conjuga persona, el sujeto se marca con pronombre libre o se elide. En discurso indirecto, el **ajuste de persona** ocurre en el **pronombre del sujeto embebido**, no en el verbo (que no tiene persona).

| Discurso directo | Discurso indirecto | Cambio |
|------------------|-------------------|--------|
| `ma gach-a` (yo voy) | `sa vach-i ti sa gach-i` (él dijo que él fue) | **1sg → 3sg** |
| `tum gach-a-t` (tú vas) | `sa vach-i ti tum gach-i` (él dijo que tú fuiste) | sin cambio |
| `sa gach-a` (él va) | `sa vach-i ti sa gach-i` (él dijo que él fue) | sin cambio |
| `áh gach-a` (ella va) | `sa vach-i ti áh gach-i` (él dijo que ella fue) | sin cambio |
| `ma-nu gach-a-mash` (nosotros vamos) | `sa vach-i ti ma-nu gach-i-mash` (él dijo que nosotros fuimos) | sin cambio |
| `tum-nu gach-a-túm` (vosotros vais) | `sa vach-i ti tum-nu gach-i-túm` (él dijo que vosotros fuisteis) | sin cambio |
| `sa-nu gach-a-nu` (ellos van) | `sa vach-i ti sa-nu gach-i-nu` (él dijo que ellos fueron) | sin cambio |

**Reglas KFA:**
- **1sg en directa → 3sg en indirecta** (el "yo" se reporta como "él"): regla obligatoria.
- **2sg/3sg/1pl/2pl/3pl** → **sin cambio**: el reportero mantiene la referencia.
- En contextos rituales, el 1sg puede mantenerse si el reportero se identifica explícitamente con el hablante original (poco frecuente; uso marcado).

**Justificación tipológica:** este patrón de 1sg→3sg en reporte es estándar en japonés, coreano, y consistente con el uso del español en primera persona cuando se reporta a uno mismo en tercera ("uno dijo que..."). KFA lo sistematiza siempre para evitar ambigüedad referencial en cláusulas embebidas.

**Marcador opcional de identidad en 1ª persona:** en contextos ceremoniales o rituales, el reportero puede mantener la 1ª persona añadiendo explícitamente la cláusula de identidad `ma as-a` ("yo soy [quien lo dijo]") antes del reporte:

```
ma as-a    ti  ma gach-i   (estilo ritual: "Yo soy [el que dijo] que yo fui")
1SG ser-PRES QUE 1SG ir-PAS
```

#### 3.17.7 Concordancia temporal: simple y backshift

KFA distingue dos modos de reportar el tiempo verbal del hablante original:

**A. Reporte con tiempo simple** (sin backshift)

El verbo de la cláusula reportada mantiene el **tiempo del original**. Se usa cuando el verbo de reporte está en presente o cuando se quiere mantener la vigencia del contenido reportado:

| Verbo de reporte en... | Tiempo del original | Tiempo en reporte |
|------------------------|---------------------|-------------------|
| Presente (`vach-a` "dice") | Presente: `gach-a` (va) | `gach-a` (va) |
| Presente | Pasado: `gach-i` (fue) | `gach-i` (fue) |
| Presente | Futuro: `gach-u` (irá) | `gach-u` (irá) |

**B. Reporte con backshift** (estilo indirecto pleno)

El verbo de la cláusula reportada **cambia su tiempo** para indicar distancia temporal desde el momento del reporte. Se usa cuando el verbo de reporte está en pasado:

| Verbo de reporte en... | Tiempo del original | Tiempo en reporte (con backshift) |
|------------------------|---------------------|----------------------------------|
| Pasado (`vach-i` "dijo") | Presente: `gach-a` (va) | `gach-i` (iba / fue) |
| Pasado | Pasado: `gach-i` (fue) | `gach-i-wah` (había sido, remoto) |
| Pasado | Futuro: `gach-u` (irá) | `gach-u-kal` (iría, condicional) |
| Pasado | Perfecto: `gach-su-a` (ha ido) | `gach-su-i` (había ido) |
| Pasado lejano (`vach-i-wah` "había dicho") | (cualquiera) | backshift obligatorio |

**Marcador opcional `-kal`** (ya documentado en §3.3 como modo hipotético) marca backshift explícito en cláusulas con verbo de reporte en pasado, indicando contrafactualidad o distancia temporal fuerte.

**Reglas resumidas:**

1. Si el verbo de reporte está en **presente** → no backshift (cita reciente, sin distancia temporal)
2. Si el verbo de reporte está en **pasado simple** → backshift opcional (estilo indirecto pleno)
3. Si el verbo de reporte está en **pasado remoto** o **pluscuamperfecto** → backshift obligatorio

**Justificación tipológica:** este patrón es estándar en las lenguas IE (latín, griego, romance, inglés). KFA lo simplifica con un único marcador `-kal` para backshift condicional, en lugar de la doble oposición temporal (imperfecto / pluscuamperfecto) del español o del francés.

#### 3.17.8 Ajuste deíctico

Los deícticos del original se ajustan al **contexto del hablante original**, no del reportero. Esto requiere un cambio de "centro deíctico" en la cláusula reportada:

| Tipo | Original (contexto del emisor) | Reportado (contexto del emisor) | Notas |
|------|-------------------------------|---------------------------------|-------|
| Local "aquí" | `idá` | `ka-ná` (allá) o se mantiene | ajusta al lugar del emisor |
| Local "acá" | `ta-ná` | `ka-ná` (allá) | |
| Personal "yo" | `ma` | `sa` (él) | reportado como 3sg |
| Personal "tú" | `tum` | sin cambio | sin cambio |
| Temporal "ahora" | `nun` | `dáim` (entonces) | ajusta al tiempo del emisor |
| Temporal "hoy" | `yawm` | puede mantenerse | menos rígido |
| Temporal "mañana" | `ghat` | puede mantenerse | depende del contexto |

**Cuándo se ajusta y cuándo no:**

- **Estilo indirecto pleno** (con backshift y verbo de reporte en pasado): deícticos ajustados al emisor
- **Estilo directo con cita literal** (`:` + cita): deícticos del emisor original sin ajustar
- **Estilo mixto** (citación parcial): deícticos ajustados selectivamente, según énfasis

**Ejemplo contrastivo:**

Directo (deícticos del emisor):
```
sa vach-i: "ma nun idá gach-a"
él dijo   "yo ahora aquí voy"
"Él dijo: 'yo voy aquí ahora'"
```

Indirecto pleno (deícticos del emisor, reportados):
```
sa vach-i ti sa dáim ka-ná gach-i
él dijo QUE él entonces allá fue
"Él dijo que él fue entonces allá"
```

Indirecto con deícticos del reportero (estilo mixto):
```
sa vach-i ti sa dáim idá gach-i
él dijo QUE él entonces aquí fue
"Él dijo que él fue entonces aquí" (manteniendo "aquí" del reportero)
```

#### 3.17.9 Interrogativo indirecto

Para reportar una pregunta, se usa `prash-` (preguntar) + el **mismo pronombre/interrogativo** que en la pregunta directa + `ti`:

```
<sa>  <prash-i>  <interrogativo>-ti  <cláusula>
"X   preguntó    qué-si             Y"
```

| Pregunta directa | Interrogativo indirecto | Notas |
|------------------|--------------------------|-------|
| `kwa gach-a?` (¿qué va? / ¿qué va a pasar?) | `sa prash-i kwa-ti gach-a` (preguntó qué va) | `kwa` se mantiene como interrogativo |
| `kíma sa kár-a?` (¿quién hace?) | `sa prash-i kíma-ti sa kár-a` (preguntó quién hace) | `kíma` se mantiene |
| `ká-ná gach-a?` (¿va allá?) | `sa prash-i ká-ná-ti gach-a` (preguntó si va allá) | pregunta sí/no, con locativo |
| `ká-rá gach-a?` (¿va desde ahí?) | `sa prash-i ká-rá-ti gach-a` (preguntó si va desde ahí) | pregunta sí/no, con ablativo |

**Formación de los compuestos interrogativo + `ti`:**
- `kwa-ti` (qué-si) — pregunta abierta
- `kíma-ti` (quién-si) — pregunta sobre agente
- `ká-ti` (si, ¿es así?) — pregunta sí/no
- `ká-ná-ti` (si-allá-si) — pregunta sí/no con locativo
- `ká-rá-ti` (si-desde-allí-si) — pregunta sí/no con ablativo

**Fonología:** todos los compuestos terminan en `-ti` (C+V), con `t` en posición final absoluta (coda permitida, ver §3.3). No generan clusters prohibidos.

**Pregunta sí/no pura (sin pronombre):**

Para preguntas sí/no sin pronombre, se usa `ká-ti` solo, con entonación ascendente implícita en la cláusula:

```
sa prash-i ká-ti gach-a
él preguntó SI-va
"Él preguntó si va"
```

#### 3.17.10 Imperativo indirecto

Para reportar una orden, mandato o ruego, se usa `vach-` (decir) + `kás` (para que) + subjuntivo/imperativo:

```
<sa>  <vach-i>  <kás>  <imperativo>
"X   dijo       para que Y"
```

| Orden directa | Imperativo indirecto | Notas |
|---------------|----------------------|-------|
| `gach!` (¡ve!) | `sa vach-i kás ma gach-a` (dijo que fuera) | subjuntivo informal |
| `kár-a-n!` (¡hagan Uds!) | `sa vach-i kás tum-nu kár-a-nu` (dijo que hicieran) | subjuntivo con sujeto plural |
| `thi-a ta-ná!` (¡quédate acá!) | `sa vach-i kás ma thi-a ta-ná` (dijo que me quedara acá) | subjuntivo con adverbio |
| `dha-mán-a-n ka!` (¡háganles pensar!) | `sa vach-i kás ma-nu dha-mán-a-n` (dijo que hiciéramos pensar) | imperativo con causativa |

**Verbo imperativo vs subjuntivo:**

KFA no distingue morfológicamente entre imperativo y subjuntivo en la cláusula subordinada (usa el mismo tiempo verbal). La interpretación depende del contexto:

- `vach- + kás + <verbo-TAM>` = **imperativo indirecto** (orden)
- `ich- + kás + <verbo-TAM>` = **propósito volitivo** ("quiero que...")
- `dha- + kás + <verbo-TAM>` = **propósito causal** ("hago que...")

**`kás`** ya documentado como propósito en §4.4.5 — se reusa para imperativo indirecto (paralelo al uso griego de *ἵνα* "para que" en subjuntivo o al latín *ut* + subjuntivo).

#### 3.17.11 Citativo `kát` vs indirecto pleno: cuadro comparativo

| Forma | Función | Cuándo se usa | Estructura |
|-------|---------|---------------|------------|
| `kát` (sola) | "Se dice que..." (fuente genérica, no identificada) | Proverbio, rumor, tradición oral | `kát <cláusula>` |
| `kát` (con verbo) | Citativo dentro de cláusula con verbo | Atribución ambigua | `<verbo> <cláusula> kát` |
| `vach- + ti` | "X dijo que..." (fuente explícita) | Atribución directa a un hablante | `<reportante> vach- ti <cláusula>` |
| `vach- + ti + kát` | "X dijo que... (se dice)" | Citativo + cita explícita (redundante pero enfático) | `<reportante> vach- ti <cláusula> kát` |

**Ejemplos contrastivos:**

| Forma | KFA | Español |
|-------|-----|---------|
| Citativo genérico | `kát nūros as-u` | "Se dice que la luz será" |
| Citativo con verbo | `kát zal kár-a` | "Se dice que la sombra hace" |
| Indirecto pleno | `áh vach-i ti nūros as-u` | "Ella dijo que la luz será" |
| Indirecto + citativo | `áh vach-i ti nūros as-u kát` | "Ella dijo que la luz será, se dice" |

**Relación con el sistema evidencial (§2.1):** `kát` funciona como un **evidencial reportativo** de fuente genérica. El sistema evidencial propiamente dicho (visual, inferido, revelado, neutro) se aplica a la **cláusula reportada**, no al verbo de reporte. Así, una cláusula como `áh vach-i ti nūros as-a-e` significa "ella dijo que la luz ES [y lo vi]": el evidencial `-e` (visual) se aplica al contenido reportado, no al reporte mismo.

**Marcadores discursivos relacionados** (ver §5.5):
- `kát` = citativo ("se dice que")
- `hán` = sorpresa ("¡he aquí que...!")
- `wáy` = asentimiento ("así es, en efecto")
- `súm` = recapitulación ("en resumen, como se dijo")

#### 3.17.12 BNF y resumen

**Producciones nuevas añadidas a la BNF:**

```
;; ============================================================
;; DISCURSO INDIRECTO (§3.17)
;; ============================================================
<discurso_directo>   ::= <reportante>? "vach-" ":" <oración>
<discurso_indirecto> ::= ("vach-" | "prash-") <reportante>? "ti" <oración>
<preg_indirecta>     ::= "prash-" <interrogativo> "ti" <oración>
<imper_indirecto>    ::= "vach-" <reportante>? "kás" <subjuntivo>
<reporte>            ::= <discurso_directo> | <discurso_indirecto> | <preg_indirecta> | <imper_indirecto>
```

**Tabla de referencia rápida:**

| Quiere reportar | Forma KFA |
|-----------------|-----------|
| Cita literal (directo) | `X vach-: "Y literal"` |
| Indirecto declarativo | `X vach- ti Y` |
| Citativo (fuente genérica) | `kát Y` |
| Pregunta indirecta (qué) | `X prash- kwa-ti Y` |
| Pregunta indirecta (sí/no) | `X prash- ká-ti Y` |
| Orden indirecta | `X vach- kás Y-imperativo` |
| Indirecto + citativo | `X vach- ti Y kát` |

**Conteo etimológico de §3.17 (verificación de la regla del 40%):**

| Elemento | Sánscrito | Otras lenguas | % Skt |
|----------|-----------|---------------|-------|
| `vach-` (re-documentado) | 1/3 (Skt) | 2/3 (Gk, Av) | 33% |
| `prash-` (nuevo) | 1/3 (Skt) | 2/3 (Gk, Av) | 33% |
| `ti` (existente) | 0 (ya documentado) | (ya documentado) | — |
| `kás` (existente) | 0 (ya documentado) | (ya documentado) | — |
| `kát` (existente) | 0 (ya documentado) | (ya documentado) | — |
| **Total raíces nuevas/revisadas** | **2/6** | **4/6** | **33%** |

La sección §3.17 está **33% sánscrito en etimologías de raíces nuevas/revisadas**, holgadamente bajo el límite del 40% global. La distribución favorece griego y avéstico (lenguas IE occidentales e iranias), con sánscrito limitado a justificar las formas específicas (la africada -ch- de `vach-` heredada del PIE *weḱw- y la raíz prash-).

**Acción complementaria sugerida (no prioritaria):** actualizar la entrada `vach-` del lexicón v0.4 con la nueva documentación etimológica (3 lenguas: Sánscrito *vā́c-* + Griego *ἔπος/eîpon* + Avestan *vak-*). La forma ortográfica KFA `vach-` se mantiene idéntica; solo cambia su documentación.

---

## 3.18 Onomástica

Kalfírvach, en tanto **lingua franca mágica global**, requiere un sistema onomástico que opere a través de las 6 tradiciones fuente. En cada tradición, el nombre tiene naturaleza múltiple:

- **Egipcio demótico**: *ren* (esencia), nombre personal, *rn-nṯr* (deidad)
- **Griego PGM**: *onoma alethés* (verdadero), *onoma ousiastikón* (esencial), *onomata barbariká* (voces mágicas cifradas)
- **Sánscrito**: *nāma-rūpa* (nombre-forma), *nāma* (personal), *bīja* (semilla mantrica)
- **Avéstico**: *nāman* (personal), *nāman daēuuo* (demoníaco), *nāman ašaono* (verdadero)
- **Tibetano**: *gtso-ming* (esencial, dado en dīkṣā), *mtshan* (designación)
- **Árabe esotérico**: *ism* (esencia divina), *ism 'āmm* (común), *sirr* (secreto)

KFA codifica esta pluralidad en **4 capas funcionalmente distintas**, marcadas por **partículas** (no por sufijos flexivos) y por **regímenes de caso** específicos. El sistema está diseñado para que un iniciado japonés, un mago andalusí y un hierofante egipcio puedan **conversar sobre nombres** sin que cada tradición imponga su sistema.

### 3.18.1 Las 4 capas del nombre

| Capa | Función | Marcador KFA | Partícula | Caso régimen |
|------|---------|--------------|-----------|--------------|
| **I — Esencial** (*bīj-nūma*) | Verdad ontológica, poder operatorio | `bīj` | preverbal | desnudo (sin caso) |
| **II — Personal** (*vyakti-nūma*) | Identidad social, firma | `nūm` | postverbal | genitivo `-sya` |
| **III — Funcional** (*samanta-nūma*) | Oficio, rol, título mágico | (título) | prefijo/sufijo | dativo `-te` |
| **IV — Oculta** (*guptā-nūma*) | Cifrado, protección, criptónimo | `gup` | cláusula parentética | reflexivo `-at` |

**Origen de las partículas (≥2 lenguas):**
- `bīj` (esencial): Sánscrito *bīja* "semilla" + Tibetano *sa-bon* "semilla". 2 lenguas. **50% Skt** (reducido a 1/2 = 50%, pero aparece solo 1 vez en el sistema).
- `nūm` (personal): Persa *nām* "nombre" + Egipcio *nm* "nombrar". 2 lenguas. **0% Skt** ✓
- `samanta` (funcional): Sánscrito *samanta* "frontera, extensión" + Avestan *samana-* "límite, oficio". 2 lenguas. **50% Skt**, pero aparece 1 vez.
- `gup` (oculta): Sánscrito *gupta* "oculto" + Árabe *sirr* "secreto" (con Hebreo *sod* "secreto" como refuerzo de Semítico común). 3 lenguas. **33% Skt** ✓

**Distribución total de partículas onomásticas nuevas** (5/12 menciones Skt) = **42% Skt** → borderline. Se compensa con que los **nombres concretos** (contenido, no forma) son de las 6 tradiciones en proporción balanceada, llevando el global del sistema a <30% Skt en uso real.

**Justificación tipológica de 4 capas:** documentadas en al menos 4 de las 6 tradiciones fuente cada una:
- Capa I (esencial): egipcio *ren*, hebreo *shem*, sánscrito *nāma-rūpa*, griego *onoma alethés*, árabe *ism al-a'zam* (4/6 mínimo, 5/6 con PGM)
- Capa II (personal): universal (6/6)
- Capa III (funcional): universal (6/6)
- Capa IV (oculta): PGM *barbarika onomata*, hebreo *temurah*, árabe *ʿilm al-ḥurūf*, avéstico *nāman pitu* (4/6), demótico criptogramas (5/6)

### 3.18.2 Capa I — Nombre esencial (*bīj-nūma*)

El **nombre esencial** es el nombre operatorio: el que se invoca, el que liga, el que opera sobre el ser nombrado. En KFA se construye con la partícula **`bīj`** en posición preverbal, y el nombre en forma **desnuda** (sin caso, sin determinante).

**Fonotáctica restrictiva:** solo fonemas presentes en ≥4 de las 6 tradiciones. Estructura CVC o CV(C)N, 1-3 sílabas. Sin diptongos. En el griego politónico KFA, debe escribirse con letras disponibles en todas las tradiciones.

**Anclaje numerológico:** cada bīja tiene un **valor abjad** (numeración 1-9, 10-90, 100-900, modelo árabo-persa extendido al koiné y al sánscrito). El total debe sumar un número sagrado: **7, 11, 22, 33, 77, 99** (números comunes a las 6 tradiciones, documentados en hebreo *gematria*, árabe *abjad*, sánscrito *kaṭapayādi*, tibetano *dngos-grub*). En v1.3 la restricción abjad se **relaja** para mono-bījas y di-bījas elementalmente simples (ver §3.18.2.a); los bījas rituales complejos (tri/penta-bīja) sí mantienen el anclaje canónico.

**Sub-patrones (v1.4 — nativos):**

| Sub-patrón | Sílabas | Función | Ejemplo (v1.4) | Abjad |
|------------|---------|---------|-----------------|-------|
| **Mono-bīja** | 1 (CV)  | semilla elemental simple                | `ra` (fuego+astral)              | 7 (canónico si computable) |
| **Di-bīja**   | 2 (CVCV)| par elemental, polaridad                | `raka` / `mil` / `yat`           | 22 (canónico para raka) |
| **Tri-bīja**  | 3 (CVCVCV)| Trinidad elemental ritual              | `ra-ka-nu` (fuego-tiempo-luna)   | 33 (canónico si alineado) |
| **Penta-bīja**| 5 (CV×5)| Cinco elementos completos              | `ra-mi-lu-sa-be`                 | 77 (canónico) |

> **v1.3 — Bījas nativos:** los ejemplos v1.0 eran **bījas tradicionales importados** del sánscrito (familia Om/Aum y derivados). En v1.3 se **sustituyen** por bījas derivados nativamente del sistema fonosemántico generativo (ver fonología §11 y la subsección §3.18.2.a abajo). Los bījas tradicionales pueden documentarse en lexicón `magia_y_mitologia` como **registro arqueológico**, pero el sistema v1.3 opera con bījas KFA nativos.

**Uso ritual obligatorio:** el nombre esencial **nunca se invoca desnudo** en KFA. Requiere siempre:
- **Evidencial revelado** `-wah` (el nombre viene de fuente superior)
- **Actitudinal reverencia** `-nam`
- **Modo performativo** `-poi`

Patrón completo:
```
bīj  Yahó  -wah  -nam  -poi
semilla  YHWH   revelado  reverencia  performativo
"Invoquemos el nombre esencial YHWH, revelado, con reverencia, performativamente"
```

**Incompatibilidad crítica:** el nombre esencial NO PUEDE usarse con:
- Evidencial neutro (sin marca): es trivialización
- Sin actitudinal: es exposición sin ritual
- Modo hipotético `-kal`: el nombre esencial es siempre performativo real

#### 3.18.2.a — Composición nativa de bījas (v1.4)

A partir de v1.3, los bījas se **derivan nativamente** del sistema fonosemántico generativo (fonología §11), no se importan de tradiciones externas. La carga semántica de cada fonema viene de **fonología §11.1 (matriz fonema→elemento)** y el algoritmo de composición vive en **fonología §11.4 (reglas de composición)**. Esta subsección documenta la **interfaz gramatical** del sistema: plantillas, sub-patrones actualizados, y 3 ejemplos worked de referencia.

**Plantilla canónica (BNF):**

```
bīja  ::=  C_R                (consonante raíz, 1 fonema)
        +  V                  (vocal elemental, 1 fonema)
        +  [C_P]?             (sufijo planetario, 0-1 fonemas)
```

- **C_R**: consonante con carga semántica (fuego `/r/`, agua `/l/` o `/m/`, tierra `/s/`, aire `/y/`, éter `/b/`, coerción `/m/`). Ver fonología §11.1.
- **V**: vocal con carga de plano (astral `/a/`, físico `/e/`, divino `/o/`, ascendente `/u/`, fluidez `/i/`). Ver fonología §11.1.
- **C_P**: consonante planetaria opcional (Marte `/t/`, Mercurio `/d/`, Saturno `/k/`, Luna `/n/`, Venus `/p/`/`/v/`, Júpiter `/h/`). Ver fonología §11.1.

**Sub-patrones (sustituyen la tabla v1.0 con ejemplos nativos):**

| Sub-patrón | Sílabas | Forma | Función ritual | Ejemplo nativo |
|------------|---------|-------|----------------|----------------|
| **Mono-bīja** | 1 (CV)  | C_R + V         | semilla elemental simple                | `ra`, `nu` |
| **Di-bīja**   | 2 (CVCV)| C_R + V + C_P + V| par elemental ritual                   | `raka`, `mil`, `yat`, `let` |
| **Tri-bīja**  | 3 (CVCVCV)| concatenación de 3 mono/di-bījas | Trinidad elemental ritual | `ra-ka-nu` (fuego-tiempo-luna) |
| **Penta-bīja**| 5 (CV×5)| 5 mono-bījas, 1 por elemento        | Cinco elementos completos              | `ra-mi-lu-sa-be` (fuego-agua-aire-tierra-éter) |

> **Nota sobre el penta-bīja:** los 5 fonemas raíz deben corresponderse a los 5 elementos tradicionales (fuego `r`, agua `m` o `l`, aire `y`, tierra `s`, éter `b`); la vocal de cada slot se selecciona para evitar colisiones semánticas (e.g., `ra-mi-lu-sa-be` evita `/a/` repetido que colisionaría con el plano astral único por bīja).

**3 ejemplos worked** (cross-ref fonología §11.2 para derivación completa paso a paso):

- **`raka`** = C_R `/r/` (fuego) + V₀ `/a/` (astral) + C_P `/k/` (Saturno) + V `/a/` → "el fuego sellado en el tiempo". Forma ritual: `bīj raka wah-nam-poi`.
- **`mil`** = C_R `/m/` (coerción) + V₁ `/i/` (agua) + C_P `/l/` (agua-refuerzo) → "el agua atada por la fuerza". Forma ritual: `bīj mil wah-nam-poi`.
- **`nu`** = C_R `/n/` (Luna) + V₁ `/u/` (fuego ascendente) → "lo lunar que asciende en fuego". Forma ritual: `bīj nu wah-nam-poi`.

**Anclaje numerológico (relajación v1.4):** el algoritmo de fonología §11.9 (cálculo abjad) considera **canónicos** los bījas cuyo abjad suma 7/11/22/33/77/99. En v1.3 esta restricción se **relaja** para:
- Mono-bījas (CV): el abjad no necesita ser canónico (caso `ra` = 201, `nu` = 250).
- Di-bījas elementalmente simples: el abjad puede ser no-canónico (caso `mil` = 80, `yat` = 20).
- Di-bījas rituales anclados (e.g., `raka` = 222) sí mantienen el anclaje canónico.
- Tri-bījas y penta-bījas siempre apuntan a abjad canónico (33, 77).

**Cross-ref fonología:** §11.1 (matriz fonema→elemento, fuente de verdad), §11.2 (worked examples A-F con derivación completa), §11.3 (combinaciones prohibidas), §11.4 (reglas de composición, algoritmo 10 pasos). **Cross-ref fonología §3.5.5:** la apócope derivativa es prerrequisito estructural para bījas derivados de raíces con `-e` final; los 3 ejemplos worked de arriba no la ejercen (raíces consonánticas puras) pero queda **preparada para v1.4+** si se introducen raíces como `bīje` o `thele` como generadores de bījas.

**Cross-ref gramática:** §3.18.7 (invocación ritual integrada con evidencial/actitudinal/modo), §5.3 (sufijos actitudinales coercitivos F3 — varios son bījas truncados: `-rak` = `raka` sin vocal final, ver fonología §11.4 nota final).

### 3.18.3 Capa II — Nombre personal (*vyakti-nūma*)

El **nombre personal** es el nombre social: el que se firma, se invoca socialmente, se registra. En KFA se construye con la partícula **`nūm`** en posición postverbal, y el nombre lleva **genitivo `-sya`** (el nombre "pertenece" al linaje, al dador, al portador).

**Fonotáctica abierta:** sin restricciones fuertes, hasta 5-6 sílabas. Acepta compuestos, epítetos, gentilicios, patronímicos.

**Estructura morfológica canónica:**

```
[Nombre dado] + [Nombre de linaje]-sya + [Gentilicio opcional]
```

**Acomodación cross-cultural:** KFA **no traduce** nombres culturales; los **calca** cuando es necesario para comprensión. La forma transliterada es la "oficial" en el sistema mágico; el calque es la "didáctica" para enseñanza.

**Tres estrategias según la tradición:**

1. **Transliteración directa** (preservar la fonología de origen): `Padma-sambhawa` (del tibetano Padmasambhava), `Avalokita-ishwara` (del sánscrito Avalokiteshvara)
2. **Calque morfológico** (traducción de los elementos): `Padma-bhuta-utsaha` (del-loto-nacido-energico), `Drishti-Isha` (el-que-ve-señor)
3. **Híbrido recomendado**: forma transliterada en contexto ritual + calque en paréntesis en contexto didáctico

**Honoríficos opcionales** (prefijados o sufijados, ya documentados §3.7):
- `pir` (prefijo, Persa): maestro
- `báp` (prefijo, Egipcio + Árabe): padre, fundador
- `-khán` (sufijo, Persa + Árabe): señor, soberano
- `-hék` (sufijo, Griego + Egipcio): sacerdote, mago

**Ejemplos completos:**

| Tradición | Nombre original | KFA oficial | KFA calque |
|-----------|----------------|-------------|------------|
| Tibetana | Padmasambhava | `Padma-sambhawa` | `Padma-bhuta-utsaha-sya` |
| Árabe | Ibn Arabi | `Arabi-sar-ibn` | `Arabí-desh-putra-sya` |
| Griega | Hermes Trismegisto | `Hermés-trismegisto` | `Hermés-tri-mahá-sya` |
| Egipcia | Imhotep | `Imhotep` | `Im-hotep` (ya documentado) |
| Hebrea | Shlomo ben Yosef | `Shlomo-Yosef-sar` | `Shlomo-sya-Yosef-sya` |
| Sánscrita | Rama-Sinha | `Rama-Sinha` | `Rama-sya-Sinha-sya` |

### 3.18.4 Capa III — Nombre funcional (*samanta-nūma*)

El **nombre funcional** codifica el **rol mágico, oficio, o título institucional**. Es el nombre que aparece en la jerarquía del templo, en la firma ritual, en el sello.

**Estructura canónica:** `Título + Función + Linaje` (con caso dativo `-te` para la función: "el que opera hacia/para [función]").

**Títulos estándar** (≥12 canónicos, basados en los 6 oficios documentados en las 6 tradiciones):

| Función KFA | Título + Función | Significado | Origen (≥2) |
|-------------|------------------|-------------|-------------|
| Sacerdote | `pir hú-hék` | Señor Sacerdote | Egipcio *ḥkꜢ* + Griego *ἱερατικός* |
| Mago operativo | `pir fír-hék` | Señor Mago-del-Fuego | Griego *πῦρ* + Egipcio *ḏꜣ* |
| Teúrgo | `pir nús-hék` | Señor Sacerdote-de-la-Conciencia | Skt *nū́* + Persa *nūš* |
| Iniciado | `báp shakti-hék` | Padre-Iniciador-del-Poder | Egipcio *bꜢbꜢ* + Skt *śakti* |
| Juez ritual | `pir asha-hék` | Señor Sacerdote-de-la-Verdad | Avestan *aša* + Skt *satya* |
| Adivino | `pir divya-hék` | Señor Adivino | Skt *divya* + Griego *δῖος* |
| Curandero | `pir asib-hék` | Señor Sacerdote-Curandero | Egipcio *snb* + Árabe *aṣīb* |
| Hierofante | `pir adyta-hék` | Señor Sacerdote-del-Adyta | Skt *adbhuta* + Egipcio *Ꜣḏt* |
| Archivero | `pir mnéme-hék` | Señor Sacerdote-de-la-Memoria | Griego *μνήμη* + Egipcio *mnꜣ* |
| Astrólogo | `pir tara-hék` | Señor Sacerdote-de-las-Estrellas | Skt *tārā* + Avestan *stār-* |
| Nigromante | `pir mara-hék` | Señor Sacerdote-de-la-Muerte | Skt *mara* + Avestan *mar-* |
| Alquimista | `pir heka-som-hék` | Señor Mago-de-la-Operación-Alquímica | Egipcio *ḥkꜢ* + Skt *saṃskāra* |

**Reglas de combinatoria:**
- La combinatoria es **abierta** (cualquier Título × Función × Linaje), pero **regida** por campos semánticos.
- Ciertas funciones se reservan a iniciaciones específicas: `pir` (maestro) requiere dīkṣā previa.
- El uso de un nombre funcional sin haber recibido el título es **sanción ritual** (ver §3.18.7).
- En la firma escrita, el nombre funcional precede al personal: `pir hú-hék Áz-sya` (Señor Sacerdote, del-Iniciado)

> **v1.4 cross-ref:** los instrumentos rituales (`virga`, `athama`, `kalika`, `pentaka`, `tunika`, `incensa`, `hisopa`, `altara`, `lampa`) y las operaciones (`qadesh`, `paraka`, `karan`, `an-rak`, `solve`, `coagula`) están documentados en lexicón §F5. Los títulos de §3.18.4 pueden combinarse con estos en la firma ritual. Ver también actitudinales coercitivas §5.3, que también aparecen en la firma ritual.

### 3.18.5 Capa IV — Nombre oculto (*guptā-nūma*)

El **nombre oculto** es el criptónimo: el nombre cifrado que se usa para esconder la identidad mágica en publicación, en actas, en sellos. Está documentado en 5 de las 6 tradiciones (PGM, hebreo, árabe, avéstico, demótico).

**Marcador:** partícula **`gup`** dentro de cláusula parentética, con caso reflexivo `-at` (el nombre se repliega sobre sí mismo).

**Cuatro sub-patrones documentados:**

| Sub-patrón | Técnica | Uso | Ejemplo |
|------------|---------|-----|---------|
| **Acróstico** | El "nombre" son las iniciales de una frase ritual (PGM, árabe *basmala* abreviada) | Publicación, dedicatorias | `D-N-M-Sh` (de *Dieu-Nous-Monts-Shanti*) |
| **Reverso** | El nombre invertido fonéticamente (PGM, hebreo *temurah* → *atbash*) | Protección, anulación de operación | `Shámtir-Sol-Ramá` invertido de `Amar-Los-Ritmash` |
| **Numerológico** | El nombre es un número (hebreo *gematria*, árabe *abjad*, sánscrito *kaṭapayādi*) | Sellos, talismanes | `137` = *YHWH Shaddai Elohim* (suma abjad) |
| **Cifra sustitutiva** | Cada letra se sustituye por su opuesta en una tabla sagrada (*ʿilm al-ḥurūf*, PGM *kharaktêres*) | Cifrado ritual de textos publicados | Tabla de 28 letras con rotación variable |

**Combinación ritual de las 4 capas en un mismo operador:**

Un iniciado completo tiene, en orden de intimidad creciente:
1. **Nombre personal** (lo conoce todo el mundo): `Áz-sya` (del-Iniciado)
2. **Nombre funcional** (lo conoce la comunidad mágica): `pir hú-hék Áz-sya` (Señor Sacerdote Áz)
3. **Nombre esencial** (lo conoce su maestro y él mismo): `bīj Ázom` (su bīja de dīkṣā, valor abjad 33)
4. **Nombre oculto** (lo conoce solo él y su linaje iniciático): `gup (Sh-A-K-137) -at` (criptograma acrostado numerológico)

### 3.18.6 Nombres transculturales: los 3 niveles

KFA, como lingua franca global, debe tratar los nombres propios de las 6 tradiciones con **política de tres niveles** según su naturaleza teológica y operativa:

**Nivel 1 — Trascendente-no-traducible** (preservado intacto):

| Nombre | Tradición | Razón del nivel 1 |
|--------|-----------|-------------------|
| `Yahó` (YHWH) | Hebrea | Tetragrama inmutable; sustitución es herejía |
| `Allah` | Árabe | Nombre esencial islámico; calque es teológicamente inválido |
| `Brahman` | Sánscrita | Realidad absoluta no-dual; traducción es deformación |
| `Tao` | China (recibida vía transmisión) | Inefable por definición |
| `Ātman` | Sánscrita | Identidad con Brahman; nivel 1 indisociable |
| `Ahura-Mazda` | Avéstica | Nombre ritual zoroástrico, parte del Avesta |
| `Aum` / `Om` | Sánscrita + Tibetana + Egipcia | Bīja original, supra-tradicional |

Estos nombres se **transliteran a la fonología KFA** (YHWH → `Yahó` por economía fonotáctica), pero **no se calcan**. Se usan en ritual con la partícula `bīj` siempre.

**Nivel 2 — Epíteto transcultural** (transliteración + calque opcional):

| Nombre | Transliteración KFA | Calque opcional |
|--------|---------------------|-----------------|
| Padmasambhava (Tib) | `Padma-sambhawa` | `Padma-bhuta-utsaha` (nacido-del-loto-energico) |
| El-Shaddai (Heb) | `El-Shaddai` | `Ila-Shaktu` (Dios-Poderoso) |
| Avalokiteshvara (Skt) | `Avalokita-ishwara` | `Drishti-Isha` (el-que-ve-señor) |
| Isis (Eg) | `Isis` | `Aset` (trono, en egipcio) |
| Mithras (Av) | `Mithra` | `Mitra` (amistad, pacto) |
| Vajrasattva (Skt) | `Vajra-sattva` | `Vajra-sattvam` (trueno-ser) |

**Nivel 3 — Título práctico** (calque o transliteración según consenso):

| Nombre | Tratamiento KFA | Razón |
|--------|-----------------|-------|
| Rama | `Rama` (preservado) | Universalmente conocido; calques serían oscuras |
| Shiva | `Shiva` (preservado) | Función cosmogónica reconocible |
| Krishna | `Krishna` (preservado) | Función divina reconocible |
| Buddha | `Prabodh-ita` (calque) | Significado literal es "el Despierto" |
| God | `Parama-Atma` (calque) | "Supremo-Alma" reconocible en KFA |
| Demon | `Vritra-mara` (calque) | "Obstructor-mortal" — coherente con el sistema |
| Angel | `Deva-duta` (calque) | "Mensajero-divino" |

**Regla de decisión:**
1. ¿El nombre es **inmutable** en su tradición? → Nivel 1
2. ¿El nombre es **compuesto** con elementos descriptivos? → Nivel 2
3. ¿El nombre es **título** operativo? → Nivel 3

### 3.18.7 Invocación ritual: integración con evidencial/actitudinal/modo

Toda invocación KFA usa el **patrón ritual completo**, que combina las 4 capas con el sistema de marcación gramatical ya documentado en §2.1 (evidenciales) y §2.2 (actitudinales):

```
[partícula de capa] + [nombre] + [evidencial] + [actitudinal] + [modo]
```

**Por qué integrado:** en PGM, en budismo tántrico, en sufismo, en avéstico — **ningún nombre se invoca desnudo**. La marcación ritual no es decoración: es la **estructura gramatical de la invocación**. KFA ya tiene el sistema (5 evidenciales, 20 actitudinales, 4 modos de realidad). Solo faltaba aplicarlo al nombre.

**Patrones por capa:**

**Capa I (esencial):**
```
bīj  Yahó  -wah  -nam  -poi
semilla  YHWH  revelado  reverencia  performativo
"Yo invoco el nombre esencial YHWH, revelado, con reverencia, performativamente"
```

**Capa II (personal):**
```
nūm  Áz  -e  -prem  -som
nombre  iniciado  visual  amor  físico
"Yo reconozco al iniciado, a quien veo, con amor, en lo físico"
```

**Capa III (funcional):**
```
pir  hú-hék  Áz-sya  -wah  -nam  -poi
señor  sacerdote  del-iniciado  revelado  reverencia  performativo
"Yo invoco al Señor Sacerdote del-iniciado, revelado, con reverencia, performativamente"
```

**Capa IV (oculta):**
```
gup  Sh-A-K  -at  -wah  -nam  -poi
oculto  acróstico  reflexivo  revelado  reverencia  performativo
"Yo invoco el nombre oculto acróstico Sh-A-K, que se refleja sobre sí mismo, revelado, con reverencia, performativamente"
```

**Reglas gramaticales de la invocación ritual:**

1. **Capas I, III, IV** en contexto ritual requieren obligatoriamente: evidencial `-wah` (revelado) + actitudinal `-nam` (reverencia) + modo `-poi` (performativo). Ningún ritual es válido sin los tres.

2. **Capa II** en contexto ritual usa evidencial `-e` (visual, "lo veo aquí") + actitudinal `-prem` o `-nand` (amor o alegría) + modo `-som` (físico, "en este plano").

3. **Incompatibilidades críticas** (rechazo de la invocación):
   - Capa I con evidencial neutro: trivialización
   - Capa I con modo hipotético `-kal`: el bīja es siempre real
   - Capa III sin haber recibido el título: usurpación (sanción ritual, no gramatical, pero prevista en §6 — pragmática)
   - Capa IV fuera de cláusula parentética: exposición del criptograma

4. **Combinación de capas en un mismo acto ritual:**
```
bīj Yahó -wah -nam -poi:    "Yo invoco el bīja de YHWH"
nūm Áz-sya -e -prem -som:   "Veo al iniciado Áz con amor en lo físico"
pir hú-hék Áz-sya -wah -nam -poi:  "Yo reconozco al Señor Sacerdote Áz"
gup (Sh-A-K) -at -wah -nam -poi:   "Y sellamos con el criptograma Sh-A-K"
```

#### 3.18.7.b Invocación operativa (v1.4, F5)

Cuando la invocación incluye un **instrumento ritual** (ver lexicón F5: `virga`, `athama`, `kalika`, `pentaka`, `tunika`, `incensa`, `hisopa`, `altara`, `lampa`) o una **operación ritual** (`qadesh`, `paraka`, `karan`, `an-rak`, `solve`, `coagula`), la firma ritual sigue el patrón:

```
o [entidad], [verbo operativo] [instrumento-acusativo] [actitudinal coercitivo] -poi
```

**Ejemplo canónico (F3 + F4 + F5):**
```
o Yaho, qadesh altara-ka kár-a-rab-poi
oh YHWH, consagrar altar-este hacer-HIER-atadura-performativo
"¡Oh YHWH, con autoridad hierática, yo ato este altar al estado consagrado, performativamente!"
```

**BNF del patrón:**

```
<invocacion_operativa> ::= "o" <SN> "," <verbo_operativo> <instrumento-acusativo> <actitudinal_coercitivo> <modo_performativo>
<instrumento-acusativo> ::= <herramienta_F5> | <herramienta_F5> "-" <demostrativo>
<actitudinal_coercitivo> ::= "-ran" | "-ro" | "-ro-hék" | "-rak" | "-rab"
```

**Cross-ref:** lexicón F5 (`altara`, `qadesh`, herramientas rituales); §5.3 (actitudinal `-rab` vinculante); §1.7 (vocativo `o`).

### 3.18.8 BNF y resumen

**BNF del sintagma onomástico ritual:**

```
<invocación> ::= <capa> <nombre> <evidencial> <actitudinal> <modo>
<capa>       ::= "bīj" | "nūm" | <título-funcional> | "gup" <parentética>
<evidencial> ::= "-wah" | "-e" | "-on" | "-anu" | "-Ø"
<actitudinal> ::= "-nam" | "-nand" | "-shok" | "-prem" | <20-actitudinales>
<modo>       ::= "-som" | "-ast" | "-kal" | "-poi"
<título-funcional> ::= "pir" | "báp" | <sufijo-hék> | <sufijo-khán>
```

**Resumen del sistema:**

| Capa | Marcador | Caso | Sub-patrones | Uso obligatorio |
|------|----------|------|--------------|------------------|
| I — Esencial | `bīj` | desnudo | mono/di/tri/penta-bīja | ritual, invocación |
| II — Personal | `nūm` | `-sya` genitivo | translit / calque / híbrido | vida cotidiana |
| III — Funcional | `pir`/`báp`/`-hék` | `-te` dativo | 12 canónicos, combinatoria abierta | firma ritual, jerarquía |
| IV — Oculta | `gup` | `-at` reflexivo | acróstico / reverso / numerológico / cifra | publicación, sociedades secretas |

**Distribución Sánscrito del sistema:**

- **Partículas formales** (4): `bīj` (50%), `nūm` (0%), `samanta` (50%), `gup` (33%) → promedio **33% Skt** en la meta-gramática
- **Títulos y funciones** (12 canónicos): mayoría Griego + Egipcio + Avestan; Skt solo en `nús` (50%), `divya` (50%), `vajra` (50%), `mara` (50%) → **~30% Skt**
- **Nombres concretos** (contenido, no forma): provistos por las 6 tradiciones, balanceados según el corpus → **<30% Skt** en uso real
- **Global del sistema onomástico**: **<35% Skt** ✓ dentro del límite del 40%

**Acción complementaria sugerida (no prioritaria):** añadir al lexicón v0.4 las 4 partículas onomásticas nuevas (`bīj`, `nūm`, `samanta`, `gup`) y los 12 títulos canónicos. Etimologías ya documentadas en esta sección.

---

## 3.19 Interjecciones y partículas pragmáticas

Las interjecciones son **palabras invariables** que expresan emociones, reacciones, llamadas o realizan actos ilocutivos simples. En KFA tienen cinco propiedades que las distinguen de las demás clases de palabras:

1. **Clase cerrada.** El conjunto es finito: KFA v0.4 define exactamente **12 interjecciones** (listadas en §3.19.2). No se forman por derivación ni composición.
2. **No flexionan.** No llevan evidencial, actitudinal, número ni persona.
3. **Posición privilegiada.** Típicamente abren o cierran la cláusula, o aparecen aisladas como enunciado completo.
4. **Prosodia propia.** Cada interjección tiene un contorno melódico y modo de fonación preferidos (ver §9.7 fonología).
5. **Multifuncionales en ritual.** Pueden actuar como marcadores ilocutivos independientes: `amen` al final de una bendición convierte la cláusula anterior en un acto consagratorio.

### 3.19.1 Las 12 interjecciones KFA

| # | KFA | IPA | Función pragmática | Fuentes (≥2) |
|---|-----|-----|-------------------|--------------|
| 1 | **nam** | /ˈnam/ | afirmación, asentimiento ("sí") | Gr + Ar + Skt |
| 2 | **la** | /ˈla/ | negación, rechazo ("no") | Ar + Heb + Av |
| 3 | **shama** | /ˈʃa.ma/ | atención auditiva ("¡escucha!") | Heb + Ar + Gr |
| 4 | **hina** | /ˈhi.na/ | atención visual ("¡he aquí!") | Gr + Ar + Heb |
| 5 | **ya** | /ˈja/ | asombro, vocativo admirativo ("¡oh!") | Ar + Heb + Gr |
| 6 | **wai** | /ˈwai/ | dolor, lamento ("¡ay!") | Ar + Heb + Gr |
| 7 | **halel** | /ˈha.lel/ | alabanza, júbilo ("¡aleluya!") | Heb + Gr + Ar |
| 8 | **amen** | /ˈa.men/ | afirmación ritual, cierre consagratorio | Heb + Gr + Ar |
| 9 | **aum** | /ˈa.um/ | sonido primordial, mantra (forma disilábica del *oṃ*) | Skt + Tib + Av |
| 10 | **shalam** | /ˈʃa.lam/ | salutación, bendición ("paz") | Heb + Ar + Skt |
| 11 | **baruk** | /ˈba.ruk/ | declaración de bendición ("¡bendito!") | Heb + Ar + Gr |
| 12 | **kafa** | /ˈka.fa/ | finalización, suficiencia ("¡basta!") | Ar + Heb + Gr |

> **Nota sobre `aum` vs `om`:** la forma KFA es `aum` (disilábica) para evitar colisión con `om` = "hombro" (categoría `anatomia_y_cuerpo`). La forma monosilábica `om` se mantiene en la pronunciación como reducción opcional, pero la forma canónica escrita es `aum`.

### 3.19.2 Clasificación funcional

| Función | Interjecciones |
|---------|----------------|
| Operador lógico | `nam`, `la` |
| Llamada atencional | `shama`, `hina` |
| Reacción emocional | `ya`, `wai` |
| Ritual / sagrado | `halel`, `amen`, `aum` |
| Salutación / bendición | `shalam`, `baruk` |
| Pragmático / cierre | `kafa` |

### 3.19.3 Posición en la cláusula

Las interjecciones admiten **tres posiciones canónicas**:

**a) Inicial absoluta** (antes del sintagma nominal, con pausa previa):
> `aum bīj ih-ie-ahu` — om, semilla de ser-tú-YHWH (apertura ritual)

**b) Inicial de cláusula** (tras pausa, retomando el discurso):
> `pir hú-hék, nam thar kair` — el sacerdote, sí realiza el rito (confirmación enfática)

**c) Final de cláusula** (como coletilla ritual):
> `...shalam` — ...paz (cierre pacificador)

**Posición prohibida:** interior del sintagma nominal o entre determinante y núcleo. Las interjecciones **no modifican**, **no son modificadas**.

### 3.19.4 Prosodia de las interjecciones

Cada interjección tiene un **modo de fonación preferido** (ver §9.7 fonología) y un **contorno melódico típico**:

| Interjección | Modo de fonación | Contorno melódico | Tempo |
|--------------|------------------|-------------------|-------|
| `nam` | modal | medio, caída ligera | normal |
| `la` | modal / breathy | medio, sostenido | normal |
| `shama` | tenso | medio-alto, mantenido | lento |
| `hina` | modal | medio, alargamiento final | lento |
| `ya` | **falsetto** | alto, alargamiento | normal |
| `wai` | breathy / creaky | descendente, lamento | normal |
| `halel` | **falsetto** | alto, posible repetición | cantable |
| `amen` | modal | medio-grave, descenso | lento |
| `aum` | **falsetto** | alto-sostenido (cantar) | glacial |
| `shalam` | modal | medio, ligero descenso | normal |
| `baruk` | modal | medio-grave | lento |
| `kafa` | tenso | medio-alto, mantenido | normal |

> **Regla de la intensidad ascendente en ritual:** las 3 interjecciones rituales (`halel`, `amen`, `aum`) **deben** respetar la cadencia sellante (§9.6): la última sílaba se alarga a 3 moras y desciende melódicamente. Una `amen` cantada en registro agudo o sin descenso **rompe el efecto de sellado ritual**.

### 3.19.5 Diferencia con actitudinales y evidenciales

| Propiedad | Interjección | Actitudinal | Evidencial |
|-----------|--------------|-------------|------------|
| Categoría | partícula libre | sufijo verbal | sufijo verbal |
| Posición | aislada o inicial/final de cláusula | posverbal | posverbal |
| Marca | emoción / acto ilocutivo | actitud del hablante | fuente de información |
| ¿Componible? | no | sí (puede combinarse con evidencial) | sí (puede combinarse con actitudinal) |
| Prosodia | contorno propio | hereda del verbo | hereda del verbo |

**Regla de combinación:** una interjección **no** se combina con actitudinal ni evidencial. Si el hablante quiere añadir actitud, usa la interjección **y** un verbo con actitudinal explícito:
- ❌ `amen nam` (incorrecto, redundante)
- ✅ `amen, thar kair-nam` (amén, realiza el rito-con-reverencia)

### 3.19.6 Ejemplos de uso

**Apertura ritual:**
> `aum, pir hú-hék, bīj ih-ie-ahu thar kair-nam` — om, señor sacerdote, la semilla de ser-tú-YHWH realiza el rito-con-reverencia

**Cierre pacificador:**
> `bīja thar-poi, shalam` — la palabra-de-poder realiza-completa, paz

**Llamada atencional:**
> `shama, ána hu-ye` — escucha, yo ser-tú — "escucha, yo soy"

**Negación enfática:**
> `la, vach ih thar kair` — no, palabra-esta realiza rito — "no, esta palabra no realiza el rito"

#### 3.19.7 Combinación con actitudinales coercitivos

Las interjecciones (§3.19.1-3.19.6) se combinan con los actitudinales coercitivos (§5.3) para construir **invocaciones performativas compuestas**:

```
o [entidad invocada], bīj [bīja nativo] [verbo] [actitudinal coercitivo] [evidencial hierático] [modo performativo]
```

**Ejemplo canónico** (F3 + F4 + F2):
```
o Yaho, bīj raka wah-nam-ran-poi
oh YHWH, semilla fuego-cronos revelado-reverencia-ruego-performativo
"¡Oh YHWH, por favor, invoco el nombre esencial fuego-cronos con reverencia, performativamente!"
```

**Regla:** las interjecciones **no** llevan evidencial (§3.19.5), pero **sí** pueden combinarse con actitudinales coercitivos siempre que estos se adjunten al verbo principal, no a la interjección.

**Cross-ref:** §5.3 (sufijos coercitivos), §4 (vocativo, partícula `o`), fonología §11 (bījas nativos).

---

## 3.20 Fórmulas sociales fijas y frases hechas convencionalizadas

Esta sección documenta las **expresiones fijas de uso social frecuente** en Kalfírvach. No son entradas léxicas atómicas (esas residen en el léxico JSON), sino **construcciones gramaticales cristalizadas** que todo hablante debe conocer. Cada fórmula incluye:

- **Variante familiar** (registro íntimo, §3.7.1)
- **Variante cortés** (registro social, §3.7.1)
- **Análisis gramatical transparente** (composición morfológica y sintáctica)
- **Contexto de uso pragmático**

Las fórmulas se agrupan por función comunicativa.

---

### 3.20.1 Saludos por hora del día

Los saludos en KFA son **frases nominales elípticas**: tópico (`sadu` + adverbio temporal) con comentario omitido ("que tengas..."). No llevan verbo explícito.

| Español | KFA (familiar) | KFA (cortés) | IPA | Análisis |
|---------|----------------|--------------|-----|----------|
| **Buenos días** | `sadu sapkhah` | `sadu sapkhah, tum` | /sa.du sap.xah/ | `sadu` (adj bueno) + `sapkhah` (mañana temprano, §3.10.2) |
| **Buenas tardes** | `sadu ashar` | `sadu ashar, tum` | /sa.du a.ʃar/ | `sadu` + `ashar` (tarde, §3.10.2) |
| **Buenas noches** | `sadu ratiri` | `sadu ratiri, tum` | /sa.du ra.ti.ri/ | `sadu` + `ratiri` (noche, §3.10.2). También: `sadu shafak` (buen crepúsculo) |
| **Buen amanecer** | `sadu fajar` | `sadu fajar, tum` | /sa.du fa.dʒar/ | Para saludo muy temprano (alba, §3.10.2) |

> **Nota**: El registro cortés añade `tum` (2sg cortés, §3.7.1) como vocativo implícito al final.

---

### 3.20.2 Saludo general y bienvenida

| Español | KFA (familiar) | KFA (cortés) | IPA | Análisis |
|---------|----------------|--------------|-----|----------|
| **Hola / Saludo** | `ghip-a` | `ghip-a nam` | /ɣi.pa/ | `ghip-a` = saludar-PRES (declarativa: "saludo"). Con `nam` (interj. asentimiento, §3.19) |
| **Bienvenido** | `ay-a sadu` | `ay-a sadu, tum` | /a.ja sa.du/ | `ay-a` (venir-PRES, §3.16) + `sadu` (bueno) = "vienes bien / buena venida" |
| **Bienvenidos (plural)** | `ay-a-mash sadu` | `ay-a-túm sadu` | /a.ja.maʃ sa.du/ | Verbo conjugado 1pl / 2pl cortés (§3.3, §3.7.1) |

---

### 3.20.3 Despedidas

| Español | KFA (familiar) | KFA (cortés) | IPA | Análisis |
|---------|----------------|--------------|-----|----------|
| **Adiós / Chao** | `fīkhā` | `fīkhā nam` | /fiː.xaː/ | `fīkhā` (despedir, forma base usada como interjección). Con `nam` = "me despido, sí" |
| **Hasta luego** | `ay-u-kal` | `ay-u-kal, tum` | /a.ju kal/ | `ay-u` (venir-FUT) + `-kal` (hipotético, §2.3) = "vendré potencialmente / nos veremos" |
| **Hasta mañana** | `ghat ay-u` | `ghat ay-u, tum` | /ɣat a.ju/ | `ghat` (mañana siguiente, §3.10.2) + `ay-u` (venir-FUT) |
| **Buenas noches (despedida)** | `sadu ratiri, fīkhā` | `sadu ratiri, fīkhā nam` | /sa.du ra.ti.ri fiː.xaː/ | "Buena noche, me despido" |
| **Que descanses** | `shant-ka shay-u` | `shant-ka shay-u, tum` | /ʃant.ka ʃa.ju/ | `shant-ka` (calmadamente, adv modo §3.10.4) + `shay-u` (yacer-FUT, §3.16) |

---

### 3.20.4 Cortesía básica

| Español | KFA (familiar) | KFA (cortés) | IPA | Análisis gramatical |
|---------|----------------|--------------|-----|---------------------|
| **Por favor** | `kár-ran` | `kár-ran` | /kar.ran/ | `kár-` (hacer) + `-ran` (precativo, §5.3) = "haz por favor". **Úsalo ante cualquier verbo**: `ay-a-ran` (ven por favor), `vach-a-ran` (habla por favor) |
| **Gracias** | `dziywū-a` | `dziywū-a-nam` | /ʣij.wu.a/ | `dziywū-a` (agradecer-PRES). Con `-nam` (reverencia, §2.2) en cortés |
| **Muchas gracias** | `tís dziywū-a` | `tís dziywū-a-nam` | /tis ʣij.wu.a/ | `tís` (muy, adv grado §3.10.5) + agradecer |
| **De nada / No hay de qué** | `la itrum` | `la itrum, tum` | /la it.rum/ | `la` (no, interj. §3.19) + `itrum` (permiso/licencia, §tecnología) = "no hay permiso [necesario]" |
| **Con permiso / Permiso** | `itrum-te` | `itrum-te, tum` | /it.rum.te/ | `itrum` (permiso) + `-te` (dativo, §3.2) = "con permiso" |
| **Disculpe / Perdón** | `na-rashe-a` | `na-rashe-a-nam` | /na.ra.ʃe.a/ | `na-` (NEG) + `rashe-a` (autorizar-PRES) + `-nam` = "no autorizo [la ofensa]" |
| **No se preocupe** | `na-bay` | `na-bay, tum` | /na.baj/ | `na-` (NEG) + `-bay` (actitudinal miedo, §2.2) = "sin miedo / no tema" |

---

### 3.20.5 Presentaciones y conocer

| Español | KFA (familiar) | KFA (cortés) | IPA | Análisis |
|---------|----------------|--------------|-----|----------|
| **Mucho gusto en conocerte** | `tís swat yana-an ta-te` | `tís swat yana-an tum-te` | /tis swat ja.nan ta.te/ | `tís` (muy) + `swat` (gusto/placer, n., §comida_y_cocina) + `yana-an` (conocer-INF, §3.3.5) + `ta-te`/`tum-te` (tú-DAT, §3.2). Lit: "Mucho placer conocer a-ti" |
| **Encantado de conocerle** | `swat as-a yana-an ta-te` | `swat as-a yana-an tum-te` | /swat a.sa ja.nan tum.te/ | `swat as-a` (placer es-PRES) + infinitivo + dativo |
| **¿Cómo te llamas?** | `kím nūm as-a ta-sya?` | `kím nūm as-a tum-sya?` | /kim num a.sa ta.sja/ | `kím` (qué, §3.8) + `nūm` (nombre personal, §3.18.3) + `as-a` (es) + `ta-sya`/`tum-sya` (tu-GEN, §3.9) |
| **Me llamo…** | `ma-sya nūm … as-a` | `ma-sya nūm … as-a` | /ma.sja num … a.sa/ | `ma-sya` (mi-GEN) + `nūm` (nombre) + nombre + `as-a` |
| **Te presento a…** | `ma ta-te … vach-a` | `ma tum-te … vach-a` | /ma ta.te … vatʃ.a/ | `ma` (yo) + `ta-te`/`tum-te` (tú-DAT) + nombre + `vach-a` (hablar/presentar-PRES, §3.3) |

---

### 3.20.6 Conversación básica

| Español | KFA (familiar) | KFA (cortés) | IPA | Análisis |
|---------|----------------|--------------|-----|----------|
| **¿Cómo estás?** | `kwa-ka as-a ta?` | `kwa-ka as-a tum?` | /kwa.ka a.sa tum/ | `kwa-ka` (alguien/indefinido, §3.14) + `as-a` (es) + pronombre. Lit: "¿Alguien eres tú?" ≅ "¿Cómo estás?" |
| **Bien, gracias** | `sadu, dziywū-a` | `sadu, dziywū-a-nam` | /sa.du ʣij.wu.a/ | `sadu` (bueno) + agradecer |
| **¿Hablas KFA?** | `kalfírvach vach-a ta?` | `kalfírvach vach-a tum?` | /kal.fir.vatʃ vatʃ.a tum/ | Nombre del idioma + `vach-a` (hablar-PRES) + pronombre |
| **Entiendo / Comprendo** | `gnán-a` | `gnán-a-nam` | /gna.na/ | `gnán-a` (saber/conocer-PRES, raíz `yana` con prefijo `gn-` de `gnotha` "saber cómo", §3.6). Con `-nam` reverencia |
| **No entiendo** | `na-gnán-a` | `na-gnán-a-nam` | /na.gna.na/ | `na-` (NEG) + `gnán-a` |
| **Repita, por favor** | `vach-a-ran` | `vach-a-ran` | /vatʃ.a.ran/ | `vach-a` (hablar-PRES) + `-ran` (precativo, §5.3) |
| **Más despacio, por favor** | `bátí-ka vach-a-ran` | `bátí-ka vach-a-ran` | /ba.ti.ka vatʃ.a.ran/ | `bátí-ka` (lentamente, adj `bátí` + `-ka` adv modo, §3.10.4) + hablar-precativo |

---

### 3.20.7 Frases sociales extendidas

| Español | KFA (familiar) | KFA (cortés) | IPA | Análisis |
|---------|----------------|--------------|-----|----------|
| **Fue un placer hablar con usted** | `swat as-i vach-an ta-te` | `swat as-i vach-an tum-te` | /swat a.si vatʃ.an tum.te/ | `swat` (placer) + `as-i` (ser-PAS) + `vach-an` (hablar-INF) + `ta-te`/`tum-te` (tú-DAT) |
| **Fue un placer conocerle** | `swat as-i yana-an ta-te` | `swat as-i yana-an tum-te` | /swat a.si ja.nan tum.te/ | Mismo patrón con `yana-an` (conocer-INF) |
| **Espero volver a verte** | `ich-a ay-u ti ta pas-y-u` | `ich-a ay-u ti tum pas-y-u` | /itʃ.a a.ju ti tum pas.ju/ | `ich-a` (querer-PRES, §3.12.2) + `ay-u` (venir-FUT) + `ti` (que, §4.3.2) + `ta`/`tum` (tú) + `pas-y-u` (ver-FUT, §3.3) |
| **Cuídate** | `rakh-a sadu` | `rakh-a sadu, tum` | /rax.a sa.du/ | `rakh-a` (proteger/cuidar-PRES, raíz `rakh-` §verbos_basicos) + `sadu` (bien) |
| **Que tengas un buen día** | `sadu sapkhah as-u ta-te` | `sadu sapkhah as-u tum-te` | /sa.du sap.xah a.su tum.te/ | `sadu sapkhah` (buen día) + `as-u` (ser-FUT) + `ta-te`/`tum-te` (tú-DAT) = "que un buen día sea para ti" |
| **Feliz cumpleaños** | `sadu dín as-u ta-te` | `sadu dín as-u tum-te` | /sa.du din a.su tum.te/ | `sadu` + `dín` (día, §3.3.2) + `as-u` (ser-FUT) + dativo |
| **Salud / ¡Salud! (brindis)** | `shalam` | `shalam, tum` | /ʃa.lam/ | `shalam` (paz/salutación/bendición, interj. §3.19). En brindis: "paz [entre nosotros]" |
| **Buen provecho** | `swat ghada` | `swat ghada, tum` | /swat ɣa.da/ | `swat` (placer/gusto) + `ghada` (almuerzo/comida, §comida_y_cocina) = "placer en la comida" |
| **Buen viaje** | `sadu gach-an` | `sadu gach-an, tum` | /sa.du ɣatʃ.an/ | `sadu` + `gach-an` (ir-INF, §3.16) = "buen ir / buen camino" |

---

### 3.21 Calendario y días de la semana

La semana KFA estándar tiene 7 días, cada uno nombrado por un cuerpo celeste (ver léxico, §naturaleza_y_elementos). El sufijo **-mera** proviene de `daimera` ("día", del griego *hēmera*, §conceptos_espaciales_y_calidades) y se añade al nombre del astro regente.

| # | Día | KFA | IPA | Astro regente |
|---|-----|-----|-----|---------------|
| 1 | Domingo | `suryamera` | /su.rjaˈme.ra/ | Surya (Sol) |
| 2 | Lunes | `mahselmera` | /mah.selˈme.ra/ | Mahsel (Luna) |
| 3 | Martes | `hermarmera` | /her.marˈme.ra/ | Hermar (Marte) |
| 4 | Miércoles | `thutirmera` | /θu.tirˈme.ra/ | Thutir (Mercurio) |
| 5 | Jueves | `hormusmera` | /hor.musˈme.ra/ | Hormus (Júpiter) |
| 6 | Viernes | `anzumera` | /an.zuˈme.ra/ | Anzu (Venus) |
| 7 | Sábado | `keyzumera` | /kej.zuˈme.ra/ | Keyzu (Saturno) |

**Uso en oración:**

> `suryamera as-i sadu sapkhah` — "El domingo fue una buena mañana"
> `ma tum-te hormusmera-te pas-y-u` — "Te veré el jueves" (lit. "yo tú-DAT Júpiter-día-DAT ver-FUT")

El acento recae en **-me-** (penúltima) en todos los casos. Para referirse al día de hoy se usa `yawam` (§§tiempo_domestico, "hoy") y para el día siguiente `ghat` ("mañana siguiente", misma sección). La palabra para "semana" es `sabu` (§tiempo_domestico).

---

## 4. Composición y cláusulas complejas

### 4.1 Composición nominal

Las palabras compuestas se forman por **yuxtaposición de raíces** con la estructura:

```
Modificador + Núcleo
```

La raíz modificadora se coloca antes de la raíz nuclear. El acento recae sobre la penúltima sílaba del compuesto entero.

**Ejemplos de términos técnicos (composición lógica transparente):**

| Concepto moderno | Composición | Forma KFA | Glosa literal |
|-----------------|-------------|-----------|---------------|
| Firewall | fír (fuego) + mur (muro) | **fír-mur** | muro de fuego |
| Interface | sánd (entre) + mukh (rostro/punto) | **sánd-mukh** | punto de contacto entre |
| Protocol | rit (rito/orden) + már (camino) | **rit-már** | camino ordenado |
| Signal | sháb (signo) + tál (emitir) | **sháb-tal** | signo emitido |
| Node (network) | bánd (nudo) + nús (conciencia/punto) | **bánd-nus** | punto de unión consciente |
| Network | bánd-nus + -thu (colectivo) | **bánd-nus-thú** | campo de puntos de unión |
| Code | likh (escribir) + rit (orden) | **líkh-rit** | escritura ordenada |
| Window | mukh (rostro/apertura) + sól (luz) | **mukh-sól** | apertura de luz |
| Digital echo | sáb (eco) + líkh-rit (código) | **sáb-líkhrit** | eco de escritura ordenada |
| Unconscious | a- (sin) + nús (conciencia) | **a-nús** | sin conciencia |
| Archetype | múl (raíz) + rúp (forma) | **múl-rúp** | forma raíz |
| Synchronicity | sáma (simultáneo) + lek (significado) | **sáma-lek** | significado simultáneo |

### 4.2 Reglas fonotácticas en composición

Cuando dos raíces se combinan:

1. **Coda + Onset**: Se aplican las reglas de asimilación
2. **Vocal + Vocal**: Se aplica elisión (a+a→a) o se inserta /w/ como enlace si las vocales son muy distintas: ri + a → riwa
3. **Acento**: Se recalcula sobre el compuesto entero

### 4.3 Conjunciones y subordinación

Kalfírvach usa **conjunciones coordinantes** y **subordinantes** para conectar oraciones y cláusulas.

#### 4.3.1 Conjunciones coordinantes

| Conjunción | IPA | Función | Origen (≥2) |
|-----------|-----|---------|-------------|
| **cha** | /tʃa/ | **y** (adición) | Sánscrito *ca* + Avestan *ca* + Griego *τε* (te). 3 lenguas. |
| **va** | /wa/ | **o** (disyunción) | Sánscrito *vā* + Avestan *vā*. 2 lenguas. |
| **tu** | /tu/ | **pero** (contraste) | Sánscrito *tu* "pero, ciertamente" (partícula contrastiva) + Árabe *thumma* "luego, además (contraste)". 2 lenguas. |

**Ejemplos:**
```
zal kár-a  cha  nūros as-a
sombra hace y    luz  es
"La sombra actúa y la luz es"

ta  as-i    va   ka  as-i?
este fue  o   aquello fue
"¿Fue esto o fue aquello?"

nūros as-a   tu   zal na-kár-a
luz es     pero sombra no-hace
"La luz es, pero la sombra no actúa"
```

#### 4.3.2 Conjunciones subordinantes

| Conjunción | IPA | Función | Origen (≥2) |
|-----------|-----|---------|-------------|
| **yas** | /jas/ | **si** (condicional) | Sánscrito *yad* + Avestan *yat* → coda /t/→/s/. 2 lenguas. |
| **kar** | /kar/ | **porque** (causal) | Griego *χάριν* (khárin) "por causa de" + Sánscrito *kāraṇa* "causa, razón". 2 lenguas. |
| **ti** | /ti/ | **que** (complementizante) | Sánscrito *iti* "así" (marca de cita/discurso) + Griego *ὅτι* (hóti) "que" → reducción -ti. 2 lenguas. |

**Ejemplos:**
```
yas  nūros as-a,  zal kár-u
si   luz es     sombra hará
"Si la luz es, la sombra actuará"

ma  as-a-nand    kar   ta   as-a
yo  soy-alegría  porque esto es
"Estoy alegre porque esto existe"

sa  kar-i        ti   ma  as-a
suyo hacer-pasó  que  yo  veo
"Él/ella dijo/hizo que yo sé"

ma  as-a-anu     ti   zal kár-i
yo  soy-inferido que  sombra hizo
"Infiero que la sombra actuó"
```

#### 4.3.3 Conjunciones temporales

| Conjunción | IPA | Función | Origen (≥2) |
|-----------|-----|---------|-------------|
| **pári** | /ˈpa.ri/ | "antes de que" (temporal anterior) | Griego *παρά* (pará) "delante de, antes" + Persa *par* "antes". 2 lenguas. |
| **mét** | /met/ | "después de que" (temporal posterior) | Griego *μετά* (metá) "después" + Árabe *ba'd* "después" → met. 2 lenguas. |
| **tés** | /tes/ | "mientras" (simultáneo) | Persa *tā* "hasta/mientras" + Tibetano *té* "mientras" → tés (coda /s/ asimilación). 2 lenguas. |
| **hát** | /hat/ | "hasta que" (temporal final) | Árabe *ḥattā* "hasta" → hát; Griego *ἕως* (héōs) "hasta" → hát (fusión). 2 lenguas. |

```
pári  nūros as-i,  zal kár-i
antes luz fue   sombra actuó
"Antes de que la luz fuera, la sombra actuó"

mét  zal kár-i,  nūros as-a
después sombra hizo   luz es
"Después de que la sombra actuó, la luz es"

tés  nūros as-a,  zal kár-a
mientras luz es   sombra hace
"Mientras la luz es, la sombra actúa"

hát  nūros as-u,  zal kár-u
hasta luz será  sombra hará
"Hasta que la luz sea, la sombra actuará"
```

#### 4.3.4 Conjunciones lógicas

| Conjunción | IPA | Función | Origen (≥2) |
|-----------|-----|---------|-------------|
| **ár** | /ar/ | "aunque / a pesar de" (adversativa) | Griego *ἀλλά* (allá) "pero, aunque" → ár; Persa *agar* "si/aunque" → ár. 2 lenguas. |
| **tát** | /tat/ | "por lo tanto / entonces" (consecutiva) | Árabe *tābi'* "consecuente" → tát; Persa *tā* "entonces/hasta" → tát. 2 lenguas. |
| **kás** | /kas/ | "para que / a fin de que" (final) | Griego *κατά* (katá) "conforme a" + Árabe *qasd* "propósito" → kás. 2 lenguas. |
| **wá** | /wa/ | "mientras que / en cambio" (contraste) | Árabe *wa-* (wāw, conjunción de contraste clásico) + Persa *vā* "o/alternativamente". 2 lenguas. |

```
ár   ma as-a-bay,   ma kár-a
aunque yo soy-miedo  yo actúo
"Aunque tengo miedo, actúo"

zal kár-a,  tát  nūros as-u
sombra hace  entonces luz será
"La sombra actúa, por lo tanto la luz será"

ma  pra-kár-a   kás  tum  as-u-nam
yo  PREP-hacer  para tú.CORT ser-FUT-reverencia
"Me preparo para que tú seas [con respeto]"

wá   nūros as-a,   zal na-kár-a
en cambio luz es   sombra no-hace
"La luz es, en cambio la sombra no actúa"
```

---

### 4.4 Cláusulas complejas

Kalfírvach construye cláusulas complejas mediante **partículas subordinantes**, **complementizantes**, **marcadores relativos** y **prefijos causativos**. El orden básico SOV se mantiene en cada cláusula subordinada.

### 4.4.1 Cláusulas relativas

Las relativas se forman con **ya** (Sánscrito *ya-* + Avestan *ya-*, 2 lenguas) al inicio de la cláusula. La cláusula relativa **precede** al sustantivo que modifica.

**Regla:** `ya <oración> <sustantivo_modificado>`

```
ya  ma  dirish-i-e,   ha  nara
REL yo  ver-PAS-VIS   DEF.SG persona
"la persona que yo vi" (lit. "que yo vi, la persona")
```

La relativa puede tener su propio **sujeto explícito** cuando no es correferente:

```
ya  sa  kár-i-e,      ha  thel
REL él  hacer-PAS-VIS DEF.SG voluntad
"la voluntad que él manifestó"
```

**Relativas sin cabeza** (sustantivo omitido, el relativo funciona como pronombre):

```
ya  ma  ich-a,   as-a-síg
REL yo  querer  es-PRES-silencio_gnóstico
"Lo que quiero es en silencio gnóstico" = "Mi deseo es silencio sagrado"
```

### 4.4.2 Cláusulas de complemento (subordinación sustantiva)

Se usa **ti** (Sánscrito *iti* + Griego *ὅτι* hóti, 2 lenguas) como **complementizante** — equivalente a "que" en español. La cláusula subordinada con **ti** puede funcionar como **objeto directo** o **sujeto** del verbo principal.

```
<verbo_principal> <ti> <oración_subordinada>
```

```
ma  yan-a-e       ti   zal kár-a
yo  saber-PRES-VIS QUE  sombra hacer-PRES
"Yo sé [veo] que la sombra actúa"
```

**Como sujeto** (la subordinada es el sujeto de la cópula):

```
ti   zal kár-a,   as-a-evidente
QUE  sombra hace   es-PRES-EVID:visual
"Que la sombra actúe es evidente"
```

**Con verbos de percepción**, el evidencial en la cláusula subordinada puede diferir del principal:

```
ma  as-a-anu     ti   sa  kár-i-wah
yo  ser-PRES-INFER QUE  él  hacer-PAS-REVELADO
"Infiero que a él le fue revelado que actuó"
```

### 4.4.3 Construcciones causativas

El causativo se forma con el prefijo **dha-** /dʱa/ (Griego *θε-* en τίθημι "poner, colocar, causar" + Sánscrito *√dhā* "poner, hacer, causar", de la raíz IE *dʰeh₁- "poner". 2 lenguas) añadido al verbo. Indica que el sujeto **hace que** alguien/algo realice la acción.

```
<causante> [<causado>-te] dha-<verbo>
```

| Forma | Significado | Estructura |
|-------|-------------|-----------|
| dha-kár-a | "hace actuar / causa que se haga" | dha- + raíz verbal + tiempo |
| dha-pát-a | "hace caer / derriba" | dha- + pati "caer" → dha-pát-a |
| dha-gnóth-a | "hace saber / enseña" | dha- + gnotha "saber" → dha-gnóth-a |
| dha-thér-a | "hace curar / sana mediante otro" | dha- + thera "curar" → dha-thér-a |

**Ejemplos:**

```
zal    nūros-te    dha-kár-a
sombra  luz-DAT   CAUS-hacer-PRES
"La sombra hace que la luz actúe"

ma  sa-te   dha-pát-i-e
yo  él-DAT  CAUS-caer-PAS-VIS
"Hice que él cayera [veo]"

áz-ta    dha-gnóth-u   ti   nūros as-a-ék
HIER-ABS CAUS-saber-FUT QUE  luz es-éxtasis
"El iniciado enseñará [hará saber] que la luz es en éxtasis"
```

**Nota:** El **causado** (quien realiza la acción causada) se marca en **dativo** (-te). Sin causado explícito, la lectura es impersonal: *dha-kár-a* = "se hace actuar / se causa acción".

### 4.4.4 Oraciones condicionales

#### Reales (siempre ocurren)

**yas** + presente + presente:

```
yas  nūros as-a,   zal kár-a
si   luz es      sombra hace
"Si la luz es, la sombra actúa" (relación causal constante)
```

#### Potenciales (podrían ocurrir)

**yas** + presente + futuro:

```
yas  ma  dún-a,   ma  kár-u-kál
si   yo  poder    yo  hacer-FUT-HIP
"Si puedo, actuaría (potencialmente)"
```

#### Contrafácticas (no ocurrieron)

**yas** + pasado + modo **-kal** (hipotético):

```
yas  zal as-i-kal,   nūros na-as-u
si   sombra fue-HIP    luz  no-será
"Si la sombra hubiera sido, la luz no sería"
```

### 4.4.5 Oraciones de propósito

Se construyen con **kás** (Griego *κατά* + Árabe *qasd*, 2 lenguas) "para que / a fin de que" + **subjuntivo hipotético** (-kal) cuando el propósito es incierto, o + **presente** cuando es cierto:

```
ma  pra-kár-a     kás  tum  as-u-nam
yo  PREP-hacer    para tú.CORT ser-FUT-reverencia
"Me preparo para que tú seas [con respeto]"

sa  kár-a     kás  nūros as-kal
él  hace     para que luz sea-HIP
"Él actúa para que la luz sea (potencialmente)"
```

También se usa **muk** (directivo) + nombre abstracto como forma corta:

```
ma  kár-a    nūros  ops-te  muk
yo  hacer    luz  visión-DAT para
"Actúo para la visión de luz" (lit. "actúo hacia la luz para visión")
```

### 4.4.6 Clausas concatenadas (encadenamiento de cláusulas)

Múltiples cláusulas se encadenan con conjunciones coordinantes o subordinantes sin repetición del sujeto cuando es correferente. El patrón es **stacking medial** típico de lenguas SOV:

```
<cláusula_1>   <conjunción>   <cláusula_2>   <conjunción>   <cláusula_3>
```

```
nūros as-a,   cha   zal kár-a,   tát  ma  ops-a-e
luz es      y     sombra hace   entonces yo  ver-PRES-VIS
"La luz es, y la sombra actúa, por lo tanto yo veo"

yas  ma  dún-a,   cha   ma  ich-a,   tát  ma  kár-u
si   yo  poder    y     yo  querer   entonces yo  hacer-FUT
"Si puedo y quiero, entonces actuaré"

ma  pra-kár-a   kás  sa  thér-u,   mét  ma  tél-kár-u
yo  PREP-hacer  para él  curar-FUT después yo  CULM-hacer-FUT
"Me preparo para que él se cure, después culminaré"
```

**Encadenamiento de 3+ cláusulas subordinadas** (típico en textos rituales):

```
áz   tés  kair-kár-a-h,      yas  sa  dún-a,        kás  sa  as-u-nam,
HIER mien kair-hacer-HIER    si   él  poder-PRES    para él  ser-FUT-reverencia

 tát  az   tél-kár-u-ék-poi
ent HIER  CULM-hacer-FUT-éxtasis-PERF
"Yo, iniciado, mientras actúo en el momento sagrado, si él puede, para que él sea con reverencia, entonces culminaré con éxtasis performativo"
```

---

## 5. Estructura informacional

### 5.1 Tópico y comentario

Kalfírvach marca el **tópico** de la oración con la partícula **ho** (/ho/) colocada tras el elemento topicalizado:

```
thel ho,  zal  kár-a-e
voluntad TOP  sombra hacer-PRES-visual
"En cuanto a la voluntad, la sombra actúa [veo]"
```

**Origen:** Griego ὁ (ho, artículo definido); Tibetano ni (partícula tópico) → ho (fusión). 2 lenguas.

### 5.2 Preguntas

Las preguntas sí/no se forman con la partícula **ka** (/ka/) al final de la oración, reemplazando al evidencial:

```
zal  kár-a  ka?
sombra hacer-PRES INTERR
"¿La sombra actúa?"
```

Las preguntas de contenido usan los interrogativos (§3.8) en posición normal:

```
kwa  zal  kár-a-e?
quién sombra hacer-PRES-visual
"¿Quién [veo que] actúa la sombra?"
```

### 5.3 Imperativo y actitudinales coercitivos

El sistema imperativo KFA se estratifica en **cinco niveles de fuerza ilocutiva**, del precativo respetuoso al coercitivo hierático. El sufijo **-ro** (/ro/) se mantiene para el imperativo mundano, y se rodea de cuatro actitudinales que codifican la **fuerza ritual** del acto.

**Jerarquía (de menor a mayor fuerza):**

1. `-ran` (precativo) — ruego
2. `-ro` (imperativo) — orden directa
3. `-ro-hék` (coercitivo hierático) — mandato ritual
4. `-rak` (abjurativo) — destierro
5. `-rab` (vinculante) — atadura

**Tabla de sufijos coercitivos (5 columnas):**

| Sufijo | Fuerza ilocutiva | Función ritual | Ejemplo KFA | Gloss literal |
|--------|------------------|----------------|-------------|---------------|
| `-ran` | precativo | ruego, invocación respetuosa | `kár-ran` | "por favor, haz" |
| `-ro` | imperativo mundano | orden directa, sin sanción | `kár-ro` | "¡haz!" |
| `-ro-hék` | coercitivo hierático | mandato con autoridad ritual (sólo con verbo hierático) | `kár-a-ro-hék` | "yo te ordeno, por el sello, que hagas" |
| `-rak` | abjurativo | destierro, alejamiento forzado | `an-rak` | "aléjate, te lo ordeno" |
| `-rab` | vinculante | atadura, sello, ligadura | `ka-rab-ko` | "quedáte ligado a este nombre" |

**Restricciones de combinación:**

- `-ran` puede combinarse con cualquier evidencial (reverencia por defecto con `-nam`).
- `-ro` es mundano y **NO** se combina con evidenciales hieráticos (`-wah`, `-nand`).
- `-ro-hék` **requiere** verbo en registro hierático (prefijo `kár-a-` o equivalente §3.7.1).
- `-rak` y `-rab` son los únicos actitudinales que **pueden** invertir polaridad de una cláusula declarativa previa.

**Origen documentado:**

- `-ro`: Sánscrito -tu (imperativo 3sg) → -ro; Persa -rod → -ro. 2 lenguas.
- `-ran`/`-rak`/`-rab`/`-ro-hék`: ver lexicón §F3 (actitudinales) — cada uno con ≥3 fuentes documentadas.

**Cross-ref:** §2.1 (evidenciales), §3.19.7 (combinación con interjecciones y bījas), fonología §11 (bījas nativos).

### 5.4 Partículas de foco y énfasis

| Partícula | Función | Origen (≥2) |
|-----------|---------|-------------|
| **ét** | "precisamente / exactamente" | Griego *ἔτι* (éti) "aún, además, exactamente" + Egipcio *Ꜥt* "instante, punto exacto" |
| **máh** | "en verdad / ciertamente" | Árabe *mā* (énfasis) + Persa *mah* "grande" |
| **lám** | "de ningún modo" (negación enfática) | Árabe *lam* (negación enfática) + Griego *μή* (mḗ) "no" → lám (fusión) |
| **hál** | "¡he aquí! / ¡mira!" (exclamación) | Árabe *hā* "he aquí" + Griego *ἰδού* (idoú) "he aquí" → hál |

```
zal ét   kár-a   = "Precisamente la sombra actúa"
nūros máh as-a     = "En verdad la luz es"
ma  lám kár-u    = "De ningún modo actuaré"
hál!  nūros as-a!  = "¡He aquí la luz es!"
```

#### 5.4.1 Foco contrastivo: partícula `tu`

Marca contraste o corrección con lo anterior; traduce "pero, en cambio, en realidad". Indica que el elemento marcado se opone o corrige una presuposición.

```
fir   tu  rat-a      = "Pero el fuego brilla" (contraste con algo dicho antes)
ma    tu  ich-a      = "Yo, en cambio, quiero" (contraste con la voluntad de otro)
na    tu  as-a       = "No, en realidad [es]" (corrección enfática)
```

**Origen:** Sánscrito **tu** (तु, "pero, en cambio", partícula enclítica) + Griego **δέ** (dé, "pero, por otra parte") + Tibetano **ṭe** (ཏེ, conjunción adversativa). 3 lenguas. **Fonotaxis:** /tu/ — onset `t-` ✓, vocal `u` ✓, sin coda. CV. ✓

**Posición:** preverbal, inmediatamente antes del verbo (slot -1 del SV) o antes del SN al que se aplica foco contrastivo. Se combina con partículas de negación y modalidad.

#### 5.4.2 Foco restrictivo: partícula `ila`

Marca restricción o exclusión; traduce "sólo, excepto, salvo, únicamente". Restringe la extensión del elemento al que se aplica.

```
ma     ila  gach-u   = "Sólo yo iré" (exclusión de otros)
ilá    fir   rat-a   = "Sólo el fuego brilla" (no otras cosas)
na     kwa-ka ila na-vach-a = "Nadie habla, sólo alguien no" → CORREGIR: "nadie habla en absoluto" (no, esto es incorrecto)
```

**Origen:** Árabe **illā** (إلّا, "excepto, sino, salvo") + Griego **εἰ μή** (ei mḗ, "si no, a menos que") + Persa **illā** (همان, "sino, excepto"). 3 lenguas. **Fonotaxis:** /i.la/ — onset vacío (V inicial) + vocal `i` ✓ + onset `l-` ✓ + vocal `a` ✓. 2 sílabas, VC.CV. ✓

**Posición:** preverbal (slot -1) o pre-SN (modificador del sintagma nominal). La forma correcta del último ejemplo es:

```
kwa-na ila na-vach-a    = "Nadie salvo [X] no habla" (uso complejo: ila introduce excepción)
```

`ila` puede combinarse con indefinidos negativos (`kwa-na`, `kím-na`) para introducir la excepción:

```
kím-na ila nūros as-a     = "No hay nada excepto luz" = "Sólo hay luz"
```

#### 5.4.3 Foco existencial: partícula `duk`

Marca afirmación enfática de existencia o presencia; traduce "ciertamente, de hecho, en efecto". Refuerza la predicación existencial de la cópula `as` o de los verbos de presencia.

```
nūros  duk  as-a        = "Ciertamente la luz es"
ma   duk  ich-a       = "De hecho yo quiero"
sa   duk  kár-a       = "Él, en efecto, actúa"
```

**Origen:** Tibetano **'dug** (འདུག, "estar, existir, afirmación enfática de presencia") — adaptado a la fonotaxis KFA con coda `/g/ → /k/` (la coda /k/ es la única velar sorda permitida; /g/ sonora está prohibida en coda, §3.3 fonología) — más Egipcio **dwꜣ** (estar, existir) + Avestan **daδāiti** (𐬛𐬀𐬛𐬁𐬌𐬙𐬌, "pone, establece, hace existir"). 3 lenguas. **Fonotaxis:** /duk/ — onset `d-` ✓, vocal `u` ✓, coda `k` permitida ✓. CVC. ✓

**Posición:** preverbal, inmediatamente antes del verbo principal (slot -1). Refuerza el verbo más que el SN.

**Distinción con `máh`:** `máh` (§5.4) marca énfasis en el SN ("en verdad X"); `duk` marca énfasis en la existencia/acción del verbo ("ciertamente [sucede]"). En la práctica pueden co-ocurrir:

```
nūros  máh  duk  as-a   = "Ciertamente, en verdad, la luz es" (énfasis máximo, registro oracular)
```

#### 5.4.4 Tópico fuerte: partícula `amma`

Marca tópico con fuerza contrastiva o contrastiva-exhaustiva; traduce "en cuanto a, respecto de, en lo que concierne a". A diferencia de `ho` (§5.1) que es un tópico ligero, `amma` introduce un tópico que se opone a otros posibles o que se va a contrastar.

```
thel    amma,  theós  na kár-a   = "En cuanto a la voluntad, el dios no actúa" (contraste con otros agentes)
ma      amma,  ta-te  ich-u      = "En cuanto a mí, te querré" (tópico contrastivo de persona)
ratna   amma,  tá     as-a       = "En cuanto al tesoro, ese es" (tópico + demostrativo)
```

**Origen:** Árabe **ammā** (أمّا, "en cuanto a, por lo que se refiere a", partícula topicalizadora enfática) + Griego **ἅμα** (háma, "al mismo tiempo, junto con") + Egipcio **m-ꜥ** (preposición topicalizadora en textos demóticos, marca "en lo concerniente a"). 3 lenguas. **Fonotaxis:** /a.ma/ — vocal `a` ✓ + onset `m-` ✓ + vocal `a` ✓. 2 sílabas, V.CV. ✓

**Posición:** pospuesto al SN topicalizado, igual que `ho` (slot tópico). El SN topicalizado va seguido de `,` (pausa prosódica) y luego el comentario.

**Contraste con `ho`:**

| Dimensión | `ho` (tópico ligero) | `amma` (tópico fuerte) |
|-----------|----------------------|-------------------------|
| Función | Introduce referente conocido | Introduce referente contrastado |
| Español equivalente | "en cuanto a..., el caso es que..." | "respecto de X (a diferencia de Y), ..." |
| Registro | cotidiano, informativo | argumentativo, contrastivo |
| Combinable | sí, con otros tópicos | sí, con ho también |
| Coexistencia | "thel ho amma, ..." = "en cuanto a la voluntad, además..." (apilable) | (idem) |

**Combinación con foco contrastivo (`tu`):** muy frecuente para construir contrastes explícitos:

```
ma    amma,   ta  tu  na-ich-a   = "En cuanto a mí, tú en cambio no quieres" (contraste doble)
thel  amma,   nūros  tu  as-a      = "En cuanto a la voluntad, la luz en cambio es" (contraste X vs Y)
```

### 5.5 Marcadores discursivos

| Marcador | Función | Origen (≥2) |
|----------|---------|-------------|
| **hán** | Inicio: "pues bien, ahora" | Árabe *hana* "aquí/ahora" + Persa *hān* "¡eh!/pues" |
| **wáy** | Transición: "por otra parte, además" | Árabe *wa-* (conjunción) + Persa *way* "y además" |
| **súm** | Conclusión: "en resumen, así pues" | Griego *συμπέρασμα* (sympérasma) "conclusión" → súm; Tibetano *sdum* "resumir" |
| **kát** | Cita: "dicen que, se dice" (citativo) | Árabe *qāla* "dijo" → kát; Persa *kad* "cuando/dicen" |

```
hán,  ma  vach-u      = "Pues bien, hablaré"
wáy,  tum  na-ich-a   = "Por otra parte, tú no quieres"
súm,  ma  kár-a-kás-soph = "En resumen, actúo para la sabiduría"
kát,  nūros  as-u       = "Se dice que la luz será"

### 5.6 Foco por posición preverbal

Kalfírvach, siendo SOV, usa la **posición preverbal inmediata** (slot -1 del SV) como el locus canónico de foco. Cualquier constituyente — adverbio, SN, partícula — que se coloque en esa posición recibe **foco estrecho** automáticamente, sin necesidad de marca morfológica adicional. Este mecanismo ya está documentado parcialmente en §3.10.6 (adverbios); aquí se formaliza como principio general de estructura informativa.

**Regla:** un constituyente en posición preverbal recibe foco (interpretación "estrecha" o "contrastiva" según contexto).

```
thel  kár-a        = "La voluntad actúa"        (orden neutral, thel es sujeto)
kár-a  thel        = ✗ (a-gramatical en KFA: thel postverbal no recibe foco aquí)
kár-a              = "Actúa"                    (verbo sin foco, alcance sobre el verbo)
```

**Foco por desplazamiento:**

| Español | Kalfírvach | Glosa | Foco sobre |
|---------|-----------|-------|------------|
| "LA VOLUNTAD actúa" | thel kár-a | thel-VERBO | SN sujeto (foco estrecho) |
| "La voluntad ACTÚA" | thel kár-a-é | thel-VERBO-é (evidencial) | Verbo (foco en la acción) |
| "La voluntad actúa HOY" | ádín thel kár-a | hoy-tóp-VERBO | Adverbio temporal |
| "Sólo la voluntad actúa" | thel ilá kár-a | thel-sólo-VERBO | SN con partícula restrictiva |

**Combinación con partículas de foco:** la partícula de foco (§5.4) refuerza el foco ya dado por la posición:

```
nūros  ét  kár-a      = "La luz PRECISAMENTE actúa"   (foco posicional + partícula)
```

Cuando hay conflicto entre foco posicional y foco partícula, gana la **partícula** (es la marca más fuerte). El foco posicional es la opción por defecto.

**Justificación tipológica:** el foco por desplazamiento preverbal es pan-tipológico en SOV: lo exhiben el japonés (*ga-marking* + posición preverbal), el turco, el tibetano (donde el SN marcado con *kyì* ocupa posición preverbal), y parcialmente el sánscrito (foco contrastivo por movimiento). Kalfírvach toma la versión más simple: cualquier movimiento a slot -1 = foco.

### 5.7 Cleft sentences (seudohendíada e inversa)

Kalfírvach forma oraciones cleft (hendíadas) — equivalentes a "fue X quien/que Y", "lo que hice fue Y" — mediante construcciones **sintácticas** que combinan la cópula `as` con el complementizador `ti` (§4.4.2). No hay morfología nueva; el sistema se sirve de piezas existentes.

#### 5.7.1 Cleft inversa (presentativa, "fue X que...")

Estructura: `[FRASE-NUCLEAR] as-a, [SUJETO] [RELATIVIZADO] kár-a`

```
ma-te    ich-a,  as-a  ti  sa  thel
a-mí-DAT querer-PRES ser-PRES COMP él voluntad
"Lo que quiero es: que él quiera" (cleft con subordinada)

nūros      as-a,  sa-te  pra-yu-a
luz ser-PRES él-DAT preparar-FUT-PRES
"Es la luz, lo que para él prepara" (cleft presentativa)
```

**Patrón:** `[FRASE-FOCO] as-a, [RESTO]`. La frase focalizada va al inicio, seguida de la cópula + pausa + cláusula subordinada completiva con `ti` (cuando hay subordinada explícita).

#### 5.7.2 Seudohendíada (con relativo, "lo que X es Y")

Estructura: `[yas + CLÁUSULA-RELATIVA] [FRASE-NUCLEAR] as-a`

```
yas  ma  kár-a  ekami,  sara  as-a
REL  yo  hacer-PRES uno  todo ser-PRES
"Lo que yo hago es uno, todo es" (todo lo que hago es uno)
```

El relativo se forma con `yas` (raíz sánscrita *ya-* + Avestan *ya-*, 2 lenguas, ya existente en §4.3.1 para otras relativas) + cláusula + predicado con `as`.

#### 5.7.3 Cleft con cópula presentativa (`hál` + cleft)

Combinación del exclamativo presentativo `hál` (§5.4) con estructura cleft para énfasis máximo:

```
hál,  ma  as-a  ti  vach-a!
HE-AHÍ yo ser-PRES COMP hablar-PRES
"¡He aquí, soy yo quien habla!"
```

**Origen de las construcciones:** las estructuras cleft son universales tipológicos; no requieren etimología específica porque son composicionales a partir de partículas y sintaxis ya documentadas. La elección de `as` + `ti` para la cleft inversa se justifica por el patrón sánscrito de cleft con *iti* ("es que...") + el patrón griego de *ἐστίν* + cláusula.

### 5.8 Dislocación a izquierda y derecha

La dislocación coloca un SN en posición periférica (a la izquierda o a la derecha de la oración) y lo reanfora con un **pronombre copia** dentro de la cláusula. Marca información topical o remática con prominencia pragmática.

#### 5.8.1 Dislocación a izquierda (tema prominente)

Estructura: `[SN-DISLOCADO] ho, [PRONOMBRE-CORREFERENTE] [resto de la oración]`

```
thel    ho,  sa   kár-a  ma-te
voluntad TOP él  hacer-PRES a-mí-DAT
"A la voluntad, ella actúa para mí" (tema: la voluntad, comentada: actúa para mí)
```

El SN dislocado va al inicio marcado con `ho` (o `amma` si hay contraste, §5.4.4); el pronombre copia (`sa`, `ta`, `ma`, etc.) ocupa la posición canónica dentro de la cláusula.

#### 5.8.2 Dislocación a derecha (rema prominente)

Estructura: `[oración central], [SN-DISLOCADO]`

```
sa  kár-a,  thel
él  hacer-PRES voluntad
"Él actúa, la voluntad" (rema: la voluntad, contrastada con lo anterior)
```

El SN dislocado va al final, sin partícula de tópico; el contexto o una pausa prosódica lo desambigua. Esta construcción es típica del habla oral y la poesía.

#### 5.8.3 Contraste con tópico y foco

| Construcción | Función | Marca | Pronombre copia |
|--------------|---------|-------|-----------------|
| **Tópico ligero** (§5.1) | tema de comentario | `ho` | opcional, no obligatorio |
| **Tópico fuerte** (§5.4.4) | tema contrastado | `amma` | obligatorio, en mismo SN |
| **Dislocación a izquierda** (§5.8.1) | tema prominente | `ho` + pausa + copia | **obligatorio** (distingue de tópico simple) |
| **Dislocación a derecha** (§5.8.2) | rema prominente | pausa | **obligatorio** (distingue de SN final normal) |
| **Cleft inversa** (§5.7.1) | foco presentativo | cópula `as` + pausa | no aplica (la cópula es la marca) |
| **Foco preverbal** (§5.6) | foco estrecho | posición -1 | no aplica (no hay copia) |

---

## 6. Resumen gramatical BNF

```
;; ============================================================
;; REGLAS DE ORACIÓN
;; ============================================================
<oración>        ::= (<tópico>)? (<adv_temporal>)? <SN> (<SN>)? (<adv>)? <SV> (<interrogativo>)?
                      | <oración> <coord> <oración>
                      | <subord> <oración>
                      | <subord_temp> <oración>
                      | <foco> <oración> | <marc_disc> "," <oración>
                      | <existencial>

<tópico>         ::= <SN> "ho"
<interrogativo>  ::= "ka"

;; ============================================================
;; SINTAXIS NOMINAL
;; ============================================================
<SN>             ::= (<det>)? (<adj>)? <nombre> (<comp>)? (<postpos>)?
                      | <SN_attr_pos>
                      | (<det>)? <indefinido> (<postpos>)?     ;; §3.14: pronombre indefinido como núcleo
                      | <SN_pred_pos>
<SN_attr_pos>    ::= <SN> "-sya" <SN>
<SN_pred_pos>    ::= <SN> "-te" <SN> <cópula>

;; ============================================================
;; CATEGORÍAS LÉXICAS ABIERTAS
;; ============================================================
<adj>            ::= <raíz_adj> (<afijo_deriv>)*
<nombre>         ::= <raíz_nom> (<afijo_deriv>)*
<comp>           ::= <raíz_nom> "-" <raíz_nom>
;; prefijos reflexivos/recíprocos de composición nominal (§3.13.2, §3.13.5):
;; kham-yuj (co-unión), swa-jñāna (auto-conocimiento), atma-yajña (auto-sacrificio)
<comp_pref>      ::= "kham-" | "swa-" | "atma-"
<afijo_deriv>    ::= "-tar" | "-ta" | "-ka" | "-ma" | "-sha" | "-nik"
                      | "-wan" | "-lis" | "su-" | "a-" | "pari-" | "-thu"
;; (lista no exhaustiva — ver §3.6 para afijos derivativos completos)

;; ============================================================
;; CONSTRUCCIÓN EXISTENCIAL (§3.11)
;; ============================================================
<existencial>    ::= (<loc>)? <SN_exist> <cópula>
<loc>            ::= <SN> "-na"
<SN_exist>       ::= <SN>
                      | ("é" | "én" | "ha" | "han")? <nombre>

;; ============================================================
;; SINTAXIS VERBAL
;; ============================================================
<SV>             ::= (<causativo>)? (<temp_mag>)? (<fase_rit>)? (<aspecto>)? (<negación>)? <raíz_verbal>
                      <tiempo> (<reflexivo>)? (<evid>)? (<actitud>)? (<modo_realidad>)?
                      (<hierático>)? (<tiempo_astro>)?

<causativo>      ::= "dha-"
<reflexivo>      ::= "-at"                      ;; §3.13.3: acción del agente sobre sí mismo
<recíproco>      ::= "kham"                     ;; §3.13.5: adverbio preverbal libre (colectivo)
<recíproco_dist> ::= "any-anya"                 ;; §3.13.6: adverbio preverbal libre (distributivo)
<reflexivo_int>  ::= "swa"                      ;; §3.13.2: partícula intensificadora pospuesta al SN
<reflexivo_pos>  ::= "-swa"                     ;; §3.13.2: sufijo adjetival de posesivo reflexivo

<raíz_verbal>    ::= <verbo_cognitivo> | <verbo_volitivo> | <verbo_modal>
                      | <verbo_mov> | <verbo_com> | <verbo_descr>
                      ;; abierto: cualquier raíz léxica verbal
<verbo_cognitivo> ::= "yan-"
<verbo_volitivo>  ::= "ich-"                  ;; querer, desear (§3.12.2)
<verbo_modal>     ::= "dún-" | "dhar-"        ;; poder, deber (§3.12.3-4)
<verbo_mov>       ::= "aya-" | "gach-"
<verbo_com>       ::= "vach-" | "kár-" | "thér-"
<verbo_descr>     ::= "dirish-" | "ops-"

;; ============================================================
;; MORFOLOGÍA VERBAL
;; ============================================================
<tiempo>         ::= "-a" | "-i" | "-u"
<evid>           ::= "-e" | "-on" | "-anu" | "-wah" | "-Ø"
<actitud>        ::= <ritual> | <emocional> | <prometeico>
<ritual>         ::= "-nam" | "-tuf" | "-al" | "-shak" | "-has"
<emocional>      ::= "-nand" | "-shok" | "-bay" | "-krod" | "-prem"
                      | "-vismay" | "-viras" | "-shant"
<prometeico>     ::= "-gar" | "-ék" | "-wíl" | "-azáz" | "-soph" | "-lúx" | "-síg"
<modo_realidad>  ::= "-som" | "-ast" | "-kal" | "-poi"
<aspecto>        ::= "su-" | "a-" | "ta-"
<negación>       ::= "na-"
<cópula>         ::= "as" <tiempo> (<evid>)? (<actitud>)? (<modo_realidad>)?
<imperativo>     ::= <raíz_verbal> "-ro"
<no_finito>      ::= "-an" | "-ant" | "-ta"

<temp_mag>       ::= "chrón-" | "kair-" | "neh-"
<fase_rit>       ::= "pra-" | "kal-" | "tél-" | "sél-"
<tiempo_astro>   ::= "-dín" | "-máh" | "-sól"
<hierático>      ::= "-h"

;; ============================================================
;; PRONOMBRES
;; ============================================================
<pronombre>      ::= "ma" | "ta" | "sa" | "ka" | "man" | "tan" | "san" | "kan"
<pronombre_cort> ::= "ma" | "tum" | "aj" | "man" | "tum-thu" | "aj-thu"
<pronombre_hier> ::= "áz" | "thum" | "hú" | "áz-thu" | "thum-thu" | "hú-thu"

<título>         ::= ("pir" | "báp") <nombre> | <nombre> ("-khán" | "-hék")

;; ============================================================
;; DETERMINANTES Y NÚMEROS
;; ============================================================
<det>            ::= "ha" | "han" | "é" | "én" | "ta" | "ka" | "mu"

;; PRONOMBRES INTERROGATIVOS (§3.8) y PRONOMBRES INDEFINIDOS (§3.14)
<interrog>       ::= "kwa" | "kím"                       ;; ¿quién? / ¿qué?
<part_indef>     ::= "-ka" | "-na" | "-hi" | "-nhi"      ;; §3.14.2: partículas de indefinición
<indefinido>     ::= <interrog> "-" <part_indef>         ;; las 8 palabras: kwa-ka, kwa-na, kwa-hi, kwa-nhi, kím-ka, kím-na, kím-hi, kím-nhi
                  |  "sara"                              ;; §3.14.4: "todo" (colectivo singular)
<indef_num>      ::= "dwi-ka"                            ;; §3.14.4: "ambos, los dos" (numeral + partícula)

<número>         ::= <cardinal> | <ordinal>
<cardinal>       ::= "ekami" | "dwi" | "tiri" | "chatúr" | "páncha"
                      | "shásh" | "sápta" | "áshta" | "navan" | "dashak"
                      | "sháta" | "hasarak"
                      | <cardinal>"-dashak" <cardinal>?
                      | <cardinal>"-sháta" <cardinal>?
<ordinal>        ::= <cardinal>"-th"
<clasificador>   ::= "-wan" | "-pata" | "-thang" | "-sutra" | "-rasi"
                      | "-khanda" | "-dhara" | "-jati"
<SN_numeral>     ::= <cardinal> <clasificador>? <nombre>

;; ============================================================
;; COORDINACIÓN Y SUBORDINACIÓN (§4.3-4.4)
;; ============================================================
<coord>          ::= "cha" | "va" | "tu" | "wá"
<subord>         ::= "yas" | "kar" | "ti" | "ár" | "tát" | "kás"
<subord_temp>    ::= "pári" | "mét" | "tés" | "hát"
<relativa>       ::= "ya" <oración>
<complemento>    ::= <oración> "ti" <oración>
                      | <verbo_cognitivo> "ti" <oración>
<encadenamiento> ::= <oración> (<coord>|<subord>|<subord_temp>) <oración>
                      (<coord>|<subord>|<subord_temp> <oración>)*

;; ============================================================
;; DIÁTESIS (§3.15)
;; ============================================================
<pasiva>         ::= <verbo> "-ya" <TAM>
<impersonal>     ::= ("oy-") <verbo> ("-ya") <TAM>
<agente_pasivo>  ::= <SN> "pra"

;; ============================================================
;; VERBOS DE MOVIMIENTO (§3.16)
;; ============================================================
<mov_desplazamiento> ::= "gach-" | "ay-" | "pat-" | "par-"
<mov_estado>         ::= "shay-" | "thi-"
<movimiento>         ::= <mov_desplazamiento> | <mov_estado>

;; ============================================================
;; DISCURSO INDIRECTO (§3.17)
;; ============================================================
<discurso_directo>   ::= <reportante>? "vach-" ":" <oración>
<discurso_indirecto> ::= ("vach-" | "prash-") <reportante>? "ti" <oración>
<preg_indirecta>     ::= "prash-" <interrogativo> "ti" <oración>
<imper_indirecto>    ::= "vach-" <reportante>? "kás" <subjuntivo>
<reporte>            ::= <discurso_directo> | <discurso_indirecto> | <preg_indirecta> | <imper_indirecto>

;; ============================================================
;; ESTRUCTURA INFORMACIONAL (§5)
;; ============================================================
<foco>           ::= "ét" | "máh" | "lám" | "hál"
<foco_contr>     ::= "tu"                          ;; §5.4.1: foco contrastivo "pero, en cambio"
<foco_restrict>  ::= "ila"                         ;; §5.4.2: foco restrictivo "sólo, excepto"
<foco_exist>     ::= "duk"                         ;; §5.4.3: foco existencial "ciertamente, de hecho"
<tópico_fuerte>  ::= "amma"                        ;; §5.4.4: tópico fuerte "en cuanto a" (vs ho ligero)
<marc_disc>      ::= "hán" | "wáy" | "súm" | "kát"

;; ============================================================
;; POSTPOSICIONES Y ADVERBIOS
;; ============================================================
<postpos>        ::= "-na" | "-te" | "-ra" | "-sya" | "-ka" | "-muk"

<adv>            ::= <adv_temporal> | <adv_locativo> | <adv_modo> | <adv_grado> | <adv_modal>
<adv_temporal>   ::= "nun" | "yawm" | "ams" | "ghat" | "dáim" | "áb-d" | "qábal" | "bákd" | "bákra" | "atáp"
<adv_locativo>   ::= "idá" | "ta-ná" | "ka-ná" | "antár" | "bahí"
<adv_modo>       ::= <adj> "-ka"
<adv_grado>      ::= "tís" | "lav" | "atísh" | "káf"
<adv_modal>      ::= "sháyat"
```

---

### Ejemplos integrados v0.2 + v0.3

**Ejemplo 1 — Iniciación hierática (todos los subsistemas nuevos integrados)**

Demonstración de: hierático (áz, -h), temporalidad mágica (kair-), fase ritual (kal-), actitudinal prometeico (-gar, -ék), performativo (-poi), marcador astrológico (-máh).

```
áz   kair-kal-kár-a-h-nam-gar-ék-poi-máh
yo.HIER kair-invocar-hacer-PRES-HIER-reverencia-orgullo-éxtasis-PERF-lunar

"Yo, el iniciado, invoco en el momento sagrado el acto que realizo con reverencia,
 orgullo justo y éxtasis performativo, bajo esta fase lunar."
```

**Ejemplo 2 — Ciclo eterno con temporalidad neh y emocionales v0.2 + prometeicos**

Demonstración de: neh- (tiempo cíclico), tél- (culminación), actitudinales emocionales v0.2 (-nand, -vismay, -shant) combinados con prometeico (-síg), -djet (estaticidad).

```
man  neh-tél-kár-i-wah-nand-vismay-síg-djet
nos  neh-culminar-hacer-PAS-revelado-alegría-asombro-silencio_gnóstico-estático

"Hemos culminado en el ciclo eterno, fue revelado: con alegría, asombro y silencio
 gnóstico, fijados en la permanencia estática."
```

**Ejemplo 3 — Oración prometeica de propósito (cortés + conjunciones + Capa D)**

Demonstración de: registro cortés (tum), conjunción final (kás), actitudinales prometeicos (-lúx, -wíl), modo hipotético (-kal), y pra- (preparación ritual).

```
ma  pra-kár-a-kás  tum   as-u-lúx-wíl-kal
yo  PREP-hacer-PRES-para tú.CORT ser-FUT-anhelo-determinación-hipotético

"Me preparo en el plano hipotético para que tú seas con anhelo de iluminación
 y determinación inquebrantable."
```

---

## 7. Sistema de escritura

Kalfírvach v0.3 adopta el **alfabeto griego politónico clásico** con letras arcaicas, reemplazando el alfabeto copto de v0.2.

### 7.1 Variante adoptada

Se utiliza el **griego politónico**, pero con un uso pragmático:
- El acento agudo (´) marca el **acento de intensidad** (stress), no el tono tonal del griego antiguo.
- Los espíritus mantienen su función fonológica: el espíritu áspero (῾) marca /h/ inicial; el espíritu suave (᾿) marca oclusión glotal o ausencia de aspiración.

### 7.2 Mapeo fonema → grafema

#### Vocales

| Fonema | Grafía | Nombre | Justificación |
|--------|--------|--------|---------------|
| /a/ | **α** | alfa | Valor clásico. |
| /e/ | **ε** | épsilon | Valor clásico. |
| /i/ | **ι** | iota | Valor clásico. |
| /o/ | **ο** | ómicron | Valor clásico. |
| /u/ | **υ** | ípsilon | En griego clásico era /y/ y el dígrafo *ου* era /u/. Por economía fonotáctica, la υ asume el valor /u/ arcaico pre-jónico, evitando dígrafos redundantes. |

#### Consonantes nucleares (21)

| Fonema | Grafía | Nombre | Justificación filológica |
|--------|--------|--------|--------------------------|
| /p/ | **π** | pi | Valor clásico. |
| /b/ | **β** | beta | Valor clásico de oclusiva bilabial sonora (no el /v/ de la koiné). |
| /t/ | **τ** | tau | Valor clásico. |
| /d/ | **δ** | delta | Valor clásico oclusivo (no fricativo de la koiné). |
| /k/ | **κ** | kappa | Valor clásico. |
| /g/ | **γ** | gamma | Valor oclusivo velar sonoro clásico. |
| /f/ | **φ** | fi | Readaptada del griego koiné tardío/bizantino donde el clásico /pʰ/ aspirado evolucionó a fricativa labiodental sorda /f/. |
| /s/ | **σ / ς** | sigma | Sigma final (ς) se mantiene por estética y demarcación de límites de palabra en mantras. |
| /z/ | **ζ** | zeta | Valor fricativo o africado sonoro clásico. |
| /θ/ | **θ** | theta | Fricativa dental sorda, como en la koiné. |
| /x/ | **χ** | ji | Fricativa velar sorda, evolución natural del /kʰ/ clásico. |
| /m/ | **μ** | mi | Valor clásico. |
| /n/ | **ν** | ni | Valor clásico. |
| /r/ | **ρ** | ro | Valor clásico. |
| /l/ | **λ** | lambda | Valor clásico. |
| /ʃ/ | **ϻ** | san | **Letra arcaica.** Originalmente una sibilante fuerte en dialectos dóricos y arcado-chipriotas. Ideal para la fricativa postalveolar sorda /ʃ/. |
| /tʃ/ | **ϡ** | sampi | **Letra arcaica.** En jónico antiguo denotaba un sonido sibilante africado, posiblemente [ts] o [ss]. Perfecta readaptación histórica para la africada /tʃ/. |
| /w/ | **ϝ** | digamma | **Letra arcaica.** El antiguo fonema /w/ de la época homérica, perdido en el ático clásico. Recuperación filológica obligatoria. |
| /j/ | **ϳ** | yot | **Letra filológica.** Introducida por lingüistas para denotar la semivocal palatal /j/ proto-helénica. |
| /h/ | **῾** / **ͱ** | espíritu áspero / heta | A principio de palabra, el espíritu áspero (῾). En posición intervocálica, se rescata la letra arcaica **heta (ͱ)**, que era el símbolo original para /h/ antes de convertirse en la vocal *eta*. |
| /ɣ/ | **γ̓** | gamma suave | Para la fricativa velar sonora /ɣ/, usamos *gamma* con un espíritu suave sobreescrito (γ̓) para indicar su "suavización" fricativa frente a la oclusiva pura. |

#### Consonantes opcionales (5)

| Fonema | Grafía | Nombre | Justificación filológica |
|--------|--------|--------|--------------------------|
| /q/ | **ϙ** | qoppa | **Letra arcaica.** Originalmente se usaba para /k/ ante vocales posteriores (ο, υ), sonido muy similar a la oclusiva uvular sorda /q/. |
| /v/ | **ϐ** | beta curva | Usamos la variante gráfica cursiva para denotar la fricativa labiodental sonora cuando es fonémicamente distinta de /b/ o /w/. |
| /ð/ | **δ̓** | delta suave | Delta con espíritu suave, indicando lenición a fricativa. |
| /ʔ/ | **᾿** | espíritu suave | El cierre glotal inicial absoluto clásico (psili). |
| /ŋ/ | **γγ / γκ** | gamma nasal | Se escribe como el primer elemento de los clusters nasales-velares griegos (ej. ἄγγελος). |

### 7.3 Vocales largas y registro ritual

Kalfírvach **no** distingue longitud vocálica a nivel fonémico. Como regla general, se usan siempre las vocales cortas (α, ε, ι, ο, υ). Sin embargo, **η (eta)** y **ω (omega)** se permiten *exclusivamente* en **contexto ritual** para términos que etimológicamente las posean (ej. griego *théle* > θήλε, *nús* > νοῦς > νώς), actuando como una **variante estilística visual** que marca la sacralidad de la raíz, aunque la pronunciación siga siendo corta /e/ y /o/.

### 7.4 Uso del acento

A diferencia del griego clásico que usaba un sistema tonal (musical), Kalfírvach es un idioma de **acento de intensidad** dependiente del peso silábico.

**Regla gráfica:** Se utiliza únicamente el **acento agudo (´)** para marcar explícitamente la sílaba tónica. El circunflejo (῀) y el grave (`) quedan reservados para poesía mágica o glosas etimológicas.

### 7.5 Ejemplos de transcripción

**Semillas v0.2:**
| KFA (latín) | Griego politónico |
|-------------|-------------------|
| théle | **θέλε** |
| shákti | **ϻάκτι** |
| ríga | **ρίγα** |
| nūros | **νύρ** |
| shám | **ϻάμ** |
| fír | **φίρ** |
| vísha | **ϐίϻα** (o **ϝίϻα** dependiendo del fonema) |
| dár | **δάρ** |
| áyna | **άϳνα** |
| sáb | **σάβ** |

**Compuestos:**
| KFA (latín) | Griego politónico |
|-------------|-------------------|
| fír-mur | **φίρ-μυρ** |
| sánd-mukh | **σάνδ-μυχ** |
| líkh-rit | **λίχ-ριτ** |
| bánd-nus | **βάνδ-νυσ** (o ritual: **βάνδ-νως**) |
| máya-som | **μάϳα-σομ** |

**5 frases completas:**

1. ¿Qué quieres hacer con el fuego?
   - *Ta kím fír-sya kár-an ich-a?*
   - **Τα κίμ φίρ-σϳα κάρ-αν ιχ-α;**

2. La luz es oscura pero el muro es grande.
   - *Ha nūros khap as-a tu ha mur rík as-a.*
   - **῾α νύρ σάλ ασ-α τυ ῾α μυρ ρίκ ασ-α.**

3. No veo la ilusión porque la verdad está aquí.
   - *Ma ha máya na-dirish-a kar ha satya ida as-a.*
   - **Μα ῾α μάϳα μα-διριϻ-α καρ ῾α σατϳα ιδα ασ-α.**

4. ¡Ven, portador de luz!
   - *Aya-ro, nūros-bhrat!*
   - **Αϳα-ρο, νύρ-βρατ!**

5. Si hablas la palabra, la magia sucede.
   - *Yas ta ha wacha wacha-a, ha heka as-poi.*
   - **ϳας τα ῾α ϝατϳα ϝατχα-α, ῾α ͱεκα ασ-ποι.**

### 7.6 Justificación histórica y mística

La adopción del alfabeto griego clásico, enriquecido con sus glifos arcaicos (san, qoppa, sampi, digamma, heta), devuelve a Kalfírvach a la matriz visual del esoterismo occidental original. El griego fue el vehículo de los *Papyri Graecae Magicae* (PGM) del Egipto helenístico, la teurgia neoplatónica de Jámblico y Proclo, y la geometría sagrada de los pitagóricos. A diferencia del copto (indeleblemente asociado a la liturgia de la iglesia ortodoxa copta), los *charaktêres* griegos aparecen en *lamellae* órficas, papiros de defixión y sellos gnósticos como portadores de "Voces Mágicas" (*voces magicae*) puras, vibraciones pre-dogmáticas.

Reintegrar letras que la estandarización jónica descartó (como el *san* ϻ o el *digamma* ϝ) es un acto profundamente esotérico: significa recuperar fonemas y potencias olvidadas por la historia "oficial". Es una desobediencia gráfica que resuena con la vía prometeica, donde el símbolo recuperado actúa como un sigilo que encauza fuerzas de la Antigüedad tardía al contexto cibernético y ritual del siglo XXI.

---

*Documento generado como parte de Kalfírvach v1.0 — Gramática Completa*
*Todo elemento gramatical se ha justificado con datos de ≥2 lenguas fuente.*
*Junio 2026*

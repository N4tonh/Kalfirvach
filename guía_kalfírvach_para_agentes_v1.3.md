---
title: "Kalfírvach v1.3 — Guía para Agentes"
version: v1.3
date: 2026-06-11
lang: es
status: stable
---

# KALFÍRVACH v1.3 — Guía para Agentes Autónomos

Esta guía captura todo el conocimiento acumulado sobre Kalfírvach que un agente necesita para trabajar con el idioma **sin leer todos los documentos fuente**. Úsala como preflight antes de tocar cualquier archivo del proyecto.

---

## 1. Datos Rápidos

| Propiedad | Valor |
|-----------|-------|
| Nombre nativo | Kalfírvach (escrito καλφιρβαχ en griego politónico) |
| Versión actual | **v1.3** |
| Léxico | ~1.167 entradas en 23 categorías |
| Archivo léxico | `kalfirvach_lexicon_v1.3.json` |
| Glosario | `glosario.md` (1.118 entradas, 3 índices) |
| Gramática | `gramatica_v1.3.md` (4.527 líneas) |
| Fonología | `fonologia_v1.3.md` (1.298 líneas) |
| Diccionario HTML | `diccionario_kalfírvach_v1.3.html` (con escritura griega politónica) |
| Escritura oficial | **Griego politónico** + Transcripción Latina (LA) |
| Lenguas fuente | Griego koiné, Sánscrito tántrico, Egipcio (demótico/antiguo), Persa/Avestan, Tibetano clásico, Árabe esotérico |
| Orden de palabras | **SOV** (Sujeto-Objeto-Verbo) |

---

## 2. Archivos del Proyecto — Mapa Mental

```
Kalfirvach_v1.3/
├── kalfirvach_lexicon_v1.3.json        ← FUENTE DE VERDAD del léxico
├── glosario.md                          ← Reflejo EXACTO del JSON (regenerable vía json2md_lexicon.py)
├── gramatica_v1.3.md                    ← Gramática completa con ejemplos
├── fonologia_v1.3.md                    ← Fonología, fonotáctica, prosodia
├── guía_kalfírvach_para_agentes_v1.3.md ← ESTE DOCUMENTO
├── diccionario_kalfírvach_v1.3.html     ← Diccionario HTML con script griego politónico
├── lexicon_data.js                      ← Datos para el HTML (generado desde JSON)
├── textos_modelo_v1.3.md               ← Textos de ejemplo
├── cuento_sol_y_luna.md                ← Cuento
├── cuento_sol_y_luna_rom.md            ← Cuento (rom.)
├── sephirot_v0.4.md                     ← Árbol sefirótico
├── json2md_lexicon.py                   ← Script para regenerar glosario.md
└── tools/                               ← Herramientas auxiliares
```

**REGLAS DE MODIFICACIÓN:**

1. **`kalfirvach_lexicon_v1.3.json` es la fuente de verdad.** Todo cambio léxico va aquí primero. `glosario.md` se regenera desde el JSON, no se edita a mano.
2. Los ejemplos en `gramatica_v1.3.md` deben reflejar el léxico actual. Si se cambia una palabra en el JSON, revisar la gramática por ejemplos que la usen.
3. Las IPAs en la gramática deben coincidir con las del léxico. Son fuente común de inconsistencias.
4. `lexicon_data.js` se regenera desde el JSON. Si se modifica el JSON, regenerar el JS.

---

## 3. Reglas de Fonología — Las QUE NO SE VIOLAN

### 3.1 Coda Prohibitions (§3.3) — Regla #1

Una consonante en **coda** (final de sílaba) **NUNCA** puede ser:

| Prohibido | Se ensordece a |
|-----------|---------------|
| /b/ | → /p/ |
| /d/ | → /t/ |
| /ɡ/ (g) | → /k/ |
| /z/ | → /s/ |
| /ɣ/ (gh) | → /x/ |
| /v/ | → /p/ (o se pierde) |
| /f/ | → /p/ opcional |
| /θ/ (th) | → /s/ |
| /ð/ (dh) | → /s/ |

**Ejemplo concreto:** `kád` → `kát` (no `kád`), `báb` → `báp`, `ghad` → `ghat`, `síg` → `sík`.

**⚠️ Error ultra común en agentes:** dejar /b/, /d/, /g/, /z/, /ɣ/ en coda. **Siempre ensordecer.**

### 3.2 Regla CC Coda (§10.3) — Regla #2

La coda puede tener **hasta 2 consonantes**, pero solo estas combinaciones:

| Coda | Ejemplo |
|------|---------|
| nasal/líquida + oclusiva sorda | `-nt`, `-mp`, `-rk`, `-lt` |
| fricativa sibilante + oclusiva sorda | `-st`, `-sk`, `-sht`, `-shk` |
| líquida + nasal | `-rm` (raro, dialectal) |

**Prohibido en coda CC:**
- ❌ oclusiva + líquida: `*-kl`, `*-tr`
- ❌ fricativa + nasal: `*-fn`, `*-sn`
- ❌ dos nasales: `*-nm`, `*-mn`
- ❌ tres consonantes: `*-rst`, `*-lft`
- ❌ oclusiva sonora en coda: ver §3.1

**Si un CC cluster viola las reglas, se resílaba con epéntesis de `/a/`:**

```
*kabrd → kábrada (epéntesis)
*kalst → kálsta   (epéntesis)
*ghadn → ghádana  (epéntesis)
```

### 3.3 Vocal Macrón — Regla de Posición

Las vocales largas (ā, ē, ī, ō, ū) SOLO pueden aparecer en una de estas 3 posiciones:

1. **Monosílabo léxico**: `bīj`, `kīr`, `mēr`, `rūt`, `yū`, `thī`
   - ❌ NO en partículas gramaticales (`cha`, `de`, `fu`, `la`, `o`, `ti`, `tu`, `va`, `ya`)
2. **Sílaba acentuada**: `dārchē`, `gīra`, `nāyak`
3. **Sílaba final abierta**: `adarī` (ī final), `tōdā` (ā final), `gashgī`

**Máximo 2 vocales largas por palabra**, y una debe estar en la sílaba acentuada.

### 3.4 Acento

- **Regla general**: penúltima sílaba.
- **Retroceso**: si la penúltima es ligera (CV con vocal breve y sin coda), el acento retrocede a la antepenúltima.
  - `kámita` (CV-CV-CV) → penúltima ligera → acento en antepenúltima.
  - `theláyon` (CV-CVC-CVC) → penúltima pesada → acento en penúltima.
- Sílaba pesada = CVC, CVV, o CV con vocal larga.
- **El acento SIEMPRE se marca con tilde aguda** (´) sobre la vocal tónica en LA. No hay excepciones.

### 3.5 Onsets Prohibidos

- ❌ Oclusiva + nasal: `*/pn-/`, `*/kn-/`, `*/tm-/` (excepto `gn-` en préstamos rituales)
- ❌ Dos oclusivas: `*/pt-/`, `*/kt-/`
- ❌ Líquida + oclusiva en onset: `*/rp-/`, `*/lk-/`
- ❌ Tres oclusivas seguidas

Onsets de 3 consonantes requieren: oclusiva o fricativa sibilante + líquida/glide + glide.

### 3.6 Diptongos Permitidos

Solo 4 son canónicos: `ay` /aj/, `aw` /aw/, `ey` /ej/, `ow` /ow/.

❌ No hay diptongos inversos (`*/ja/`, `*/wa/` en núcleo — se analizan como C+jV, C+wV).
❌ `*/ao/`, `*/oa/`, `*/ae/`, etc. no son diptongos KFA — se silabifican como hiato.

---

## 4. La Escritura Oficial — Griego Politónico

Kalfírvach se escribe con alfabeto **griego politónico** usando letras arcaicas. La Transcripción Latina (LA) es por claridad tipográfica.

### 4.1 Mapa de Transliteración (LA → Griego)

| LA | Griego | Nota |
|----|--------|------|
| a | α | — |
| e | ε | — |
| i | ι | — |
| o | ο | — |
| u | υ | — |
| ā | ᾱ | alfa con macrón |
| ē | η | eta (o ε con macrón en algunos textos) |
| ī | ῑ | iota con macrón |
| ō | ω | omega (u ο con macrón) |
| ū | ῡ | ypsilon con macrón |
| b | β | beta |
| d | δ | delta |
| g | γ | gamma |
| k | κ | kappa |
| l | λ | lambda |
| m | μ | mu |
| n | ν | nu |
| p | π | pi |
| r | ρ | rho |
| s | σ/ς | sigma (ς final) |
| t | τ | tau |
| f | φ | phi |
| th | θ | theta |
| kh | χ | chi |
| gh | γ̓ | gamma + espíritu suave |
| sh | ϻ | **san** (letra arcaica) |
| ch | ϡ | **sampi** (letra arcaica) |
| h | ἁ / ͱ | espíritu áspero o **heta** |
| w | ϝ / ου | **digamma** (letra arcaica) u ου |
| v | ϐ | beta curva (variante de β) |
| y/j | ι / ϳ | semivocal ι o **yot** (letra arcaica) |
| dz | δζ | delta + zeta |
| ny | νϳ | nu + yot |
| ts | τσ | tau + sigma |
| ps | ψ | psi |
| x | ξ | xi |

### 4.2 Reglas de Escritura

- Las vocales acentuadas llevan **tilde aguda** (τόνος): ά έ ή ί ό ύ ώ
- El espíritu áspero (ἁ) se usa para /h/ antes de vocal: `ha` → `ἁ`, `héka` → `ἥκα`
- Las letras arcaicas (ϻ san, ϡ sampi, ϝ digamma, ϳ yot, ͱ heta) representan fonemas que el griego clásico perdió
- Sigma es `ς` al final de palabra, `σ` en cualquier otra posición

### 4.3 Ejemplos

```
kalfirvach  → καλφιρβαχ
sham        → ϻαμ
thel        → θελ
nús         → νυσ
bīj         → βηϳ
vismay      → ϐισμαϳ
pir hú-hék  → πιρ χου-χεκ
```

---

## 5. IPA — Convenciones y Gotchas

### 5.1 Reglas de IPA en el Léxico

| Letra LA | IPA | Nota |
|----------|-----|------|
| a | /a/ | breve |
| ā | /aː/ | larga |
| e | /e/ | breve |
| ē | /eː/ | larga |
| i | /i/ | breve |
| ī | /iː/ | larga |
| o | /o/ | breve |
| ō | /oː/ | larga |
| u | /u/ | breve |
| ū | /uː/ | larga |
| **v** | **/w/** | ⚠️ **v en LA se pronuncia /w/ en IPA** (no /v/) |
| **w** | **/w/** | w también es /w/ |
| y | /j/ | semivocal |
| j | /j/ | equivalente a y |
| sh | /ʃ/ | — |
| ch | /tʃ/ | africada |
| kh | /x/ | fricativa velar |
| gh | /ɣ/ | fricativa velar sonora |
| th | /θ/ | fricativa dental |
| dh | /ð/ | fricativa dental sonora |
| dz | /d͡z/ | africada |
| ny | /nj/ | — |
| ng | /ŋɡ/ | o /ŋ/ como alófono |

### 5.2 El Gran Gotcha: /v/ en LA tiene IPA /w/

**Esta es la fuente DE MÁS errores en el proyecto.**

En el kalfirvach (LA), la letra **`v`** se conserva por razones etimológicas (del sánscrito, persa, árabe), pero su **pronunciación es /w/**:

| KFA | IPA | Significado |
|-----|-----|-------------|
| náva | /ˈna.wa/ (no */ˈna.va/) | 9 |
| va | /wa/ (no */va/) | y (conjunción) |
| vismay | /-ˈwis.maj/ (no */ˈvis.maj/) | asombro (sufijo) |
| viras | /-ˈwi.ras/ (no */ˈvi.ras/) | disgusto (sufijo) |
| dvi | /dwi/ (no */dvi/) | 2 |

**NUNCA** escribir IPA /v/ para palabras con `v` en LA. Siempre /w/. Este error ocurrió en ~29 entradas y se corrigió en la limpieza v1.3.

### 5.3 Otro Gotcha: /q/ en LA tiene IPA /k/

La letra **`q`** aparece solo en palabras de origen árabe/avéstico. Su IPA es **/k/**, no /q/:

| KFA | IPA | Significado |
|-----|-----|-------------|
| qábal | /ˈka.bal/ | antes |
| qalb | /kalb/ | corazón |

### 5.4 Acento en IPA

La tilde en IPA (ˈ) marca el **inicio de la sílaba tónica**, no la vocal tónica misma:

- `/ˈna.wa/` (acento en **na**)
- `/ˈka.bal/` (acento en **ka**)
- `/tʃaˈtur/` (sin tilde en tʃa, acento en **tur**)
- `/ˈdaːr.tʃeː/` (acento en **dār**)

### 5.5 Separación Silábica en IPA

En el léxico, las sílabas se separan con punto (.):

- Correcto: `/ˈa.nja/`, `/ˈka.bal/`
- Incorrecto: `/ˈanja/`, `/ˈkabal/`

No confundir con el guión que se usa para afijos en la gramática.

---

## 6. Gramática — Lo Esencial

### 6.1 Estructura de la Oración

```
Sujeto + Objeto + Verbo (SOV)

Ej:  ma   sham  kár-a
     1SG  sombra hacer-PRES
     "Yo actúo la sombra"
```

### 6.2 Sintagma Verbal Expandido

```
[Tiempo-mágico]-[Fase-ritual]-[Aspecto-]RAÍZ-Tiempo-Evidencial-Actitudinal-ModoRealidad-[Hierático]-[Astrológico]
```

Ejemplo completo:

```
áz   kair-kal-su-kár-a-e-nam-gar-ék-poi-h-máh
yo.HIER  kair-invocar-PFV-hacer-PRES-visual-reverencia-orgullo-éxtasis-PERF-HIER-lunar
```

### 6.3 Evidenciales (obligatorios en contexto ritual)

| Sufijo | Valor | IPA |
|--------|-------|-----|
| -e | Visual | /e/ |
| -on | Onírico | /on/ |
| -anu | Inferido | /a.nu/ |
| -wah | Revelado | /wah/ |
| -Ø | Neutro | — |

### 6.4 Postposiciones (NO preposiciones)

| Sufijo | Valor | IPA |
|--------|-------|-----|
| -na | Locativo ("en") | /na/ |
| -te | Dativo ("a/para") | /te/ |
| -ra | Ablativo ("desde") | /ra/ |
| -sya | Genitivo ("de") | /sja/ |
| -ka | Instrumental ("con") | /ka/ |
| -muk | Directivo ("hacia") | /muk/ |

### 6.5 Afijos Derivativos

| Afijo | Función | IPA |
|-------|---------|-----|
| -tar | Agente | /tar/ |
| -ta | Abstracto | /ta/ |
| -ka | Adjetivizador | /ka/ |
| -ma | Resultado | /ma/ |
| -sha | Lugar | /ʃa/ |
| -nik | Instrumento | /nik/ |
| -wan | Poseedor | /wan/ |
| -lis | Diminutivo | /lis/ |
| su- | Aumentativo | /su/ |
| a- | Privativo | /a/ |
| pari- | Transformación | /pa.ri/ |
| -thu | Colectivo | /θu/ |
| na- | Negación | /na/ |

### 6.6 Apócope Derivativa (§3.5.5 fonología)

**Regla productiva y obligatoria:** la `-e` final de un tema nominal/adjetival se **elide** ante sufijo consonántico:

- `θéle` (voluntad) + `-tár` → `θeltár` (no `θeletár`)
- `θéle` + `-ká` → `θelká`
- `θéle` + `-shá` → `θelshá`

No aplica si el sufijo empieza con vocal, ni a temas en `-a` u `-o`.

### 6.7 Negación

- **Prefijo** `na-` (cambiado de `ma-` en v1.3 para evitar colisión con pronombre 1sg `ma`)
- `na-kár-a` = "no hace", `na-su-kár-a` = "no ha completado"
- Negación de la cópula: `na-as-a` (junto, una palabra)

### 6.8 Tiempos Verbales

| Sufijo | Tiempo |
|--------|--------|
| -a | Presente |
| -i | Pasado |
| -u | Futuro |

### 6.9 Artículos

| Artículo | Valor |
|----------|-------|
| ha | definido singular |
| han | definido plural |
| é | indefinido singular |
| én | indefinido plural |

Los sustantivos NO flexionan por número. El número se expresa en el artículo.

---

## 7. Léxico — Convenciones

### 7.1 Formato del JSON

```json
{
  "kalfirvach_lexicon_v1.3": {
    "categorias": {
      "verbos_basicos": {
        "entradas": [
          {
            "kalfirvach": "kár",              ← palabra en LA (SIN guiones)
            "forma_final": "kár",             ← forma canónica (SIN guiones)
            "ipa": "/kar/",                   ← SIEMPRE con / /, acento con ˈ
            "concepto": "hacer, actuar",      ← definición en español
            "pos": "verb",                    ← categoría gramatical
            "origen": {                       ← etimología
              "lengua": "Sanscrito/Avestan/Griego",
              "raiz_original": "kṛ 'hacer' / kar- 'hacer' / ..."
            }
          }
        ]
      }
    }
  }
}
```

### 7.2 Reglas para el campo `kalfirvach`

1. **SIN guiones.** Las palabras léxicas no llevan guión. Los guiones solo aparecen en la gramática para separar morfemas en ejemplos.
2. **Con acento.** Toda palabra de 2+ sílabas lleva tilde aguda en LA. El acento SIEMPRE se marca.
3. **v etimológica, no fonética.** `v` se conserva aunque suene /w/. No cambiar a `w` en el campo kalfirvach.
4. **q en préstamos árabes.** `q` se conserva en palabras de origen árabe/avéstico aunque suene /k/.
5. **Macrón para vocales largas.** Usar ā, ē, ī, ō, ū (Unicode, precomposed).
6. **Una palabra por entrada.** No combinar variantes. Cada entrada es una palabra individual.

### 7.3 El campo `ipa`

1. **SIEMPRE** entre barras `/ /`.
2. **SIEMPRE** con acento primario `ˈ` antes de la sílaba tónica.
3. **SIEMPRE** con separación silábica por punto `.`.
4. **v → /w/**, nunca /v/.
5. **q → /k/**, nunca /q/.
6. **th → /θ/**, **dh → /ð/**, **sh → /ʃ/**, **ch → /tʃ/**, **kh → /x/**, **gh → /ɣ/**.
7. **Macrón en LA = /ː/ en IPA.** `ā` → /aː/, `ī` → /iː/, `ū` → /uː/, `ē` → /eː/, `ō` → /oː/.
8. **Dígrafos con una letra IPA.** `dz` → /d͡z/ (con ligadura, no /dz/).

### 7.4 Categorías del Léxico (23)

actitudinales, anatomia_y_cuerpo, animales, biologia_y_micologia, comida_y_cocina, conceptos_espaciales_y_calidades, conjunciones_y_particulas, dimensiones_y_adjetivos, emociones_y_estados_afectivos, interjecciones_y_exclamaciones, magia_y_mitologia, medicina_y_salud, naturaleza_y_elementos, numeros, onomastica, personas_y_parentesco, profesiones_y_roles, pronombres_y_deicticos, seres_vivos_plantas, tecnologia, tiempo_domestico, verbos_basicos, vivienda_y_arquitectura

### 7.5 Valores para `pos`

Usar: `verb`, `noun`, `adj`, `adv`, `pronoun`, `conjunction`, `interjection`, `particle`, `suffix`, `prefix`, `numeral`, `aux`, `preposition`, `title`, `classifier`, `determiner`.

---

## 8. Creación de Nuevas Palabras

### 8.1 Algoritmo

1. Determinar el concepto y las lenguas fuente candidatas (griego koiné, sánscrito, árabe, persa, avestan, egipcio, tibetano).
2. Buscar raíces en ≥2 lenguas fuente. **No se aceptan palabras con raíz en 1 sola lengua** (excepto documentación esotérica explícita).
3. Aplicar el **Filtro de Homogeneización**:
   - Reemplazar fonemas ajenos al núcleo (retroflejas → dentales, aspiradas sonoras → simples, faringalizadas → no marcadas, /ħ/ → /h/, /ʕ/ → /ʔ/ o pérdida)
   - Ajustar clusters a la estructura (C)(G)V(C)
   - Aplicar acento penúltimo (retroceso si ligera)
4. Verificar **obligatoriamente**:
   - ✅ Coda sorda (nunca /b,d,g,z,ɣ/ — ensordecer)
   - ✅ CC coda permitida (§3.3 fonología)
   - ✅ Onset permitido (sin oclusiva+nasal, sin dos oclusivas)
   - ✅ Vocal larga en posición válida
   - ✅ Sin guiones en el campo kalfirvach
   - ✅ Acento marcado con tilde aguda
   - ✅ IPA con /w/ para v, /k/ para q

### 8.2 Epéntesis por Defecto

Cuando una palabra viola fonotáctica, la vocal epentética por defecto es **/a/**:

```
kabrd → kábrada (epéntesis de a)
bákr  → bákra   (epéntesis de a)
qábl  → qábal   (epéntesis de a)
fajr  → fajar   (epéntesis de a)
```

### 8.3 Bījas (Palabras de Poder)

Los bījas se generan mediante el **algoritmo fonosemántico** (§11 fonología):

```
Slot: [C_R] V [C_P]?
Donde:
  C_R = consonante raíz (r=fuego, l=agua, s=tierra, y=aire, m=coerción...)
  V   = vocal de plano (a=astral, e=físico, o=divino)
  C_P = sufijo planetario (k=Saturno, t=Marte, d=Mercurio...)
```

Forma ritual obligatoria: `bīj [bīja] wah-nam-poi`

Ejemplos: `raka` (fuego+cronos), `mil` (coerción+agua), `nu` (luna+fuego ascendente).

---

## 9. Escritura Griega Politónica en el Diccionario HTML

El archivo `diccionario_kalfírvach_v1.3.html` carga `lexicon_data.js` (generado desde el JSON) y renderiza cada entrada con:

- **Escritura griega** vía `latinToGreek()` (ϻ, ϡ, θ, χ, γ̓, ϐ, ϝ, etc.)
- **Transcripción latina** entre paréntesis
- **IPA** con la pronunciación real

Si se modifica el JSON, **hay que regenerar `lexicon_data.js`**:

```python
import json
with open('kalfirvach_lexicon_v1.3.json') as f:
    data = json.load(f)
js = "const LEXICON_DATA = \n" + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"
with open('lexicon_data.js', 'w') as f:
    f.write(js)
```

El HTML referencia `LEXICON_DATA["kalfirvach_lexicon_v1.3"].categorias`. Si se cambia la key del JSON, hay que actualizar el HTML.

---

## 10. Errores Conocidos y Gotchas

### 10.1 Errores Históricos (ya corregidos en v1.3)

| Error | Ocurría en | Se corrigió |
|-------|-----------|-------------|
| IPA /v/ en lugar de /w/ para v | 29 entradas del léxico | /v/ → /w/ |
| IPA /q/ en lugar de /k/ para q | 10 entradas del léxico | /q/ → /k/ |
| /b,d,g,z,ɣ/ en coda | 17 palabras del léxico | Ensordecimiento a /p,t,k,s,x/ |
| CC coda ilegal | 59 palabras del léxico | Resílabación con epéntesis /a/ |
| Coda /v/ (vismay, viras) | Sufijos actitudinales | kf sin cambios, IPA /w/ |
| 6 IPAs desactualizadas en gramática | -vismay, -viras, náva, lav, va, tís | /v/→/w/ y /z/→/s/ |
| 9 carry-overs fonológicos en gramática | kád, tíz, báb, ghad, atáf, bákr, qábl, gétig, fajr | Formas coda-legal |
| lexicon_data.js v0.2 obsoleto | JS para HTML | Regenerado desde v1.3 |
| diccionario.html apuntaba a v0.2 | Referencia en HTML | Actualizado a v1.3 |

### 10.2 Gotchas Activos (que los agentes repiten)

1. **"v suena a /v/"** — NO, v en KFA suena /w/. El error más común.
2. **Olvidar el acento** — toda palabra de 2+ sílabas lleva tilde aguda en LA. No hay excepciones.
3. **Poner guiones en palabras léxicas** — los guiones solo se usan en la gramática para separar morfemas. En el JSON y glosario, NO hay guiones.
4. **Crear palabras con 1 sola lengua fuente** — requiere ≥2 lenguas para el núcleo.
5. **Usar /z/ en IPA para "s" sonora** — en KFA "s" es siempre /s/ (sorda). La /z/ es un fonema separado, escrito "z".
6. **Confundir el acento prosódico con el escrito** — el acento prosódico cae en penúltima (o antepenúltima por retroceso). El escrito SIEMPRE se marca con tilde aguda.
7. **No aplicar apócope derivativa** — cuando una raíz termina en -e y se le agrega un sufijo consonántico, la -e se pierde: `θéle + -tár → θeltár`.
8. **Negación ma- vs na-** — desde v1.3, la negación es `na-`. `ma-` ya no se usa (era el pronombre 1sg).

### 10.3 Cuidado con...

- **`bát-zam`** tiene guión en el léxico (entrada preexistente). Es una excepción. No crear nuevas entradas con guión.
- **`dvi`** se escribe con `v` pero suena /dwi/. El onset `dv-` es legal (oclusiva + glide).
- **Los sufijos actitudinales** (`-vismay`, `-viras`) tienen `v` en LA pero /w/ en IPA: `/-ˈwis.maj/`, `/-ˈwi.ras/`.
- **`tís`** significa "muy" y su IPA es `/tis/` (s sorda, no /z/).
- **`gh`** en KFA es /ɣ/ (fricativa velar sonora), NO /g/ + /h/ ni /gh/.
- **Los clasificadores numerales** son obligatorios con números para entidades concretas: `dwi-wan nara` (dos personas), no `dwi nara`.

---

## 11. Cambios Clave de v1.3 Respecto a Versiones Anteriores

| Cambio | Detalle |
|--------|---------|
| Negación `ma-` → `na-` | Para evitar colisión con pronombre 1sg `ma` |
| IPA /v/ → /w/ | Todas las entradas con v ahora tienen IPA /w/ |
| IPA /q/ → /k/ | Todas las entradas con q ahora tienen IPA /k/ |
| Coda devoicing | Obligatorio para todas las entradas |
| CC coda §10.3 | Epéntesis de /a/ donde sea necesario |
| Fonosemántica §11 | Nuevo sistema generativo de bījas |
| Apócope derivativa | Regla nueva §3.5.5 fonología |
| Número de categorías | 23 (homogéneas, sin duplicados) |
| Diccionario HTML | Actualizado a v1.3 con script griego politónico |

---

## 12. Palabras Frecuentes (Recordatorio Rápido)

| KFA | IPA | Significado |
|-----|-----|-------------|
| ma | /ma/ | yo (1sg) |
| ta | /ta/ | tú (2sg) |
| sa | /sa/ | él/ella (3sg animado) |
| ka | /ka/ | esto/aquello (3sg inanimado) |
| as | /as/ | ser/estar (cópula) |
| kár | /kar/ | hacer, actuar |
| núr | /nuːr/ | luz |
| sham | /ʃam/ | sombra |
| thel | /θel/ | voluntad |
| nús | /nuːs/ | conciencia, mente |
| va | /wa/ | y (conjunción) |
| tís | /tis/ | muy |
| ha | /ha/ | el/la (art. def.) |
| é | /e/ | un/una (art. indef.) |
| na- | /na/ | no (prefijo negación) |
| bīj | /biːdʒ/ | semilla, nombre esencial, palabra de poder |
| o | /o/ | oh (partícula vocativa) |
| ya | /ja/ | ¡ah! (interjección admirativa) |
| kím | /kim/ | ¿qué? |
| kwa | /kwa/ | ¿quién? |
| mu | /mu/ | todo |
| dín | /diːn/ | día |
| rátrí | /ˈra.triː/ | noche |

---

*Documento generado como guía de referencia rápida para agentes autónomos que trabajen con Kalfírvach v1.3. Versión: 2026-06-11.*

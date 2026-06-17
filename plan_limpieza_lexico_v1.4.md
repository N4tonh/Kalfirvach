# Plan de Limpieza Léxica — Kalfírvach v1.4

> **Versión del plan:** 1.0
> **Fecha:** 2026-06-16
> **Estado:** pendiente de aprobación
> **Objetivo:** Sanear el léxico de Kalfírvach para cumplir estrictamente con las reglas de creación de palabras (≥2 lenguas fuente, sánscrito <40%, solo lenguas permitidas, etimologías reales y verificables).

---

## 1. Diagnóstico — Problemas detectados

Escaneo automático sobre las 1.280 entradas del `kalfirvach_lexicon_v1.4.json`.

### 1.1 Resumen cuantitativo

| # | Problema | Afectadas | % | Gravedad |
|---|----------|-----------|---|----------|
| A | Sánscrito como única lengua fuente | 48 | 3.8% | 🔴 Alta |
| B | Lenguas fuente no permitidas (Hebreo, Latín, PIE, etc.) | 53 | 4.1% | 🔴 Alta |
| C | Etimologías alucinadas / raíces placeholder / corpus vacío | ~713 | 55.7% | 🔴 Crítica |
| D | Una sola lengua fuente (viola regla de 2+) | 99 | 7.7% | 🟡 Media |
| E | Campos requeridos faltantes (`kalfirvach`, `ipa`, `pos`, `origen`) | 0 | 0% | ✅ Sin problema |
| F | Duplicación `forma_final` / `kalfirvach` | 1.280 | 100% | 🟡 Media |

### 1.2 Lenguas fuente permitidas (guía §1)

1. **Griego Koiné** (Ἑλληνιστί)
2. **Sánscrito Védico** (संस्कृतम्)
3. **Egipcio Demótico** (Demótico egipcio) — lengua fuente primaria egipcia
4. **Copto** (ⲙⲉⲧⲣⲉⲙⲛⲭⲏⲙⲓ) — alternativa cuando el Demótico no esté disponible; ambos conviven como lenguas fuente separadas
5. **Persa Avéstico** (𐬀𐬭𐬆𐬙𐬀𐬐𐬀𐬭𐬆𐬫𐬀)
6. **Tibetano Clásico** (བོད་སྐད།)
7. **Árabe esotérico** (العربية الباطنية)

> **Nota sobre Egipcio:** El Demótico es la fuente primaria. El Copto se añadió como alternativa porque los LLMs no tienen suficiente vocabulario entrenado en Demótico. Cuando no se sepa una raíz en Demótico, proponerla en Copto en su lugar. Ambas lenguas coexisten como fuentes válidas e independientes.

**NO permitidas bajo ningún concepto:** Hebreo, Latín, Arameo, Acadio, Sumerio, PIE (protoindoeuropeo), o cualquier otra no listada arriba.

### 1.3 Ejemplos concretos de cada problema

#### A) Sánscrito como única fuente (48 entradas)

| Concepto | KFA actual | Lengua | Problema |
|----------|-----------|--------|----------|
| vacío/potencial | `shúnya` | Sánscrito | 100% Skt, copia directa, sin blend |
| veneno/sabiduría | `vísha` | Sánscrito tántrico | 100% Skt, solo cambio /ṣ/→/sh/ |
| inconsciente | `anus` | Sánscrito | Sin segunda lengua |
| punto central/esencia | `bíndu` | Sánscrito | Sin segunda lengua |
| iniciación | `díksha` | Sánscrito tántrico | Sin segunda lengua |
| maestro/guía | `gúrú` | Sánscrito | Sin segunda lengua |
| ofrenda | `hóm` | Sánscrito | Sin segunda lengua |

#### B) Lenguas no permitidas (53 entradas)

| Concepto | KFA actual | Lengua (inválida) |
|----------|-----------|-------------------|
| consagrar | `qadesh` | **Hebreo** + **Latín** + Árabe |
| portador | `brat` | **Latín** + **PIE** |
| pezón | `maza` | **Latín** |
| dar | `dun` | **Latín** |
| querer | `ich` | **PIE** |

#### C) Etimologías alucinadas (713 entradas con corpus vacío)

Ejemplo crítico — entrada `wīli` (sacrificar):

```json
{
  "concepto": "sacrificar (ofrendar)",
  "forma_final": "wīli",
  "ipa": "/ˈwiː.li/",
  "origen": {
    "lengua": "Griego Koiné/Egipcio Demótico/Tibetano Clásico",
    "raiz_original": "(raíz Griego) / (raíz Egipcio) / (raíz Tibetano)",
    "corpus": ""
  }
}
```

**Problemas:**
- `raiz_original` contiene texto placeholder — no hay raíces reales
- `corpus` está vacío
- La palabra `wīli` no muestra rastro fonológico de ninguna de las 3 lenguas que reclama
- Es una alucinación completa: el sistema inventó las fuentes sin respaldo real

#### D) Una sola lengua fuente (99 entradas)

| Concepto | KFA actual | Lengua única |
|----------|-----------|--------------|
| talón | `akip` | árabe |
| ceja | `apru` | persa medio |
| codo | `aran` | griego koiné |
| riñón | `kalya` | griego koiné |
| labio | `lap` | griego koiné |

Muchas de estas además tienen corpus vacío y raíces placeholder, acumulando múltiples problemas.

---

## 2. Plan de Mitigación — Fases

### Fase 1: Estandarización estructural (preparación automatizada)

**Esfuerzo:** ⚡ Bajo — scripts automatizados

#### 1.1 Unificar campo canónico del lexema

Actualmente cada entrada tiene dos campos con el mismo valor: `forma_final` y `kalfirvach`.

**Decisión:** `kalfirvach` es el campo canónico. `forma_final` se elimina.

**Acción:** Script que recorre todas las entradas, verifica que `kalfirvach` exista, y elimina `forma_final`.

#### 1.2 Normalizar etiquetas de `origen.lengua`

Las lenguas fuente aparecen con variantes inconsistentes. Unificar a los nombres canónicos:

| Variante actual | Normalizar a |
|----------------|-------------|
| `"Sanscrito"`, `"Sánscrito"`, `"Sánscrito tántrico"` | `"Sánscrito Védico"` |
| `"Avestan"`, `"Av"`, `"Persa"`, `"Persa medio"`, `"MPers."` | `"Persa Avéstico"` |
| `"Egipcio"`, `"Egipcio demótico"` | `"Egipcio Demótico"` |
| `"Copto"` | `"Copto"` (fuente separada; no fusionar con Demótico) |
| `"Griego"`, `"Griego koiné"` | `"Griego Koiné"` |
| `"Tibetano"` | `"Tibetano Clásico"` |
| `"Arabe"`, `"Árabe"` | `"Árabe esotérico"` |

#### 1.3 Eliminar lenguas no permitidas

Las siguientes lenguas NO deben aparecer en ningún `origen.lengua`:

- Hebreo → eliminar
- Latín → eliminar
- Arameo → eliminar
- Acadio → eliminar
- Sumerio → eliminar
- PIE → eliminar

**Regla:** Si después de eliminar las lenguas no permitidas una entrada se queda con 0 o 1 lenguas válidas, pasa automáticamente a la Fase 3 (reformulación).

#### 1.4 Script de normalización completo

Un script `tools/normalizar_lexico_v1.4.py` que ejecute 1.1, 1.2 y 1.3 en un solo pase, y genere:
- El JSON normalizado
- Un reporte de cambios (diff)
- Una lista de entradas que requieren intervención manual (Fase 2 o 3)

---

### Fase 2: Reparación de etimologías existentes

**Esfuerzo:** 🔴 Alto — requiere investigación y edición manual o semiasistida

#### 2.1 Completar `origen.corpus` (~713 entradas)

Cada entrada debe tener un `origen.corpus` que cite las fuentes textuales reales de las que provienen las raíces. Ejemplos de formato válido:

```
"corpus": "Ṛgveda 1.1.2; Avesta Yasna 28.1; PGM 23.5"
```

Si la raíz es una reconstrucción lingüística y no proviene de un texto específico:

```
"corpus": "Reconstrucción desde raíces atestiguadas: Maitrāyaṇī Saṃhitā (Skt), Yasna 34.1 (Av)"
```

#### 2.2 Reemplazar raíces placeholder

Entradas como `wīli` donde `raiz_original` contiene texto template:

```json
"raiz_original": "(raíz Griego) / (raíz Egipcio) / (raíz Tibetano)"
```

Deben ser reescritas con raíces reales en escritura original y transliteración:

```json
"raiz_original": "θύω thýō 'sacrificar' (Gr) / ⲥⲟⲟⲩⲛ sooun 'ofrecer' (Cop) / མཆོད་པ mchod.pa 'ofrendar' (Tib)"
```

#### 2.3 Verificación de coherencia fonológica

Para cada entrada reparada, verificar que la palabra KFA resultante sea un blend fonológico genuino de las lenguas listadas, no una copia directa de una sola fuente.

---

### Fase 3: Reformulación de entradas inválidas

**Esfuerzo:** 🟡 Medio — crear blends nuevos siguiendo el método aprobado

#### 3.1 Entradas con 1 sola lengua fuente (99 entradas)

Para cada una:
1. Identificar el concepto en 2-3 lenguas fuente permitidas adicionales
2. Crear un blend homogéneo (siguiendo el método aprobado en la sesión del 2026-06-15)
3. Aplicar filtro fonológico completo (coda devoicing, CC coda, onset restrictions, acento)
4. Verificar que sánscrito <40% de influencia

**Prioridad:** Las 48 entradas 100% sánscrito son el subconjunto más urgente.

#### 3.2 Entradas con lenguas no permitidas que no se pueden reparar (53 entradas)

Para cada una:
1. Identificar lenguas fuente válidas que cubran el mismo concepto
2. Si el blend actual se puede adaptar reemplazando la raíz inválida → adaptar
3. Si no → reformular desde cero

**Caso especial `qadesh`:** La palabra en sí podría mantenerse si se reemplazan Hebreo y Latín por, ej., Egipcio Copto (ϣⲁϫⲉ) y Árabe esotérico (قدس qds que SÍ es Árabe, no Hebreo — la raíz √QDS existe en ambas lenguas semíticas pero el Árabe está permitido). Habría que verificar que el blend sea genuino.

#### 3.3 Método de creación de palabras (recordatorio)

##### 3.3.1 Principio de homogeneización distribuida

**REGLAS DE ORO — no negociables:**

El resultado final NO puede ser copia o adaptación directa de UNA sola lengua fuente. Debe ser un **blend homogéneo y bien distribuido** donde cada lengua aporte y el resultado sea irreconocible como perteneciente a una sola.

**Ejemplo ilustrativo (lenguas romances, solo como analogía):**

```
Raíces: "amar" (Esp) + "love" (Eng) + "aimer" (Fr)

  ❌ "amar"     → copia directa del español, 0 blend
  ❌ "lovar"    → raíz inglesa + sufijo español, blend pobre
  ✅ "ailer"    /ˈaj.leɾ/ — toma onset /a/ del esp, /l/ del ing, rima /er/ del fr
                  El resultado NO se parece a ninguna de las tres lenguas
```

**Traducido a Kalfírvach con lenguas fuente reales:**

```
Concepto: "sabiduría"
Raíces:  सोफía sophía (Gr) + חכמה ḥokmāh (he — NO, esto es hebreo, no permitido)
         En su lugar: jnꜥ (Dem) + ཤེས་རབ shes.rab (Tib) + sophía (Gr)

  ❌ "sofía"     → copia directa del Griego
  ❌ "shesrab"   → copia directa del Tibetano
  ✅ "sofsheb"   /ˈsof.ʃeb/ — s- del Gr, -sheb del Tib, blend homogéneo
```

**El test definitivo:** Si mostrás la palabra a alguien que conoce las lenguas fuente y puede identificar cuál fue la dominante → está MAL. El blend debe ser tan homogéneo que ninguna lengua reclame la palabra como propia.

##### 3.3.2 Cómo investigar raíces (usando websearch)

El MCP de websearch está disponible y NUNCA se usó. A partir de ahora:

- **Desconocés una raíz en Demótico/Copto** → websearch: "demotic egyptian word for [concepto]" o "coptic ⲃⲉⲕⲉ [concepto]"
- **Desconocés una raíz en Avéstico** → websearch: "avestan word for [concepto]"
- **Desconocés una raíz en Tibetano Clásico** → websearch: "classical tibetan word for [concepto] ཡིག་ཆ"
- **Querés verificar que una raíz existe** → websearch antes de inventar

**No más raíces placeholder.** Si no encontrás la raíz en una lengua después de buscar, no la inventes ni pongas "(raíz X)" — usá otra lengua fuente que sí puedas verificar, o reconocé explícitamente la limitación.

##### 3.3.3 Proceso paso a paso

Para cada nueva palabra:

1. **Investigación:** Buscar el concepto en ≥3 lenguas fuente permitidas usando websearch cuando sea necesario. Registrar las raíces encontradas con su escritura original.

2. **Análisis fonético:** Identificar sonidos compartidos entre las raíces, puntos de convergencia natural.

3. **Blendeo:** Construir la palabra tomando segmentos de diferentes raíces:
   - Onset de una, núcleo de otra, coda de otra
   - O bien fusionar raíces completas con puntos de corte fonológicos naturales
   - El resultado debe ser **irreconocible** como perteneciente a una sola lengua

4. **Filtro fonológico KFA** (obligatorio, contra `fonologia_v1.4.md`):
   - Coda devoicing: /b,d,g,z,ɣ/→/p,t,k,s,x/
   - CC coda permitidas solo: /rk, rt, rn, rm, rp, st, sk, ks, kt, ps, ts, sp, xt, ft/
   - Onsets permitidos: cualquier C simple, C+líquida, C+glide /j w/
   - Sin /dʒ/ (usar /j/ o /d͡z/)
   - Vocal larga solo en sílaba tónica si la estructura lo permite
   - Acento: penúltima si es pesada (CVC/CVV), retrocede a antepenúltima si penúltima es ligera (CV breve)

5. **Verificación de influencia sánscrita:**
   - Si Skt está presente: debe ser ≤1 de ≥3 lenguas totales
   - Si solo hay 2 lenguas: Skt NO puede ser una de ellas (quedaría en 50% → >40%)

6. **Documentación:** Registrar en `origen`:
   - `lengua`: lista de lenguas separadas por /
   - `raiz_original`: raíces en escritura original + transliteración + glosa
   - `corpus`: fuentes textuales específicas, no genéricas

7. **Autocomprobación:** Preguntarse "¿esta palabra se parece demasiado a una sola lengua fuente?" Si la respuesta es sí → replantear el blend.

---

### Fase 4: Validación y cierre

**Esfuerzo:** ⚡ Bajo — script automatizado + revisión muestra

#### 4.1 Script de validación automática

Crear `tools/validar_lexico_v1.4.py` que verifique por entrada:

- [ ] `kalfirvach` presente y no vacío
- [ ] `ipa` presente con acento primario `ˈ`
- [ ] `pos` presente
- [ ] `origen` presente con `lengua`, `raiz_original`, `corpus`
- [ ] `origen.lengua` → 2+ lenguas permitidas
- [ ] `origen.lengua` → sin lenguas prohibidas
- [ ] `origen.raiz_original` → sin texto placeholder `(raíz`
- [ ] `origen.corpus` → no vacío
- [ ] Sánscrito <40%: si 2 lenguas → 1 Skt = 50% ❌; si 3+ lenguas → 1 Skt = ≤33% ✅
- [ ] Si hay `forma_final` → warning (campo obsoleto)

El script debe:
- Fallar (exit code 1) si hay errores críticos
- Emitir warnings para problemas menores
- Generar reporte JSON con el detalle

#### 4.2 Auditoría manual posterior

Después de aprobar el pase automático:
- Revisión manual del 10% de las entradas reformuladas
- Verificar que las palabras suenen naturales y no sean copias literales
- Confirmar que los corpus citados sean verosímiles

#### 4.3 Actualización de archivos derivados

- Regenerar `glosario.md`
- Regenerar `lexicon_data.js`
- Regenerar `diccionario_kalfírvach_v1.4.html`
- Actualizar guía de agente si hubo cambios en las reglas

---

## 3. Estimación de esfuerzo total

| Fase | Tipo | Entradas | Esfuerzo |
|------|------|----------|----------|
| Fase 1 | Automatizado (script) | 1.280 + normalización | ⚡ Bajo (~15 min) |
| Fase 2.1 | Manual + semiasistido | ~713 (corpus vacío) | 🔴 Alto (varias horas) |
| Fase 2.2 | Manual + semiasistido | ~50 (raíces placeholder) | 🟡 Medio |
| Fase 3.1 | Manual creativo | 99 (1 sola lengua) | 🟡 Medio |
| Fase 3.2 | Manual creativo | 48 (100% sánscrito) | 🟡 Medio |
| Fase 3.3 | Manual creativo | 53 (lenguas prohibidas) | 🟡 Medio |
| Fase 4.1 | Automatizado (script) | 1 pase | ⚡ Bajo |
| Fase 4.2 | Manual | ~10% muestra | 🟡 Medio |
| Fase 4.3 | Automatizado | regeneración | ⚡ Bajo |

---

## 4. Dependencias y orden

```
Fase 1 (normalización estructural)
    │
    ▼
Fase 2 (rellenar corpus y raíces de entradas que YA tienen lenguas válidas)
    │
    ▼
Fase 3 (reformular entradas inválidas: 1 lengua, 100% Skt, lenguas prohibidas)
    │
    ▼
Fase 4 (validación + regeneración de derivados)
```

**NOTA:** Fase 2 y Fase 3 pueden ejecutarse en paralelo porque trabajan sobre conjuntos disjuntos de entradas (las de Fase 2 ya tienen lenguas válidas, las de Fase 3 no).

---

## 5. Criterios de aceptación para v1.4

- [ ] 0 entradas con sánscrito como única fuente
- [ ] 0 entradas con lenguas no permitidas
- [ ] 0 entradas con 1 sola lengua fuente
- [ ] 0 entradas con corpus vacío
- [ ] 0 entradas con raíces placeholder
- [ ] 0 campos `forma_final` en el JSON
- [ ] 1.280+ entradas pasan el script de validación sin errores
- [ ] Regenerados glosario, JS y HTML con versión v1.4

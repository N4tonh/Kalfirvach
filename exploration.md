## Exploration: Análisis de cobertura léxico-gramatical de Kalfirvach v1.5

### Estado Actual

El proyecto Kalfirvach v1.3 consta de dos artefactos principales:

1. **`kalfirvach_lexicon_v1.5.json`** — 1670 entradas en 24 categorías semánticas
2. **`gramatica_v1.4.md`** — 248 bloques de código con ejemplos, reglas y morfología

Ambos documentos evolucionaron por separado y **nunca se sincronizaron sistemáticamente**. El léxico se organiza por campos semánticos (verbos, naturaleza, magia, tecnología, etc.), mientras que la gramática expone un sistema morfosintáctico que incluye casos, aspecto, evidenciales y registro hierático.

### Hallazgos Clave

#### 1. Sistema de casos inexistente en el léxico

La gramática usa **6 sufijos casuales** que NO existen en el léxico:

| Sufijo | Función | En léxico |
|--------|---------|-----------|
| `-sya` | Genitivo/posesivo | ✗ |
| `-te` | Dativo/locativo | ✗ |
| `-ra` | Ablativo/origen | ✗ |
| `-na` | Locativo/posición | ✗ |
| `-ka` | Instrumental/medio | ✗ |
| `-lo` | Acusativo/objeto directo | ✗ |
| `-muk` | Direccional/hacia | ✗ |

Ejemplos de la gramática: `nús-te` (a la conciencia), `nūros-sya` (de la luz), `shaktí-ka` (mediante poder), `sól-muk` (hacia la luz).

#### 2. Prefijos de aspecto ausentes

La gramática define 4 prefijos aspectuales que NO están en el léxico:

| Prefijo | Valor | En léxico |
|---------|-------|-----------|
| `su-` | Perfectivo | ✗ |
| `a-` | Imperfectivo | ✗ |
| `ta-` | Habitual | ✗ |
| `na-` | Negación | ✗ |

Ejemplos: `su-kár-a` (ha hecho), `a-kár-a` (está haciendo), `ta-kár-a` (suele hacer), `na-kár-a` (no hace).

#### 3. Sufijos verbales derivacionales ausentes

| Sufijo | Función | En léxico |
|--------|---------|-----------|
| `-an` | Infinitivo | ✗ |
| `-ant` | Participio activo | ✗ |
| `-ta` | Participio pasivo | ✗ (existe `ta` como pronombre) |
| `-ro` | Imperativo | ✗ |

#### 4. Marca de registro hierático incompleta

La gramática usa `-h` como marca de registro hierático. El léxico tiene `-hék` como "autoridad hierática (sello ritual)" — posiblemente relacionado pero no es el mismo morfema.

#### 5. Afijos actitudinales con diferencias ortográficas

| Gramática usa | Léxico tiene | Diferencia |
|---------------|-------------|------------|
| `-gar` (orgullo) | `gar**p**` (sustantivo) | No existe como afijo; raíz distinta |
| `-ék` (éxtasis) | `wajtas` (éxtasis), `-hék` (autoridad hierática) | Significado/distinta raíz |
| `-poi` (performativo) | `-poyit` (performativo) | Variante ortográfica |

#### 6. Sufijo de certeza mágica ausente

El sufijo `-al` ("certeza mágica") se usa en ejemplos como `kár-a-wah-al-poi` y `as-a-wah-al` pero no existe en el léxico.

#### 7. Pronombres y determinantes — SORPRESIVAMENTE BIEN CUBIERTOS

Contrario a lo esperado, la categoría `pronombres_y_deicticos` (60 entradas) cubre casi todo:
- `ma` (yo), `sa` (él/ella), `ha` (art. def. sg), `han` (art. def. pl), `az` (yo hierático)
- `e` (indef. sg), `en` (indef. pl) — sin tilde en el léxico, con tilde `é`/`én` en la gramática
- `ta` (este/tú), `ka` (aquel/ello), `mu` (todo), `para` (más)

#### 8. Palabras léxicas que aparecen en ejemplos gramaticales Y están en el léxico

| Palabra | Significado | Categoría |
|---------|-------------|-----------|
| `nūros` | luz | verbos_sustantivos_primarios |
| `zal` | sombra/acción | verbos_sustantivos_primarios |
| `rík` | grande | cualidades_y_adjetivos |
| `thel` | voluntad | verbos_sustantivos_primarios |
| `khap` | oscura | cualidades_y_adjetivos |
| `kár` | hacer | verbos_sustantivos_primarios |
| `as` | ser/estar | verbos_sustantivos_primarios |
| `kair` | momento ritual | magia_y_mitologia |
| `vach` | hablar | verbos_basicos (292 entradas) |
| `nús` | conciencia | magia_y_mitologia |
| `shaktí` | poder | magia_y_mitologia |
| `kāsmopte` | supremamente | cualidades_y_adjetivos |
| `romālik` | rey | gobierno_politica_derecho |
| `jurmbōn` | crimen | gobierno_politica_derecho |
| `kolnamē` | crimen/delito | gobierno_politica_derecho |

### Áreas Afectadas

- **`kalfirvach_lexicon_v1.5.json`** — Debería incorporar ~20+ entradas faltantes (sufijos casuales, prefigos aspectuales, sufijos derivacionales, afijos actitudinales)
- **`gramatica_v1.4.md`** — Las secciones de morfología nominal y verbal referencian afijos que el léxico no documenta
- **`pronombres_y_deicticos`** (dentro del JSON) — Contiene `e`/`en` sin tilde; la gramática usa `é`/`én` con tilde — inconsistencia ortográfica
- **Cualquier generador/validador futuro** — No podrá validar oraciones completas porque los afijos gramaticales no existen en el léxico

### Enfoques

1. **Sincronización léxico-gramática (recomendado)**
   - Agregar TODOS los afijos faltantes al JSON: sufijos casuales, prefigos aspectuales, sufijos derivacionales, y los afijos actitudinales faltantes/divergentes
   - Estandarizar ortografía: decidir si `e`/`é`, `en`/`én`, `az`/`áz`, `poi`/`poyit`
   - Agregar nota de que estos son afijos gramaticales obligatorios
   - Pros: Léxico completo y autorreferencial; validación posible; claridad para nuevos hablantes
   - Cons: Requiere decisión de diseño sobre ortografía estandarizada
   - Esfuerzo: Medio (~30 min de edición + revisión)

2. **División en dos léxicos**
   - Mantener el léxico semántico actual como está
   - Crear un `grammatical_affixes.json` separado que documente el sistema de casos y aspecto
   - Pros: Separa claramente contenido léxico de gramática; no rompe nada existente
   - Cons: Dos artefactos que referenciar; riesgo de que sigan desincronizados
   - Esfuerzo: Bajo (crear nuevo archivo)

3. **No hacer nada (status quo)**
   - Dejar la gramática como descripción independiente y el léxico como diccionario semántico
   - Pros: Sin trabajo
   - Cons: Inconsistencia permanente; cualquier herramienta que procese KFA no podrá analizar oraciones completas; confusión para aprendices

### Recomendación

**Enfoque 1**, pero como paso preparatorio: primero sincronizar los afijos, agregar una categoría `gramatica_afijos` (o distribuir en `actitudinales` + nueva categoría `casos_y_aspecto`). Estandarizar las variantes ortográficas hacia una forma canónica (propongo la forma que usa la gramática con tilde: `é`, `én`, `áz`, `poi`, `gar`, `ék`, `-h`).

Los afijos casuales merecen su propia categoría porque son morfología obligatoria, no opcional como los actitudinales.

### Riesgos

- **R1**: Decidir una ortografía canónica puede requerir consultar al creador. Las variantes con/sin tilde (`e`/`é`) pueden ser intencionales (diferentes tonos o registros)
- **R2**: Algunos afijos como `-kal` tienen DOS significados: en el léxico es "hipotético", en la gramática es prefijo "invocar". Podría ser una coincidencia ortográfica, no el mismo morfema
- **R3**: El sufijo `-h` (hierático/sacro) y `-hék` (autoridad hierática) podrían ser alomorfos — necesitamos decisión del creador
- **R4**: `gar` (orgullo como afijo) vs `gar**p**` (orgullo como sustantivo) — podría ser que la forma del afijo se derive del sustantivo con pérdida de la `p`

### Listo para Propuesta

Sí. El análisis es completo y los hallazgos están claros. La propuesta debería:
1. Confirmar con el creador las variantes ortográficas preferidas
2. Decidir si `-kal` y `kal-` son el mismo morfema
3. Resolver si `-hék` y `-h` son alomorfos
4. Proceder con la sincronización léxico → añadir ~25 entradas faltantes

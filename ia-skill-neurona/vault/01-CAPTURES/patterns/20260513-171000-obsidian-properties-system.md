---
created: 2026-05-13T17:10:00-05:00
type: patterns
status: processed
source: baseline immersion
source_file: docs/01-CAPTURES/patterns/20260513-172100-baseline-source-consolidated.md
tags:
  - mem
  - obsidian
  - properties
  - baseline
aliases:
  - Obsidian properties system
  - Baseline immersion index
---

# Sistema de Propiedades de Obsidian

## Idea

Las propiedades de Obsidian son metadatos estructurados almacenados como frontmatter YAML al inicio de notas Markdown. Hacen que las notas sean más fáciles de filtrar, consultar, agrupar y reutilizar entre plugins, Bases, plantillas y flujos de agentes.

## Tipos de Propiedad

| Tipo | Forma YAML | Mejor para | Notas |
| --- | --- | --- | --- |
| Text | `status: draft` | Etiquetas cortas, valores únicos, texto libre | Úsalo para valores que deban permanecer atómicos y legibles por humanos. |
| List | `aliases:`<br>`  - Memory skill` | Varios valores, alias, colecciones | Buen valor por defecto cuando un campo puede contener más de un valor. |
| Number | `priority: 2` | Conteos, puntuaciones, precios, valores medibles | Permite orden numérico, comparación y fórmulas. |
| Checkbox | `published: false` | Estado binario | Úsalo cuando el valor sea realmente sí/no. |
| Date | `review_date: 2026-05-13` | Revisiones diarias, vencimientos, fechas de publicación | Prefiere formato de fecha ISO por portabilidad. |
| Date & time | `captured_at: 2026-05-13T16:30:00-05:00` | Marcas temporales, hora de captura, trazas de auditoría | Úsalo cuando importe el orden dentro de un día. |
| Tags | `tags:`<br>`  - memory`<br>`  - obsidian` | Flujos de etiquetas de Obsidian | Obsidian trata la propiedad `tags` de forma especial. |

## Propiedades Predeterminadas

| Propiedad | Tipo | Propósito | Convención local |
| --- | --- | --- | --- |
| `tags` | List / Tags | Etiquetas para búsqueda y grafo en Obsidian | Manténlas amplias y estables; evita sobre-etiquetar. |
| `aliases` | List | Nombres alternativos de la nota | Úsalos para nombres que un humano o agente pueda buscar. |
| `cssclasses` | List | Ganchos de estilo CSS por nota | Evítalas salvo que un estilo visual sea realmente necesario. |

## Propiedades de Obsidian Publish

| Propiedad | Propósito | Convención local |
| --- | --- | --- |
| `publish` | Controla si una nota se selecciona para flujos de publicación | No lo pongas por defecto salvo que publicar sea intencional. |
| `permalink` | Define la ruta URL publicada | Úsalo sólo para notas públicas con URLs estables. |
| `description` | Descripción de vista previa social/enlace | Mantenla concisa y orientada al lector. |
| `image` | Imagen de vista previa social/enlace | Usa una ruta relativa o URL estable. |
| `cover` | Imagen de portada para vistas previas | Úsala cuando la nota tenga un activo visual principal. |

## Propiedad Deprecada

| Propiedad | Reemplazo | Nota |
| --- | --- | --- |
| `tag` | `tags` | Alias deprecado; evítalo en notas nuevas. |

## Borrador de Convención Local para Agentes

| Propiedad | Tipo | Propósito |
| --- | --- | --- |
| `type` | Text | Clase de captura como `observations`, `patterns`, `questions`, `numbers` o `reactions`. |
| `status` | Text | Estado de flujo como `draft`, `processed`, `connected` o `published`. |
| `source` | Text | Origen de la nota: manual, documento base, transcripción, artículo, reunión o salida de herramienta. |
| `source_file` | Text | Ruta relativa al archivo fuente original cuando la nota deriva de material local. |
| `created` | Date & time | Marca temporal de creación para orden determinista. |
| `reviewed` | Date | Última fecha de revisión humana o del agente. |
| `confidence` | Number | La nota contiene claims extraídos o inferidos con fuerza incierta. |

## Propiedades Canónicas para `$mem`

Las propiedades interpretadas como canónicas para el flujo actual son:

- `created`: trazabilidad temporal.
- `type`: clasificación de la nota.
- `status`: estado de flujo.
- `source`: origen corto.
- `tags`: recuperación transversal.
- `aliases`: nombres alternativos.
- `source_file`: procedencia local.
- `reviewed`: revisión posterior.
- `confidence`: fuerza de inferencia cuando aplique.

Estas propiedades son las que deben guiar la curaduría y el indexado de las capturas relacionadas. Las demás propiedades de Obsidian permanecen como referencia útil, pero no son obligatorias para `$mem` salvo que una nota lo necesite.

## Relacionado

- [Patrones Base](../../references/baseline-patterns.md)
- [Fuente consolidada de `docs/baseline`](20260513-172100-baseline-source-consolidated.md)
- [Estructura de la Bóveda](../../references/vault-structure.md)
- [Flujos de Inteligencia](../../references/intelligence-workflows.md)

## Decisión Estructural

Adopta frontmatter YAML para las notas nuevas de `$mem` como capa estructural de metadatos. Mantén el cuerpo Markdown como la capa de razonamiento. Esto preserva la compatibilidad con Obsidian y da a los agentes campos previsibles para búsqueda, filtrado, agrupación y trazas de auditoría.

Las notas históricas con metadata en bullets siguen siendo válidas. Las notas nuevas generadas deben usar primero frontmatter.

## Responsibility Boundary

Las propiedades son riendas, no el jinete. Restringen estructura, recuperación y auditabilidad, pero
no deben tratarse como autoridad sobre el significado.

El LLM toma decisiones sobre:

- Creación y modificación de contenido.
- Qué contexto importa.
- Qué notas deben vincularse, fusionarse, moverse o ignorarse.
- Si las clasificaciones, etiquetas, conexiones o briefs generados son realmente válidos.

El skill define restricciones sobre:

- Propiedades requeridas y formas de valor permitidas.
- Estructura de carpetas y convenciones de nombres.
- Operaciones deterministas sobre archivos.
- Salidas legibles por máquinas y superficies de validación.

## Inmersión Base

Usar la fuente consolidada como inmersión recurrente, no como una sola importación. La capa histórica quedó absorbida y la referencia activa debe quedar indexada, enlazada y curada desde el inbox hasta que pueda prescindirse de duplicaciones futuras.

### Mapa de inmersión

- [Fuente consolidada de `docs/baseline`](20260513-172100-baseline-source-consolidated.md) -> captura de origen curado

### Salidas relacionadas

- [Conexión: pila de skills nativa para agentes](20260513-162007-baseline-agent-native-skill-stack.md)
- [Brief: skills nativos para agentes](20260513-162008-agent-native-skills.md)

## Propiedades Requeridas de `$mem`

| Property | Type | Required for | Rule |
| --- | --- | --- | --- |
| `created` | Date & time | All generated notes | ISO-8601 timestamp with timezone when available. |
| `type` | Text | All generated notes | Use stable classes: `inbox`, `observations`, `reactions`, `patterns`, `questions`, `numbers`, `connection`, `brief`. |
| `status` | Text | All generated notes | Use workflow states: `raw`, `processed`, `draft`, `connected`, `published`. |
| `source` | Text | All generated notes | Short origin label: `manual`, `inbox`, `generated`, `baseline`, `transcript`, `tool`. |
| `tags` | Tags / List | All generated notes | Broad, stable tags only. |

## Propiedades Opcionales de `$mem`

| Property | Type | Use when |
| --- | --- | --- |
| `aliases` | List | A note has likely search names or title variants. |
| `source_file` | Text / List | A note derives from one or more local files. |
| `reviewed` | Date | A human or agent has reviewed the note after creation. |
| `confidence` | Number | The note contains extracted or inferred claims with uncertain strength. |

## Evaluación de Implementación

| Opción | Pros | Contras | Decisión |
| --- | --- | --- | --- |
| Mantener sólo metadata en bullets | Markdown simple, ya usado | Pobre integración con Obsidian, más difícil de consultar para agentes | Retener sólo para notas antiguas. |
| Usar frontmatter YAML para notas nuevas | Propiedades nativas de Obsidian, consultables, portables, legibles por agentes | Requiere cambios en CLI/plantillas y disciplina de migración | Adoptar. |
| Usar frontmatter y metadata en bullets | Redundancia legible por humanos | Riesgo de deriva y estado duplicado | Evitar salvo listas de fuente específicas del cuerpo. |
| Retroportar todas las notas viejas ahora | Bóveda uniforme | Genera churn y cambios accidentales posibles | Posponer; migrar sólo al tocar una nota. |

## Reglas de Trabajo

- Mantén las propiedades pequeñas, atómicas y legibles por máquinas.
- Pon el razonamiento largo en el cuerpo de la nota, no en las propiedades.
- Prefiere claves estables antes que nombres de propiedad de una sola vez.
- Usa referencias de fuente siempre que una nota derive de otro archivo.
- Evita propiedades anidadas; Obsidian no las soporta plenamente en la interfaz de propiedades.

## Preguntas Para Iterar

- ¿`type` debe usar exactamente los nombres de carpeta (`patterns`) o clases semánticas en singular (`pattern`) para conexiones y briefs?
- ¿Qué transiciones de estado debe sugerir la CLI sin dejar de estar sujetas al juicio del LLM?
- ¿Las notas procesadas existentes deben migrarse gradualmente o mediante un comando explícito de migración?
- ¿`confidence` debe reservarse sólo para notas inferidas?

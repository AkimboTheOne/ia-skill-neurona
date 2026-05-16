# Estructura de la bóveda

Usa esta referencia al inicializar una bóveda descendiente, validarla o cambiar convenciones de almacenamiento.

## Carpetas

Inicializa la bóveda del repositorio y las variables temporales del shell con:

```bash
eval "$(scripts/init-repo-vault.sh)"
```

Esto exporta `NEURONA_VAULT` a la bóveda descendiente del repositorio, normalmente `docs/`, sólo para la
sesión actual del shell.

Para pruebas, prefiere una bóveda ignorada y local al repositorio:

```bash
eval "$(scripts/init-test-vault.sh)"
```

Esto exporta `NEURONA_VAULT` a `.tmp/vault`, evitando rutas temporales específicas del host.

- `00-INBOX/`: capturas crudas. No edites para borrar el texto original.
- `01-CAPTURES/observations/`: cosas observadas en el mundo o en el trabajo.
- `01-CAPTURES/reactions/`: respuesta subjetiva, desacuerdo, sorpresa o instinto.
- `01-CAPTURES/patterns/`: principio repetido entre dominios o contextos.
- `01-CAPTURES/questions/`: preguntas abiertas que el usuario realmente quiere responder.
- `01-CAPTURES/numbers/`: métricas, medidas, fechas, conteos o precios concretos.
- `02-CONNECTIONS/`: vínculos sintetizados entre dos o más notas de captura.
- `03-BRIEFS/`: briefs de contenido o pensamiento listos para desarrollar.
- `05-NEURONA/`: memoria operativa del proyecto, manifiestos del skill, configuración y metadatos dirigidos a agentes.

`docs/` es la bóveda concreta del proyecto actual. El mismo skill puede instanciarse en otros proyectos
con semánticas distintas, pero conservando este contrato estructural.

La raíz del repositorio no es una bóveda válida. Si la instancia necesita otra ubicación para la bóveda activa,
debe declararla como descendiente explícito del repo y validarla con el setup o con la configuración de instancia.

Los pendientes de trabajo viven en `docs/00-INBOX/` mientras sigan siendo ideas crudas o propuestas sin implementar.
No crees una carpeta separada para “pendings” salvo que una instancia lo declare explícitamente como variante de contrato.
La condición de pendiente debe declararse con metadata (`status`, `tags`, `aliases` o campos de instancia), no con una carpeta nueva.

`references/` no fija una semántica única. Debe leerse como base agnóstica y luego ajustarse por plantilla
según el caso de uso de la instancia:

- memoria temporal de trabajo;
- memoria documental;
- memoria tipo “cerebro” o conocimiento operativo;
- otros usos que el agente/LLM identifique como compatibles con el contrato.

Si el skill necesita memoria de trabajo temporal para mapas o planes, úsala fuera de la bóveda viva del proyecto,
por ejemplo en `.tmp/`. La personalización de referencia debe ocurrir en la instancia operativa y no en el contrato
central del skill.

## Nombres de nota

Usa nombres con marca de tiempo al inicio:

```text
YYYYMMDD-HHMMSS-short-slug.md
```

Si un archivo ya existe, añade `-2`, `-3` y así sucesivamente.

## Forma de nota de captura

Las notas crudas del inbox son entrada sin modificar, no entendimiento generado. Conserva origen y marca temporal en
frontmatter YAML:

```markdown
---
created: 2026-05-13T16:30:00-05:00
type: inbox
status: raw
source: manual
tags:
  - capture
  - inbox
  - mem
aliases:
  - Capture: short title
---

# Capture: short title

## Raw

Original unmodified text.
```

## Forma de nota procesada

Las notas procesadas deben preservar la captura cruda y añadir una oración afinada:

```markdown
---
created: 2026-05-13T16:35:00-05:00
type: observations
status: processed
source: inbox
source_file: 00-INBOX/example.md
tags:
  - observation
  - capture
  - mem
aliases:
  - Capture: short title
---

# Título afinado

## Afinado

Una oración específica.

## Captura cruda

Texto original de la captura.
```

El campo `## Afinado` puede ser generado o mejorado por el LLM. El campo `## Captura cruda`
debe permanecer fiel a la entrada original para que el razonamiento futuro pueda auditarla.

## Propiedades

Usa frontmatter YAML compatible con Obsidian para las notas generadas.
Las propiedades son riendas estructurales para recuperación y auditoría; no deciden el significado,
la importancia, la ubicación ni los enlaces de una nota. El LLM debe elegir eso según el contexto fuente y
la intención del usuario.

Propiedades requeridas:

- `created`: ISO-8601 date-time.
- `type`: one stable class such as `inbox`, `observations`, `reactions`, `patterns`, `questions`, `numbers`, `connection`, or `brief`.
- `status`: estado del flujo, como `raw`, `processed`, `draft`, `connected` o `published`.
- `source`: short origin label such as `manual`, `inbox`, `generated`, `baseline`, `transcript`, or `tool`.
- `tags`: list of broad tags.

Propiedades opcionales:

- `aliases`: searchable alternative names.
- `source_file`: relative path or list of relative paths when the note derives from local files.
- `reviewed`: ISO date of last review.
- `confidence`: numeric score from 1 to 5 when useful.

Mantén las propiedades pequeñas, atómicas y legibles por máquina. Pon el razonamiento largo, la evidencia y la síntesis en el cuerpo.
Evita propiedades anidadas porque Obsidian no las soporta por completo en la interfaz de propiedades.

## Manifiestos

`05-NEURONA/agent.json` es el manifiesto estructurado del servicio para agentes. `05-NEURONA/llms.txt` es el acompañante ligero y legible. Mantén ambos pequeños y estables.

## Configuración

`05-NEURONA/instance.json` puede usarse para declarar la instancia activa del skill: modo de uso, bóveda del proyecto, memoria temporal y contextos conectados.
No confundir esa configuración con la memoria viva del proyecto.

## Plantillas de referencia

Cuando una instancia requiera criterios distintos, crea o ajusta plantillas de `references/` para ese caso de uso.
La plantilla debe conservar el espíritu modular del skill: guía la adaptación, no la reemplaza.

## Leer más

Si necesitas afinar cómo leer `docs/` como instancia concreta del skill o cómo separar la memoria temporal del skill de la memoria viva del proyecto, consulta:

- [Neurona del Proyecto](../docs/05-NEURONA/neurona.md)
- [Como otro agente llegaría a la misma conclusión](../docs/05-NEURONA/como-otro-agente-llegaria-a-la-misma-conclusion.md)
- [docs/ como bóveda concreta de la instancia actual del skill](../docs/01-CAPTURES/observations/20260514-102952-idea-el-repositorio-docs-de-este-proyecto-es-una-insta.md)

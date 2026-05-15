---
name: mem
description: Skill local de memoria en Markdown, referenciado históricamente como ia-skill-neurona, para capturar ideas, inicializar y mantener una bóveda estilo Obsidian, procesar notas de entrada, encontrar conexiones entre notas y generar resúmenes a partir de una base de conocimiento personal o de proyecto. Úsalo cuando el usuario invoque $mem o cuando Codex necesite construir u operar flujos de captura, almacenamiento o inteligencia sobre una bóveda local con salida de CLI legible por agentes.
---

# Memoria

## Overview

`$mem` es el identificador de activación de este skill. Mantén `ia-skill-neurona` como nombre de referencia histórico y del repositorio cuando documentes rutas, manifiestos o notas de migración.

`references/` debe operar en dos niveles:

- referencias agnósticas por defecto, reutilizables entre instancias;
- plantillas ajustables por caso de uso, para que cada instancia pueda afinar su lectura sin romper el contrato central.

La doctrina de preferencia editorial vive en `references/` y se aplica también en `05-NEURONA`: lenguaje natural para superficies humanas, `snake_case` sólo donde la máquina lo necesita. Si una instancia necesita ajustar tono, densidad o formalidad, debe declararlo explícitamente.

Usa este skill para operar una bóveda local de memoria en Markdown a través de tres capas: capturar entradas crudas, guardarlas en una estructura estable de carpetas y apoyar el trabajo de síntesis sobre las notas almacenadas.

`docs/` es la bóveda concreta del proyecto actual desde la cual se instancia este skill. El mismo contrato puede instanciarse en otros proyectos con contexto y semántica propios. La forma se comparte; el significado se resuelve por proyecto.

Si necesitas profundizar en esa distinción sin cargar el contrato principal, revisa `references/` y el apéndice de "Leer Más" allí vinculado. La regla es que el agente o usuario que instala el skill tome las plantillas como punto de partida, y que el agente/LLM que usa el skill proponga ajustes a las referencias de la instancia cuando el caso de uso lo requiera.

`$mem` también usa una memoria de trabajo temporal en `.tmp/` para mapas, planes y ayudas locales del skill. Esa memoria no es la memoria viva del proyecto y no debe confundirse con la bóveda del usuario ni con la red del proyecto.

Interpreta el skill como riendas: restringe estructura, flujo, contratos de archivos y operaciones deterministas. No posee decisiones sobre contenido, creación, modificación, vinculación, contexto o significado. El LLM que usa el skill posee esas decisiones.

Prefiere la CLI para operaciones deterministas sobre archivos. La CLI no posee la inteligencia generativa: captura, almacena, clasifica heurísticamente y prepara artefactos en Markdown. El LLM que usa el skill posee inferencia, síntesis, afinado, detección de contradicciones, ubicación de notas, vinculación entre notas, selección de contexto y calidad final de escritura.

## Inicio Rápido

Ejecuta la CLI desde esta carpeta del skill:

```bash
eval "$(scripts/init-repo-vault.sh)"
eval "$(scripts/init-test-vault.sh)"
scripts/neurona.sh init --vault /path/to/vault
scripts/neurona.sh capture --vault /path/to/vault --text "raw idea or observation"
scripts/neurona.sh process-inbox --vault /path/to/vault
scripts/neurona.sh connect --vault /path/to/vault --days 7
scripts/neurona.sh brief --vault /path/to/vault --topic "topic name"
scripts/neurona.sh status --vault /path/to/vault
bash scripts/mini-suite.sh
```

`init-repo-vault.sh` inicializa el repositorio actual como bóveda y emite exportaciones temporales:
`NEURONA_VAULT` y `NEURONA_SKILL_DIR`. Después de evaluarlo, los comandos CLI pueden omitir `--vault`.

`init-test-vault.sh` inicializa una bóveda de prueba ignorada y local al repositorio en `.tmp/vault` por defecto.
Úsalo para pruebas portables en lugar de carpetas temporales específicas del host.

`scripts/mini-suite.sh` ejecuta un smoke test funcional completo sobre una bóveda temporal y valida el flujo
`init -> status -> capture -> process-inbox -> connect -> brief`.

Todos los comandos devuelven JSON por stdout y errores por stderr. Trata stdout como el contrato legible por máquinas.

`init` valida o crea la bóveda del proyecto. `config` declara la instancia activa, la memoria temporal del skill y los contextos conectados. Si no se indica otra cosa, el skill asume la bóveda del proyecto actual y una memoria de trabajo separada en `.tmp/`.

## Instalación Local

Usa `scripts/install-local-skill.sh` sólo cuando trabajes en este skill o cuando lo instales como skill local tipo plugin por línea de comandos. Crea un symlink local al repositorio en `.codex/skills/mem`; el uso normal de la bóveda no requiere este paso.

El repositorio todavía puede ser referenciado como `ia-skill-neurona` en rutas y notas de migración.

## Flujo

1. Detecta la ruta de la bóveda desde `--vault`, luego `NEURONA_VAULT`, luego la solicitud del usuario. Si falta, pídela o usa el directorio actual sólo cuando ya contenga `00-INBOX` y `05-NEURONA`.
2. Ejecuta `status` antes de asumir cosas sobre la bóveda.
3. Para bóvedas nuevas, ejecuta primero `init`. Crea la estructura de carpetas y los manifiestos estáticos.
4. Para entradas crudas, ejecuta `capture`. Conserva el texto original intacto.
5. Para mantenimiento del inbox, ejecuta `process-inbox`, luego usa juicio del LLM para revisar clasificaciones débiles, frases afinadas, etiquetas o ubicación de notas.
6. Para trabajo de inteligencia, ejecuta `connect` o `brief` sólo como andamiaje, luego usa razonamiento del LLM para desarrollar insight real, evidencia, contradicciones y prosa.

## Instancias Del Skill

`$mem` puede instanciarse de varias formas. Cada una conserva el mismo contrato estructural, pero resuelve contextos distintos:

- **CLI cross del agente**: el skill actúa como herramienta compartida para operar una bóveda concreta.
- **Plugin en otro repositorio**: el skill se instala como capa de memoria de un proyecto distinto.
- **Incepción en su propio proyecto**: el skill se usa para reformarse a sí mismo y endurecer su modelo.
- **Futuro CLI/MCP server**: el skill expone capacidades complementarias a otro skill o agente.

Cada instancia debe declarar qué contexto usa, qué bóveda gobierna, dónde reside su memoria de trabajo y qué plantilla de referencias adopta. No debe heredar semántica ajena por defecto. La personalización de la instancia vive en sus referencias operativas, no en el contrato central.

## Resolución De Contexto

Cuando el skill opere con varias memorias al mismo tiempo, resuelve en este orden:

1. memoria del usuario;
2. memoria de trabajo temporal del skill (`.tmp/`);
3. memoria del proyecto (`docs/` o la bóveda instanciada);
4. memorias conectadas externas.

No fusiones esos contextos por defecto. Si una fuente no está identificada, trátala como local y conservadora hasta que el LLM decida lo contrario.

## Modelo De Memoria Temporal

`.tmp/` es memoria de trabajo del skill. Se usa para mapas, planes, inicializaciones y ayudas auxiliares que el agente necesita para operar mejor el skill.

`.tmp/` no es:

- memoria del proyecto;
- red viva de conocimiento;
- reemplazo de `05-NEURONA`;
- repositorio de decisiones finales.

Si una idea ya gobierna el proyecto, debe subir a `05`. Si sólo ayuda a planificar o inicializar el skill, puede permanecer en `.tmp/`.

## Frontera de Responsabilidad

Trata `$mem` como un conjunto de riendas estructurales, no como el jinete. El skill puede definir:

- Distribución de carpetas, formas de notas, propiedades requeridas y convenciones de nombres.
- Operaciones deterministas de CLI y salidas legibles por máquinas.
- Criterios de calidad, listas de verificación y referencias que guían al LLM.

El LLM debe decidir:

- Qué contenido merece ser creado, cambiado, fusionado, vinculado o ignorado.
- Qué notas fuente importan para el contexto actual.
- Si una clasificación, etiqueta, conexión o brief generado por la CLI es realmente útil.
- Cómo preservar significado, evidencia, intención del usuario y calidad final de la prosa.

## Modelo De Memoria Del Proyecto

`$mem` no es una bóveda paralela ni un archivo total del conocimiento. Es la memoria operativa del proyecto.

La unidad viva de esa memoria es la neurona: una nota u objeto de conocimiento con propósito claro, propiedades mínimas, trazabilidad y capacidad de conectarse con otras neuronas sin perder su origen.

En este modelo:

- `baseline` es materia prima histórica y fuente madre de patrones, doctrina y evidencia.
- La neurona nace cuando esa materia prima se convierte en una unidad curada, operativa y reutilizable.
- La red vive en `01-CAPTURES`, `02-CONNECTIONS` y `03-BRIEFS`.
- `05-NEURONA` gobierna el modelo: define neurona, contratos, reglas, mapas e índices del proyecto.

El skill define la forma y las riendas. El LLM decide el contenido, el valor y los vínculos.

La traducción útil es funcional, no literal. La evidencia primaria se conserva; la superficie operativa se simplifica para el trabajo diario.

## Contrato de Bóveda

La estructura estándar de la bóveda es:

```text
00-INBOX/
01-CAPTURES/
  observations/
  reactions/
  patterns/
  questions/
  numbers/
02-CONNECTIONS/
03-BRIEFS/
05-NEURONA/
```

Lee `references/vault-structure.md` antes de cambiar nombres de carpetas, nombres de notas o manifiestos.

## Contrato de Propiedades

Usa frontmatter YAML para las notas nuevas para que Obsidian y los agentes puedan consultar metadatos de forma consistente. Las propiedades requeridas para notas generadas son `created`, `type`, `status`, `source` y `tags`. Usa `source_file` cuando una nota derive de otro archivo local. Mantén las propiedades atómicas y coloca el razonamiento en el cuerpo Markdown.

## Reglas de Inteligencia

Trata los archivos generados de conexiones y briefs como borradores. El LLM debe inspeccionar las notas fuente y realizar el razonamiento real antes de presentar conclusiones al usuario.

Una conexión útil debe hacer al menos una de estas cosas:

- Encontrar el mismo principio subyacente en notas distintas.
- Exponer una contradicción o tensión no resuelta.
- Unir tres o más capturas en un patrón.
- Responder una nota de pregunta con evidencia de otra nota.

Para briefs de contenido, conserva exactamente estos campos: `ONE THING`, `PROOF`, `READER TRANSFORMATION`, `THREE HOOKS` y `THREE CLOSERS`.

Lee `references/intelligence-workflows.md` al generar, evaluar o revisar salidas de síntesis.

## Restricciones de Diseño

- Mantén las operaciones primero locales y primero Markdown.
- No requieras Obsidian; la bóveda debe seguir siendo utilizable como archivos planos.
- Mantén los scripts deterministas pequeños y explícitos.
- Prefiere salidas JSON, códigos de salida estables y errores claros.
- Mantén los manifiestos estáticos en `05-NEURONA/` al día cuando cambien las capacidades de la CLI.

Lee `references/baseline-patterns.md` al extender el skill o añadir integraciones.

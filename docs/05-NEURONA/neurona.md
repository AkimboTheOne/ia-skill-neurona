---
type: manifesto
status: active
source: mem operational doctrine
source_file: docs/01-CAPTURES/patterns/20260513-172100-baseline-source-consolidated.md
tags:
  - mem
  - neurona
  - doctrine
  - network
aliases:
  - Neurona
  - Contrato de neurona
  - Neuro-nodo
---

# Neurona del proyecto

## Definición

Una neurona en `$mem` es la unidad viva de la memoria del proyecto: una nota u objeto de conocimiento con propósito claro, propiedades mínimas, trazabilidad y capacidad de conectarse con otras neuronas sin perder su origen.

No es una nota cualquiera. Es una pieza que ya pasó por una decisión editorial.

## Alcance

`05-NEURONA` no guarda todo el conocimiento. Guarda el modelo operativo de la memoria del proyecto: definiciones, contratos, reglas, taxonomías, mapas y decisiones que permitan que la red siga siendo coherente.

Eso lo vuelve compatible con una bóveda viva y con un corpus histórico curado, sin duplicar todo el contenido de `01`, `02` y `03`.

## Instancias y contextos

`$mem` puede instanciarse como CLI cruzado, plugin, incepción o servicio futuro. Cada instancia conserva el mismo contrato estructural, pero resuelve contextos distintos.

La resolución de contexto debe ser explícita:

- memoria del usuario;
- memoria de trabajo temporal del skill (`.tmp/`);
- memoria del proyecto (`docs/` o la bóveda instanciada);
- contextos conectados externos.

No fusionar esos contextos por defecto. Si una fuente no está identificada, tratarla como local y conservadora hasta que el LLM decida lo contrario.

## Referencias agnósticas y plantillas

`references/` debe funcionar por defecto como base agnóstica del skill. Cuando una instancia tenga un caso de uso distinto, la instancia puede derivar o ajustar una plantilla de referencias para su propósito.

El agente o usuario que instala el skill debe tomar esas plantillas como punto de partida. El agente/LLM que usa el skill debe proponer ajustes cuando el caso de uso requiera:

- memoria temporal de trabajo;
- memoria documental;
- memoria tipo “cerebro”;
- o cualquier otro ajuste que preserve la maniobrabilidad sin romper el contrato central.

La personalización pertenece a la instancia, no al núcleo del skill.

## Relación con `baseline`

`baseline` es la materia prima histórica y la fuente madre de patrones, ejemplos y doctrina. La neurona no es `baseline`; la neurona nace cuando esa materia prima se convierte en una unidad curada, operativa y reutilizable dentro de la bóveda.

En esa relación:

- `baseline` aporta origen, tesis y evidencia.
- la neurona aporta forma, propiedades, vínculo y uso futuro.
- la red aporta contexto, navegación y síntesis.

## Relación con `docs/`

`docs/` es la bóveda concreta del proyecto actual desde la cual se instancia `$mem`.
No es el skill en sí. El contrato se comparte, pero la semántica y la red son específicas de la instancia.

## Qué queda dentro y fuera

Dentro:

- contratos de propiedades
- reglas de idioma y curaduría
- definición de neurona
- mapas de red
- decisiones de operación
- manifestos e índices del proyecto

Fuera:

- capturas de trabajo crudas
- síntesis temáticas extensas
- corpus histórico completo
- contenido sustantivo repetido de `01/02/03`

## Qué la hace neurona

- Tiene una intención o función identificable.
- Conserva procedencia mediante `source` y, cuando aplica, `source_file`.
- Puede vivir en una red de relaciones con otras notas.
- Está escrita para que el LLM la pueda usar sin ambigüedad estructural.
- No mezcla autoridad estructural con autoridad semántica.

## Riendas asociadas

- `created`
- `type`
- `status`
- `source`
- `tags`
- `aliases`
- `source_file`
- `reviewed`
- `confidence`

## Regla operativa

El skill define la forma de la neurona.
El LLM decide su contenido, su valor y sus vínculos.

## Configuración

`init` valida o crea la bóveda del proyecto.
`config` declara la instancia activa, la memoria temporal del skill y los contextos conectados.
`docs/` es la bóveda concreta del proyecto actual; `.tmp/` es memoria de trabajo del skill.

## Relacionado

- [Fuente consolidada de `docs/baseline`](../01-CAPTURES/patterns/20260513-172100-baseline-source-consolidated.md)
- [Sistema de Propiedades de Obsidian](../01-CAPTURES/patterns/20260513-171000-obsidian-properties-system.md)
- [Conexión: pila nativa de skills para agentes](../02-CONNECTIONS/20260513-162007-baseline-agent-native-skill-stack.md)
- [Diagrama de arquitectura instanciable](diagrama-arquitectura-instanciable.md)
- [Doctrina de Preferencia Editorial](doctrina-preferencia-editorial.md)
- [Flujo completo de automatización para agentes LLM](flujo-completo-de-automatizacion-para-agentes-llm.md)
- [Criterios para no confundir operación con implementación](criterios-para-no-confundir-operacion-con-implementacion.md)
- [Índice de ayuda operativa para agentes LLM](indice-de-ayuda-operativa-para-agentes-llm.md)
- [Guía operativa canónica para automatizaciones de agentes LLM](guia-operativa-canonica-para-automatizaciones-de-agentes-llm.md)
- [docs/ como bóveda concreta de la instancia actual del skill](../01-CAPTURES/observations/20260514-102952-idea-el-repositorio-docs-de-este-proyecto-es-una-insta.md)
- [El skill puede instanciarse en otros proyectos](../01-CAPTURES/observations/20260514-102952-idea-puede-instanciarse-en-otros-proyectos.md)

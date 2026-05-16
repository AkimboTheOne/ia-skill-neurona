---
created: 2026-05-15T08:22:27-05:00
type: patterns
status: processed
source: inbox
source_file: 00-INBOX/20260515-075031-revision-integral-para-refactorizacion-controlada.md
tags:
  - pattern
  - capture
  - mem
aliases:
  - Arquitectura conceptual, madurez doctrinal y referencias agnósticas
---

# La arquitectura del proyecto ya es sólida, pero necesita endurecer su implementación

## Sharpened

El proyecto ya tiene una arquitectura conceptual sólida, pero su siguiente salto es convertir esa doctrina en una implementación reusable sin drift entre contrato, referencias e instancia.

## Raw Capture

El proyecto ya tiene una arquitectura conceptual sólida: la bóveda `docs/` opera como instancia concreta del skill, `05-NEURONA` gobierna el modelo, `01-CAPTURES` separa tipos de memoria y `02-CONNECTIONS` / `03-BRIEFS` materializan la capa de inteligencia. La propuesta es buena para reutilización porque separa captura, curaduría y síntesis, y porque declara una frontera clara entre riendas estructurales y juicio del LLM.

Los puntos más fuertes son la forma modular por capas, el contrato de propiedades, el uso de manifiestos estáticos para descubrimiento y la orientación CLI-first con salida JSON. Eso facilita instalación, depuración, automatización y eventual instanciación en otros proyectos.

Las tensiones que conviene revisar antes de una refactorización grande son estas:

- La doctrina está más desarrollada que la implementación; la semántica del proyecto vive fuerte en `SKILL.md`, `references/` y `05-NEURONA`, pero la CLI todavía parece un esqueleto funcional corto que puede quedar desalineado con esa doctrina si cambia el contrato.
- Hay duplicación parcial entre `SKILL.md`, `docs/05-NEURONA/neurona.md`, `docs/05-NEURONA/llms.txt`, `docs/05-NEURONA/agent.json` e `instance.json`; la misma idea aparece en varios lugares con distintos niveles de detalle, lo que sugiere necesidad de una fuente de verdad más nítida.
- La instanciación está bien conceptualizada, pero la configuración todavía parece más declarativa que operativa: falta verificar que los modos `project`, `cli-cross`, `plugin`, `inception` y `server` tengan contratos explícitos y tests que prueben el comportamiento real.
- La reutilización modular es prometedora, pero la separación entre contratos estables, referencias de soporte y salidas generadas podría endurecerse para evitar drift entre manifiestos y CLI.

Hipótesis de refactorización controlada:

1. consolidar la fuente normativa por capa;
2. definir un contrato explícito entre skill, vault e instancias;
3. aislar la lógica determinista de la CLI del contenido doctrinal;
4. añadir verificación para que manifiestos, referencias y scripts no diverjan;
5. preservar la compatibilidad de la bóveda mientras se endurece el modelo.

## Raw Capture

La refactorización debería comenzar por inventariar qué archivo es fuente de verdad para cada contrato: estructura de bóveda, propiedades, instancia, manifiestos, comandos y flujos de síntesis. Sin ese mapa, el proyecto corre el riesgo de crecer por repetición doctrinal más que por modularidad real.

## Raw Capture

Casos de uso a madurar:

- usar el skill como bóveda operativa local de un proyecto;
- instalarlo como skill reutilizable en otros repositorios;
- instanciarlo como contrato concreto de proyecto con contexto propio;
- usarlo como capa de captura y síntesis para trabajo continuo de memoria;
- usar sus manifiestos y salidas JSON para que otros agentes puedan descubrir capacidades sin leer el corpus completo;
- usar la CLI como interfaz estable para automatización, pruebas y composición.

Formas de implementación del producto que conviene distinguir:

1. **Skill local en repositorio**
   - El proyecto vive como bóveda y como contrato operativo de memoria.
   - La implementación prioriza archivos, CLI y referencias.

2. **Skill instalado en otro proyecto**
   - El mismo contrato se reutiliza con semántica distinta.
   - Cambia la instancia, no la forma.

3. **Instancia declarada por configuración**
   - `instance.json` y la CLI formalizan modo, contextos y memoria temporal.
   - Útil para ambientes con múltiples agentes o bóvedas.

4. **Servicio futuro o integración MCP**
   - La bóveda permanece como verdad duradera.
   - La interfaz se expone como herramienta descubierta por agentes.

Diagrama de arquitectura propuesto:

```text
                    +---------------------------+
                    |        LLM / Agente       |
                    |  juicio, síntesis, red    |
                    +-------------+-------------+
                                  |
                                  v
                    +---------------------------+
                    |   SKILL / CONTRATO MEM    |
                    |  SKILL.md + references/   |
                    +-------------+-------------+
                                  |
          +-----------------------+------------------------+
          |                        |                       |
          v                        v                       v
+------------------+   +---------------------+   +----------------------+
|    CLI / scripts |   |   Manifiestos       |   |   Instancia          |
| neurona.sh/.py   |   | agent.json, llms.txt|   | instance.json        |
+---------+--------+   +----------+----------+   +----------+-----------+
          |                       |                        |
          +-----------+-----------+------------------------+
                      |
                      v
        +-----------------------------------------------+
        |                DOCS / BÓVEDA                  |
        | 00-INBOX -> 01-CAPTURES -> 02-CONNECTIONS     |
        | -> 03-BRIEFS -> 05-NEURONA                    |
        +---------------------+-------------------------+
                              |
                              v
               +----------------------------------+
               |  REPOSITORIO / OTROS PROYECTOS   |
               | instalación, instanciación, reuse |
               +----------------------------------+
```

La hipótesis de producto que conviene madurar es que `$mem` no es sólo una herramienta para guardar notas: es un sistema de memoria operativa instanciable. Su valor aparece cuando la doctrina, la bóveda y la CLI se alinean como una sola superficie reutilizable para distintos contextos de proyecto.

## Raw Capture

Hay que introducir una regla explícita para `references/`:

- el skill debe traer `references/` agnósticas por defecto, como contrato base reutilizable;
- además debe poder ofrecer plantillas de `references/` ajustadas por caso de uso;
- quien instala u opera el skill debe tomar esas plantillas como referencia inicial, no como destino rígido;
- el agente/LLM que usa el skill debe proponer ajustes a las `references/` de la instancia cuando el caso de uso lo exija;
- eso aplica especialmente cuando hay necesidades distintas de memoria temporal de trabajo, memoria tipo “cerebro” o memoria documental como en este proyecto.

La idea no es hacer el skill rígido ni hiperpersonalizado, sino maniobrable con criterio: modular por defecto, adaptable por instancia, y siempre preservando las riendas estructurales y la madurez doctrinal. La personalización debe ocurrir en la instancia y en sus referencias operativas, no rompiendo el contrato central del skill.

## Idea Origin

La idea origen de esta refactorización es que el proyecto ya alcanzó madurez doctrinal suficiente para definir su forma, pero todavía necesita endurecer su implementación para que esa doctrina sea operable sin drift.

## Rationale

La refactorización no busca más contenido ni más documentación; busca convertir el contrato existente en una arquitectura reutilizable:

- un núcleo estable para el skill;
- referencias agnósticas por defecto;
- plantillas ajustables por caso de uso;
- instancias que declaren su propósito y sus preferencias;
- una CLI que conserve la ejecución determinista;
- y una capa de juicio del LLM que adapte sin reescribir el contrato.

El criterio de éxito es que el sistema pueda instalarse e instanciarse en distintos contextos sin perder la forma común ni ocultar las personalizaciones necesarias.

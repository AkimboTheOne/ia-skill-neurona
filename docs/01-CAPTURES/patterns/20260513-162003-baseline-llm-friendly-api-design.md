---
created: 2026-05-13T16:20:03-05:00
type: patterns
status: processed
source: baseline import
source_file: docs/01-CAPTURES/patterns/20260513-172100-baseline-source-consolidated.md
tags:
  - api-design
  - schemas
  - agent-compatibility
  - llm
aliases:
  - LLM-Friendly API Design
  - diseño de API amigable para LLM
---

# Las APIs amigables para LLM reducen ambigüedad y bucles de corrección

- Date: 2026-05-13T16:20:03-05:00
- Type: patterns
- Tags: api-design, schemas, agent-compatibility
- Fuente consolidada: 20260513-172100-baseline-source-consolidated.md

## Afinado

Las APIs se vuelven más fáciles de usar para agentes cuando nombres, versiones, esquemas, errores y rutas de interacción son lo bastante explícitos como para que el modelo infiera el uso correcto sin prueba y error repetido.

## Cobertura de Fuente

La fuente completa quedó absorbida en [Fuente consolidada de `docs/baseline`](20260513-172100-baseline-source-consolidated.md).

## Expansión para Agente

El patrón trata al LLM como consumidor legítimo de la API. Un humano a menudo puede recuperarse de nombres vagos, versiones implícitas e indirection anidada. Un agente también puede, pero gasta más tokens y falla con mayor frecuencia.

Las buenas APIs dirigidas a agentes hacen visible la versión actual, mantienen las funciones autoexplicativas, validan parámetros temprano y devuelven errores que indiquen la siguiente acción correctiva. Esto no es sólo pulido de documentación; cambia la confiabilidad de ejecución.

## Implicaciones Operativas

- Expón la información de versión donde el modelo la verá.
- Prefiere operaciones directas sobre cadenas profundas de abstracciones auxiliares.
- Usa JSON Schema, OpenAPI o interfaces tipadas cuando sea posible.
- Diseña los mensajes de error como instrucciones de recuperación.
- Instrumenta latencia, fallos y rutas de respaldo.

## Tensiones

Optimizar para agentes puede introducir acoplamiento con el comportamiento actual de los agentes. Mantén la interfaz lo bastante simple para humanos y máquinas, y evita trucos específicos del modelo salvo que estén aislados y documentados.

## Relacionado

- [Diseño de skill primero CLI](20260513-162001-baseline-cli-first-skill-design.md)
- [Herramientas y registro primero para agentes](20260513-162000-baseline-agent-first-tooling-and-logging.md)
- [Manifiestos estáticos de servicio](20260513-162004-baseline-static-service-manifest.md)

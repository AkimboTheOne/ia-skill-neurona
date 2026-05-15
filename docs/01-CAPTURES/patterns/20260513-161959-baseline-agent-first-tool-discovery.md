---
created: 2026-05-13T16:19:59-05:00
type: patterns
status: processed
source: baseline import
source_file: docs/01-CAPTURES/patterns/20260513-172100-baseline-source-consolidated.md
tags:
  - tool-discovery
  - agent-infrastructure
  - mcp
  - discovery
aliases:
  - Agent-First Tool Discovery
  - descubrimiento de herramientas para agentes
---

# El descubrimiento de herramientas primero para agentes vuelve estructurada la búsqueda de herramientas

- Date: 2026-05-13T16:19:59-05:00
- Type: patterns
- Tags: tool-discovery, agent-infrastructure, mcp
- Fuente consolidada: 20260513-172100-baseline-source-consolidated.md

## Afinado

Los agentes necesitan índices de búsqueda estructurados y verificados para herramientas porque los manifiestos estáticos describen un servicio a la vez, pero no resuelven el descubrimiento de capacidades en tiempo de ejecución entre muchos servicios.

## Cobertura de Fuente

La fuente completa quedó absorbida en [Fuente consolidada de `docs/baseline`](20260513-172100-baseline-source-consolidated.md).

## Expansión para Agente

Este patrón define la capa faltante entre catálogos locales de herramientas e integración autónoma: un índice de búsqueda legible por agentes. El índice debería devolver metadatos estructurados como nombre del servicio, etiquetas de capacidad, protocolo, URL base, modelo de autenticación, disponibilidad de esquema, tiempo de actividad, latencia y estado de verificación.

El cambio importante es clasificar por utilidad para el agente y no por SEO humano. Un índice útil debe responder: "¿Puede un agente usar esta capacidad de forma segura y directa ahora?" y no "¿Es popular esta página?"

## Implicaciones Operativas

- Trata el descubrimiento como una herramienta con su propio protocolo, no como una página de documentación.
- Prefiere capacidades verificadas sobre texto de marketing autodeclarado.
- Expón resultados de búsqueda como JSON o salidas MCP que puedan filtrarse y puntuarse.
- Mantén descubrimiento y uso nativos al protocolo para que la herramienta seleccionada pueda invocarse sin una segunda capa de traducción.

## Tensiones

Este patrón depende de la confianza en el operador del índice. Si la puntuación es opaca, está desactualizada o sesgada, el agente hereda ese fallo. Las herramientas privadas también necesitan índices locales o específicos de la organización porque el descubrimiento público no verá capacidades internas.

## Relacionado

- [Manifiestos estáticos de servicio](20260513-162004-baseline-static-service-manifest.md)
- [Herramientas y registro primero para agentes](20260513-162000-baseline-agent-first-tooling-and-logging.md)
- [Diseño de API amigable para LLM](20260513-162003-baseline-llm-friendly-api-design.md)

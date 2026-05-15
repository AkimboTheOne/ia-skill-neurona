---
created: 2026-05-13T16:20:04-05:00
type: patterns
status: processed
source: baseline import
source_file: docs/01-CAPTURES/patterns/20260513-172100-baseline-source-consolidated.md
tags:
  - manifests
  - service-discovery
  - llms-txt
  - agent-infrastructure
aliases:
  - Static Service Manifest for Agents
  - manifiesto estático de servicio para agentes
---

# Los manifiestos estáticos de servicio dan a los agentes un mapa inicial barato

- Date: 2026-05-13T16:20:04-05:00
- Type: patterns
- Tags: manifests, service-discovery, llms-txt
- Fuente consolidada: 20260513-172100-baseline-source-consolidated.md

## Afinado

Los agentes pueden planear el uso de herramientas con más confiabilidad cuando los servicios publican manifiestos estáticos pequeños como `llms.txt` y `agent.json` que describen capacidades, autenticación, endpoints y restricciones.

## Cobertura de Fuente

La fuente completa quedó absorbida en [Fuente consolidada de `docs/baseline`](20260513-172100-baseline-source-consolidated.md).

## Expansión para Agente

Este patrón es el equivalente de un mapa a la entrada para servicios locales. El agente no debería gastar contexto en documentación completa ni descubrir capacidades por prueba y error. Un manifiesto corto en lenguaje natural más un catálogo JSON estructurado dan suficiente orientación para decidir si hace falta descubrimiento más profundo de esquemas.

Para `$mem`, `docs/05-NEURONA/agent.json` y `docs/05-NEURONA/llms.txt` son la expresión local de este patrón. Deben seguir siendo pequeños y estables, y deben cambiar cuando cambien las capacidades de la CLI.

## Implicaciones Operativas

- Mantén `llms.txt` conciso y legible.
- Mantén `agent.json` determinista y parecido a un esquema.
- Incluye campos de versión para que los agentes detecten drift.
- Lista sólo comandos o endpoints estables.
- Trata los manifiestos como parte de la higiene de release, no como documentación opcional.

## Tensiones

Los manifiestos estáticos derivan si no se actualizan junto con la implementación. Funcionan mejor como mapa inicial, y luego se emparejan con validación ejecutable, esquemas o descubrimiento MCP para detalles exactos de invocación.

## Relacionado

- [Descubrimiento de herramientas primero para agentes](20260513-161959-baseline-agent-first-tool-discovery.md)
- [Diseño de API amigable para LLM](20260513-162003-baseline-llm-friendly-api-design.md)
- [Sistema de Propiedades de Obsidian](20260513-171000-obsidian-properties-system.md)

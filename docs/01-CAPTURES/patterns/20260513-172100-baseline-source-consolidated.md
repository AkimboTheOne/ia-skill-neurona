---
created: 2026-05-13T17:21:00-05:00
type: source
status: processed
source: baseline consolidated import
source_file: docs/baseline
tags:
  - baseline
  - source
  - mem
  - obsidian
  - agent-patterns
aliases:
  - Fuente consolidada de baseline
  - Baseline consolidated source
  - Ingesta fuente de baseline
---

# Fuente consolidada de `docs/baseline`

## Propósito

Este archivo reúne en una sola nota la sustancia útil de `docs/baseline`, traducida al español como referencia operativa para `$mem`. La fuente original queda absorbida como trasfondo histórico; esta nota existe para que la curaduría viva ocurra en un solo lugar y no se pierda el hilo de trabajo.

## Síntesis Integrada

El corpus base converge en una sola tesis: los agentes funcionan mejor cuando la infraestructura está diseñada para ellos desde el inicio. Eso implica descubrimiento explícito, herramientas observables, diseño de CLI primero, APIs legibles por LLM, manifiestos estáticos, memoria local curada y una capa de propiedades que permita filtrar, auditar y vincular sin ambigüedad.

La arquitectura que emerge no separa memoria, herramientas y documentación. Las trata como capas cooperantes de un mismo sistema:

- La capa de descubrimiento hace visibles los activos correctos.
- La capa de ejecución permite invocación y depuración predecibles.
- La capa de memoria conserva contexto útil sin convertirlo en ruido.
- La capa de curaduría decide qué enlazar, qué resumir y qué conservar como referencia.

## Capturas Relacionadas

Cada documento base ya fue convertido en una captura procesada. Esta nota las consolida como un solo origen curado:

- [Descubrimiento de herramientas primero para agentes](./20260513-161959-baseline-agent-first-tool-discovery.md)
- [Herramientas y registro primero para agentes](./20260513-162000-baseline-agent-first-tooling-and-logging.md)
- [Diseño de skill primero CLI](./20260513-162001-baseline-cli-first-skill-design.md)
- [Mejora de interfaz de herramientas MCP en modo código](./20260513-162002-baseline-code-mode-mcp-interface.md)
- [Diseño de API amigable para LLM](./20260513-162003-baseline-llm-friendly-api-design.md)
- [Manifiesto estático de servicio para agentes](./20260513-162004-baseline-static-service-manifest.md)
- [Arquitectura de skill de memoria](./20260513-162005-baseline-memory-skill-architecture.md)
- [Índice de patrones de línea base](./20260513-162006-baseline-pattern-index.md)

## Traducción Operativa

La traducción no es literal. Es funcional. El objetivo es preservar la intención arquitectónica y el valor de decisión para `$mem`:

- `CLI-first` pasa a ser una prioridad de operación local.
- `LLM-friendly` pasa a ser una prioridad de forma de datos y contratos.
- `agent-first discovery` pasa a ser visibilidad de herramientas y manifiestos.
- `tooling and logging` pasa a ser trazabilidad y depuración.
- `static service manifest` pasa a ser un contrato de localización y composición.
- `memory skill architecture` pasa a ser memoria utilizable, no archivo pasivo.
- `pattern index` pasa a ser doctrina de diseño, no lista suelta.

## Propiedades Interpretadas

La capa de propiedades que se consolidó en esta inmersión queda como criterio práctico para las notas nuevas:

- `created`
- `type`
- `status`
- `source`
- `tags`
- `aliases`
- `source_file`
- `reviewed`
- `confidence`

Estas propiedades no mandan sobre el significado. Ordenan la recuperación, la auditoría y la curaduría.

## Relación Con El Resto De Objetos

Esta fuente consolidada se relaciona con:

- [Sistema de Propiedades de Obsidian](./20260513-171000-obsidian-properties-system.md)
- [Conexión: pila nativa de skills para agentes](../../02-CONNECTIONS/20260513-162007-baseline-agent-native-skill-stack.md)
- [Brief: skills nativos para agentes](../../03-BRIEFS/20260513-162008-agent-native-skills.md)

## Curaduría Siguiente

Desde aquí, `docs/baseline` deja de ser el punto de trabajo principal y puede prescindirse como superficie activa. La nota consolidada en español pasa a ser la superficie de consulta, enriquecimiento y enlace.

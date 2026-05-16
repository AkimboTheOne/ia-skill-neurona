---
created: 2026-05-13T16:20:00-05:00
type: patterns
status: processed
source: baseline import
source_file: docs/01-CAPTURES/patterns/20260513-172100-baseline-source-consolidated.md
tags:
  - observability
  - structured-output
  - agent-tools
  - logging
aliases:
  - Agent-First Tooling and Logging
  - herramientas y registro para agentes
---

# Las herramientas primero para agentes vuelven legible por máquinas el estado por defecto

- Date: 2026-05-13T16:20:00-05:00
- Type: patterns
- Tags: observability, structured-output, agent-tools
- Fuente consolidada: 20260513-172100-baseline-source-consolidated.md

## Afinado

Los entornos de desarrollo se vuelven más confiables para agentes cuando los registros, las salidas de CLI y las respuestas de herramientas son estructuradas, unificadas, verbosas y diseñadas para parseo por máquinas.

## Cobertura de Fuente

La fuente completa quedó absorbida en [Fuente consolidada de `docs/baseline`](20260513-172100-baseline-source-consolidated.md).

## Expansión para Agente

La idea central es que el trabajo del agente falla menos cuando el entorno deja de optimizar sólo para lectura humana. Las personas se benefician de resúmenes compactos y color; los agentes se benefician de esquemas estables, estado explícito, códigos de salida previsibles y trazas completas.

Este patrón apoya directamente a `$mem`: la CLI devuelve JSON, los errores van a stderr y la bóveda almacena manifiestos legibles por máquinas. El mismo principio debe aplicarse a cada script futuro en este repositorio.

## Implicaciones Operativas

- Emite JSON o JSONL para la salida de comandos dirigida a agentes.
- Mantén una sola corriente de registro autoritativa al depurar flujos con múltiples servicios.
- Incluye suficiente contexto en los errores para que un agente se autocorrija.
- Usa esquemas para formas de salida repetidas.
- Conserva la usabilidad humana como vista secundaria, no como contrato primario.

## Tensiones

La salida legible por máquinas puede sentirse ruidosa para humanos. El compromiso práctico es una salida de doble modo: estructurada por defecto para no-TTY o `--json` explícito, y una representación humana concisa para sesiones interactivas de terminal.

## Relacionado

- [Diseño de skill primero CLI](20260513-162001-baseline-cli-first-skill-design.md)
- [Diseño de API amigable para LLM](20260513-162003-baseline-llm-friendly-api-design.md)
- [Sistema de Propiedades de Obsidian](20260513-171000-obsidian-properties-system.md)

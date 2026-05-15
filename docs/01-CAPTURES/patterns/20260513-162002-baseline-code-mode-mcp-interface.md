---
created: 2026-05-13T16:20:02-05:00
type: patterns
status: processed
source: baseline import
source_file: docs/01-CAPTURES/patterns/20260513-172100-baseline-source-consolidated.md
tags:
  - mcp
  - code-mode
  - token-efficiency
  - orchestration
aliases:
  - Code Mode MCP Tool Interface Improvement Pattern
  - modo código MCP
---

# El modo código saca del contexto del modelo el trabajo MCP de múltiples pasos

- Date: 2026-05-13T16:20:02-05:00
- Type: patterns
- Tags: mcp, code-mode, token-efficiency
- Fuente consolidada: 20260513-172100-baseline-source-consolidated.md

## Afinado

Los LLM suelen ser más eficientes escribiendo código que orquesta herramientas que llamando directamente muchas herramientas MCP a través de múltiples turnos de chat.

## Cobertura de Fuente

La fuente completa quedó absorbida en [Fuente consolidada de `docs/baseline`](20260513-172100-baseline-source-consolidated.md).

## Expansión para Agente

El modo código separa la autoridad persistente de la orquestación efímera. Los servidores MCP conservan credenciales, políticas, cuotas y acceso externo; el código generado maneja bucles, joins, transformaciones, reintentos y síntesis dentro de un sandbox. Sólo el resultado final condensado necesita volver al modelo.

La prueba decisiva es si el flujo puede planearse antes de ejecutarse. Si los pasos son conocidos y el desafío principal es fan-out o transformación, el modo código puede ahorrar tokens y latencia. Si la inteligencia debe insertarse entre cada paso, la interacción directa del agente sigue siendo mejor.

## Implicaciones Operativas

- Prefiere ejecución de código para operaciones masivas sobre bucles repetidos de llamadas a herramientas.
- Genera interfaces tipadas a partir de esquemas de herramientas para que el código tenga un contrato estable.
- Mantén las credenciales en bindings o servidores MCP, nunca en el código generado.
- Devuelve salidas condensadas, no cada payload JSON intermedio.
- Añade checkpoints para fallos parciales en flujos de larga duración.

## Tensiones

El modo código puede ocultar razonamiento intermedio al modelo si el resultado final queda demasiado comprimido. La capa de ejecución debe devolver suficiente traza para auditar decisiones importantes sin volcar el flujo completo en contexto.

## Relacionado

- [Herramientas y registro primero para agentes](20260513-162000-baseline-agent-first-tooling-and-logging.md)
- [Diseño de API amigable para LLM](20260513-162003-baseline-llm-friendly-api-design.md)
- [Diseño de skill primero CLI](20260513-162001-baseline-cli-first-skill-design.md)

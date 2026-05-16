---
created: 2026-05-16T00:00:00-05:00
type: manifesto
status: active
source: mem operational doctrine
source_file:
  - references/operational-loop-templates.md
tags:
  - mem
  - guidance
  - loop
  - llm
aliases:
  - Loop operativo para agentes LLM
  - Protocolo preparar operar cerrar
---

# Loop operativo para agentes LLM

## Propósito

Esta neurona fija cómo un agente debe conversar con la bóveda a través de `$mem` cuando no puede asumir contexto interno.

El skill actúa como caja negra estructural: entrega comandos, plantillas, índices y rutas. El agente decide significado, selección de contexto, relaciones y calidad de la síntesis.

## Loop

El protocolo mínimo es:

`preparar -> operar -> cerrar`

## Preparar

Antes de escribir, el agente debe:

- ejecutar `status` o confirmar que la bóveda está inicializada;
- usar `ask` o lectura directa cuando necesite contexto previo;
- pedir la plantilla de fase con `templates show --phase <fase>`;
- declarar frontera de escritura y fuentes consultadas.

## Operar

Durante la operación, el agente debe usar la plantilla como andamio, no como sustituto de juicio.

Para conversaciones, la forma esperada es síntesis densa: contexto operativo, resumen sustantivo, decisiones, evidencia, relaciones sugeridas, pendientes, próximos pasos, riesgos y transcripción relevante.

## Cerrar

Al cerrar, el agente debe dejar handoff explícito:

- resultado;
- evidencia o notas fuente;
- relaciones creadas o sugeridas;
- pendientes;
- próxima acción;
- criterio de elevación o no elevación a `05-NEURONA`.

## Regla

La CLI puede advertir secciones faltantes, pero no debe fingir inteligencia semántica. Si falta contexto, el agente debe recuperarlo o declararlo como pendiente.

Los índices y relaciones son estrictos: una conversación o síntesis sin `conversation_id`, fuentes, pendientes o relaciones sugeridas pierde capacidad de continuidad.

## Relacionado

- [Índice de ayuda operativa para agentes LLM](indice-de-ayuda-operativa-para-agentes-llm.md)
- [Flujo completo de automatización para agentes LLM](flujo-completo-de-automatizacion-para-agentes-llm.md)
- [Cierre del loop y comportamiento esperado al cerrar](cierre-del-loop-y-comportamiento-esperado-al-cerrar.md)
- [Gobernanza multi-instancia y bóveda descendiente](gobernanza-multi-instancia-y-boveda-descendiente.md)

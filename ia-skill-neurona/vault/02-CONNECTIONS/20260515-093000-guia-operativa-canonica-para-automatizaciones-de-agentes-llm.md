---
created: 2026-05-15T09:30:00-05:00
type: connection
status: draft
source: generated
tags:
  - connection
  - guidance
  - automation
  - mem
aliases:
  - Guía operativa canónica para automatizaciones de agentes LLM
source_file:
  - docs/01-CAPTURES/patterns/20260515-084500-flujos-automatizados-de-inbox-a-neurona-con-prompt-templates.md
  - docs/01-CAPTURES/patterns/20260515-084500-ayuda-operativa-para-agentes-llm-separa-operacion-de-implementacion.md
  - docs/05-NEURONA/indice-de-ayuda-operativa-para-agentes-llm.md
  - docs/05-NEURONA/flujo-completo-de-automatizacion-para-agentes-llm.md
  - docs/05-NEURONA/criterios-para-no-confundir-operacion-con-implementacion.md
  - docs/05-NEURONA/guia-de-captura-para-agentes-llm.md
  - docs/05-NEURONA/guia-de-conexiones-para-agentes-llm.md
  - docs/05-NEURONA/guia-de-briefs-para-agentes-llm.md
  - docs/05-NEURONA/guia-de-elevacion-a-neurona.md
---

# Guía operativa canónica para automatizaciones de agentes LLM

## Conexión

La mini-red de ayuda operativa en `05-NEURONA` y las dos capturas procesadas asociadas convergen en una tesis ya estable: `$mem` necesita una guía operativa canónica para agentes LLM que describa el flujo completo de automatización, pero que permanezca separada del plano de implementación del skill.

La conexión no es sólo entre notas; es entre capas del sistema:

- `01-CAPTURES` conserva la materia prima racionalizada;
- `05-NEURONA` convierte esa materia prima en ayuda navegable y reusable;
- `02-CONNECTIONS` fija la relación entre ambos como criterio del proyecto;
- y la implementación del skill queda fuera de esta guía para no mezclar operación con modificación del producto.

## Principio

La guía operativa canónica debe cumplir cuatro condiciones:

1. describir el flujo completo `00-INBOX -> 01-CAPTURES -> 02-CONNECTIONS -> 03-BRIEFS -> 05-NEURONA`;
2. ofrecer ayudas por caso de uso para agentes LLM;
3. incluir diagramas de secuencia que expliquen el recorrido;
4. y validar su propia coherencia contra el core del skill antes de subir a `05`.

## Tensión resuelta

Antes, la conversación corría el riesgo de mezclar tres planos:

- cómo usar el módulo;
- cómo implementarlo;
- y cómo personalizarlo para una instancia.

La mini-red resuelve eso al dejar que `05-NEURONA` enseñe operación, mientras `SKILL.md`, `references/` y el código mantienen el contrato base y la implementación.

## Consecuencia

Si un futuro agente LLM quiere automatizar `$mem`, esta guía ya le dice cómo hacerlo sin inventar el recorrido desde cero y sin interferir con la conversación de desarrollo del producto.

## Relacionado

- [Índice de ayuda operativa para agentes LLM](indice-de-ayuda-operativa-para-agentes-llm.md)
- [Flujo completo de automatización para agentes LLM](flujo-completo-de-automatizacion-para-agentes-llm.md)
- [Criterios para no confundir operación con implementación](criterios-para-no-confundir-operacion-con-implementacion.md)

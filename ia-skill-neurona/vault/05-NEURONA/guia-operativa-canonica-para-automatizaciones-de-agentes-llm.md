---
created: 2026-05-15T09:35:00-05:00
type: manifesto
status: active
source: mem operational doctrine
source_file:
  - docs/02-CONNECTIONS/20260515-093000-guia-operativa-canonica-para-automatizaciones-de-agentes-llm.md
  - docs/05-NEURONA/indice-de-ayuda-operativa-para-agentes-llm.md
  - docs/05-NEURONA/flujo-completo-de-automatizacion-para-agentes-llm.md
  - docs/05-NEURONA/criterios-para-no-confundir-operacion-con-implementacion.md
tags:
  - mem
  - guidance
  - automation
  - llm
aliases:
  - Guía operativa canónica para automatizaciones de agentes LLM
  - Criterio operativo canónico para automatizaciones
---

# Guía operativa canónica para automatizaciones de agentes LLM

## Definición

`$mem` debe ofrecer una guía operativa canónica para agentes LLM que automatizan memoria. Esa guía vive en `05-NEURONA`, describe el flujo completo de maduración y mantiene una frontera explícita respecto del plano de implementación del skill.

## Criterio

La guía es canónica cuando cumple todas estas condiciones:

1. describe el recorrido `00-INBOX -> 01-CAPTURES -> 02-CONNECTIONS -> 03-BRIEFS -> 05-NEURONA`;
2. puede ajustarse por caso de uso sin perder el core;
3. incluye ayudas, secuencias y criterios de madurez;
4. y deja claro que su función es operativa, no de implementación.

La madurez no consiste en repetir más instrucciones sino en hacer más corto el camino al criterio.

## Regla

El agente LLM que usa `$mem` debe leer esta neurona como protocolo de operación, no como manual de producto. Si hay que cambiar el skill, esa decisión pertenece al plano de implementación.
Las guías de captura, conexiones y briefs sólo deben detallar el tramo que les corresponde.

## Consecuencia

Esta guía permite que distintas conversaciones o agentes usen el módulo de memoria de forma consistente, sin reinventar el flujo y sin contaminar la conversación sobre cómo modificar el repositorio.

## Relacionado

- [Guía operativa canónica para automatizaciones de agentes LLM](20260515-093000-guia-operativa-canonica-para-automatizaciones-de-agentes-llm.md)
- [Índice de ayuda operativa para agentes LLM](indice-de-ayuda-operativa-para-agentes-llm.md)
- [Flujo completo de automatización para agentes LLM](flujo-completo-de-automatizacion-para-agentes-llm.md)
- [Criterios para no confundir operación con implementación](criterios-para-no-confundir-operacion-con-implementacion.md)

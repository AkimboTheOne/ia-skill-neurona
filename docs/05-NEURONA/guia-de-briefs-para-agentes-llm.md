---
created: 2026-05-15T09:10:00-05:00
type: manifesto
status: active
source: mem operational doctrine
source_file:
  - docs/00-INBOX/20260515-090000-ayuda-operativa-para-agentes-llm-sin-interferir-en-la-implementacion.md
tags:
  - mem
  - guidance
  - brief
  - llm
aliases:
  - Guía de briefs para agentes LLM
---

# Guía de briefs para agentes LLM

## Propósito

Esta neurona fija cuándo una red de capturas y conexiones ya tiene forma de brief útil.

## Regla

Un brief debe salir sólo cuando hay:

- una tesis central clara;
- prueba concreta;
- transformación del lector;
- y ganchos/cierres que sirvan a comunicación o pensamiento.

## Criterio

Si la evidencia es débil, el brief debe decirlo. No debe compensar falta de prueba con adornos retóricos.

## Secuencia

```mermaid
sequenceDiagram
    participant LLM as Agente LLM
    participant CON as 02-CONNECTIONS
    participant B as 03-BRIEFS

    LLM->>CON: Leer conexiones útiles
    LLM->>B: Redactar brief con tesis y prueba
    B-->>LLM: Exigir claridad y evidencia
    LLM->>B: Mantener el brief sobrio si la prueba es débil
```

## Relacionado

- [Brief: $mem como producto instanciable y referencias agnósticas](../03-BRIEFS/20260515-080000-mem-como-producto-instanciable-y-referencias-agnosticas.md)
- [Flujo completo de automatización para agentes LLM](flujo-completo-de-automatizacion-para-agentes-llm.md)

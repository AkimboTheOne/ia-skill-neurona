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
  - capture
  - llm
aliases:
  - Guía de captura para agentes LLM
---

# Guía de captura para agentes LLM

## Propósito

Esta neurona guía cómo pasar de una captura cruda a una captura tipada sin perder procedencia ni forzar síntesis.

## Regla

- Mantener el texto original intacto.
- Clasificar por el tipo de captura más útil, no por tema.
- Afinar en una sola oración verificable.
- Guardar siempre `source_file` cuando la captura derive del inbox.

## Criterio

Si la captura aún depende de contexto implícito, no debe inflarse a doctrina. Debe permanecer como captura procesada hasta que tenga claridad para conectar, sintetizar o subir de nivel.

## Secuencia

```mermaid
sequenceDiagram
    participant LLM as Agente LLM
    participant IN as 00-INBOX
    participant CAP as 01-CAPTURES

    LLM->>IN: Leer captura cruda
    LLM->>CAP: Clasificar y afinar
    CAP-->>LLM: Conservar origen y procedencia
    LLM->>CAP: Mantener si aún no madura
```

## Relacionado

- [Flujo completo de automatización para agentes LLM](flujo-completo-de-automatizacion-para-agentes-llm.md)
- [Criterios para no confundir operación con implementación](criterios-para-no-confundir-operacion-con-implementacion.md)

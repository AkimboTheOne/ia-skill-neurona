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
  - neuron
  - llm
aliases:
  - Guía de elevación a neurona
---

# Guía de elevación a neurona

## Propósito

Esta neurona indica cuándo una captura, conexión o brief ya debe subir a `05-NEURONA` como criterio del proyecto.

## Regla

Sube a `05` sólo cuando la idea:

- define una regla;
- aclara una frontera;
- explica un modo de uso;
- o estabiliza cómo leer la red del proyecto.

## Criterio

Si la idea sólo ayuda a pensar, permanece en `01`, `02` o `03`. Si ya gobierna el modelo, entonces merece `05`.

## Secuencia

```mermaid
sequenceDiagram
    participant LLM as Agente LLM
    participant MID as 01/02/03
    participant N as 05-NEURONA

    LLM->>MID: Evaluar madurez
    LLM->>N: Subir sólo si hay criterio estable
    N-->>LLM: Regla reutilizable y navegable
```

## Relacionado

- [Cierre del loop y comportamiento esperado al cerrar](cierre-del-loop-y-comportamiento-esperado-al-cerrar.md)
- [Criterios para no confundir operación con implementación](criterios-para-no-confundir-operacion-con-implementacion.md)

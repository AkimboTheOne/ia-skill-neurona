---
created: 2026-05-15T08:15:00-05:00
type: manifesto
status: active
source: mem operational doctrine
source_file:
  - docs/05-NEURONA/neurona.md
  - docs/05-NEURONA/agent.json
  - docs/05-NEURONA/instance.json
tags:
  - mem
  - architecture
  - instancing
  - references
aliases:
  - Diagrama de arquitectura instanciable
  - Arquitectura de referencias agnósticas
---

# Diagrama de arquitectura instanciable de `$mem`

```mermaid
flowchart TD
    U[Usuario / Agente] --> S[SKILL.md]
    S --> R[references/]
    S --> C[CLI: scripts/neurona.sh + neurona.py]
    S --> N[docs/05-NEURONA/neurona.md]

    R --> R0[Base agnóstica]
    R --> RT[Plantillas por caso de uso]

    N --> I[ia-skill-neurona/instance.json]
    N --> A[docs/05-NEURONA/agent.json]
    N --> L[docs/05-NEURONA/llms.txt]

    I --> T[Plantilla de referencia de instancia]
    I --> V[ia-skill-neurona/vault/ = bóveda activa descendiente]
    I --> M[.tmp/ = memoria temporal]

    C --> V
    C --> D0[00-INBOX]
    C --> D1[01-CAPTURES]
    C --> D2[02-CONNECTIONS]
    C --> D3[03-BRIEFS]
    C --> D5[05-NEURONA]

    A --> G[Descubrimiento de capacidades]
    L --> G
    R0 --> G
    RT --> G
    T --> G

    G --> LLM[LLM / juicio editorial]
    LLM --> V
    LLM --> D1
    LLM --> D2
    LLM --> D3
    LLM --> D5
```

## Lectura

- `SKILL.md` define el contrato central.
- `references/` define doctrina base agnóstica y plantillas de ajuste.
- `instance.json` declara la instancia activa y sus bóvedas nombradas.
- `agent.json` y `llms.txt` exponen el mapa de capacidades.
- La CLI mueve y organiza la bóveda.
- El LLM decide adaptación, curaduría y síntesis.
- La raíz del repo no es una bóveda válida; la instancia debe apuntar a un descendiente explícito.

## Relacionado

- [Neurona del Proyecto](neurona.md)
- [Modelo de instanciación del skill](modelo-de-instanciacion-del-skill.md)
- [Cómo otro agente llegaría a la misma conclusión](como-otro-agente-llegaria-a-la-misma-conclusion.md)
- [Estructura de la Bóveda](vault-structure.md)

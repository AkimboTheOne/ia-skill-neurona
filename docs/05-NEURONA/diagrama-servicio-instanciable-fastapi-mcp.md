---
created: 2026-05-16T00:00:00-05:00
type: manifesto
status: active
source: mem operational doctrine
source_file:
  - docs/00-INBOX/20260516-000000-propuesta-servicio-instanciable-fastapi-mcp-y-binding-de-boveda.md
  - docs/05-NEURONA/diagrama-arquitectura-instanciable.md
tags:
  - mem
  - architecture
  - service
  - fastapi
  - mcp
aliases:
  - Diagrama de servicio instanciable FastAPI/MCP
  - Arquitectura de servicio de bóveda
---

# Diagrama de servicio instanciable FastAPI/MCP de `$mem`

## ASCII

```text
┌──────────────────────────────────────────────────────────┐
│ skill_root                                               │
│  SKILL.md  references/  scripts/  docs/05-NEURONA/      │
└───────────────────────┬──────────────────────────────────┘
                        │
                        v
┌──────────────────────────────────────────────────────────┐
│ instancia explícita                                       │
│  mode: project | cli-cross | plugin | inception | server │
│  NEURONA_VAULT / instance.json                           │
└───────────────────────┬──────────────────────────────────┘
                        │
                        v
┌──────────────────────────────────────────────────────────┐
│ servicio local o permanente                               │
│  plugins/mem-api                                           │
│  FastAPI ahora, MCP después                                │
└───────────────────────┬──────────────────────────────────┘
                        │
                        v
┌──────────────────────────────────────────────────────────┐
│ bóveda consumida                                          │
│  docs/ o vault declarada por instancia                    │
│  00-INBOX -> 01 -> 02 -> 03 -> 05                         │
└───────────────────────┬──────────────────────────────────┘
                        │
                        v
┌──────────────────────────────────────────────────────────┐
│ LLM / agente                                               │
│  decide topología, contexto y modo de exposición          │
└──────────────────────────────────────────────────────────┘
```

## Mermaid

```mermaid
flowchart TD
    S[skill_root] --> D[docs/05-NEURONA]
    S --> R[references/]
    S --> C[scripts/neurona.py]

    D --> I[instance.json]
    D --> A[agent.json]
    D --> L[llms.txt]

    I --> V[NEURONA_VAULT / vault declarado]
    I --> M[mode: project | cli-cross | plugin | inception | server]

    A --> X[Contrato y capacidades]
    L --> X

    subgraph P[plugins/mem-api]
        F[FastAPI]
        M1[MCP adapter future]
        ENV[Env + instance binding]
    end

    X --> P
    ENV --> F
    ENV --> M1
    V --> F
    V --> M1
    F --> CLI[scripts/neurona.py]
    CLI --> V
    M1 --> V

    LLM[LLM / agente] --> I
    LLM --> P
    LLM --> V
```

## Lectura

- La instancia declara la bóveda consumida.
- El servicio expone primero FastAPI.
- MCP es una extensión futura, no el primer contrato operativo.
- El LLM decide si la instancia es local o permanente y qué bóveda gobierna.
- Una instancia, una bóveda, un servicio.
- `plugins/mem-api` es un spike interno; si madura como runtime, debe poder extraerse a un proyecto separado que consuma `$mem` como submódulo Git fijado a versión.

## Relacionado

- [Spike de servicio API/MCP y proyecto separado](spike-servicio-api-mcp-y-proyecto-separado.md)

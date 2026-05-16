---
created: 2026-05-15T18:00:00-05:00
type: manifesto
status: active
source: mem operational doctrine
source_file:
  - docs/01-CAPTURES/patterns/20260515-161700-soporte-visual-diagrama-multi-repo-y-gobernanza.md
  - docs/05-NEURONA/gobernanza-multi-instancia-y-boveda-descendiente.md
tags:
  - mem
  - diagram
  - governance
  - instancing
aliases:
  - Diagrama multi-repo y gobernanza
---

# Diagrama multi-repo y gobernanza

```mermaid
flowchart TD
    subgraph S[skill_root / skill cross]
        SK[SKILL.md]
        RF[references/]
        SC[scripts/]
        MF[agent.json / instance.json / llms.txt]
    end

    S --> A[Instancia explícita]
    A --> PRJ[project_repo]
    A --> VAULT[vault_repo]
    A --> TMP[skill_tmp]

    PRJ --> X[Contexto operativo]
    VAULT --> Y[docs/ como documentación del producto]
    TMP --> T[Mapas y trabajo temporal]

    X --> LLM[LLM / agente]
    Y --> LLM
    SK --> LLM
    RF --> LLM
    SC --> LLM
    MF --> LLM
```

## Lectura

- El skill cross aporta contrato y herramientas.
- La instancia declara repo de trabajo, bóveda y memoria temporal.
- `docs/` es documentación del producto.
- La raíz del repo no es una bóveda válida.

## Relacionado

- [Gobernanza multi-instancia y bóveda descendiente](gobernanza-multi-instancia-y-boveda-descendiente.md)
- [Diagrama de arquitectura instanciable](diagrama-arquitectura-instanciable.md)

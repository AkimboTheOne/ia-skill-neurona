---
created: 2026-05-15T08:00:00-05:00
type: brief
status: draft
source: generated
source_file:
  - 00-INBOX/20260515-075031-revision-integral-para-refactorizacion-controlada.md
tags:
  - brief
  - product
  - architecture
  - mem
aliases:
  - Brief: $mem como producto instanciable
---

# Brief: $mem como producto instanciable y referencias agnósticas

## ONE THING

`$mem` debe definirse como un producto modular de memoria operativa instanciable, donde el contrato base es agnóstico y cada instancia ajusta sus `references/` según el caso de uso sin romper las riendas centrales.

## PROOF

La revisión del proyecto ya mostró una separación real entre `SKILL.md`, `references/`, `docs/05-NEURONA`, la CLI y los manifiestos. También dejó claro que `docs/` actúa como instancia concreta del skill y que `05-NEURONA` gobierna el modelo operativo.

## READER TRANSFORMATION

El lector entiende que la discusión no es si el skill “sirve”, sino qué forma de producto debe ser: una base reutilizable con referencias agnósticas por defecto y una capa de adaptación explícita por instancia y caso de uso.

## THREE HOOKS

1. El skill no necesita ser rígido para ser consistente.
2. La personalización debe vivir en la instancia, no en el contrato central.
3. Las referencias son una plantilla de maniobra, no una jaula.

## THREE CLOSERS

1. Si la instancia no puede ajustar sus referencias, el producto todavía no está maduro.
2. Un skill modular útil no copia contexto: lo gobierna.
3. La reutilización real aparece cuando la forma se conserva y la semántica se adapta.

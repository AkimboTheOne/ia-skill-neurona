---
created: 2026-05-15T14:45:00-05:00
type: brief
status: draft
source: generated
source_file:
  - 00-INBOX/20260515-143525-objetivo-de-la-iteraci-n-hacer-que-el-m-dulo-de-memori.md
  - 00-INBOX/20260515-144242-siguiente-fase-planear-el-feature-y-el-release-estable.md
tags:
  - brief
  - release
  - governance
  - mem
aliases:
  - Brief: release estable y coexistencia con Memories
---

# Brief: release estable y coexistencia con Memories

## ONE THING

`$mem` debe publicarse como una capa de memoria de proyecto explícita y modular que complementa la memoria nativa del agente, en lugar de competir con ella.

## PROOF

El repositorio ya separa contrato, doctrina, bóveda y CLI: `SKILL.md` define el contrato, `docs/05-NEURONA/` define la gobernanza, `references/` define el soporte reusable y `scripts/` materializa la operación determinista. La fricción restante está en la claridad de instancia, instalación y precedencia entre memoria del agente y memoria del proyecto.

## READER TRANSFORMATION

El lector entiende que el valor del producto no es guardar más cosas, sino gobernar con precisión qué memoria se usa, dónde vive, cómo se instala y cómo se publica sin mezclar contexto conversacional con memoria operativa del repo.

## THREE HOOKS

1. La memoria nativa del agente no reemplaza la memoria de proyecto.
2. El skill es más útil cuando declara su frontera, no cuando intenta absorberlo todo.
3. Un release estable necesita reglas de instancia antes que más código.

## THREE CLOSERS

1. Si el modo de uso no es inequívoco, el producto todavía no está listo para publicarse.
2. La coexistencia correcta no fusiona memorias: las ordena.
3. La primera versión estable debe enseñar al agente cuándo usar `mem` y cuándo no.

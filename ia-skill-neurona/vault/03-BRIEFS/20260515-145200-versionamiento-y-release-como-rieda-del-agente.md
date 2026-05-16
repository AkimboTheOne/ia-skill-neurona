---
created: 2026-05-15T14:52:00-05:00
type: brief
status: draft
source: generated
source_file:
  - references/versioning-and-release.md
  - AGENTS.md
tags:
  - brief
  - governance
  - release
  - mem
aliases:
  - Brief: versionamiento y release como rienda del agente
---

# Brief: versionamiento y release como rienda del agente

## ONE THING

El versionamiento debe tratarse como una rienda del proyecto y del agente: una secuencia repetible que lleva de una idea madura a una versión visible y publicable sin dejar decisiones dispersas.

## PROOF

El repositorio ya separa contrato, doctrina, instanciación y operación. También tiene validaciones deterministas y un cierre de loop previsto. Lo que faltaba era convertir la subida de versión en una secuencia explícita para que cada release siga el mismo orden y no dependa de memoria informal. Para este proyecto, el tag verificado del repo puede ser además la fuente descargable canónica para otro proyecto o un skill cross.

## READER TRANSFORMATION

El lector entiende que un release no es sólo subir un tag. Es el cierre disciplinado de una iteración donde el alcance, la validación y la publicación quedan gobernados por una misma secuencia.

## THREE HOOKS

1. Un release estable no improvisa su propia forma.
2. La versión visible debe corresponder a una decisión ya cerrada.
3. El agente necesita una rienda de publicación, no sólo instrucciones dispersas.

## THREE CLOSERS

1. Si la secuencia cambia cada vez, la gobernanza todavía no está madura.
2. Un tag sin cierre documentado es una publicación frágil.
3. La consistencia de release es parte del producto, no un detalle de mantenimiento.

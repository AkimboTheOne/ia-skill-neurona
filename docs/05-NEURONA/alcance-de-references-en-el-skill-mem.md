---
type: manifesto
status: active
source: mem operational doctrine
source_file: docs/05-NEURONA/neurona.md
tags:
  - mem
  - references
  - skill
  - governance
aliases:
  - Alcance de references en el skill mem
  - Support scope of references
---

# Alcance de `references/` en el skill `$mem`

## Tesis

`references/` no es documentación narrativa del skill. Es la carpeta de soporte normativo y operativo que permite funcionar con consistencia sobre una bóveda de proyecto.

## Qué es

Dentro del skill, `references/` contiene las piezas que el contrato principal consulta para operar con precisión:

- estructura de bóveda;
- flujos de inteligencia;
- contratos de propiedades;
- doctrinas y patrones base;
- definiciones operativas que guían la curaduría;
- reglas que el LLM debe respetar al usar la bóveda.

## Qué no es

`references/` no es:

- la superficie viva de memoria del proyecto;
- un depósito de conocimiento sustantivo;
- una segunda bóveda paralela;
- un lugar para duplicar capturas, conexiones o briefs.

## Relación con la memoria del proyecto

La memoria operativa del proyecto vive en `01-CAPTURES`, `02-CONNECTIONS`, `03-BRIEFS` y `05-NEURONA`.
`references/` no compite con esa red: la orienta.

En este esquema:

- `SKILL.md` define el contrato núcleo.
- `references/` guarda los criterios reutilizables del skill.
- la red del proyecto guarda la memoria viva.

## Impacto en la mejora del skill

Esta separación permite mejorar el skill sin mezclar dos capas distintas:

1. El skill puede aprender y endurecer sus reglas.
2. El proyecto puede conservar su memoria propia.
3. El LLM puede decidir contenido y semántica con mayor claridad porque la capa de soporte no se confunde con la capa de memoria.

## Regla operativa

Si una pieza sirve para ejecutar mejor el skill, va a `references/`.
Si una pieza sirve para recordar y pensar el proyecto, va a la red de memoria.

## Relacionado

- [Neurona del Proyecto](neurona.md)
- [Fuente consolidada de `docs/baseline`](../01-CAPTURES/patterns/20260513-172100-baseline-source-consolidated.md)
- [Flujos de Inteligencia](../references/intelligence-workflows.md)

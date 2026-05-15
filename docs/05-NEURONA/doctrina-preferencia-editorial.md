---
created: 2026-05-15T10:05:00-05:00
type: manifesto
status: active
source: mem operational doctrine
source_file:
  - references/editorial-preference.md
tags:
  - mem
  - editorial
  - style
  - doctrine
aliases:
  - Doctrina de preferencia editorial
  - Preferencia editorial de mem
---

# Doctrina de preferencia editorial

## Definición

`$mem` privilegia la lectura humana en las superficies narrativas y la operabilidad de máquina en las superficies técnicas.

## Regla

La lectura humana tiene prioridad en:

- `README.md`
- `SKILL.md`
- neuronas de `05-NEURONA`
- briefs
- capturas procesadas

Los títulos deben escribirse en formato de frase: `Titulo de una seccion`, no `Titulo De Una Seccion`.
La mayúscula inicial se reserva para nombres propios, siglas y términos que lo requieran por precisión.

La señal técnica tiene prioridad en:

- `scripts/`
- manifiestos
- rutas
- nombres de archivo
- frontmatter y contratos estructurales

## Override

Una instancia puede ajustar tono, formalidad o densidad, pero debe declararlo explícitamente en su configuración o en su referencia operativa. El override adapta la superficie; no invalida la doctrina base.

## Consecuencia

Si un término técnico reduce la lectura sin mejorar precisión, debe bajar de prioridad en la prosa humana y permanecer como contexto de máquina o nota técnica.

## Relacionado

- [Doctrina de Preferencia Editorial](../../references/editorial-preference.md)
- [Neurona del Proyecto](neurona.md)
- [Índice de ayuda operativa para agentes LLM](indice-de-ayuda-operativa-para-agentes-llm.md)

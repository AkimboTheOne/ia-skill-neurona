---
created: 2026-05-16T12:59:16-05:00
type: brief
status: draft
source: implementation
source_file:
  - SKILL.md
  - README.md
  - references/operational-loop-templates.md
  - docs/05-NEURONA/loop-operativo-para-agentes-llm.md
  - scripts/neurona.py
tags:
  - brief
  - release
  - mem
aliases:
  - Release 0.2.0: loop operativo y plantillas
---

# Brief: release 0.2.0 loop operativo y plantillas

## ONE THING

`$mem` pasa de tener sólo un circuito de maduración documental a ofrecer un loop operativo explícito para que agentes usen la bóveda con plantillas, handoff y síntesis densa.

## PROOF

La CLI incorpora `templates list/show`, la doctrina fija `preparar -> operar -> cerrar` y `conversation` ahora espera síntesis densa con contexto, decisiones, evidencia, relaciones, pendientes, próximos pasos y riesgos.

## READER TRANSFORMATION

Un agente nuevo ya no necesita adivinar cómo conversar con la bóveda: puede pedir el andamio de fase, operar con juicio propio y cerrar dejando continuidad auditable.

## THREE HOOKS

1. El problema no era guardar notas; era cerrar conversaciones sin perder el hilo.
2. Una memoria útil no piensa por el agente: le exige dejar índices y relaciones.
3. `$mem` ahora tiene un protocolo para usar la caja negra sin mirar dentro.

## THREE CLOSERS

1. La próxima prueba real es instanciar este loop fuera del repo del skill.
2. Si una conversación no deja handoff, no quedó guardada como memoria operativa.
3. El skill sigue siendo agnóstico; la diferencia es que ahora guía mejor al agente que lo usa.

---
created: 2026-05-15T08:45:00-05:00
type: patterns
status: processed
source: inbox
source_file: 00-INBOX/20260515-085500-flujos-automatizados-de-inbox-a-neurona-con-prompt-templates.md
tags:
  - pattern
  - capture
  - mem
aliases:
  - Flujos automatizados de inbox a neurona con prompt templates
---

# La memoria debe empaquetar flujos operables, no sólo contrato y doctrina

## Sharpened

La memoria del skill debe materializar su secuencia de trabajo como plantillas operables y ajustables que permitan a agentes distintos construir neuronas consistentes desde `00-INBOX` hasta `05-NEURONA`.

## Raw Capture

Hay que materializar toda la secuencia de flujo de trabajo de la memoria como parte de las referencias y/o la documentación del skill. La idea es que existan instrucciones predefinidas pero ajustables por el usuario para generar flujos automatizados de agentes, de modo que esos flujos construyan neuronas consistentes desde `00-INBOX` hasta `05-NEURONA`, respetando toda la lógica del módulo de memoria.

Si bien la decisión final siempre debe ser del LLM entendiendo las referencias y los manifiestos, conviene estructurar ejemplos sólidos de prompts que puedan ser usados en automatizaciones para que agentes diferentes produzcan salidas consistentes y navegables.

La hipótesis de producto es que no basta con tener contrato y doctrina: hace falta empaquetar recorridos de trabajo como plantillas operables, para que un usuario o agente pueda disparar flujos repetibles sin reinventar cada vez el proceso de captura, curaduría, conexión y elevación a neurona.

La duda abierta es cómo balancear:

- contrato normativo del skill;
- referencias base agnósticas;
- plantillas de prompt por caso de uso;
- y personalización por instancia o usuario.

## Raw Capture

Hay una tensión entre documentar demasiado el flujo y mantener el skill modular. La siguiente iteración debería validar si esto vive mejor como:

1. referencias ajustables del skill;
2. documentación operativa del skill;
3. o ambos, con la documentación explicando el contrato y las plantillas proporcionando ejemplos de ejecución.

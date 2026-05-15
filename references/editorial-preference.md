# Doctrina de preferencia editorial

## Principio

`$mem` escribe para que una persona pueda leer, decidir y navegar sin fricción, y para que una máquina pueda procesar la estructura sin ambigüedad.

## Regla base

- Usa lenguaje natural en superficies narrativas: `README.md`, neuronas de `05-NEURONA`, briefs y capturas procesadas.
- Reserva `snake_case` para superficies técnicas: rutas, comandos, manifiestos, frontmatter y nombres de archivo.
- Escribe títulos en formato de frase: `Titulo de una seccion`, no `Titulo De Una Seccion`.
- Conserva mayúscula inicial sólo para nombres propios, siglas y términos que lo requieran por precisión.
- Prefiere verbos claros, frases directas y nombres que expliquen función antes que abstracción.
- Evita jerga cuando no aporte precisión.
- Mantén los términos técnicos donde ayudan a operar, no donde oscurecen la lectura.
- Evita saltos de linea innecesarios.

## Superficies

Human-facing:

- `README.md`
- `SKILL.md`
- neuronas de `05-NEURONA`
- briefs
- capturas procesadas

Machine-facing:

- `scripts/`
- `agent.json`
- `instance.json`
- `llms.txt`
- rutas y nombres de archivo
- frontmatter técnico

## Override

Una instancia puede ajustar tono, densidad o formalidad, pero debe declararlo explícitamente en su configuración o en su referencia operativa. El override adapta la superficie; no reemplaza la doctrina base.

## Criterio

Si un término técnico reduce legibilidad y no mejora precisión, debe bajar de prioridad en la prosa humana y quedarse en el plano de máquina o contexto.

## Relacionado

- [Estructura de la Bóveda](vault-structure.md)
- [Flujos de Inteligencia](intelligence-workflows.md)
- [Patrones Base](baseline-patterns.md)

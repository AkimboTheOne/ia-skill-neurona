# AGENTS.md

Guía para agentes de codificación IA que trabajan en este repositorio.

## Propósito

Este archivo orienta sesiones nuevas para que un agente pueda:

- cargar contexto del repositorio con rapidez;
- navegar la documentación a profundidad;
- distinguir entre el contrato del skill y la documentación del proyecto;
- cambiar el producto sin romper el `SKILL.md`.

## Sesión Y Setup

- Si el repositorio necesita compatibilidad local para un agente o herramienta, ejecuta primero `scripts/setup-repo-for-agents.sh`.
- Si esta guía cambia durante una sesión, reinicia la sesión para que el agente adopte el nuevo contexto de forma limpia.
- No asumas que `AGENT.md`, `CLAUDE.md`, enlaces simbólicos o aliases existen por defecto; el setup debe materializarlos cuando haga falta.
- El setup acepta superficies adicionales por parámetro; la base por defecto cubre compatibilidad “cross” para agentes de codificación IA.
- El setup escribe su último estado en `.tmp/agents-setup-state.json`; usa `scripts/agents-healthcheck.sh` para comprobarlo.
- Si el healthcheck cambia de estado o la guía cambia, reinicia la sesión o recarga el contexto del agente.

## Mapa Del Repositorio

- `README.md`: puerta de entrada humana del producto.
- `SKILL.md`: contrato central del skill `$mem`.
- `docs/`: bóveda documental del proyecto.
- `docs/05-NEURONA/`: doctrina operativa y guías para agentes LLM.
- `references/`: normas reutilizables y referencias agnósticas.
- `scripts/`: CLI determinista, smoke tests y utilidades.
- `agents/`: configuración de agente para consumos externos.

## Orden De Lectura

1. `README.md` para entender el producto.
2. `SKILL.md` para entender el contrato del skill.
3. `docs/05-NEURONA/neurona.md` para entender el modelo del proyecto.
4. `docs/05-NEURONA/indice-de-ayuda-operativa-para-agentes-llm.md` para entender el flujo operativo.
5. `references/vault-structure.md` y `references/intelligence-workflows.md` para entender la bóveda y la síntesis.
6. `references/editorial-preference.md` para mantener la voz editorial.

## Cómo Navegar La Red Documental

- Usa `docs/05-NEURONA/` para criterios, fronteras y doctrina.
- Usa `docs/01-CAPTURES/` para la materia prima curada.
- Usa `docs/02-CONNECTIONS/` para relaciones y tensiones entre notas.
- Usa `docs/03-BRIEFS/` para síntesis listas para comunicar.
- Usa `docs/baseline/` sólo como corpus histórico o fuente inspiracional.

## Reglas De Trabajo

- Mantén los cambios de fondo en `SKILL.md` y `docs/05-NEURONA/` separados de los ajustes de presentación.
- No reescribas `docs/baseline/` salvo que el usuario lo pida explícitamente.
- Prefiere ajustes de forma sobre reingeniería cuando el objetivo sea editorial.
- No introduzcas instrucciones que compitan con `SKILL.md`; este archivo guía el trabajo en el repo, no reemplaza el contrato del skill.
- Conserva el idioma y la convención editorial del proyecto: títulos en formato de frase, con mayúscula inicial sólo donde aporte precisión.

## Comandos Útiles

```bash
bash scripts/setup-repo-for-agents.sh
bash scripts/setup-repo-for-agents.sh --surface CLAUDE.md=AGENTS.md
bash scripts/agents-healthcheck.sh
python3 scripts/neurona.py status --vault .tmp/vault
bash scripts/mini-suite.sh
python3 scripts/neurona.py init --vault .tmp/vault
python3 scripts/neurona.py capture --vault .tmp/vault --text "..."
python3 scripts/neurona.py process-inbox --vault .tmp/vault
python3 scripts/neurona.py connect --vault .tmp/vault --days 7
python3 scripts/neurona.py brief --vault .tmp/vault --topic "..."
```

## Criterio De Éxito

Un agente que entra aquí debería poder:

- ubicar rápidamente qué parte del repositorio es contrato, qué parte es doctrina y qué parte es implementación;
- editar documentación sin romper el modelo operativo;
- ejecutar la CLI y validar el flujo básico con la mini suite;
- volver a otra sesión sin perder la estructura mental del proyecto.

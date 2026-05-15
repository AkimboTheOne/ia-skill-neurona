# AGENTS.md

Guía para agentes de codificación IA que trabajan en este repositorio.

## Propósito

Este archivo orienta sesiones nuevas para que un agente pueda:

- cargar contexto del repositorio con rapidez;
- navegar la documentación a profundidad;
- distinguir entre el contrato del skill y la documentación del proyecto;
- cambiar el producto sin romper el `SKILL.md`.

## Sesión y setup

- Si el repositorio necesita compatibilidad local para un agente o herramienta, ejecuta primero `scripts/setup-repo-for-agents.sh`.
- Si esta guía cambia durante una sesión, reinicia la sesión para que el agente adopte el nuevo contexto de forma limpia.
- No asumas que `AGENT.md`, `CLAUDE.md`, enlaces simbólicos o aliases existen por defecto; el setup debe materializarlos cuando haga falta.
- El setup acepta superficies adicionales por parámetro; la base por defecto cubre compatibilidad “cross” para agentes de codificación IA.
- El setup escribe su último estado en `.tmp/agents-setup-state.json`; usa `scripts/agents-healthcheck.sh` para comprobarlo.
- Si el healthcheck cambia de estado o la guía cambia, reinicia la sesión o recarga el contexto del agente.

## Mapa del repositorio

- `README.md`: puerta de entrada humana del producto.
- `SKILL.md`: contrato central del skill `$mem`.
- `docs/`: bóveda documental del proyecto.
- `docs/05-NEURONA/`: doctrina operativa y guías para agentes LLM.
- `references/`: normas reutilizables y referencias agnósticas.
- `scripts/`: CLI determinista, smoke tests y utilidades.
- `agents/`: configuración de agente para consumos externos.

## Orden de lectura

1. `README.md` para entender el producto.
2. `SKILL.md` para entender el contrato del skill.
3. `docs/05-NEURONA/neurona.md` para entender el modelo del proyecto.
4. `docs/05-NEURONA/indice-de-ayuda-operativa-para-agentes-llm.md` para entender el flujo operativo.
5. `references/vault-structure.md` y `references/intelligence-workflows.md` para entender la bóveda y la síntesis.
6. `references/editorial-preference.md` para mantener la voz editorial.

## Cómo navegar la red documental

- Usa `docs/05-NEURONA/` para criterios, fronteras y doctrina.
- Usa `docs/01-CAPTURES/` para la materia prima curada.
- Usa `docs/02-CONNECTIONS/` para relaciones y tensiones entre notas.
- Usa `docs/03-BRIEFS/` para síntesis listas para comunicar.
- Usa `docs/baseline/` sólo como corpus histórico o fuente inspiracional.

## Reglas de trabajo

- Mantén los cambios de fondo en `SKILL.md` y `docs/05-NEURONA/` separados de los ajustes de presentación.
- No reescribas `docs/baseline/` salvo que el usuario lo pida explícitamente.
- Prefiere ajustes de forma sobre reingeniería cuando el objetivo sea editorial.
- No introduzcas instrucciones que compitan con `SKILL.md`; este archivo guía el trabajo en el repo, no reemplaza el contrato del skill.
- Conserva el idioma y la convención editorial del proyecto: títulos en formato de frase, con mayúscula inicial sólo donde aporte precisión.
- Las ideas pendientes viven en `docs/00-INBOX/` y se declaran con metadata; no las muevas a una carpeta separada salvo que la instancia lo exija explícitamente.

## Comandos útiles

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

## Versionado y release

Cuando la iteración alcance estabilidad, sigue siempre la misma rienda:

1. fija el alcance en inbox, captura o brief;
2. aplica los cambios en documentación, gobernanza o implementación;
3. actualiza la versión visible donde corresponda;
4. valida `scripts/setup-repo-for-agents.sh`, `scripts/agents-healthcheck.sh` y `bash scripts/mini-suite.sh`;
5. registra el cierre en `05-NEURONA` o en una brief de release;
6. etiqueta el release en Git si el estado es publicable.

La secuencia canónica vive en `references/versioning-and-release.md`. No inventes un flujo paralelo salvo que el modelo de publicación cambie.

Para `mem` como skill cross o plugin local, el tag verificado del repo puede ser la fuente canónica descargable. En ese caso:

- el tag fija la versión;
- el release de GitHub publica esa versión;
- el checkout del tag sirve como fuente instalable o referenciable en otro proyecto.

No hace falta empaquetado adicional salvo que el caso de uso lo pida explícitamente.

## Criterio de éxito

Un agente que entra aquí debería poder:

- ubicar rápidamente qué parte del repositorio es contrato, qué parte es doctrina y qué parte es implementación;
- editar documentación sin romper el modelo operativo;
- ejecutar la CLI y validar el flujo básico con la mini suite;
- volver a otra sesión sin perder la estructura mental del proyecto.

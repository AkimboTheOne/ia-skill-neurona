---
title: mem
project: ia-skill-neurona
description: Módulo de memoria operativa instanciable en Markdown para capturar, curar, conectar y sintetizar conocimiento de proyecto.
status: active
version: 0.2.1
tags:
  - mem
  - skill
  - markdown
  - cli
  - obsidian
  - knowledge-base
  - agent-ready
---

# `$mem` / `ia-skill-neurona`

[![Version](https://img.shields.io/badge/version-0.2.1-blue.svg)](.)
[![Status](https://img.shields.io/badge/status-active-green.svg)](.)
[![License](https://img.shields.io/badge/license-GPLv3-lightgrey.svg)](LICENSE)
[![Docs](neurona.md)
[![CLI](https://img.shields.io/badge/cli-neurona.sh%20%7C%20neurona.py-orange.svg)](scripts/neurona.sh)

`$mem` es un módulo de memoria operativa en Markdown para proyectos que necesitan capturar, curar, conectar y sintetizar conocimiento de forma navegable por agentes IA.
Complementa una memoria nativa del agente como `Memories`: no la reemplaza, sino que aporta una bóveda de proyecto explícita, portátil y auditable.
Cuando este repo se usa sobre sí mismo, la bóveda activa vive en `ia-skill-neurona/vault/` y `references/` fija las riendas; la curaduría busca que el LLM entienda más con menos contexto implícito.

Este repositorio es el producto completo:

- `SKILL.md` define el contrato del skill.
- `ia-skill-neurona/vault/` contiene la bóveda contextual del proyecto.
- `references/` contiene la doctrina agnóstica y las reglas reutilizables.
- `scripts/` contiene la CLI determinista y la mini suite funcional.
- `AGENTS.md` orienta a agentes de codificación IA que entren por el repositorio.
- `scripts/setup-repo-for-agents.sh` materializa compatibilidad local cuando hace falta.

No es sólo una carpeta de notas. Es un sistema de trabajo para construir memoria de proyecto con estructura, trazabilidad y una capa de síntesis reutilizable. El contenido de `ia-skill-neurona/vault/` está pensado sobre todo para el agente/LLM que opera el flujo del proyecto, no para competir con el contrato del skill.
Cuando el skill se usa sobre sí mismo, el repositorio entra en modo de instancia de trabajo: la documentación gobierna el contrato y la CLI sólo ejecuta operaciones deterministas.

La bóveda activa de esta instancia vive en `ia-skill-neurona/vault/`, no en la raíz del repositorio. `docs/` queda fuera del alcance operativo del skill y existe como documentación del producto. Esa frontera es intencional: la raíz preserva el contrato del producto y la bóveda preserva la memoria operativa.

## Setup para agentes

Si vas a trabajar el repositorio como agente de codificación IA, ejecuta primero el setup local:

```bash
bash scripts/setup-repo-for-agents.sh
```

Si `AGENTS.md` cambia durante la sesión, reinicia el contexto del agente para adoptar la nueva guía de forma limpia.

Modos útiles:

- base: crea los aliases de industria por defecto con symlinks o un fallback por copia;
- extendido: agrega superficies extra con `--surface DEST=SOURCE`;
- compatible: usa `--copy DEST=SOURCE` cuando el entorno no acepte symlinks;
- healthcheck: valida la última composición guardada en `.tmp/agents-setup-state.json`.

Ejemplos:

```bash
bash scripts/setup-repo-for-agents.sh --surface CLAUDE.md=AGENTS.md
bash scripts/setup-repo-for-agents.sh --copy CLAUDE.md=AGENTS.md
bash scripts/agents-healthcheck.sh
```

El estado del setup vive en `.tmp/agents-setup-state.json`. Si ese archivo cambia, vuelve a correr el healthcheck y recarga o reinicia la sesión del agente cuando la composición local haya sido reescrita.

Si ya usas una memoria nativa del agente, trata este repo como la capa de memoria del proyecto. No mezcles ambos contextos por defecto: primero decide si la información pertenece a la conversación general del agente o a la bóveda del proyecto.

## Qué resuelve

- Captura ideas crudas con fricción mínima.
- Organiza la memoria por tipo, no por tema.
- Conecta notas cuando existe un principio, tensión o patrón común.
- Genera briefs cuando la red ya tiene forma comunicable.
- Eleva ideas maduras a la bóveda de neuronas cuando ya gobiernan el modelo.
- Cura y compacta la documentación para reducir extensión sin perder procedencia ni calidad.
- Reorienta sesiones nuevas con una entrada clara del repositorio y su documentación.

## Para quién es

- Equipos o personas que quieren una memoria de proyecto más estructurada que un cuaderno suelto.
- Usuarios que trabajan con agentes LLM y necesitan una bóveda navegable.
- Mantenedores que quieren una superficie clara para instalar, adaptar o instanciar el módulo en otros contextos.

## Qué hay en este repositorio

- `AGENTS.md` / `AGENT.md`: guía de arranque para agentes de codificación IA.
- `SKILL.md`: contrato de uso del skill.
- `scripts/`: CLI determinista para inicializar, capturar, procesar y resumir memoria.
- `ia-skill-neurona/vault/`: bóveda contextual del proyecto.
- `references/`: referencias base y plantillas ajustables por caso de uso.
- `agents/`: configuración de agente para consumos externos.

## Uso rápido

Inicializa la bóveda contextual del repositorio:

```bash
eval "$(scripts/init-repo-vault.sh)"
scripts/neurona.sh status --vault "$NEURONA_VAULT"
```

Captura una idea cruda:

```bash
scripts/neurona.sh capture --vault "$NEURONA_VAULT" --text "una idea breve"
```

Procesa el inbox:

```bash
scripts/neurona.sh process-inbox --vault "$NEURONA_VAULT"
```

Genera conexiones o briefs:

```bash
scripts/neurona.sh connect --vault "$NEURONA_VAULT"
scripts/neurona.sh brief --vault "$NEURONA_VAULT" --topic "tema"
scripts/neurona.sh ask --vault "$NEURONA_VAULT" --query "tema"
```

`ask` consulta la bóveda por etapas con coincidencia heurística y devuelve JSON con coincidencias, puntuación y un `preview` breve. Sirve para reabrir stages y alimentar el razonamiento del LLM.

### Smoke test

Ejecuta una mini suite funcional sobre una bóveda temporal para validar el flujo completo:

```bash
bash scripts/mini-suite.sh
```

La suite crea una bóveda efímera en `ia-skill-neurona/vault`, ejecuta `init`, `status`, `capture`,
`process-inbox`, `connect`, `ask` y `brief`, y verifica que cada etapa deje artefactos válidos.

## Cómo está estructurado

La bóveda vive en `ia-skill-neurona/vault/` y se organiza así:

```text
00-INBOX/
01-CAPTURES/
  observations/
  reactions/
  patterns/
  questions/
  numbers/
02-CONNECTIONS/
03-BRIEFS/
05-NEURONA/
```

Resumen operativo:

- `00-INBOX`: entradas crudas.
- `01-CAPTURES`: notas tipadas y curadas.
- `02-CONNECTIONS`: relaciones entre notas.
- `03-BRIEFS`: síntesis listas para usar.
- `05-NEURONA`: doctrina, guías e índice del modelo materializados por la CLI.

## Gobernanza de instancia

La instancia actual se declara sobre una bóveda descendiente explícita:

- `skill_root`: este repositorio;
- `project_repo`: el repositorio donde opera el agente;
- `vault_repo`: `ia-skill-neurona/vault/` como bóveda viva por defecto;
- `skill_tmp`: `.tmp/` para trabajo temporal y mapas.

`ask` es parte del MVP y está disponible como superficie pública de consulta. Úsalo cuando quieras recuperar evidencia por etapas sin navegar manualmente toda la red:

```bash
scripts/neurona.sh ask --vault "$NEURONA_VAULT" --query "descendant vault"
scripts/neurona.sh ask --vault "$NEURONA_VAULT" --query "governance" --stage captures --stage connections
```

La memoria nativa del agente, si existe, sigue siendo conversacional. `mem` gobierna la memoria operativa del proyecto. No se mezclan por defecto.

## Cómo navegar el repositorio

Si entras por primera vez como agente de codificación IA:

1. Ejecuta `bash scripts/setup-repo-for-agents.sh` si necesitas compatibilidad local para herramientas de agente.
2. Lee `AGENTS.md` para orientarte en el repo.
3. Lee `README.md` para entender el alcance del producto.
4. Lee `SKILL.md` para entender el contrato del skill.
5. Usa `docs/especificacion/` para navegar la red documental del proyecto.
6. Usa `references/` para recuperar la doctrina estable y los contratos reutilizables.
7. Usa `scripts/mini-suite.sh` para validar el flujo básico cuando hagas cambios.

Las ideas pendientes se quedan en `ia-skill-neurona/vault/00-INBOX/` con metadata declarativa; no hace falta una carpeta separada de “pendings” para mantenerlas visibles.

## Instancias y personalización

El proyecto está diseñado para instanciarse en otros contextos.

- `references/` ofrece una base agnóstica.
- Las instancias pueden ajustar plantillas según caso de uso.
- La personalización vive en la instancia, no en el núcleo del skill.
- La doctrina editorial privilegia lectura humana en superficies narrativas y operabilidad de máquina en superficies técnicas.
- Las salidas legibles para humanos pueden publicarse en otras superficies, pero la fuente de verdad sigue en `ia-skill-neurona/vault/`.
- Los títulos del producto usan formato de frase: una sola mayúscula inicial salvo nombres propios o términos que lo exijan.

Eso hace que el módulo sea reutilizable sin perder su forma.

## Casos de uso

La mini-red operativa de la bóveda documenta recorridos concretos para automatizaciones con agentes LLM.

- Capturar ideas crudas y convertirlas en capturas tipadas.
- Conectar notas cuando existe una tensión, principio o patrón útil.
- Sintetizar una red madura en briefs reutilizables.
- Elevar criterios estables a neuronas gobernantes del proyecto.

Si quieres ver la guía operativa de esos recorridos:

- [`Índice de ayuda operativa para agentes LLM`](docs/especificacion/indice-de-ayuda-operativa-para-agentes-llm.md)
- [`Modelo de instanciación del skill`](docs/especificacion/modelo-de-instanciacion-del-skill.md)

## Qué debes leer si vas a usarlo

- [`SKILL.md`](SKILL.md)
- [`docs/especificacion/neurona.md`](docs/especificacion/neurona.md)
- [`docs/especificacion/doctrina-preferencia-editorial.md`](docs/especificacion/doctrina-preferencia-editorial.md)
- [`docs/especificacion/indice-de-ayuda-operativa-para-agentes-llm.md`](docs/especificacion/indice-de-ayuda-operativa-para-agentes-llm.md)
- [`references/vault-structure.md`](references/vault-structure.md)
- [`references/intelligence-workflows.md`](references/intelligence-workflows.md)
- [`references/editorial-preference.md`](references/editorial-preference.md)

## Primera versión

Este repositorio ya está en un punto útil para una primera publicación remota:

- contrato del skill definido;
- CLI funcional;
- bóveda estructurada;
- referencias base y plantillas de instancia;
- red de neuronas para operación y criterio.

La versión visible en este `README.md` debe coincidir con el tag publicado del repositorio. Para consumo cross o instalación local, el checkout del tag estable es la fuente canónica descargable.

## Licencia

Este proyecto se distribuye bajo la licencia indicada en [`LICENSE`](LICENSE).

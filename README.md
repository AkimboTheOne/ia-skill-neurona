---
title: mem
project: ia-skill-neurona
description: Módulo de memoria operativa instanciable en Markdown para capturar, curar, conectar y sintetizar conocimiento de proyecto.
status: active
version: 0.1.0
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

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](.)
[![Status](https://img.shields.io/badge/status-active-green.svg)](.)
[![License](https://img.shields.io/badge/license-GPLv3-lightgrey.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-Markdown%20vault-informational.svg)](docs/05-NEURONA/neurona.md)
[![CLI](https://img.shields.io/badge/cli-neurona.sh%20%7C%20neurona.py-orange.svg)](scripts/neurona.sh)

`$mem` es un módulo de memoria operativa en Markdown. Este repositorio contiene la bóveda, la CLI y el contrato del proyecto para capturar ideas, procesarlas, conectarlas y convertirlas en criterio reutilizable.

No es sólo una carpeta de notas. Es un sistema de trabajo para construir memoria de proyecto con estructura, trazabilidad y una capa de síntesis reutilizable.

## Qué Resuelve

- Captura ideas crudas con fricción mínima.
- Organiza la memoria por tipo, no por tema.
- Conecta notas cuando existe un principio, tensión o patrón común.
- Genera briefs cuando la red ya tiene forma comunicable.
- Eleva ideas maduras a `05-NEURONA` cuando ya gobiernan el modelo.

## Para Quién Es

- Equipos o personas que quieren una memoria de proyecto más estructurada que un cuaderno suelto.
- Usuarios que trabajan con agentes LLM y necesitan una bóveda navegable.
- Mantenedores que quieren una superficie clara para instalar, adaptar o instanciar el módulo en otros contextos.

## Qué Hay En Este Repositorio

- `SKILL.md`: contrato de uso del skill.
- `scripts/`: CLI determinista para inicializar, capturar, procesar y resumir memoria.
- `docs/`: bóveda viva del proyecto.
- `references/`: referencias base y plantillas ajustables por caso de uso.
- `agents/`: configuración de agente para consumos externos.

## Uso Rápido

Inicializa la bóveda del repositorio:

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
```

### Smoke test

Ejecuta una mini suite funcional sobre una bóveda temporal para validar el flujo completo:

```bash
bash scripts/mini-suite.sh
```

La suite crea una bóveda efímera en `.tmp/mini-suite-vault`, ejecuta `init`, `status`, `capture`,
`process-inbox`, `connect` y `brief`, y verifica que cada etapa deje artefactos válidos.

## Cómo Está Estructurado

La bóveda vive en `docs/` y se organiza así:

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
- `05-NEURONA`: doctrina, guías e índice del modelo.

## Instancias Y Personalización

El proyecto está diseñado para instanciarse en otros contextos.

- `references/` ofrece una base agnóstica.
- Las instancias pueden ajustar plantillas según caso de uso.
- La personalización vive en la instancia, no en el núcleo del skill.
- La doctrina editorial privilegia lectura humana en superficies narrativas y operabilidad de máquina en superficies técnicas.
- Los títulos del producto usan formato de frase: una sola mayúscula inicial salvo nombres propios o términos que lo exijan.

Eso hace que el módulo sea reutilizable sin perder su forma.

## Casos De Uso

La mini-red operativa de `05-NEURONA` documenta recorridos concretos para automatizaciones con agentes LLM.

- Capturar ideas crudas y convertirlas en capturas tipadas.
- Conectar notas cuando existe una tensión, principio o patrón útil.
- Sintetizar una red madura en briefs reutilizables.
- Elevar criterios estables a neuronas gobernantes del proyecto.

Si quieres ver la guía operativa de esos recorridos:

- [`Índice de ayuda operativa para agentes LLM`](docs/05-NEURONA/indice-de-ayuda-operativa-para-agentes-llm.md)

## Qué Debes Leer Si Vas A Usarlo

- [`SKILL.md`](SKILL.md)
- [`docs/05-NEURONA/neurona.md`](docs/05-NEURONA/neurona.md)
- [`docs/05-NEURONA/doctrina-preferencia-editorial.md`](docs/05-NEURONA/doctrina-preferencia-editorial.md)
- [`docs/05-NEURONA/indice-de-ayuda-operativa-para-agentes-llm.md`](docs/05-NEURONA/indice-de-ayuda-operativa-para-agentes-llm.md)
- [`references/vault-structure.md`](references/vault-structure.md)
- [`references/intelligence-workflows.md`](references/intelligence-workflows.md)
- [`references/editorial-preference.md`](references/editorial-preference.md)

## Primera Versión

Este repositorio ya está en un punto útil para una primera publicación remota:

- contrato del skill definido;
- CLI funcional;
- bóveda estructurada;
- referencias base y plantillas de instancia;
- red de neuronas para operación y criterio.

## Licencia

Este proyecto se distribuye bajo la licencia indicada en [`LICENSE`](LICENSE).

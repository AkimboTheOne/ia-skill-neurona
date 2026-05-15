---
created: 2026-05-15T10:55:00-05:00
type: manifesto
status: active
source: mem operational doctrine
source_file:
  - SKILL.md
  - README.md
  - AGENTS.md
  - scripts/setup-repo-for-agents.sh
  - scripts/agents-healthcheck.sh
tags:
  - mem
  - instancing
  - agent
  - setup
aliases:
  - Modelo de instanciación del skill
  - Instancia local del skill
---

# Modelo de instanciación del skill

## Definición

`$mem` puede instalarse como una composición local del repositorio para agentes de codificación IA. Esa composición no cambia el contrato central del skill: materializa una superficie de entrada, un estado verificable y una forma explícita de recargar contexto cuando cambian las guías.

## Qué Debe Existir

Una instancia local bien formada debe tener, como mínimo:

- `AGENTS.md` como guía canónica para el agente del repo;
- `scripts/setup-repo-for-agents.sh` como materializador de la composición local;
- `scripts/agents-healthcheck.sh` como verificador del último estado;
- `.tmp/agents-setup-state.json` como registro del setup más reciente;
- una superficie de compatibilidad para herramientas del ecosistema cuando haga falta.

## Regla

La composición local no debe inferirse por accidente. Debe poder instalarse, verificarse y recargarse de forma explícita. Si el estado o las guías cambian, el agente debe volver a cargar el contexto o reiniciar la sesión antes de seguir operando.

## Criterio

La instancia es válida cuando:

- el setup puede ejecutarse más de una vez sin romper el entorno;
- el healthcheck devuelve un estado útil y legible;
- la guía del agente deja claro qué leer primero;
- el README explica qué hace la composición local y cuándo recargar contexto;
- el skill sigue sin competir con su propio contrato central.

## Relación Con `docs/` Y `references/`

`docs/` sigue siendo la bóveda del proyecto y `references/` sigue siendo el soporte agnóstico. Este modelo sólo aclara cómo se monta la instancia local para que un agente nuevo pueda orientar la sesión sin adivinar la presencia de archivos, symlinks o copias.

## Relacionado

- [Neurona del Proyecto](neurona.md)
- [Guía operativa canónica para automatizaciones de agentes LLM](guia-operativa-canonica-para-automatizaciones-de-agentes-llm.md)
- [Diagrama de arquitectura instanciable](diagrama-arquitectura-instanciable.md)
- [Alcance de `references/` en el skill `$mem`](alcance-de-references-en-el-skill-mem.md)

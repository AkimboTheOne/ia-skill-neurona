---
created: 2026-05-15T16:00:00-05:00
type: brief
status: draft
source: inbox-synthesis
tags:
  - brief
  - mem
  - governance
  - multi-instance
  - vault
  - mcp
aliases:
  - "Brief: gobernanza multi-instancia y bóveda descendiente"
---

# Brief: gobernanza multi-instancia y bóveda descendiente

## Resumen

Esta línea de trabajo agrupa tres capturas del inbox en un solo mini-proyecto:

1. endurecer el `setup` para que la bóveda viva no se materialice en la raíz;
2. definir una gobernanza multi-instancia para `mem` como proveedor de contexto coordinado;
3. documentar visualmente el patrón multi-repo para que el contrato sea entendible por agentes y humanos.

La idea central es que `mem` deje de verse sólo como una bóveda local y pase a comportarse como una capa de contexto gobernada:

- el skill cross aporta contrato, scripts y referencias;
- la instancia declara qué repo es trabajo y cuál es bóveda;
- la bóveda vive en una carpeta descendiente explícita, por defecto `docs/`;
- la memoria puede consultarse y coordinarse con otras fuentes de contexto.

## Problema

Hoy el diseño tiene dos tensiones:

- el setup puede volver a materializar carpetas espejo en la raíz si se interpreta “repo actual = bóveda”;
- la memoria del proyecto quiere coexistir con otras memorias o contextos, pero todavía no existe una política declarativa clara para múltiples instancias.

Eso deja tres riesgos:

- contaminación del working tree;
- ambigüedad entre contrato del skill y memoria del proyecto;
- falta de una forma explícita de inicializar y coordinar contextos externos.

## Objetivo del mini-proyecto

Definir una política y una interfaz documental para que `mem` pueda:

- inicializar una bóveda descendiente sin contaminar la raíz;
- declarar una instancia con `project_repo`, `vault_repo` y `skill_root`;
- coexistir con múltiples módulos de memoria o contextos externos;
- exponer una superficie de consulta tipo `ask` que permita recuperar evidencia y reabrir stages de la memoria bajo demanda;
- representar el patrón en diagramas y referencias reutilizables.

## Alcance

### Entra

- Ajustes en `scripts/init-repo-vault.sh` y validaciones afines.
- Reglas de setup e instanciación en `SKILL.md`, `AGENTS.md`, `README.md` y `references/`.
- Aclaración de que la bóveda del proyecto vive en un descendiente, no en la raíz.
- Política de multi-instancia y de coexistencia con otras fuentes de memoria o contexto.
- Soporte visual y diagramas para el patrón `skill_root / project_repo / vault_repo`.

### No entra todavía

- Implementación completa de una API o servicio MCP real.
- Query semántico sofisticado sobre toda la bóveda.
- Migración de la bóveda a un formato distinto de Markdown.
- Reescritura del CLI más allá de lo necesario para setup e instancia.

## Preguntas de diseño

1. ¿Debe `init` rechazar cualquier intento de usar la raíz como bóveda activa?
2. ¿Debe el default de instancia ser siempre `docs/` cuando el skill corre en su propio repo?
3. ¿Cómo se declara una instancia alternativa sin romper la política general?
4. ¿Qué parte vive en `references/` como doctrina reusable y qué parte vive en `docs/05-NEURONA/` como criterio operativo?
5. ¿Cómo se expresa una consulta `ask` no semántica sin confundirla con navegación o búsqueda manual?

## Criterio de éxito

El mini-proyecto queda bien cerrado si:

- el setup no vuelve a crear carpetas espejo en la raíz;
- la documentación coincide en que la bóveda vive en un descendiente explícito;
- la instancia puede describir múltiples contextos sin mezclar sus fronteras;
- el soporte visual permite explicar el patrón sin ambigüedad;
- una rama futura puede implementar la feature sin redecidir la política base.

## Lectura recomendada

- [Setup agnóstico y bóveda descendiente](../01-CAPTURES/patterns/20260515-161500-set-up-agnostico-y-boveda-descendiente.md)
- [Gobernanza multi-instancia y API de contexto](../01-CAPTURES/patterns/20260515-161600-gobernanza-multi-instancia-y-api-de-contexto.md)
- [Soporte visual de diagrama multi-repo y gobernanza](../01-CAPTURES/patterns/20260515-161700-soporte-visual-diagrama-multi-repo-y-gobernanza.md)
- [Release de `ask` MVP y gobernanza multi-instancia](20260516-000000-release-nota-ask-mvp-y-gobernanza-multi-instancia.md)

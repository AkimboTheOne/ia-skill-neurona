---
created: 2026-05-15T18:00:00-05:00
type: manifesto
status: active
source: mem operational doctrine
source_file:
  - docs/03-BRIEFS/20260515-160000-mini-proyecto-gobernanza-multi-instancia-y-boveda-descendiente.md
  - docs/01-CAPTURES/patterns/20260515-161500-set-up-agnostico-y-boveda-descendiente.md
  - docs/01-CAPTURES/patterns/20260515-161600-gobernanza-multi-instancia-y-api-de-contexto.md
  - docs/01-CAPTURES/patterns/20260515-161700-soporte-visual-diagrama-multi-repo-y-gobernanza.md
tags:
  - mem
  - governance
  - instancing
  - vault
  - context
aliases:
  - Gobernanza multi-instancia y bóveda descendiente
---

# Gobernanza multi-instancia y bóveda descendiente

## Tesis

`$mem` puede operar como contrato reutilizable con una instancia concreta que declara su bóveda viva de forma explícita.
La raíz del repo no es memoria viva; la bóveda del proyecto vive en un descendiente validado, normalmente `ia-skill-neurona/vault/`.

## Vocabulario mínimo

- `skill_root`: repositorio del skill.
- `project_repo`: repositorio donde trabaja el agente.
- `vault_repo`: bóveda activa descendiente.
- `skill_tmp`: memoria temporal fuera de la red viva.
- `context`: fuente conectada explícitamente.

## Reglas

- No fusionar contextos por defecto.
- No usar la raíz del repo como bóveda activa.
- Si la instancia usa una bóveda alternativa, debe declararla explícitamente.
- `ask` es el MVP de recuperación coordinada y devuelve coincidencias heurísticas por stage.
- Si la instancia publica salidas más legibles para humanos en otro espacio, la bóveda viva sigue siendo la fuente de verdad.

## Relación con la red

La normalización de objetos en la bóveda viva sigue el circuito `00-INBOX -> 01-CAPTURES -> 02-CONNECTIONS -> 03-BRIEFS -> 05-NEURONA`.
Ese circuito distingue captura, curaduría, conexión, síntesis y doctrina. No introduce una tercera red paralela.

## Relacionado

- [Neurona del Proyecto](neurona.md)
- [Modelo de instanciación del skill](modelo-de-instanciacion-del-skill.md)
- [Diagrama de arquitectura instanciable](diagrama-arquitectura-instanciable.md)
- [Alcance de `references/` en el skill `$mem`](alcance-de-references-en-el-skill-mem.md)

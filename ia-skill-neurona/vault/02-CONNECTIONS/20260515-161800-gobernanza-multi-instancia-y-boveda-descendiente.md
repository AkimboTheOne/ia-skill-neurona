---
created: 2026-05-15T16:18:00-05:00
type: connection
status: connected
source: generated
source_file:
  - docs/01-CAPTURES/patterns/20260515-161500-set-up-agnostico-y-boveda-descendiente.md
  - docs/01-CAPTURES/patterns/20260515-161600-gobernanza-multi-instancia-y-api-de-contexto.md
  - docs/01-CAPTURES/patterns/20260515-161700-soporte-visual-diagrama-multi-repo-y-gobernanza.md
tags:
  - connection
  - mem
  - governance
  - vault
  - instancing
aliases:
  - Conexión de gobernanza multi-instancia y bóveda descendiente
---

# Conexión: gobernanza multi-instancia y bóveda descendiente

## Tesis

Las tres capturas apuntan al mismo principio: `$mem` sólo es estable si separa con claridad contrato, instancia, contexto y bóveda viva, y si trata `docs/` como descendiente explícito mientras deja `ask` como frontera futura.

## Evidencia

- La captura de setup exige que la raíz no se convierta en bóveda y que `docs/` sea la bóveda descendiente por defecto.
- La captura de gobernanza multi-instancia exige múltiples contextos explícitos, una frontera de escritura por instancia y un `ask` no semántico aún no materializado.
- La captura visual pide un diagrama donde `skill_root`, `project_repo` y `vault_repo` queden separados para que no haya contaminación entre contrato y memoria viva.

## Tensión resuelta

Antes de la implementación, la arquitectura mezclaba vocabulario de instancia, bóveda y contexto en varias capas. Esta conexión los ordena:

- `skill_root` gobierna contrato y tooling;
- `project_repo` nombra el repo donde trabaja el agente;
- `vault_repo` nombra la bóveda activa descendiente;
- `skill_tmp` queda fuera de la red viva;
- `context` designa fuentes conectadas explícitamente.

## Implicación

La gobernanza ya no se explica como una idea futura, sino como un patrón operativo:

1. no contaminar la raíz;
2. declarar la instancia;
3. separar contextos;
4. visualizar el patrón;
5. dejar `ask` como contrato futuro hasta que exista superficie ejecutable.

## Relacionado

- [Setup agnóstico y bóveda descendiente](20260515-161500-set-up-agnostico-y-boveda-descendiente.md)
- [Gobernanza multi-instancia y API de contexto](20260515-161600-gobernanza-multi-instancia-y-api-de-contexto.md)
- [Soporte visual de diagrama multi-repo y gobernanza](20260515-161700-soporte-visual-diagrama-multi-repo-y-gobernanza.md)

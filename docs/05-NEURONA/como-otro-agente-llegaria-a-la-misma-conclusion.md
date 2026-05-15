---
type: manifesto
status: active
source: mem operational doctrine
source_file: docs/05-NEURONA/neurona.md
tags:
  - mem
  - governance
  - skill
  - llm
aliases:
  - Cómo otro agente llegaría a la misma conclusión
  - Portabilidad de la conclusión
---

# Cómo otro agente llegaría a la misma conclusión

## Tesis

Otro agente puede llegar a la misma conclusión si el skill y sus referencias dejan explícito el modo de lectura del proyecto, no sólo la forma de operar la bóveda.

La conclusión no depende de una memoria privada entre sesiones. Depende de que el contrato del skill y la documentación del proyecto hagan visible:

- qué es la bóveda del proyecto;
- qué es memoria operativa;
- qué es neurona;
- qué es baseline;
- qué vive en `01`, `02`, `03` y `05`;
- qué pertenece a `references/`;
- qué decisiones ya son criterio del sistema.

## Cómo se llegó a esa conclusión

La conclusión surge al combinar tres capas del contrato actual:

1. **Frontera de responsabilidad**
   - El skill pone riendas.
   - El LLM decide significado, contexto, vínculos y síntesis.

2. **Modelo de memoria del proyecto**
   - `baseline` es materia prima histórica.
   - la neurona es la unidad viva curada.
   - la red vive en `01/02/03`.
   - `05-NEURONA` gobierna el modelo.

3. **Uso del proyecto como instancia del skill**
   - `docs/` es una instancia concreta de `$mem`.
   - Otros proyectos pueden instanciar el mismo contrato con contextos y semánticas distintas.
   - La forma se comparte; el significado se ajusta al proyecto.

## Oportunidades de mejora para el skill

Para que la conclusión sea replicable por otro agente, `SKILL.md` debería dejar más explícito:

- que `docs/` es una instancia del skill, no el skill en sí;
- que el skill opera sobre proyectos con semánticas distintas;
- que `05` es memoria operativa del proyecto, no bóveda paralela;
- que `baseline` es fuente madre y materia prima;
- que `references/` es soporte normativo y operativo;
- que `references/` debe ser agnóstica por defecto y ajustable por plantilla según el caso de uso;
- que una neurona es una unidad viva de la memoria del proyecto, no cualquier nota.

## Oportunidades de mejora para `references/`

Las referencias deberían reforzar la reproducibilidad de la lectura:

- `references/vault-structure.md` debe decir con claridad qué vive en cada capa;
- `references/intelligence-workflows.md` debe dejar claro cómo distinguir borrador de conclusión;
- `references/baseline-patterns.md` debe explicitar la relación entre fuente madre, corpus histórico y superficie operativa;
- cualquier nueva referencia debería describir la red del proyecto y no sólo la utilidad de la CLI.

## Criterio práctico

Si estas piezas están bien escritas, otro agente puede llegar a la misma conclusión sin depender de esta conversación:

- entenderá que el skill es reutilizable;
- entenderá que cada proyecto es una instancia distinta;
- entenderá que la memoria es del proyecto, no del agente;
- y podrá decidir con más consistencia cuándo una idea sube a `05`.

## Relacionado

- [Neurona del Proyecto](neurona.md)
- [Alcance de `references/` en el skill `$mem`](alcance-de-references-en-el-skill-mem.md)
- [Fuente consolidada de `docs/baseline`](../01-CAPTURES/patterns/20260513-172100-baseline-source-consolidated.md)

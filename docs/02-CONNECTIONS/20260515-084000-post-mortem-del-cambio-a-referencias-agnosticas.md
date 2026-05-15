---
created: 2026-05-15T08:40:00-05:00
type: connection
status: draft
source: generated
tags:
  - connection
  - postmortem
  - architecture
  - mem
aliases:
  - Post-mortem del cambio a referencias agnósticas
  - Cambio ya aplicado y racionalizado
source_file:
  - docs/01-CAPTURES/patterns/20260515-082227-arquitectura-conceptual-madurez-doctrinal-y-referencias-agnosticas.md
  - docs/03-BRIEFS/20260515-080000-mem-como-producto-instanciable-y-referencias-agnosticas.md
---

# Post-mortem del cambio a referencias agnósticas

## Conexión

La captura procesada sobre [arquitectura conceptual, madurez doctrinal y referencias agnósticas](../01-CAPTURES/patterns/20260515-082227-arquitectura-conceptual-madurez-doctrinal-y-referencias-agnosticas.md) y el brief de [`$mem` como producto instanciable](../03-BRIEFS/20260515-080000-mem-como-producto-instanciable-y-referencias-agnosticas.md) ya no describen una intención futura: juntos registran el cambio que el proyecto necesitaba y que ya fue aplicado en el contrato del skill.

La relación importante no es sólo temática. Es de secuencia operativa:

1. el proyecto ya tenía doctrina suficiente para definir su forma;
2. el skill se ajustó para separar contrato central, referencias agnósticas y plantilla de instancia;
3. la captura original pasó de intuición a patrón procesado;
4. el brief convirtió ese patrón en tesis de producto;
5. el post-mortem fija la decisión como criterio reutilizable.

## Tensión resuelta

Antes del cambio, el riesgo era que `references/` actuara como documentación genérica sin capacidad de adaptación por caso de uso. Después del cambio, la regla quedó más precisa:

- el contrato central permanece estable;
- `references/` da una base agnóstica;
- la instancia puede derivar plantillas ajustadas;
- el agente/LLM propone esos ajustes cuando el uso lo requiere;
- la personalización vive en la instancia, no en el núcleo del skill.

## Criterio que queda

El proyecto ya no debe leerse como un vault con notas y scripts, sino como un producto modular de memoria operativa que puede instanciarse en distintos contextos sin perder sus riendas estructurales.

## Relacionado

- [La arquitectura del proyecto ya es sólida, pero necesita endurecer su implementación](../01-CAPTURES/patterns/20260515-082227-arquitectura-conceptual-madurez-doctrinal-y-referencias-agnosticas.md)
- [Brief: $mem como producto instanciable y referencias agnósticas](../03-BRIEFS/20260515-080000-mem-como-producto-instanciable-y-referencias-agnosticas.md)
- [Diagrama de arquitectura instanciable](../05-NEURONA/diagrama-arquitectura-instanciable.md)

---
created: 2026-05-15T08:00:00-05:00
type: patterns
status: processed
source: generated
source_file:
  - 00-INBOX/20260515-075031-revision-integral-para-refactorizacion-controlada.md
tags:
  - architecture
  - instancing
  - references
  - mem
aliases:
  - Arquitectura instanciable y referencias agnósticas
---

# La arquitectura del skill debe separar contrato base, plantilla de referencias e instancia operativa

## Afinado

El skill debe distribuir su conocimiento en tres capas: un contrato base agnóstico, `references/` adaptables por caso de uso y una instancia operativa que ajuste esos materiales sin perder la forma modular del sistema.

## Expansión

La revisión del proyecto sugiere que la madurez no depende de endurecer todo en un único molde. Depende de distinguir con precisión qué es estable y qué es configurable:

- el contrato base define la forma del skill;
- `references/` aporta doctrina y guías reutilizables;
- la instancia concreta ajusta memoria temporal, documentación o cerebro de trabajo según propósito;
- el agente/LLM debe proponer esos ajustes cuando el contexto lo amerite.

Esto resuelve una tensión práctica: si todo es demasiado genérico, el skill pierde utilidad; si todo es demasiado específico, pierde reutilización. La solución es un núcleo fijo con referencias agnósticas por defecto y plantillas de referencias que se especializan al instalar u operar cada instancia.

## Implicaciones

- Mantener `SKILL.md` como contrato central.
- Tratar `references/` como capa de doctrina base, no como configuración única.
- Definir plantillas de referencias por caso de uso.
- Permitir que la instancia derive o adapte sus referencias operativas.
- Preservar la compatibilidad entre reutilización modular y personalización contextual.

## Relacionado

- [Neurona del Proyecto](neurona.md)
- [Cómo otro agente llegaría a la misma conclusión](como-otro-agente-llegaria-a-la-misma-conclusion.md)
- [Revisión integral del proyecto para refactorización controlada](../../00-INBOX/20260515-075031-revision-integral-para-refactorizacion-controlada.md)

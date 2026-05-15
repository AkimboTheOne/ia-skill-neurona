---
created: 2026-05-13T16:20:01-05:00
type: patterns
status: processed
source: baseline import
source_file: docs/01-CAPTURES/patterns/20260513-172100-baseline-source-consolidated.md
tags:
  - cli
  - skills
  - composability
  - unix
aliases:
  - CLI-First Skill Design
  - diseño de skill primero CLI
---

# El diseño de skill primero CLI mantiene los skills depurables y componibles

- Date: 2026-05-13T16:20:01-05:00
- Type: patterns
- Tags: cli, skills, composability
- Fuente consolidada: 20260513-172100-baseline-source-consolidated.md

## Afinado

Los skills deben exponer primero una CLI porque la misma interfaz puede servir a humanos, agentes, automatización, pruebas y flujos programados sin duplicar superficies de producto.

## Cobertura de Fuente

La fuente completa quedó absorbida en [Fuente consolidada de `docs/baseline`](20260513-172100-baseline-source-consolidated.md).

## Expansión para Agente

La CLI es el denominador común de menor fricción entre la depuración humana y la ejecución por agentes. Hace que el comportamiento sea inspeccionable con comandos de shell, fácil de componer con otras herramientas y fácil de validar en CI.

Para este repositorio, `$mem` ya sigue el patrón: `scripts/neurona.sh` expone subcomandos, devuelve JSON, usa variables de entorno para configuración y mantiene deterministas las operaciones sobre archivos. El siguiente paso de madurez es asegurar que cada comando tenga ayuda estable, códigos de salida documentados y pruebas representativas.

## Implicaciones Operativas

- Mantén un único punto de entrada ejecutable por capacidad del skill.
- Usa subcomandos para acciones en lugar de modos ocultos.
- Pon los datos legibles por máquinas en stdout y los errores en stderr.
- Haz que los comandos sean no interactivos por defecto.
- Soporta configuración basada en variables de entorno para sesiones repetidas.

## Tensiones

Las interfaces de shell son portables y transparentes, pero se vuelven incómodas para grafos de objetos complejos o llamadas de alta frecuencia. Usa primero CLI como valor por defecto; pasa a APIs en proceso sólo cuando el rendimiento o la complejidad lo exijan.

## Relacionado

- [Herramientas y registro primero para agentes](20260513-162000-baseline-agent-first-tooling-and-logging.md)
- [Manifiestos estáticos de servicio](20260513-162004-baseline-static-service-manifest.md)
- [Sistema de Propiedades de Obsidian](20260513-171000-obsidian-properties-system.md)

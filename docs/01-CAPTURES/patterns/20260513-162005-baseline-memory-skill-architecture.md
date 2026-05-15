---
created: 2026-05-13T16:20:05-05:00
type: patterns
status: processed
source: baseline import
source_file: docs/01-CAPTURES/patterns/20260513-172100-baseline-source-consolidated.md
tags:
  - memory
  - vault-design
  - synthesis
  - second-brain
aliases:
  - AI Memory Skill definition
  - arquitectura de sistema de memoria
---

# Los sistemas de memoria sólo compiten cuando captura, almacenamiento e inteligencia están separados

- Fecha: 2026-05-13T16:20:05-05:00
- Tipo: patterns
- Etiquetas: memory, vault-design, synthesis
- Fuente consolidada: 20260513-172100-baseline-source-consolidated.md

## Afinado

Un sistema útil de memoria de IA necesita captura de baja fricción, almacenamiento estable en Markdown y una capa activa de inteligencia que devuelva conexiones, contradicciones, briefs y preguntas al usuario.

## Cobertura de Fuente

La fuente completa quedó absorbida en [Fuente consolidada de `docs/baseline`](20260513-172100-baseline-source-consolidated.md).

## Expansión para Agente

La fuente sostiene que la mayoría de los cerebros secundarios fallan porque optimizan la entrada y descuidan la salida. Una bóveda que sólo almacena notas se convierte en una forma organizada de olvidar. La capa de inteligencia debe procesar periódicamente elementos del inbox, encontrar vínculos entre notas, generar briefs y mostrar preguntas sin depender de que el usuario recuerde qué recuperar.

Esto inspiró directamente a `$mem`, con una adaptación: el repositorio actual comprime el modelo original de cinco carpetas en un contrato de bóveda más ajustado centrado en `00-INBOX`, `01-CAPTURES`, `02-CONNECTIONS`, `03-BRIEFS` y `05-NEURONA`. El principio sigue siendo el mismo: organizar por tipo y no por tema para que dominios no relacionados puedan encontrarse.

## Implicaciones Operativas

- Mantén la fricción de captura cerca de cero.
- Conserva las entradas crudas antes de afinarlas.
- Procesa las notas del inbox en capturas tipadas.
- Ejecuta los flujos de conexión y brief como salidas regulares, no como limpieza ocasional.
- Trata las contradicciones y preguntas como artefactos de memoria de primera clase.

## Tensiones

La automatización puede crear volumen sin insight. El criterio de calidad no es si una nota se archivó, sino si hace más fácil el razonamiento futuro: afirmaciones más afiladas, mejor procedencia, vínculos más fuertes y recuperación más útil.

## Relacionado

- [Sistema de Propiedades de Obsidian](20260513-171000-obsidian-properties-system.md)
- [Conexión: pila de skills nativa para agentes](../../02-CONNECTIONS/20260513-162007-baseline-agent-native-skill-stack.md)
- [Brief: skills nativos para agentes](../../03-BRIEFS/20260513-162008-agent-native-skills.md)

# Conexión: pila nativa de skills para agentes

- Date: 2026-05-13T16:20:07-05:00
- Type: connection
- Tags: agent-native, skill-design, tool-use, obsidian, properties
- Source files:
  - docs/01-CAPTURES/patterns/20260513-171000-obsidian-properties-system.md
  - docs/01-CAPTURES/patterns/20260513-162000-baseline-agent-first-tooling-and-logging.md
  - docs/01-CAPTURES/patterns/20260513-162001-baseline-cli-first-skill-design.md
  - docs/01-CAPTURES/patterns/20260513-162003-baseline-llm-friendly-api-design.md
  - docs/01-CAPTURES/patterns/20260513-162004-baseline-static-service-manifest.md
  - docs/01-CAPTURES/patterns/20260513-162005-baseline-memory-skill-architecture.md
  - docs/01-CAPTURES/patterns/20260513-162006-baseline-pattern-index.md

## Conexión

Los captures convergen en una tesis más concreta que la versión anterior: un skill nativo para agentes no es un prompt ni una carpeta, sino una pila local con cuatro capas coordinadas. Primero, manifiestos y propiedades hacen descubrible el sistema. Segundo, CLI y logging lo hacen ejecutable y depurable. Tercero, la memoria organizada por tipo lo hace acumulativo. Cuarto, el LLM decide la curaduría, los vínculos y el significado.

## Evidencia

- Las propiedades de Obsidian dan una capa estructural para búsqueda, filtrado y auditoría.
- El diseño primero CLI y el registro estructurado vuelven la operación inspectable.
- Los manifiestos estáticos dan un mapa inicial que evita leer todo el corpus.
- La arquitectura de memoria separa captura, almacenamiento e inteligencia para que el sistema componga.
- El índice base funciona como doctrina local que conecta el resto de los patrones.

## Principio expandido

Construye skills como productos locales para agentes. Un buen skill debería responder cinco preguntas sin explicación extra:

1. ¿Qué puedo hacer?
2. ¿Cómo lo invoco?
3. ¿Qué forma de salida debo esperar?
4. ¿Dónde se almacena el estado duradero?
5. ¿Cómo convierto el estado almacenado en mejor razonamiento?

## Consecuencia de diseño para `$mem`

`$mem` debe mantener sincronizadas su CLI, manifiestos, referencias, propiedades y distribución de bóveda. El repositorio debe resistirse a añadir documentos puramente narrativos que no sean ejecutables, referenciables o convertidos en artefactos de memoria procesados.

## Tensión abierta

El Modo Código sugiere mover la orquestación de herramientas de múltiples pasos a código efímero, mientras que el flujo de memoria requiere juicio del LLM entre pasos. La frontera debe ser: usa scripts para movimiento e indexación deterministas; usa el agente para afinado, detección de contradicciones y síntesis.

## Relacionado

- [Sistema de Propiedades de Obsidian](20260513-171000-obsidian-properties-system.md)
- [Diseño de skill primero CLI](20260513-162001-baseline-cli-first-skill-design.md)
- [Herramientas y registro primero para agentes](20260513-162000-baseline-agent-first-tooling-and-logging.md)

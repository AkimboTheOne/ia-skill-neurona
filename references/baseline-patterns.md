# Patrones base

Usa esta referencia al extender el skill, cambiar la CLI o añadir integraciones.

## Contexto

Los documentos originales en `docs/baseline` quedaron absorbidos por la fuente consolidada en español. El directorio histórico puede prescindirse como superficie de trabajo; las capturas procesadas, conexiones, briefs y referencias operativas de `$mem` usan español como idioma de trabajo.

`docs/` es la bóveda del proyecto actual, no el skill. El mismo contrato puede instanciarse en otros proyectos con contextos distintos. La forma se comparte; la semántica se resuelve por instancia.

`references/` debe actuar como doctrina base agnóstica. Las variaciones por caso de uso no cambian el contrato central: se expresan como plantillas de instancia o referencias operativas ajustadas para memoria temporal, memoria documental o memoria tipo “cerebro”.

## Diseño de skill primero CLI

Expón la capacidad reutilizable primero como comandos. Mantén los comandos no interactivos por defecto, usa códigos de salida estables, escribe datos en stdout y errores en stderr.

## Herramientas y registro primero para agentes

Devuelve JSON estructurado para agentes. Incluye suficiente detalle para autocorrección: nombre del comando, ruta de la bóveda, archivos creados, archivos actualizados, advertencias y resumen.

## Diseño de API amigable para LLM

Usa nombres explícitos, parámetros simples, versionado visible y errores accionables. Prefiere comandos directos sobre flujos de interacción anidados.

## Manifiesto estático de servicio para agentes

Publica manifiestos pequeños en la bóveda para que futuros agentes puedan descubrir lo que ofrece el sistema sin leer cada archivo.

## Mejora de interfaz de herramientas MCP en modo código

Al añadir flujos masivos, prefiere código que itere sobre archivos localmente y devuelva resultados condensados. No envíes cada nota intermedia por el contexto del modelo salvo que la calidad de la síntesis lo requiera.

## Descubrimiento de herramientas primero para agentes

Si luego se añaden herramientas remotas o servidores MCP, descríbelos con protocolo, autenticación, capacidades y estado de verificación antes de esperar que los agentes los usen.

## Resolución de contexto

Cuando el skill opere sobre varios contextos, declara explícitamente cuál es la memoria del proyecto, cuál es la memoria temporal del skill y cuáles son los contextos conectados.
No asumas que una instancia puede leer o escribir en otra sin decirlo.

## Versionamiento y release

Cuando una iteración alcance estabilidad, trata el versionamiento como una rienda del proyecto y del agente: captura el alcance, fija la versión visible, valida el setup, y sólo después etiqueta el release. La secuencia canónica vive en [Versionamiento y release](versioning-and-release.md).

## Leer más

Profundiza sólo si necesitas rehacer el contrato de uso o la forma de instanciación:

- [Neurona del Proyecto](../docs/05-NEURONA/neurona.md)
- [Como otro agente llegaría a la misma conclusión](../docs/05-NEURONA/como-otro-agente-llegaria-a-la-misma-conclusion.md)
- [docs/ como bóveda concreta de la instancia actual del skill](../docs/01-CAPTURES/observations/20260514-102952-idea-el-repositorio-docs-de-este-proyecto-es-una-insta.md)
- [El skill puede instanciarse en otros proyectos](../docs/01-CAPTURES/observations/20260514-102952-idea-puede-instanciarse-en-otros-proyectos.md)

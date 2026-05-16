---
created: 2026-05-16T00:00:00-05:00
type: patterns
status: processed
source: inbox
source_file: docs/00-INBOX/20260516-000000-propuesta-servicio-instanciable-fastapi-mcp-y-binding-de-boveda.md
tags:
  - mem
  - fastapi
  - mcp
  - service
  - instancing
aliases:
  - "Patrón: servicio instanciable FastAPI/MCP y binding de bóveda"
---

# Patrón: servicio instanciable FastAPI/MCP y binding de bóveda

## Afinado

El servicio `$mem` debe poder levantarse como una instancia local o permanente con una bóveda declarada explícitamente, primero como FastAPI y después como MCP sobre la misma base.

## Captura cruda

El skill `$mem` debe poder instanciar una bóveda como servicio local o permanente, y ese servicio puede exponerse primero como FastAPI y luego como MCP. La decisión de si el servicio vive como API, como MCP o como ambos debe quedar en manos del LLM que opera el skill, porque el skill provee las riendas y el agente manda sobre la arquitectura concreta de la instancia.

La primera iteración debe ser simple y explícita: un servicio por bóveda, con configuración de la bóveda consumida desde la instancia y el entorno. El contenedor no debe adivinar qué conocimiento leer; debe recibir el repo o ruta de la bóveda de forma declarativa.

La ruta de implementación recomendada es crear una superficie en `plugins/` para el servicio, con una app FastAPI que encapsule la CLI de `$mem` y un contrato preparado para añadir MCP después sin rehacer la base.

También conviene documentar el flujo con un diagrama ASCII y un diagrama Mermaid para que la arquitectura quede visible:

- contrato del skill;
- instancia explícita;
- servicio local o permanente;
- bóveda consumida;
- y punto de extensión hacia MCP.

Esta idea forma parte del objetivo core del skill: operar varias bóvedas o neuronas bajo un mismo contrato, con contexto explícito y sin mezclar memoria viva con contrato del producto.


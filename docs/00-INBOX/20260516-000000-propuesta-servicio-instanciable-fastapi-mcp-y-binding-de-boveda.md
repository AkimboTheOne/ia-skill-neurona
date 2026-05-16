---
created: 2026-05-16T00:00:00-05:00
type: inbox
status: raw
source: manual
tags:
  - capture
  - inbox
  - mem
  - fastapi
  - mcp
  - service
aliases:
  - "Capture: Propuesta de servicio instanciable FastAPI/MCP y binding de bóveda"
---

# Capture: Propuesta de servicio instanciable FastAPI/MCP y binding de bóveda

## Raw

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


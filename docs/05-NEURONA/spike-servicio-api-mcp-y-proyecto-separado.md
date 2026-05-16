---
created: 2026-05-16T00:00:00-05:00
type: manifesto
status: active
source: mem operational doctrine
source_file:
  - docs/00-INBOX/20260516-000000-propuesta-servicio-instanciable-fastapi-mcp-y-binding-de-boveda.md
  - docs/05-NEURONA/diagrama-servicio-instanciable-fastapi-mcp.md
tags:
  - mem
  - spike
  - service
  - fastapi
  - mcp
  - governance
aliases:
  - Spike de servicio API/MCP
  - Servicio API/MCP como proyecto separado
  - Rama spike/mem-api-mcp-service
---

# Spike de servicio API/MCP y proyecto separado

## Decisión actual

La rama `spike/mem-api-mcp-service` concentra el trabajo exploratorio para exponer `$mem` como servicio FastAPI primero y MCP después.

El objetivo de la rama no es fijar que el servicio deba vivir para siempre dentro del repo central. Su función es dejar una referencia operativa completa: requisitos, doctrina, diagrama, scaffold, Docker, scripts de setup, API inicial y pruebas mínimas.

## Tensión detectada

El repo `ia-skill-neurona` gobierna el contrato del skill, su CLI, sus referencias y la bóveda de proyecto. Una API o servidor MCP tiene otro ciclo de vida:

- dependencias de aplicación;
- contenedores;
- puertos;
- pruebas de integración;
- compatibilidad de API;
- posible autenticación;
- despliegue local o permanente;
- y versionado del runtime.

Si esas superficies crecen dentro del repo central, el skill puede perder frontera entre núcleo de memoria y forma de prestación.

## Criterio recomendado

El servicio API/MCP debería extraerse a un proyecto separado cuando deje de ser spike.

La forma recomendada para ese proyecto es:

```text
mem-service/
  Dockerfile
  FastAPI
  MCP
  Makefile
  scripts/
  tests/
  vendor/ia-skill-neurona -> git submodule pinned to tag
```

Ese proyecto debe incorporar `$mem` como submódulo Git fijado a una versión concreta del repo central. El servicio consume el skill como contrato externo, no como código interno mezclado.

## Contrato entre servicio y skill

El servicio debe hablar con `$mem` por la interfaz estable de la CLI:

```bash
scripts/neurona.py status --vault <vault>
scripts/neurona.py capture --vault <vault> --text "..."
scripts/neurona.py process-inbox --vault <vault>
scripts/neurona.py connect --vault <vault>
scripts/neurona.py brief --vault <vault> --topic "..."
```

La API/MCP no debe depender de significado interno ni reinterpretar la bóveda. Debe resolver:

- ruta del skill versionado;
- ruta de la bóveda consumida;
- entorno de runtime;
- exposición FastAPI o MCP;
- traducción mínima de request a comando CLI;
- y respuesta JSON compatible con el contrato existente.

## Estado del spike

La rama contiene:

- captura canónica en `docs/00-INBOX`;
- diagrama ASCII y Mermaid en `05-NEURONA`;
- scaffold `plugins/mem-api`;
- FastAPI funcional sobre la CLI;
- Dockerfile y `docker-compose.yml`;
- `Makefile`;
- scripts bash para `setup`, `build`, `up`, `down`, `logs`, `smoke` y `test`;
- placeholder explícito para MCP;
- y pruebas de humo del binding de instancia.

## Regla de interpretación

`plugins/mem-api` es prototipo interno de referencia, no destino arquitectónico definitivo.

Sirve para completar el aprendizaje de producto dentro de la rama spike. Cuando el contrato se estabilice, el runtime debe moverse a un repo propio y este repo debe conservar sólo:

- contrato del skill;
- CLI determinista;
- documentación de integración;
- referencia al proyecto externo;
- y versión/tag consumible por el servicio.

## Regla de instancia

Mientras el spike viva en este repo, conserva la topología inicial:

- una instancia;
- una bóveda;
- un servicio;
- `NEURONA_VAULT` o `instance.json` como binding explícito;
- FastAPI como primera fachada;
- MCP como extensión posterior.

La operación multi-bóveda sigue siendo el objetivo core a futuro, pero no debe colarse en la primera entrega del runtime.

## Próximo cierre

Para terminar el plan, el spike debe dejar:

1. implementación operable dentro de la rama;
2. documentación clara de por qué el servicio puede salir a otro repo;
3. contrato de submódulo Git fijado a versión;
4. mapa de migración hacia `mem-service`;
5. y validación mínima del flujo Docker/API.

## Relacionado

- [Diagrama de servicio instanciable FastAPI/MCP](diagrama-servicio-instanciable-fastapi-mcp.md)
- [Mapa de migración del spike a `mem-service`](mapa-migracion-spike-a-mem-service.md)
- [Modelo de instanciación del skill](modelo-de-instanciacion-del-skill.md)
- [Diagrama de arquitectura instanciable](diagrama-arquitectura-instanciable.md)
- [Neurona del Proyecto](neurona.md)

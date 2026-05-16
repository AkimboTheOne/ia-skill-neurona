---
created: 2026-05-16T00:00:00-05:00
type: manifesto
status: active
source: mem operational doctrine
source_file:
  - docs/05-NEURONA/spike-servicio-api-mcp-y-proyecto-separado.md
  - plugins/mem-api/README.md
tags:
  - mem
  - spike
  - migration
  - service
  - submodule
aliases:
  - Mapa de migración del spike a mem-service
  - Migración de mem-api a proyecto separado
---

# Mapa de migración del spike a `mem-service`

## Propósito

Este mapa define cómo convertir el spike `plugins/mem-api` en un proyecto separado sin perder el contrato de `$mem`.

## Proyecto destino

```text
mem-service/
  Dockerfile
  docker-compose.yml
  Makefile
  app/
  mcp/
  scripts/
  tests/
  vendor/ia-skill-neurona/
```

`vendor/ia-skill-neurona/` debe ser un submódulo Git fijado a un tag estable del repo central.

## Contrato de dependencia

El servicio no debe importar semántica interna del skill. Debe invocar la CLI versionada:

```bash
vendor/ia-skill-neurona/scripts/neurona.py <command> --vault <vault>
```

La versión del submódulo fija la compatibilidad entre runtime y skill. Si el contrato de salida JSON cambia, el servicio debe subir su compatibilidad de forma explícita.

## Pasos de migración

1. Crear el repo `mem-service`.
2. Añadir `ia-skill-neurona` como submódulo en `vendor/ia-skill-neurona`.
3. Fijar el submódulo a un tag estable del skill.
4. Mover `plugins/mem-api` al layout de aplicación del nuevo repo.
5. Cambiar las rutas internas para resolver la CLI desde `vendor/ia-skill-neurona`.
6. Mantener `NEURONA_VAULT` como binding obligatorio o preferente de bóveda.
7. Ejecutar smoke Docker contra una bóveda montada.
8. Documentar qué versión del skill consume cada release del servicio.

## Qué queda en este repo

El repo `ia-skill-neurona` debe conservar:

- el contrato del skill;
- la CLI determinista;
- la doctrina de instancia;
- la documentación de integración;
- y una referencia al proyecto externo cuando exista.

No debe asumir que el runtime API/MCP vive permanentemente dentro del core.

## Criterio de cierre

La migración está lista cuando `mem-service` puede levantar FastAPI contra una bóveda montada, ejecutar la CLI del submódulo, devolver JSON compatible y declarar la versión exacta de `$mem` que consume.


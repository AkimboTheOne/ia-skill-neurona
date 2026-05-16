# mem-api

Servicio FastAPI inicial para instanciar `$mem` como fachada local sobre una bóveda declarada por instancia.

## Propósito

- Exponer una API sobre la CLI de `scripts/neurona.py`.
- Recibir explícitamente la bóveda a consumir por entorno o configuración de instancia.
- Preparar la evolución hacia MCP sin rehacer el núcleo.

## Convención base

- Una instancia, una bóveda.
- `NEURONA_VAULT` define la bóveda activa en runtime.
- `NEURONA_INSTANCE_FILE` puede apuntar al `instance.json` de la instalación.

## Endpoints base

- `GET /health`
- `GET /config`
- `GET /instance`
- `GET /status`
- `POST /capture`
- `POST /process-inbox`
- `POST /connect`
- `POST /brief`

## Comportamiento

- Si `NEURONA_VAULT` no está definido, la API intenta usar la bóveda declarada en `instance.json`.
- Si tampoco hay instancia, la API cae en `docs/` del repositorio.
- Cada request delega en `scripts/neurona.py` para conservar el contrato operativo del skill.

## Operación local

- `make install` prepara la configuracion local inicial.
- `make setup` crea o reusa `.env`.
- `make build` construye la imagen del contenedor.
- `make up` levanta el servicio.
- `make smoke` valida el endpoint de salud y el binding de bóveda.
- `make test` ejecuta las pruebas del plugin dentro del contenedor.

## Para agentes

- Lee `AGENTS.md` antes de cambiar el plugin.
- Lee `INSTALL.md` para reproducir el setup desde cero.

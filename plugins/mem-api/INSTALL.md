# Instalacion de `mem-api`

## Requisitos

- Docker Desktop o Docker Engine.
- Docker Compose v2.
- `make`.
- Una boveda `$mem` inicializada y montable por el contenedor.

## Setup rapido

```bash
make setup
make smoke
make test
```

`make setup` crea `.env` desde `.env.example` si no existe.

## Configuracion

La configuracion minima vive en `.env`:

```bash
NEURONA_VAULT=/vault
NEURONA_INSTANCE_FILE=/vault/05-NEURONA/instance.json
NEURONA_MODE=service
NEURONA_SERVICE_KIND=fastapi
NEURONA_SERVICE_NAME=mem-api
```

En el spike actual, `docker-compose.yml` monta `../../docs` como `/vault`.
En un repo externo, ese volumen debe apuntar a la boveda real de la instancia.

## Operacion

```bash
make up
make logs
make down
```

El servicio queda disponible en `http://127.0.0.1:8000`.

## Migracion futura

Cuando el runtime salga a `mem-service`, instala `ia-skill-neurona` como submodulo Git:

```bash
git submodule add <repo-url> vendor/ia-skill-neurona
git -C vendor/ia-skill-neurona checkout <tag>
```

El servicio debe invocar:

```bash
vendor/ia-skill-neurona/scripts/neurona.py <command> --vault <vault>
```


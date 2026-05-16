# AGENTS.md

Guia para agentes que trabajan en `plugins/mem-api`.

## Proposito

`mem-api` es un spike de servicio FastAPI para exponer `$mem` sobre una boveda declarada por instancia. Su destino probable es migrar a un repo separado como `mem-service`, consumiendo `ia-skill-neurona` como submodulo Git fijado a tag.

## Orden de lectura

1. `README.md`
2. `.env.example`
3. `Makefile`
4. `scripts/setup.sh`
5. `app.py`
6. `mcp/README.md`

## Reglas

- Conserva una instancia, una boveda, un servicio.
- No dupliques logica de `scripts/neurona.py`; delega en la CLI del skill.
- Usa `NEURONA_VAULT` como binding preferente de boveda.
- Trata MCP como adaptador futuro sobre la misma base, no como contrato paralelo.
- Si este spike migra a repo externo, cambia la ruta de la CLI a `vendor/ia-skill-neurona/scripts/neurona.py`.

## Validacion

```bash
make setup
make smoke
make test
```


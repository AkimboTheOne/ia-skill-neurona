---
created: 2026-05-15T15:35:00-05:00
type: inbox
status: raw
source: manual
tags:
  - capture
  - inbox
  - mem
  - governance
  - multi-instance
  - mcp
aliases:
  - "Capture: Propuesta de gobernanza multi-instancia y API de contexto"
---

# Capture: Propuesta de gobernanza multi-instancia y API de contexto

## Raw

El siguiente paso de `$mem` no debería ser sólo endurecer setup o limpiar la raíz del repo. La iteración siguiente ya apunta a una gobernanza multi-instancia: un proyecto de memoria puro deja de ser sólo una bóveda local y pasa a ser una fuente de contexto, utilizable como módulo, API o servicio MCP para otros agentes o repositorios.

La idea central es que podamos tener múltiples módulos de memoria coexistiendo como proveedores de contexto. Cada uno expone una superficie de uso distinta, pero todos deben poder coordinarse bajo una disciplina común. En ese escenario, `$mem` no sólo administra una bóveda; también ayuda al modelo LLM a inicializar conexiones MCP hacia otros contextos que quiera usar coordinadamente dentro de una misma sesión o flujo de trabajo.

Esto sugiere una feature mayor, no una nota menor:

1. Un skill de memoria no debería asumir que existe una sola bóveda.
2. Debería poder declarar y gobernar varias instancias de memoria.
3. Debería asistir al agente para conectar contextos externos de manera explícita, no implícita.
4. Debería permitir que cada instancia tenga su propio contrato de uso, su propio modo de exposición y su propia frontera de escritura.

Además, falta una capacidad reflexiva de consulta:

- memoria y neuronas deberían admitir un `ask` o query no semántico;
- ese query no sería “buscar por significado” en sentido puro, sino recuperar material útil para que el modelo llegue a conclusiones nuevas;
- el query debería permitir re-abrir la memoria en cualquiera de sus stages bajo demanda: inbox, capturas, conexiones, briefs o neuronas;
- también debería poder actuar como apoyo para el razonamiento del modelo cuando necesita evidencias, contraste o contexto antes de seguir operando.

La hipótesis de diseño es que el sistema de memoria no sólo almacena y madura contenido, sino que también se deja consultar como infraestructura de razonamiento. Eso implica que la gobernanza multi-instancia y la query capability están relacionadas:

- múltiples fuentes de contexto;
- múltiples instancias de memoria;
- una forma clara de orquestarlas;
- y un mecanismo para preguntarle a la memoria qué necesita el modelo en ese momento.

La pregunta de fondo es si esta feature debe materializarse como:

- una doctrina en `05-NEURONA`;
- una ampliación de `references/` sobre policy de instancia;
- un contrato de `agent.json` / `instance.json` para multi-contexto;
- y/o una capa futura de interfaz tipo MCP/API para discovery, query y coordinación.

Objetivo de la iteración:

- convertir `mem` en una pieza de gobernanza multi-instancia, no sólo en una bóveda local;
- permitir que el agente CLI decida cómo inicializar o conectar contextos de memoria de forma explícita;
- dar al modelo una capacidad de pregunta y recuperación que no dependa sólo de navegación humana;
- preparar el skill para coexistir con otros módulos de memoria, propios o externos, como fuentes de contexto coordinadas.

La implementación debería dejar claro qué es:

- fuente de contexto;
- instancia de memoria;
- conexión externa;
- consulta sobre memoria;
- y promoción de resultados a un stage superior.

Si esta idea madura, la próxima rama no debería tratarla como documentación auxiliar, sino como feature de plataforma para memoria coordinada.

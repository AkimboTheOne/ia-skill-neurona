# Plantillas del loop operativo

Usa esta referencia cuando un agente necesite operar `$mem` sin conocer la semántica interna de la bóveda.

## Principio

El skill entrega estructura, índices y plantillas. El agente conserva el control del contexto, decide qué importa y escribe la síntesis final.

El loop operativo mínimo es:

`preparar -> operar -> cerrar`

Antes de operar, el agente recupera contexto suficiente. Durante la operación, usa la plantilla de fase como andamio. Al cerrar, deja handoff explícito para que otra sesión pueda continuar sin reconstruir la conversación completa.

## Uso desde CLI

```bash
scripts/neurona.sh templates list
scripts/neurona.sh templates show --phase prepare
scripts/neurona.sh templates show --phase conversation
```

Las plantillas son ayudas para el agente, no validadores semánticos. Si una sección no aplica, el agente debe decirlo en la nota en vez de borrarla silenciosamente.

## Fases

- `prepare`: recuperar contexto, frontera de escritura y siguiente operación.
- `capture`: guardar entrada cruda con procedencia y señales de madurez.
- `conversation`: consolidar una conversación como síntesis densa.
- `connect`: justificar una relación fuerte entre notas.
- `brief`: sintetizar una red madura con prueba explícita.
- `close`: dejar resultado, relaciones, pendientes y criterio de elevación.

## Conversaciones

Cuando el usuario pida guardar una conversación en `$mem`, no guardes un resumen escueto. Prepara una síntesis densa con:

- contexto operativo;
- resumen sustantivo;
- decisiones;
- evidencia y enlaces;
- relaciones sugeridas;
- pendientes;
- próximos pasos;
- riesgos;
- transcripción relevante.

La transcripción relevante no es el chat completo por defecto. Es el mínimo material que permite auditar lo que se decidió.

## Índices y relaciones

El agente debe tratar los índices y relaciones como componentes estrictos del handoff:

- usar `conversation_id` cuando una conversación pueda actualizarse;
- nombrar notas fuente cuando una conexión o brief depende de evidencia local;
- declarar relaciones sugeridas aunque todavía no se materialicen;
- separar pendientes de decisiones tomadas;
- no elevar a `05-NEURONA` si la idea todavía no gobierna el modelo.

## Cierre

Un cierre útil debe permitir responder:

- qué cambió o qué se aprendió;
- qué evidencia sostiene el cambio;
- qué queda pendiente;
- qué debería conectarse;
- si el criterio debe permanecer en `01/02/03` o subir a `05-NEURONA`.

## Relacionado

- [Estructura de la bóveda](vault-structure.md)
- [Flujos de inteligencia](intelligence-workflows.md)
- [Plantilla de referencia de instancia](instance-reference-template.md)

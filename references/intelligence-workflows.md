# Flujos de inteligencia

Usa esta referencia al producir conexiones, briefs o síntesis desde una bóveda Neurona.

## Frontera de responsabilidad

El skill pone riendas: restringe estructura y movimiento, pero no decide significado. Los scripts sólo proveen operaciones deterministas, heurísticas simples y andamiajes de borrador; el LLM decide contenido, vínculo, síntesis y prosa final.
Trata las salidas de `connect` y `brief` como puntos de partida, no como conclusiones autoritarias. La curaduría compacta la red sin perder evidencia.

## Instancias y contextos

`$mem` puede instanciarse como CLI cruzado, plugin de otro proyecto, instancia de trabajo sobre su propio proyecto o servicio futuro. Cada instancia declara una bóveda activa, una memoria temporal de trabajo y uno o más contextos conectados.

No fusionar memorias por defecto. Si la fuente no se identifica con claridad, el LLM debe tratarla como contexto local y decidir su valor explícitamente.

## Referencias y plantillas

Las referencias de este skill tienen dos usos:

- una base agnóstica que preserva el contrato común;
- una plantilla ajustable por caso de uso que la instancia puede adoptar o refinar.

El agente/LLM debe proponer ajustes cuando la instancia necesite una de estas orientaciones:

- memoria temporal de trabajo;
- memoria documental;
- memoria tipo “cerebro” o conocimiento operativo;
- otro caso de uso con preferencias o personalización explícitas.

La regla es no romper el espíritu modular del skill: la plantilla orienta, la instancia adapta y el contrato central permanece estable.

## Gobernanza multi-instancia

El contrato de esta fase no implementa una API de consulta completa. Sí fija el vocabulario mínimo para que la
instancia pueda declararse sin ambigüedad:

- `skill_root`: repositorio del skill.
- `project_repo`: repo donde el agente está trabajando.
- `vault_repo`: bóveda activa descendiente, por defecto `ia-skill-neurona/vault/`.
- `skill_tmp`: memoria temporal fuera de la red viva.
- `context`: fuente conectada explícitamente.

No fusionar contextos por defecto. Si una fuente no está identificada, trátala como local hasta que el LLM decida su valor y su frontera de escritura.

`ask` queda como contrato futuro de recuperación guiada. En esta iteración sólo se documenta la intención y la
separación de responsabilidades entre consulta, navegación y síntesis.

## Procesamiento del inbox

Clasifica cada nota cruda en un tipo de captura:

- `observations`: hecho observado o experiencia.
- `reactions`: respuesta subjetiva, preferencia, duda o desacuerdo.
- `patterns`: principio reutilizable o estructura repetida.
- `questions`: pregunta no resuelta.
- `numbers`: dato numérico o métrica concreta.

Afina cada nota en una sola oración que pueda sostenerse sin contexto oculto. Añade exactamente tres etiquetas.
Si la oración generada por la CLI es superficial, reescríbela con juicio del LLM preservando la captura cruda.
Si la clasificación o el destino de la CLI es incorrecto, mueve la nota al mejor lugar y preserva la procedencia.

## Criterio de calidad de conexiones

Prefiere menos conexiones, pero más fuertes. Una conexión es fuerte cuando sorprende, resulta útil y está respaldada por notas fuente específicas.

Tipos de conexión:

- `same-principle`: un principio aparece en dos dominios distintos.
- `contradiction`: dos notas crean tensión.
- `pattern`: tres o más notas apuntan a un insight mayor sin nombre.
- `question-answer`: una nota pregunta algo que otra nota ayuda a responder.

No aceptes resúmenes que sólo repitan las notas.
No aceptes coincidencias de palabras de la CLI como conexión fuerte salvo que la revisión del LLM confirme la idea subyacente.

## Forma del brief

Crea briefs con exactamente cinco campos:

```markdown
# Brief: tema

## ONE THING
Una sola oración.

## PROOF
La evidencia, número o ejemplo más concreto disponible.

## READER TRANSFORMATION
Qué entiende el lector después de leer.

## THREE HOOKS
1. Gancho agresivo.
2. Gancho curioso.
3. Gancho personal.

## THREE CLOSERS
1. Cierre urgente.
2. Cierre memorable.
3. Cierre reflexivo.
```

Si la prueba es débil, dilo directamente y nombra la evidencia faltante.
El brief no compite con la red: la comprime para que otro agente pueda entender el criterio sin rehacer el recorrido completo.

## Madurez de neurona

Sube una idea a `05-NEURONA` sólo cuando deje de ser una intuición y pase a ser criterio del proyecto:

- define una regla;
- aclara una frontera;
- explica un modo de uso;
- o estabiliza cómo leer la red del proyecto.

Si sólo ayuda a pensar, permanece en `01`, `02` o `03`.

## Leer más

Cuando el contexto te obligue a distinguir entre memoria del proyecto, memoria temporal del skill e instancias múltiples, profundiza en:

- [Neurona del Proyecto](neurona.md)
- [Alcance de `references/` en el skill `$mem`](alcance-de-references-en-el-skill-mem.md)
- [ia-skill-neurona/vault/ es la bóveda concreta de la instancia actual del skill](20260514-102952-idea-el-repositorio-docs-de-este-proyecto-es-una-insta.md)
- [El skill puede instanciarse en otros proyectos](20260514-102952-idea-puede-instanciarse-en-otros-proyectos.md)

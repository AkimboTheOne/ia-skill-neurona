---
type: source
kind: original-article
status: curated
source: x article
source_file: docs/baseline/AI Memory Skill definition (inspiration).md
reference: https://x.com/Sprytixl/article/2054161677508129265
tags:
  - baseline
  - memory
  - source
  - claude
aliases:
  - AI Memory Skill definition
  - baseline memory source
---

# AI Memory Skill definition (inspiration)

## Curaduría

Artículo original histórico que inspira la arquitectura de memoria de `$mem`. La fuente validada es un X article; la superficie operativa curada está en la [Fuente consolidada de `docs/baseline`](20260513-172100-baseline-source-consolidated.md).

La mayoría de las personas pierde entre 30 y 40 minutos en cada sesión de Claude reexplicando lo que ya sabía desde ayer. Eso equivale a perder una jornada laboral completa por semana en repetición. Cada sesión arranca desde cero. Tu arquitectura, tus convenciones, ese caso límite que Claude depuró durante una hora, desaparecen cuando la ventana se cierra.

Las personas que entendieron esto dejaron de tratar Obsidian como una app para tomar notas. Construyeron un sistema de memoria. Claude lo lee, lo conecta, te entrega briefs cada mañana y se vuelve más útil cada día que agregas material sin hacer trabajo extra.

Este es el sistema exacto. Cada archivo. Cada prompt. Cada automatización.

## Por qué mueren todos los segundos cerebros de la misma manera

Empiezas organizado. Dos semanas después, el mantenimiento se acumula: actualizar etiquetas, mantener al día las referencias cruzadas, reorganizar cuando la estructura evoluciona. Eso suma trabajo adicional sobre una carga ya completa, así que lo postergas, el sistema se degrada y vuelves a notas dispersas. Seis meses después intentas reconstruirlo y el ciclo se repite.

El modo de falla siempre es el mismo. El sistema está diseñado para entrada. Nadie diseña para salida. Capturas todo. No recuperas nada. La bóveda crece. Tu pensamiento no.

Un segundo cerebro que nunca responde no es un segundo cerebro. Es una manera muy ordenada de olvidar cosas.

Tres cosas específicas matan cualquier sistema de conocimiento, y las tres se pueden corregir. Fricción de captura: si agregar algo toma más de 10 segundos de esfuerzo manual, te detendrás bajo carga cognitiva real. Sin capa de conexión: la mayoría de las bóvedas son colecciones de notas aisladas sin un mecanismo que mire todo y exponga lo que importa hoy. Sin razón para volver: si la bóveda no te devuelve ideas, tú debes recordar ir a buscarlas. Nadie recuerda.

Claude rompe este ciclo de forma permanente. El mantenimiento es sólo un comando. El trabajo humano es curar fuentes y hacer buenas preguntas. El trabajo de Claude es todo lo demás.

## La arquitectura: cuatro capas, una dirección

Antes de tocar cualquier herramienta, entiende la estructura. Cada pieza de software cumple exactamente una función. Nada se superpone. Todo fluye en una sola dirección.

```text
Layer 4: Intelligence (Claude)
reads vault, connects, briefs, writes

Layer 3: Storage (Obsidian vault)
markdown files, permanent ground truth

Layer 2: Pipeline (N8N automation)
routes captures to correct vault folder

Layer 1: Capture (Readwise, Airr, bot)
everything in, zero manual effort
```

Si omites una capa, las demás se degradan. Comparten efecto o no funcionan.

[Imagen](https://x.com/Sprytixl/article/2054161677508129265/media/2054160372752351232)

## 

## Parte 1 - Captura: cero fricción o el sistema se rompe

La capa de captura tiene una sola tarea: recogerlo todo sin pedirte nada. Cada punto de fricción al capturar es una futura brecha en tu base de conocimiento. Configúralo una vez. No lo toques de nuevo.

Artículos y destacados: Readwise es la base. Instala la extensión del navegador. Cada artículo que leas, resalta las frases que importan. Readwise las guarda automáticamente. Sin resumir, sin etiquetar, sin categorizar. Sólo resalta y sigue. Readwise también conecta con Kindle, marcadores de Twitter, Instapaper y Pocket. Una herramienta agrupa todo desde todas las plataformas.

Podcasts and audio - Airr lets you clip podcast moments with a shake of your phone. The transcript saves automatically. For meetings, lectures and voice notes - record and run through Whisper. Paste the audio file and get a clean transcript in seconds. A raw transcript is noise - thousands of filler words and false starts. A structured knowledge note is signal. From a single 90-minute conference talk this pipeline typically extracts 12-18 distinct claims, 3-5 named frameworks and 5-8 actionable techniques.

Quick capture from anywhere - build a Telegram bot that accepts any message you send and routes it to your vault's inbox folder automatically. An idea that hits you in the car. A tweet you want to think about. A question that comes up in conversation. Send it to the bot. It lands in your vault within seconds. Takes 30 minutes to build once with Claude Code and N8N:

```text
Node 1: Telegram Trigger - event: message - chat_id: your_bot_id
Node 2: Code (format note) - filename: inbox/{{date}}-capture.md
        content: # Quick Capture / {{message}} / Date: {{date}}
Node 3: Write File - path: /your-vault/inbox/ - operation: create
```

## Parte 2 - Estructura de la bóveda: cinco carpetas, una regla

La estructura de carpetas determina qué tan bien navega Claude la bóveda. No sobreingenierices esto. Cinco carpetas. Esa es toda la estructura.

```text
your-vault/
- 00-INBOX/          # everything lands here first, unprocessed
- 01-CAPTURES/       # processed highlights, articles, clips
  - observations/    # things you noticed
  - reactions/       # your gut response to something
  - patterns/        # same principle in two different domains
  - questions/       # things you genuinely don't know
  - numbers/         # real data points with specific numbers
- 02-CONNECTIONS/    # synthesized insights from 2+ captured notes
- 03-BRIEFS/         # content ready to write, hook and closer done
- 04-PUBLISHED/      # archived content with performance data
- 05-CLAUDE/         # CLAUDE.md, skills, context
```

The most important architectural decision: organize by type not by topic. When you organize by topic a note about AI content strategy and a note about how attention works psychologically never meet. When you organize by type they both land in the patterns folder and Claude finds the connection automatically. This single decision is what makes the connection layer work.

One rule: when in doubt put it in inbox. Simplicity is intentional. Every complex folder structure eventually collapses under its own weight because you stop knowing which folder something belongs in and the capture friction rises until the system breaks.

## Parte 3 - CLAUDE.md: el archivo más importante del sistema

Sin este archivo, Claude empieza cada sesión en frío, sin contexto sobre quién eres, en qué estás trabajando ni qué quieres de la bóveda. Con un `CLAUDE.md` sólido actúa como un colaborador que ha estado leyendo tus notas durante meses.

`CLAUDE.md` vive en la raíz de tu bóveda. Claude lo lee automáticamente al iniciar cada sesión. Copia esta plantilla directamente:

```text
# SYSTEM - CLAUDE.md

## Identidad
Nombre: [tu nombre]
Trabajo: [qué haces, con precisión]
Enfoque: [la única cosa en la que intentas mejorar ahora]
Metas: [3 resultados concretos que buscas este año]

## Proyectos Actuales
Activo: [qué estás construyendo ahora]
Atascado en: [dónde necesitas más ayuda de pensamiento]
Próximo hito: [cómo se ve terminado el sprint actual]

## Estructura de la Bóveda
- 00-INBOX: capturas sin procesar, revisa siempre primero aquí
- 01-CAPTURES: organizado por tipo, no por tema
- 02-CONNECTIONS: ideas sintetizadas desde notas enlazadas
- 03-BRIEFS: contenido listo para escribir
- 04-PUBLISHED: contenido archivado con datos de desempeño

## Mi Voz
[describe tu estilo de escritura con precisión]
Frases cortas y contundentes. Los números reales siempre le ganan a las afirmaciones vagas.
Sin relleno. Cada frase gana su lugar.

## Reglas Duras
- Nunca leas ni modifiques archivos `.env`
- Nunca modifiques `04-PUBLISHED` sin instrucción explícita
- Nunca crees carpetas fuera de la estructura establecida
- Cuestiona mis supuestos antes de estar de acuerdo con ellos

## Lo Que Quiero De Ti
- Expón conexiones que no he visto
- Cuando te pregunte en qué enfocarme, responde desde el contexto de la bóveda, no genéricamente
- Señala cuando algo que creo contradice algo que guardé antes
- Actualiza la sección `Proyectos Actuales` cada lunes
```

Actualiza la sección `Proyectos Actuales` cada lunes en la mañana. Cinco minutos. Este solo hábito mantiene el contexto de Claude preciso mientras tu trabajo evoluciona. Un `CLAUDE.md` viejo produce respuestas viejas.

## Parte 4 - Cuatro habilidades que ejecutan todo el sistema

Una habilidad es un flujo de trabajo reutilizable almacenado como archivo Markdown en tu carpeta `05-CLAUDE/skills/`. La llamas por nombre y Claude ejecuta el proceso completo cada vez. Estas cuatro cubren el 90% de lo que hace el sistema.

[Imagen](https://x.com/Sprytixl/article/2054161677508129265/media/2054160501890805760)

Habilidad 1 - Procesar Inbox (disparador: "process my inbox"):

```text
1. Lee cada nota en `00-INBOX/`
2. For each note:
   a. Determine which CAPTURES subfolder it belongs to
   b. Sharpen the raw note into one punchy sentence
   c. Add exactly three tags - no more, no fewer
   d. Move the sharpened note to the correct subfolder
3. Después de procesar todas las notas, entrega:
   - Total de notas procesadas y destino de cada una
   - Cualquier patrón detectado entre las capturas de hoy
   - Una conexión que valga la pena explorar a partir del lote de hoy

Barra de calidad: una nota afinada debe ser lo bastante específica
como para que un desconocido entienda exactamente qué se observó
sin contexto adicional. Si aún necesita explicación, no está lo
suficientemente afinada. Reescríbela.
```

Habilidad 2 - Conexiones semanales (disparador: "run connection session"):

```text
1. Lee todas las notas agregadas a `01-CAPTURES/` en los últimos 7 días
2. Busca conexiones entre TODAS las subcarpetas al mismo tiempo
3. Una conexión fuerte es uno de estos cuatro tipos:
   TIPO A: mismo principio subyacente en dos dominios distintos
   TIPO B: contradicción entre dos notas que crea tensión
   TIPO C: patrón que conecta 3+ notas en una sola idea sin nombre
   TIPO D: una pregunta de una nota que otra nota responde

Barra de calidad: si la conexión es obvia, no califica.
Sólo expón conexiones que realmente sorprenderían
a la persona que escribió las notas.
Mínimo 3 conexiones. Máximo 5. Calidad sobre cantidad.
```

Habilidad 3 - Generar Brief (disparador: "generate a brief for [topic]"):

```text
Crea un brief de contenido con exactamente cinco campos:

UNA SOLA COSA - la única idea sobre la que se construye la pieza.
Debe ser una sola oración. Cuestiona si está difusa.

PRUEBA - el ejemplo o número real más específico que
demuestre la única cosa. Sólo números reales. Una prueba vaga
invalida el brief.

TRANSFORMACIÓN DEL LECTOR - ¿qué sabrá el lector al final que
no sabía antes? Si no puede decirse con claridad, la pieza no
tiene razón de existir.

## Tres Ganchos

- Gancho 1: agresivo.
- Gancho 2: curioso.
- Gancho 3: personal.

## Tres Cierres

- Cierre 1: el más urgente.
- Cierre 2: el más memorable.
- Cierre 3: el más breve y afilado.

El cierre se escribe antes del cuerpo. Siempre.
```

## Habilidad 4 - Escribir contenido

Disparador: "write the brief for [topic]"

```text
1. Lee el brief especificado en `03-BRIEFS/`.
2. Lee todas las notas fuente enlazadas en el brief.
3. Escribe la pieza completa con la voz exacta del usuario desde `CLAUDE.md`.
4. Estructura: gancho, prueba, cuerpo, cierre.
5. Cada sección debe aportar valor específico. Sin relleno.
6. El resultado debe sonar indistinguible del contenido que el usuario habría escrito.
```

## Parte 5 - El ritual diario: 20 minutos, se ejecuta solo

Así se ejecuta el sistema cada mañana. Tiempo total: veinte minutos. La mayor parte del tiempo Claude trabaja mientras tú lees.

Minutos 1-5 - captura. Antes de abrir cualquier otra cosa, dedica cinco minutos a añadir capturas crudas a `00-INBOX`. Transcripciones de notas de voz. Cosas que notaste. Un número que viste. Una reacción a algo que leíste anoche. Crudo. Sin pulir. Sólo ingrésalo.

Minutos 6-10 - proceso. Ejecuta la habilidad de procesar inbox. Lee el reporte. Observa qué se archivó y qué patrones detectó Claude entre las capturas de hoy.

Minutos 11-15 - conexión. Pregunta: "¿Hay conexiones fuertes entre las capturas de hoy y algo de mi bóveda de los últimos 14 días?" Este es el momento JARVIS: el sistema piensa a través de tu historia reciente y expone lo que pertenece junto.

Minutos 16-20 - brief. "Generate a brief for the connection about [la que más te sorprendió]." Listo. Tienes un brief de contenido antes de abrir cualquier red social. El resto del día es ejecución, no ideación.

## Parte 6 - El brief diario que corre automáticamente

Cada mañana, antes de abrir una sola app, la bóveda te entrega un brief. Nuevas conexiones encontradas durante la noche. Patrones entre las capturas de esta semana. La única pregunta que vale la pena pensar hoy. No lo pides: corre automáticamente por N8N a las 6:00 a. m. Cuando te sientas, ya está esperando en tu inbox.

Configura este prompt dentro de tu nodo Claude en N8N con un horario diario de 6:00 a. m.:

```text
Estás leyendo mi bóveda de conocimiento de Obsidian. Lee todo
lo que esté en `/inbox` de las últimas 24 horas y todo lo que
esté en `/notes` de los últimos 7 días.

Luego haz tres cosas:

CONEXIONES - Encuentra las 3 conexiones más interesantes
entre capturas recientes y notas viejas que probablemente no
haya notado. Sé específico. Cita los pasajes relevantes.

PATRÓN - Identifica un patrón en todo lo que he estado
leyendo esta semana. ¿En qué está trabajando claramente mi
mente aunque no lo haya dicho explícitamente?

PREGUNTA - Dame una pregunta que valga la pena sostener hoy
basada en el patrón que identificaste. No una tarea. Una pregunta.

Escribe esto como un archivo Markdown limpio, formateado para Obsidian.
Guárdalo en `/inbox/brief-{{date}}.md`.
```

Léelo antes de abrir cualquier otra cosa. Este solo hábito vale más que todo lo demás de esta guía junto.

## Parte 7 - La síntesis semanal que compone todo

Una vez por semana siéntate con Claude durante 15 minutos y habla sobre hacia qué ha estado apuntando la bóveda. Ejecuta este prompt:

```text
Lee toda mi bóveda de Obsidian. Enfócate en todo lo agregado
durante los últimos 7 días.

TESIS EMERGENTE - ¿Hacia qué idea me estoy moviendo sin
haberla formulado explícitamente todavía?

CONTRADICCIONES - ¿Qué he guardado recientemente que contradice
algo que creía antes? Muéstrame ambos lados desde mis propias notas.

VACÍOS DE CONOCIMIENTO - Con base en lo que estoy leyendo, ¿qué
no estoy leyendo claramente y debería leer? ¿Qué perspectiva
falta?

UNA ACCIÓN - Dado todo lo que hay en esta bóveda, ¿cuál es la
única acción de mayor apalancamiento que podría hacer esta semana?

Sé directo. Desafíame. No resumas lo que ya sé.
```

La sesión de síntesis es donde ocurre el verdadero efecto compuesto. El brief diario expone conexiones. La síntesis semanal construye una tesis. Después de seis meses de sesiones semanales tienes un registro de cómo evolucionó tu pensamiento.

## El efecto compuesto

A un mes la bóveda se siente como una herramienta útil. A los tres meses Claude empieza a conectar cosas del mes uno con cosas del mes tres, encontrando esa nota relevante de hace ocho semanas que habías olvidado por completo. A los seis meses tienes un registro de cada creencia que sostuviste y cambiaste.

```text
Sin este sistema:
Reexplicar contexto:       30-40 min por sesión
Perdido por semana:        1 jornada laboral completa
Sesiones que reinician:    100%
Conocimiento acumulado:    0%

Con este sistema:
Inicio de sesión:         0 min reexplicando
Brief diario:             automático, esperando cuando despiertas
Conocimiento que compone:  cada día
```

La IA que tienes después de seis meses no es la misma con la que empezaste. Ha estado leyendo tu pensamiento mientras tú estabas ocupado viviendo tu vida. Tu competidor que empieza seis meses después no sólo va detrás en la configuración: va detrás de seis meses de conexiones, patrones y síntesis que hacen que el sistema sea realmente inteligente respecto a tu forma específica de pensar. Esa brecha no se cierra trabajando más duro. Sólo se cierra empezando antes.

La mayoría de las personas empieza desde cero todos los días. Este sistema se asegura de que tú nunca vuelvas a hacerlo.

La mayoría lee. Unos pocos actúan. La brecha entre ambos se compone todos los días.

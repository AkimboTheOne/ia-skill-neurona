---
created: 2026-05-15T16:15:00-05:00
type: patterns
status: processed
source: inbox
source_file: docs/03-BRIEFS/20260515-160000-mini-proyecto-gobernanza-multi-instancia-y-boveda-descendiente.md
tags:
  - pattern
  - capture
  - mem
  - setup
  - vault
aliases:
  - Setup agnóstico y bóveda descendiente
---

# Setup agnóstico y bóveda descendiente

## Sharpened

El setup de `$mem` debe rechazar la raíz como bóveda activa y tratar `docs/` como bóveda descendiente por defecto para preservar la frontera entre contrato y memoria viva.

## Raw Capture

Necesitamos una feature doctrinal y de implementación para cerrar la tensión entre setup, bóveda del proyecto y uso del skill como herramienta cross.

La inquietud central es esta: el setup de `$mem` no debe contaminar la raíz del repositorio ni convertirla en bóveda activa por accidente. La bóveda viva del proyecto debería vivir en una carpeta descendiente explícita, por defecto `docs/`, y la raíz del repo debe conservar sólo contrato, manifiestos, scripts, referencias y superficies de implementación.

La decisión a tomar no es sólo operativa, sino de diseño. Si permitimos que la raíz actúe como bóveda, el skill pierde frontera entre memoria viva y contrato del producto. Eso complica el uso del skill sobre sí mismo, la publicación de releases y la instalación como skill cross o plugin local.

La feature debería resolver, como mínimo, estas preguntas:

1. ¿Debe `setup` rechazar explícitamente materializar la bóveda en la raíz?
2. ¿Debe el skill asumir por defecto `docs/` como bóveda del proyecto cuando se trabaja en este repo?
3. ¿Cómo se declara y valida una instancia alternativa sin romper la regla general?
4. ¿Qué partes de `SKILL.md`, `AGENTS.md`, `references/` y `docs/05-NEURONA/` deben reforzar esta frontera?
5. ¿Qué validaciones o healthchecks deberían evitar que el proyecto vuelva a contaminarse con carpetas espejo en la raíz?

Objetivo de la iteración:

- dejar una doctrina clara sobre dónde vive la bóveda;
- evitar contaminación del working tree por artefactos de setup;
- permitir que el agente CLI implemente el skill sin perder compatibilidad cross;
- preservar el repositorio como skill instanciable sin confundir memoria del proyecto con contrato del skill.

La solución debe ser lo bastante explícita para que otra rama la implemente sin tener que decidir la política principal desde cero.

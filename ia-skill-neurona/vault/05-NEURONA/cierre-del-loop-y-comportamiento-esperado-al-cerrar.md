---
created: 2026-05-15T08:45:00-05:00
type: manifesto
status: active
source: mem operational doctrine
source_file:
  - docs/02-CONNECTIONS/20260515-084000-post-mortem-del-cambio-a-referencias-agnosticas.md
  - docs/01-CAPTURES/patterns/20260515-082227-arquitectura-conceptual-madurez-doctrinal-y-referencias-agnosticas.md
  - docs/03-BRIEFS/20260515-080000-mem-como-producto-instanciable-y-referencias-agnosticas.md
tags:
  - mem
  - doctrine
  - closure
  - architecture
aliases:
  - Cierre del loop
  - Comportamiento esperado al cerrar
  - Loop cerrado del cambio a referencias agnósticas
---

# Cierre del loop y comportamiento esperado al cerrar

## Definición

Cuando `$mem` cierra un cambio de arquitectura o contrato, el cierre esperado no es sólo declarar éxito operativo. El comportamiento correcto es convertir la secuencia completa en doctrina reusable:

1. cambio aplicado en la implementación;
2. racionalización en `00-INBOX`;
3. captura procesada en `01-CAPTURES`;
4. conexión que fija la tensión o secuencia;
5. neurona que eleva el criterio a regla del proyecto.

## Regla

El cierre del loop debe dejar una huella explícita en la red del proyecto. Si el cambio ya fue aplicado, el skill no debe dejar la decisión dispersa entre notas sueltas. Debe consolidarla en una neurona cuando:

- la doctrina ya esté madura;
- el comportamiento sea repetible;
- la personalización o maniobra de la instancia quede claramente delimitada;
- y el criterio pueda guiar futuros cierres sin reabrir la misma discusión.

Cerrar bien también implica compactar: dejar menos texto repetido, más relación útil y una versión más corta del criterio que abrió la discusión.

Para cambios de versionamiento y release, la secuencia canónica se fija además en [Versionamiento y release](versioning-and-release.md), de modo que futuras subidas de versión sigan la misma rienda: alcance, aplicación, validación, cierre y etiquetado.

## Comportamiento esperado del skill

Al cerrar, `$mem` debe:

- racionalizar la idea origen;
- procesarla a captura tipada;
- conectar la captura con el brief o la tensión resuelta;
- y subir el cierre a `05-NEURONA` si ya gobierna el modelo.

Eso significa que el cierre no termina en documentación. Termina cuando el proyecto sabe explicar su propia forma de cerrarse.

## Relacionado

- [Post-mortem del cambio a referencias agnósticas](20260515-084000-post-mortem-del-cambio-a-referencias-agnosticas.md)
- [La arquitectura del proyecto ya es sólida, pero necesita endurecer su implementación](20260515-082227-arquitectura-conceptual-madurez-doctrinal-y-referencias-agnosticas.md)
- [Brief: $mem como producto instanciable y referencias agnósticas](20260515-080000-mem-como-producto-instanciable-y-referencias-agnosticas.md)
- [Brief: curaduría documental y loop de madurez de `$mem`](20260516-120000-curaduria-documental-y-loop-de-madurez.md)

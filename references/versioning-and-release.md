# Versionamiento y release

Usa esta referencia cuando el skill vaya a subir versión, preparar un release o publicar una iteración estable.

## Principio

El versionamiento del skill no es un trámite aislado. Es una rienda de gobernanza que debe dejar claros tres puntos: qué cambió, qué versión representa el cambio y cómo se verifica que el repositorio quedó listo para publicarse.

## Regla

Cada iteración de versión debe dejar una secuencia repetible:

1. fijar el alcance del cambio en una captura o brief;
2. aplicar la gobernanza o implementación necesaria;
3. actualizar la versión visible en los artefactos del proyecto;
4. verificar setup, healthcheck y mini suite;
5. registrar el cierre como doctrina reutilizable;
6. etiquetar el release cuando la iteración ya sea estable.

## Criterio de release

Un release está listo cuando:

- el contrato del skill sigue coherente con la doctrina de `05-NEURONA`;
- la instalación y la composición local son idempotentes;
- la CLI sigue operando sin ambigüedad de contexto;
- la documentación pública explica el modo de uso sin mezclar memoria del agente con memoria del proyecto;
- el cambio ya puede repetirse en futuras iteraciones sin reinterpretación manual.

## Rienda para futuros incrementos

Cuando el proyecto vuelva a subir versión, reutiliza esta referencia como checklist canónica. No inventes una secuencia distinta salvo que cambie el modelo de publicación.

## Relacionado

- [Patrones base](baseline-patterns.md)
- [Cierre del loop y comportamiento esperado al cerrar](../docs/05-NEURONA/cierre-del-loop-y-comportamiento-esperado-al-cerrar.md)
- [Plantilla de referencia de instancia](instance-reference-template.md)

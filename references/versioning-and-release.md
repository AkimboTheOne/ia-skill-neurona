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
- el `README.md` muestra la misma versión visible que el tag que se va a publicar;
- el badge, el frontmatter y el tag deben cambiar juntos en la misma iteración;
- el cambio ya puede repetirse en futuras iteraciones sin reinterpretación manual.

## Distribución por tag

Para este proyecto, el mecanismo principal de distribución puede ser el propio tag verificado del repo. Si otra instancia necesita el skill como plugin cross o como checkout local, puede descargar el source del tag estable y usarlo como fuente canónica.

La regla práctica es:

- `tag` = versión inmutable de referencia;
- `GitHub Release` = publicación visible asociada al tag;
- `checkout` del tag = artefacto descargable e instalable cuando no se necesita empaquetado adicional.

Si en el futuro se necesita un bundle más pequeño o un artefacto recortado, eso se tratará como un paso adicional de publicación, no como sustituto de esta regla.

## Rienda para futuros incrementos

Cuando el proyecto vuelva a subir versión, reutiliza esta referencia como checklist canónica. No inventes una secuencia distinta salvo que cambie el modelo de publicación.

## Relacionado

- [Patrones base](baseline-patterns.md)
- [Cierre del loop y comportamiento esperado al cerrar](cierre-del-loop-y-comportamiento-esperado-al-cerrar.md)
- [Plantilla de referencia de instancia](instance-reference-template.md)

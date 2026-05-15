# Plantilla de referencia de instancia

Usa esta plantilla cuando una instancia de `$mem` necesite ajustar `references/` sin romper el contrato base.

## Propósito

Definir cómo la instancia interpreta el skill según su caso de uso, manteniendo la forma modular y las riendas estructurales.

La instancia debe poder decir dónde está montada, cómo se repara o valida su composición local y qué superficie debe recargar el agente cuando cambian las guías.

## Campos a vigilar

- `type` de memoria esperada.
- grado de personalización permitido.
- límites de contexto conectados.
- criterios de curaduría.
- señales de compatibilidad con la bóveda viva.

## Casos de uso compatibles

- memoria temporal de trabajo.
- memoria documental.
- memoria tipo “cerebro” o conocimiento operativo.
- instancias mixtas que requieran personalización explícita.
- repositorios con entrada de agente propia y setup local materializado por script.

## Regla de uso

La plantilla no reemplaza el contrato central. Sirve para adaptar la instancia con juicio del agente/LLM y dejar explícito qué cambia, qué permanece y por qué.

## Release de la instancia

Si la instancia participa en una iteración de versionamiento, usa [Versionamiento y release](versioning-and-release.md) como rienda base para mantener una secuencia consistente de versión visible, validación y publicación.

## Relacionado

- [Estructura de la Bóveda](vault-structure.md)
- [Flujos de Inteligencia](intelligence-workflows.md)
- [Patrones Base](baseline-patterns.md)

---
created: 2026-05-15T08:45:00-05:00
type: patterns
status: processed
source: inbox
source_file: 00-INBOX/20260515-090000-ayuda-operativa-para-agentes-llm-sin-interferir-en-la-implementacion.md
tags:
  - pattern
  - capture
  - mem
aliases:
  - Ayuda operativa para agentes LLM separada de implementación
---

# La ayuda operativa del skill debe servir al agente LLM sin invadir la implementación

## Sharpened

El skill debe organizar neuronas de ayuda por caso de uso para agentes LLM, con una frontera explícita que impida que la guía operativa interfiera con la conversación de implementación del producto.

## Raw Capture

La siguiente iteración del módulo debe organizar varias neuronas de ayuda en `05-NEURONA`, una por caso de uso, enfocadas al agente LLM que opere automatizaciones. Estas neuronas deben describir el flujo completo `00-INBOX -> 01-CAPTURES -> 02-CONNECTIONS -> 03-BRIEFS -> 05-NEURONA` para que el LLM entienda cómo debe operar el skill en automatización.

La restricción es importante: esta capa de conocimiento sólido debe guiar al agente que usa el módulo, pero no debe interferir en el agente del repositorio que decide cómo implementar y modificar el skill. Son dos planos distintos:

- plano del operador/usuario/LLM que ejecuta el skill;
- plano del dueño/desarrollador del producto que modifica el skill.

El módulo debe seguir siendo personalizable por quien lo descargue o instale, pero esa personalización dependerá del estilo y caso de uso de cada instancia. Por eso la ayuda operativa debe vivir como conocimiento sólido en `05-NEURONA`, separado del contrato de implementación, para evitar que una guía de uso invada las decisiones de producto.

La idea es generar neuronas de ayuda/autoayuda para agentes LLM que hagan explícito:

- qué flujo ejecutar;
- cuándo madurar una captura;
- cuándo conectar o sintetizar;
- cómo reconocer que una idea ya debe subir a `05`;
- y cómo no confundir operación con implementación.

## Raw Capture

La documentación del skill debe poder servir a dos tipos de conversación:

1. la conversación que implementa y modifica el producto;
2. la conversación que usa el producto para operar memoria.

La ayuda de `05-NEURONA` debe estar diseñada para la segunda, sin contaminar la primera.

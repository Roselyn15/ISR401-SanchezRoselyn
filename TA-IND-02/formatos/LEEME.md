# Cómo usar la boleta de votación

Este archivo es una **plantilla en blanco**. No contiene votos, participantes ni resultados.

## Qué es

Es una hoja en la que cada participante reparte **exactamente 100 puntos** entre los 20 requisitos R01–R20. Es la técnica de votación ponderada prevista en el kit de formatos de la tarea.

## Cómo se hace

1. Imprima **tres copias** de `boleta_votacion_para_llenar.pdf`.
2. Antes de entregar cada copia, aplique el consentimiento informado (`consentimiento_TA-IND-02_DOM03`).
3. Asigne códigos anónimos: `V1`, `V2` y `V3`. **No escriba nombres** en la boleta.
4. Cada persona escribe un número entero entre 0 y 100 en la columna "Puntos".
5. Revise que la **suma de los 20 valores sea 100** en cada boleta. Si no es 100, pida al participante que la corrija; no la ajuste usted.
6. Envíeme las tres boletas llenas (foto, PDF o los 20 números por participante). Yo las digito en `datos/votacion.csv`, recalculo Spearman y actualizo el informe.

## Formato para enviar los datos escritos

Si prefiere escribirlos en lugar de enviar la foto, use este formato por cada participante:

```text
participante,requisito,puntos
V2,R01,<puntos reales que escribió la persona>
V2,R02,<puntos reales que escribió la persona>
...
V2,R20,<puntos reales que escribió la persona>
```

Reglas: 20 filas por participante, valores enteros, suma exacta de 100 por participante, sin nombres ni cédulas.

## Estado actual del repositorio

Mientras no se recojan las boletas, `datos/votacion.csv` conserva **únicamente** la tabla real entregada (escala 3–5, total 85) y el informe declara esa limitación. La plantilla no cambia los resultados: solo permite recolectar datos reales nuevos.

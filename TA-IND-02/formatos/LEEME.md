# Uso de la boleta de votación

La boleta `boleta_votacion_para_llenar.pdf` es una plantilla en blanco. No contiene votos, participantes ni resultados.

## Procedimiento

1. Imprimir tres copias de la boleta.
2. Aplicar el consentimiento informado antes de entregar cada copia.
3. Usar códigos anónimos nuevos (`V5`, `V6`, ...) si se recogen más boletas; `V2`, `V3` y `V4` ya están registradas. No escribir nombres.
4. Cada participante anota un número entero entre 0 y 100 para cada requisito R01–R20.
5. Comprobar que la suma de los 20 valores sea exactamente 100. Si no es así, la persona participante corrige sus propios valores.
6. Transcribir los números a `datos/votacion.csv` y recalcular Spearman.

## Formato de transcripción

```text
participante,requisito,puntos
V3,R01,<puntos escritos por la persona>
V3,R02,<puntos escritos por la persona>
...
V3,R20,<puntos escritos por la persona>
```

Reglas: 20 filas por participante, valores enteros, suma exacta de 100 por participante, sin nombres ni cédulas.

## Estado del repositorio

Las tres boletas oficiales (`V2`, `V3` y `V4`) ya están registradas en `datos/votacion.csv`. La tabla inicial de escala 3–5 se conserva en `datos/ponderacion_escala3a5.csv` y no se mezcla con las boletas.

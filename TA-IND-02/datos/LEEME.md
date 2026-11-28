# Formato de los datos y del script

## CSV

- `participante`: código anónimo. En `kano_respuestas.csv` se usan `ENT-01` a `ENT-05`. En `votacion.csv` se usa `V2` para la boleta oficial de 100 puntos. Nunca nombres.
- `kano_respuestas.csv`: una fila por participante y característica (5 × 8 = 40 filas). `respuesta_funcional` y `respuesta_disfuncional` toman uno de cinco valores: *me gusta*, *debe ser así*, *me da igual*, *lo tolero*, *no me gusta*. `categoria_kano` se completó con la tabla de evaluación (M/O/A/I/R/Q).
- `votacion.csv`: 20 filas de la boleta V2. Cada participante reparte exactamente 100 puntos entre R01–R20 con enteros no negativos. Falta recolectar dos boletas más para completar las tres del kit.
- `ponderacion_escala3a5.csv`: tabla real entregada inicialmente (escala 3–5, total 85). Se conserva como referencia, pero **no se mezcla** con `votacion.csv` porque usa otra escala.
- `moscow.csv`: una fila por requisito con categoría M/S/C/W y horas estimadas por el analista.

Estos archivos solo contienen datos reales entregados. No se agregan filas de prueba.

## Cómo funciona `calcular_spearman.py` (para poder explicarlo en clase)

1. `BASE` ubica los CSV junto al script, sin depender de la carpeta desde la que se ejecute.
2. `MOSCOW` convierte M/S/C/W en 4/3/2/1 para que mayor número signifique mayor prioridad.
3. `promediar_rangos(valores)` ordena los valores y asigna a cada uno el promedio de las posiciones que ocupa; así los empates reciben el mismo rango.
4. `pearson(x, y)` calcula la correlación de Pearson entre los dos vectores de rangos. Ese valor es el rho de Spearman con empates.
5. `leer_moscow()` valida que existan al menos dos clasificaciones reales y devuelve el puntaje ordinal de cada requisito.
6. `leer_votacion()` suma los puntos por participante y por requisito. Si cada participante suma 100, valida el formato oficial; si no, imprime una nota y trata los puntos como ponderación directa.
7. `main()` intersecta los requisitos presentes en ambos CSV, calcula los rangos de MoSCoW y de la votación, y muestra `rho de Spearman`.

Resultado con los datos actuales: `n = 20`, `rho de Spearman = 0,7069`.

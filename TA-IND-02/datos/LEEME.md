# Formato de los datos y de los scripts

## Archivos CSV

- `participante`: código anónimo. En `kano_respuestas.csv` se usan `ENT-01` a `ENT-05`. En `votacion.csv` se usa `V2` para la boleta oficial de 100 puntos. Nunca nombres.
- `kano_respuestas.csv`: una fila por participante y característica (5 × 8 = 40 filas). `respuesta_funcional` y `respuesta_disfuncional` toman uno de cinco valores: *me gusta*, *debe ser así*, *me da igual*, *lo tolero*, *no me gusta*. La categoría se obtiene con la tabla de evaluación (M/O/A/I/R/Q).
- `votacion.csv`: 60 filas correspondientes a tres boletas (V2, V3 y V4). Cada participante reparte exactamente 100 puntos entre R01–R20 con enteros no negativos.
- `ponderacion_escala3a5.csv`: tabla inicial de escala 3–5 (total 85). Se conserva como referencia, pero no se mezcla con `votacion.csv` por usar otra escala.
- `moscow.csv`: una fila por requisito con categoría M/S/C/W y horas estimadas.

Los archivos contienen únicamente datos entregados. No se incluyen filas de prueba.

## Scripts

- `clasificar_kano.py`: aplica la tabla de evaluación a `kano_respuestas.csv`, escribe `kano_clasificado.csv` e informa de los empates sin decidirlos; el criterio de desempate está declarado en el informe.
- `calcular_spearman.py`: convierte M/S/C/W en 4/3/2/1, promedia los rangos empatados y calcula la correlación de Pearson entre rangos, que es el rho de Spearman. Valida que cada votante sume 100 puntos.

Resultado con los datos actuales: `n = 20`, `rho de Spearman = 0,7613`.

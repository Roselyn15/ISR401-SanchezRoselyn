# Formato de los datos

- `participante`: código anónimo (P01, P02, ...), el mismo que se usa en `evidencias/MANIFIESTO.md`. Nunca nombres.
- `kano_respuestas.csv`: una fila por participante y característica. `respuesta_funcional` y
  `respuesta_disfuncional` toman uno de cinco valores (me gusta / debe ser así / me da igual /
  lo tolero / no me gusta). `categoria_kano` se completa al aplicar la tabla de evaluación.
- `votacion.csv`: una fila por participante y requisito. Cada participante reparte 100 puntos
  entre los 20 requisitos (R01 a R20), de modo que sus puntos sumen 100.

Estos archivos solo contienen datos reales obtenidos de personas. No se agregan filas de prueba.

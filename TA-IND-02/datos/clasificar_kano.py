#!/usr/bin/env python3
"""Clasifica las respuestas Kano con la tabla de evaluación y cuenta categorías por característica.

Entrada : datos/kano_respuestas.csv  (participante,caracteristica,respuesta_funcional,respuesta_disfuncional,...)
Salida  : datos/kano_clasificado.csv (una fila por respuesta con su categoría)
          y un resumen en pantalla (conteo por característica).

No modifica el CSV de datos crudos. Si hay empate en la categoría más frecuente, lo informa y
NO decide: el criterio de desempate debe escribirlo y citarlo el autor en el informe.
"""
import csv
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent
ENTRADA = BASE / "kano_respuestas.csv"
SALIDA = BASE / "kano_clasificado.csv"

# Orden de las respuestas, tanto para filas (funcional) como columnas (disfuncional).
OPCIONES = ["me gusta", "debe ser asi", "me da igual", "lo tolero", "no me gusta"]

# Tabla de evaluación de Kano (filas = respuesta funcional, columnas = disfuncional).
# A atractiva, O desempeño, M básica, I indiferente, R inversa, Q cuestionable.
TABLA = [
    # gusta  debe   igual  tolero no gusta
    ["Q",    "A",   "A",   "A",   "O"],   # funcional: me gusta
    ["R",    "I",   "I",   "I",   "M"],   # funcional: debe ser así
    ["R",    "I",   "I",   "I",   "M"],   # funcional: me da igual
    ["R",    "I",   "I",   "I",   "M"],   # funcional: lo tolero
    ["R",    "R",   "R",   "R",   "Q"],   # funcional: no me gusta
]


def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto.strip().lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def categoria(funcional, disfuncional):
    f = OPCIONES.index(normalizar(funcional))
    d = OPCIONES.index(normalizar(disfuncional))
    return TABLA[f][d]


def main():
    with ENTRADA.open(encoding="utf-8-sig", newline="") as archivo:
        filas = [fila for fila in csv.DictReader(archivo) if fila["participante"].strip()]
    if not filas:
        sys.exit("kano_respuestas.csv no contiene respuestas reales todavía.")

    conteo = defaultdict(Counter)
    for fila in filas:
        try:
            fila["categoria_kano"] = categoria(fila["respuesta_funcional"], fila["respuesta_disfuncional"])
        except ValueError:
            sys.exit(f"Respuesta no válida en {fila['participante']} / {fila['caracteristica']}. "
                     f"Use: me gusta, debe ser así, me da igual, lo tolero, no me gusta.")
        conteo[fila["caracteristica"]][fila["categoria_kano"]] += 1

    with SALIDA.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(filas[0].keys()))
        escritor.writeheader()
        escritor.writerows(filas)

    for caracteristica, contador in sorted(conteo.items()):
        mayor = max(contador.values())
        lideres = sorted(c for c, n in contador.items() if n == mayor)
        detalle = ", ".join(f"{c}={n}" for c, n in sorted(contador.items()))
        aviso = "" if len(lideres) == 1 else "  <-- EMPATE: aplique y cite su criterio"
        print(f"{caracteristica}: {detalle}  -> más frecuente: {'/'.join(lideres)}{aviso}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Calcula la correlación de rangos de Spearman entre MoSCoW y la votación.

Entradas:
  datos/moscow.csv     -> requisito,moscow
  datos/votacion.csv   -> participante,requisito,puntos (boletas de 100 puntos)

La tabla inicial de escala 3--5 se conserva en ponderacion_escala3a5.csv y no
se mezcla con las boletas oficiales porque usa otra escala.

La categoría MoSCoW se convierte en puntaje ordinal:
  M=4, S=3, C=2, W=1  (mayor puntaje = mayor prioridad).
Los rangos se promedian en caso de empate. Si las boletas suman 100 por
participante se valida el formato oficial; si no, se trata la columna
`puntos` como una ponderación directa y se documenta la limitación.
Además de rho global, se calcula rho contra cada boleta individual.
"""

import csv
import math
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent  # carpeta del script, no la carpeta de ejecución
MOSCOW = {"M": 4, "S": 3, "C": 2, "W": 1}  # mayor número = mayor prioridad


def promediar_rangos(valores):
    """Devuelve el rango de cada valor, promediando los empates."""
    orden = sorted(valores, key=lambda par: par[1])
    rangos = {}
    i = 0
    while i < len(orden):
        j = i
        while j + 1 < len(orden) and orden[j + 1][1] == orden[i][1]:
            j += 1
        promedio = (i + j + 2) / 2.0  # promedio de posiciones ocupadas por el empate
        for k in range(i, j + 1):
            rangos[orden[k][0]] = promedio
        i = j + 1
    return rangos


def pearson(x, y):
    n = len(x)
    mx = sum(x) / n
    my = sum(y) / n
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    den = math.sqrt(sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y))
    # Correlación de Pearson entre rangos = rho de Spearman con empates
    return num / den if den else float("nan")


def leer_moscow():
    with (BASE / "moscow.csv").open(encoding="utf-8-sig", newline="") as archivo:
        filas = list(csv.DictReader(archivo))
    if not filas or not any(fila.get("moscow", "").strip() for fila in filas):
        raise ValueError("moscow.csv no contiene clasificaciones reales aún.")
    resultado = {}
    for fila in filas:
        categoria = fila.get("moscow", "").strip().upper()
        if categoria in MOSCOW:
            resultado[fila["requisito"].strip()] = MOSCOW[categoria]
    if len(resultado) < 2:
        raise ValueError("Se necesitan al menos dos clasificaciones MoSCoW reales.")
    return resultado


def leer_votacion():
    por_votante = defaultdict(int)
    totales = defaultdict(int)
    puntos_por_votante = defaultdict(dict)
    with (BASE / "votacion.csv").open(encoding="utf-8-sig", newline="") as archivo:
        for fila in csv.DictReader(archivo):
            if not fila.get("puntos"):
                continue
            votante = fila["participante"].strip()
            requisito = fila["requisito"].strip()
            puntos = int(fila["puntos"])
            por_votante[votante] += puntos  # control de 100 puntos por votante
            totales[requisito] += puntos  # total de cada requisito
            puntos_por_votante[votante][requisito] = puntos
    if all(suma == 100 for suma in por_votante.values()):
        print("Validación OK: cada votante reparte exactamente 100 puntos.")
    else:
        print("Nota: la ponderación disponible no usa boletas de 100 puntos; se calcula rho con los valores entregados.")
    if not totales:
        raise ValueError("votacion.csv no contiene datos reales aún.")
    return totales, puntos_por_votante


def main():
    moscow = leer_moscow()
    votos, puntos_por_votante = leer_votacion()
    requisitos = sorted(set(moscow) & set(votos))  # solo requisitos presentes en ambos CSV
    if len(requisitos) < 2:
        raise ValueError("Se necesitan al menos dos requisitos comunes.")

    rangos_m = promediar_rangos([(r, moscow[r]) for r in requisitos])
    rangos_v = promediar_rangos([(r, votos[r]) for r in requisitos])

    rho = pearson([rangos_m[r] for r in requisitos], [rangos_v[r] for r in requisitos])
    print(f"n = {len(requisitos)}")
    print(f"rho de Spearman = {rho:.4f}")

    for votante in sorted(puntos_por_votante):
        puntos = puntos_por_votante[votante]
        comunes = [r for r in requisitos if r in puntos]
        if len(comunes) < 2:
            continue
        rangos_p = promediar_rangos([(r, puntos[r]) for r in comunes])
        rho_p = pearson([rangos_m[r] for r in comunes], [rangos_p[r] for r in comunes])
        print(f"rho {votante} = {rho_p:.4f}")


if __name__ == "__main__":
    main()

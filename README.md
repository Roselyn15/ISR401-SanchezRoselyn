# ISR401-SanchezRoselyn

Repositorio personal de **Ingenieria de Requerimientos (ISR-401)**, Facultad de
Ciencias de la Computacion, Universidad Tecnica Estatal de Quevedo.

- **Estudiante:** Sanchez Centeno Roselyn Andreina
- **Paralelo:** A (cuarto nivel)

## Contenido del repositorio

| Carpeta | Actividad | Archivo principal |
|---|---|---|
| `FORM-TL-01/` | Taller formativo de tipos de requisitos | `main.tex` |
| `TA-IND-01/` | Actividad sumativa: IEEE 29148 y tipos de requisitos de Shein | `main.tex` |

Cada carpeta contiene sus fuentes LaTeX, su bibliografia y el PDF compilado.

## Compilador y dependencias

- **Compilador:** pdfLaTeX (TeX Live 2023 o superior, o MiKTeX 24.x).
- **Bibliografia:** BibTeX con el estilo `IEEEtran` (`IEEEtran.bst`).
- **Paquetes LaTeX:** `babel-spanish`, `geometry`, `microtype`, `graphicx`,
  `booktabs`, `longtable`, `array`, `tabularx`, `pdflscape`, `enumitem`,
  `xcolor`, `caption`, `cite`, `hyperref`.
- **Alternativa sin instalacion:** [Tectonic](https://tectonic-typesetting.github.io/).

## Como compilar TA-IND-01

Desde la carpeta `TA-IND-01/`:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

El orden importa: la primera pasada genera los auxiliares, `bibtex` procesa
`referencias.bib` y las dos pasadas finales resuelven citas y referencias
cruzadas. El resultado es `TA-IND-01/main.pdf`.

Con Tectonic basta un comando (resuelve BibTeX automaticamente):

```bash
tectonic main.tex
```

## Como compilar FORM-TL-01

Desde la carpeta `FORM-TL-01/`:

```bash
pdflatex main.tex
pdflatex main.tex
pdflatex entrega.tex
```

`main.pdf` es el informe y `entrega.pdf` es la hoja de una pagina para el SGA.

## Figuras

Las capturas propias del sistema Shein estan en `TA-IND-01/figuras/` con los
nombres `cap01_pantalla_inicio.jpeg`, `cap02_busqueda_catalogo.jpeg`,
`cap03_carrito_compra.jpeg` y `cap04_pantalla_pago.jpeg`. El documento las
inserta con `\includegraphics`; si falta una, el PDF muestra un recuadro rojo
de aviso en su lugar.

## Estructura de TA-IND-01

```
TA-IND-01/
  main.tex            Informe (descripcion, resumen, glosario, requisitos,
                      clasificacion, autoevaluacion, reflexion)
  referencias.bib     Bibliografia en formato IEEE
  main.pdf            PDF compilado
  figuras/            Capturas propias de Shein
```

## Notas de entrega

- El PDF de la tarea del SGA debe tener **una sola pagina** con los datos
  informativos y la URL del repositorio en una sola linea.
- La fecha de cierre de TA-IND-01 es el **sabado 7 de noviembre de 2026, 23:59**.

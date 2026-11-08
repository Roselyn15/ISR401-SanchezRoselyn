# ISR401-SanchezRoselyn

Repositorio personal de **Ingeniería de Requerimientos (ISR-401)**, Facultad de
Ciencias de la Computación, Universidad Técnica Estatal de Quevedo.

- **Estudiante:** Sánchez Centeno Roselyn Andreina
- **Paralelo:** A (cuarto nivel)

## Contenido del repositorio

| Carpeta | Actividad | Archivo principal |
|---|---|---|
| `FORM-TL-01/` | Taller formativo de tipos de requisitos | `main.tex` |
| `TA-IND-01/` | Actividad sumativa: IEEE 29148 y tipos de requisitos de Shein | `main.tex` |

Cada carpeta contiene sus fuentes LaTeX, su bibliografía y el PDF compilado.

## Compilador y dependencias

- **Compilador:** pdfLaTeX (TeX Live 2023 o superior, o MiKTeX 24.x).
- **Bibliografía:** BibTeX con el estilo `IEEEtran` (`IEEEtran.bst`).
- **Paquetes LaTeX:** `babel-spanish`, `geometry`, `microtype`, `graphicx`,
  `booktabs`, `longtable`, `array`, `tabularx`, `pdflscape`, `subcaption`,
  `enumitem`, `xcolor`, `caption`, `cite`, `hyperref`.
- **Alternativa sin instalación:** [Tectonic](https://tectonic-typesetting.github.io/).

## Cómo compilar TA-IND-01

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

Con Tectonic basta un comando (resuelve BibTeX automáticamente):

```bash
tectonic main.tex
```

## Cómo compilar FORM-TL-01

Desde la carpeta `FORM-TL-01/`:

```bash
pdflatex main.tex
pdflatex main.tex
pdflatex entrega.tex
```

`main.pdf` es el informe y `entrega.pdf` es la hoja de una página para el SGA.

## Figuras

Las capturas propias del sistema Shein están en `TA-IND-01/figuras/` con los
nombres `cap01_pantalla_inicio.jpeg`, `cap02_busqueda_catalogo.jpeg`,
`cap03_carrito_compra.jpeg` y `cap04_pantalla_pago.jpeg`. El informe las
inserta con `\includegraphics` en dos figuras de dos paneles cada una.

## Estructura de TA-IND-01

```
TA-IND-01/
  main.tex            Informe (descripción, resumen, glosario, requisitos,
                      clasificación, autoevaluación, reflexión)
  referencias.bib     Bibliografía en formato IEEE
  main.pdf            PDF compilado
  figuras/            Capturas propias de Shein
```

## Uso de inteligencia artificial

- **Herramienta:** asistente de IA OpenCode, modelo Big Pickle (noviembre de 2026).
- **Propósito:** estructura del documento LaTeX, plantillas de tablas, archivo
  de referencias, resolución de errores de compilación y revisión de ortografía
  y gramática.
- **Declaración completa:** sección 8 de `TA-IND-01/main.tex`.

### Prompts utilizados

Revisión de ortografía y gramática del texto final:

```text
Corrige únicamente la ortografía y la gramática del siguiente texto en
español. No cambies el contenido, el orden de las ideas ni el significado
técnico; no agregues ni elimines párrafos. Conserva los términos técnicos
de ISO/IEC/IEEE 29148:2018 y de ISO/IEC 25010:2023 tal como están escritos.
Devuelve el texto corregido y, al final, una lista de las correcciones
realizadas con la palabra original y la corregida.
```

Verificación: cada corrección se comparó con el texto original y se conservó
solo cuando corregía una falta real; las cifras, las métricas y los
identificadores de requisito no se modificaron.

## Notas de entrega

- El PDF de la tarea del SGA debe tener **una sola página** con los datos
  informativos y la URL del repositorio en una sola línea.
- La fecha de cierre de TA-IND-01 es el **sábado 7 de noviembre de 2026, 23:59**.

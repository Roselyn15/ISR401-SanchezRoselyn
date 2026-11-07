# ISR401-SanchezRoselyn

Repositorio personal de Ingeniería de Requerimientos (ISR-401), UTEQ.
Estudiante: Sánchez Centeno Roselyn Andreina

## FORM-TL-01: Taller de tipos de requisitos

### Archivos

- `FORM-TL-01/main.tex`: archivo principal (fuente en LaTeX).
- `FORM-TL-01/main.pdf`: PDF compilado.
- `FORM-TL-01/entrega.tex` y `entrega.pdf`: PDF de una página para el SGA.

### Compilador

- `pdflatex` (TeX Live o MiKTeX)

### Dependencias

Paquetes de LaTeX: `inputenc`, `fontenc`, `babel` (spanish), `geometry`,
`longtable`, `booktabs`, `array`, `hyperref`, `url`.

Vienen incluidos en las instalaciones completas de TeX Live y MiKTeX.

### Cómo compilar

1. Clonar el repositorio:

        git clone https://github.com/Roselyn15/ISR401-SanchezRoselyn.git
        cd ISR401-SanchezRoselyn/FORM-TL-01

2. Compilar el documento principal (dos veces, para actualizar referencias):

        pdflatex main.tex
        pdflatex main.tex

3. Compilar el PDF de entrega:

        pdflatex entrega.tex

### Resultado

Se generan `main.pdf` y `entrega.pdf` en la carpeta `FORM-TL-01/`.

# Generador de las series

Cada serie es un módulo de datos (`data_*.py`) con la serie (`SERIE`) y sus píldoras (`PILDORAS`). El constructor genera un HTML autocontenido.

## Regenerar o editar una serie
1. Edita el `data_<serie>.py` (textos, preguntas, ejemplos).
2. Desde esta carpeta, ejecuta:
   `python3 -I make_gen.py <slug> data_<serie>.py "<Título línea 1>" "<Título línea 2 en rojo>" "<Público>" ../serie-<nombre>.html`
   Ejemplo: `python3 -I make_gen.py habitos data_habitos.py "Siete hábitos" "de efectividad" "Captadores" ../serie-siete-habitos.html`
3. La tarjeta `href="#<slug>"` debe existir ya en `../index.html` (de ahí sale el icono).
4. Copia el HTML resultante en `META` y `DOCS` de `index.html` para que se abra desde la biblioteca.

## Archivos
- `build_s.py`: constructor genérico (HTML, estilos y script).
- `finish.py` y `pasos.html`: remate (logo, pie, pasos de la portada).
- `styles_v3.html`, `styles_k.html`, `tpl_k.js`, `logo.b64`: estilos, script y logo.
- `ch_tpl.js` y `disc_tpl.js`: scripts de los tests de las series de Selección y DISC.
- `data_*.py`: contenido de cada serie.

La serie del Eneagrama se retiró de la biblioteca y sus datos no se incluyen.

## Series de conocimiento de una ONG (Aldeas, Cruz Roja)
Usan `build_k.py` y `make_k.py` (mismos argumentos que `make_gen.py`). Ejemplo: `python3 -I make_k.py cruzroja data_cruzroja.py "Conoce" "Cruz Roja Española" "Captadores" ../serie-cruzroja.html`. La serie de Aldeas se generó con una versión anterior del constructor.

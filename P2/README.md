# Práctica 2 de Visión por Computador

**Autores:**

* David Miranda Campos
* Alejandro Guerra Jimenez

## Tareas realizadas

1. **Conteo de píxeles blancos por filas**

   * Se modifica el conteo de píxeles blancos para que se realice **fila por fila** en lugar de por columnas.
   * Se obtiene el valor máximo de píxeles blancos en una fila (`maxfil`) y se localizan las filas que superan el 90% de este valor.
   * El resultado permite identificar de forma visual las zonas de la imagen con mayor concentración de píxeles blancos, resaltando patrones horizontales.

2. **Umbralizado de Sobel y comparación con Canny**

   * Se aplica el operador **Sobel** para calcular gradientes y se convierte la imagen resultante a 8 bits.
   * Tras aplicar un **umbral**, se realiza un conteo de píxeles no nulos tanto por filas como por columnas.
   * Se identifican las posiciones que superan el 90% del valor máximo y se remarcan sobre la imagen del mandril mediante primitivas gráficas.
   * Finalmente, se comparan los resultados de este proceso con los obtenidos usando **Canny**, analizando similitudes y diferencias en la detección de bordes.

3. **Demostrador interactivo con webcam**

   * Se desarrolla un programa que captura imágenes en tiempo real desde la cámara web.
   * El usuario puede alternar entre diferentes **modos de visualización**:

     * Imagen original en color.
     * Procesamiento en escala de grises.
     * Detección de bordes con Canny.
     * PopArt sacado de la practica 1, detección de colores en bloques de 5 y recoloración de los mismos según el color dominante.

4. **Propuesta creativa inspirada en instalaciones interactivas**

   * Se plantea un sistema de detección de círculos de color naranja en la imagen capturada por la webcam.
   * Para ello se emplean técnicas de segmentación por color en el espacio HSV, filtrando el rango correspondiente al naranja.
   * Una vez detectadas las regiones candidatas, se aplican algoritmos de detección de contornos y la transformada de Hough para identificar círculos.
   * Los círculos detectados se remarcan en tiempo real sobre el flujo de vídeo, permitiendo una interacción inmediata con objetos físicos de ese color.

## Ejecución

Las tareas se encuentran en el notebook `VC_P2.ipynb`.
Para ejecutarlas:

1. Abrir el cuaderno en Jupyter Notebook o JupyterLab.
2. Ejecutar las celdas en orden.
3. En las tareas que utilizan la cámara, se abrirá una ventana de vídeo interactiva.
4. En el demostrador, el usuario podrá alternar entre modos mediante las teclas definidas en el código.

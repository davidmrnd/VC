# Practica 5

# Clasificación de Rangos de Edad con PCA + KNN y Webcam

Este proyecto utiliza técnicas de visión por computador y machine learning para clasificar el rango de edad de una persona en tiempo real utilizando una cámara web. El pipeline de clasificación se basa en la Reducción de Dimensión con **PCA (Análisis de Componentes Principales)** y un clasificador **KNN (K-Vecinos más Cercanos)**.

El notebook incluye dos demostraciones principales:
1.  **Discriminador de Edades:** Detecta una cara y dibuja un recuadro de color con la etiqueta del rango de edad predicho.
2.  **Filtro por Edades:** Detecta una cara y superpone un accesorio (filtro) diferente según el rango de edad (ej. un chupete para "Niño", unas gafas para "Adolescente").

---

## Metodología


1.  **Carga de Datos:** Las imágenes se cargan desde una carpeta `Dataset/`. Se espera que este directorio contenga subcarpetas nombradas con la edad de las personas en las imágenes (ej. "1", "2", ..., "60", etc.).
El modelo de clasificación se entrena siguiendo estos pasos:
2.  **Definición de Rangos:** Las edades se agrupan en cinco categorías:
    * **Niño:** <= 12 años
    * **Adolescente:** 13-19 años
    * **Joven:** 20-35 años
    * **Adulto:** 36-60 años
    * **Anciano:** > 60 años
3.  **Preprocesamiento:** Todas las imágenes se convierten a escala de grises y se redimensionan a 100x100 píxeles.
4.  **Reducción de Dimensión (PCA):** Se calcula PCA sobre el conjunto de datos de entrenamiento para reducir la dimensionalidad de 10,000 características (100x100) a 100 componentes principales.
5.  **Clasificación (KNN):** Se entrena un clasificador `KNeighborsClassifier` (con k=5 en el modelo final) utilizando las características extraídas por PCA.


---

## Estructura del Proyecto

Para que el notebook funcione correctamente, se espera la siguiente estructura de archivos y carpetas:

```
.
├── VC\_P5\_Clasificacion\_Rangos\_Edad.ipynb  \# El notebook principal
├── FaceDetectors.py                       \# Módulo detector de caras (dependencia)
├── FaceNormalizationUtils.py              \# Módulo de normalización (dependencia)
├── Dataset/                               \# (Requerido para entrenamiento)
│   ├── 01/
│   │   ├── img1.jpg
│   │   └── ...
│   ├── 02/
│   └── ...
└── assets/                                \# (Requerido para la demo de filtros)
    ├── baston.png
    ├── chupete.png
    ├── gafas.png
    └── gorra.png

```

---

## Dependencias

El proyecto requiere las siguientes bibliotecas de Python. Puedes instalarlas usando `pip`:

* **opencv-python:** Para la captura de cámara y procesamiento de imágenes.
* **numpy:** Para operaciones numéricas y matriciales.
* **scikit-learn:** Para el KFold, KNN y cálculo de métricas.


Además, el código depende de dos módulos locales que deben estar en el mismo directorio:

  * `FaceDetectors.py` (Utilizado para la detección facial, específicamente MTCNN).
  * `FaceNormalizationUtils.py` (Utilizado para la normalización facial en la demo de filtros).

-----

## Cómo Ejecutar

1.  **Para poder preparar el entorno se siguieron los siguientes pasos:**
    - 1.- Abrir AnacondaPrompt
    - 2.- Una vez abierto ejecutar: \
          >```conda create --name VC_P5 python=3.11.5``` \
          >```conda activate VC_P5``` \
          >```pip install opencv-python matplotlib imutils mtcnn tensorflow deepface tf-keras cmake``` \
          >```pip install scikit-learn```
2.  **Instalar Dependencias:** Asegúrate de tener todas las bibliotecas listadas anteriormente. Ejecuta la 1ª celda 
3.  **Preparar los Datos (Opcional - Entrenamiento):** Las imagenes para entrenar el modelo se encuentaran en `Dataset/` lleno de caras organizadas en subcarpetas por edad. Luego, ejecutar de la 2ª a la 6ª celda.
4.  **Ejecutar las Demos:**
      * **Demo 1 (Discriminador):** Ejecuta la 7ª celda ("Discriminante por edades").
      * **Demo 2 (Filtros):** Ejecuta la 8ª, 9ª y 10ª celda ("Filtro por edades").


## Autores

- **Alejandro Guerra Jiménez**
- **David Miranda Campos**

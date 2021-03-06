# 4.4Proyecto_de_la_unidad
Este es el proyecto desarrollado para concluir el cuarto parcial de mi materia de Análisis y Procesamiento de Imágenes

## **INSTRUCCIONES**

Usar los 3 tableros( [Tablero1](https://github.com/eljuanrv/4.4Proyecto_de_la_unidad/blob/main/tablero1.png), [Tablero2](https://github.com/eljuanrv/4.4Proyecto_de_la_unidad/blob/main/tablero2.png), [Tablero3](https://github.com/eljuanrv/4.4Proyecto_de_la_unidad/blob/main/tablero3.png)  ) adjuntos para detectar las posiciones tanto de las piezas blancas como de las piezas cafés. Las consideraciones son las siguientes:

1. Aplicar una máscara para que sepa qué piezas son blancas y qué piezas son cafés.
2. Contar el número de piezas blancas en el tablero y poner el resultado en la parte superior izquierda con color azul.
3. Contar el número de piezas cafés en el tablero y poner el resultado en la parte inferior izquierda con color verde.
4. A cada pieza blanca colocarle su posición con texto sobre la misma pieza con texto color azul.
5. A cada pieza café colocarle su posición con texto sobre la misma pieza con texto color verde.

La forma de calificar será: 
- yo correr el programa cargando un tablero que tenga en mi computadora. 
- Este último tablero mencionado será de la misma dimensión que los adjuntos pero con diferente posición en la fichas. 
- Si detecta bien la posición de las fichas, el programa tendrá 100. 
- Si no detecta bien la posición de la fichas, tendrán que hacer el proyecto de regularización 4.  

Se entregan cuatro archivos en total. Entregables:
- El programa *.py utilizado (por favor no poner menús, en cuanto se corra, debe abrir la ventana con el resultado del procesamiento, ya que yo lo voy usar para probar un cuarto tablero)
- Las tres capturas *.jpg de los tres tableros conocidos (recortar sólo la ventana del imshow par que se alcance a leer el texto)

## **Herramientas**

Para simplificar el desarrollo de este proyecto unicamente se utilizaron 2 herramientas

1. [Sublime Text](https://www.sublimetext.com/): es un editor de texto y editor de código fuente. Está escrito en C++ y Python para los plugins. Desarrollado originalmente como una extensión de Vim, con el tiempo fue creando una identidad propia. 
Se puede descargar y evaluar de forma gratuita. Sin embargo no es software libre o de código abierto y se debe obtener una licencia para su uso continuado, aunque la versión de evaluación es plenamente funcional y no tiene fecha de caducidad. [Fuente](https://es.wikipedia.org/wiki/Sublime_Text)

2. [CMD de Windows](https://www.reviewhardware.com/como-funciona/que-es-cmd-que-significa-y-para-que-sirve#:~:text=CMD%20es%20una%20abreviatura%20que%20significa%20%E2%80%9CCommand%E2%80%9D%20y,de%20la%20introducci%C3%B3n%20de%20comandos%20de%20textos%2C%20): No realizé la ejecución de los programas directamente desde *Sublime Text*, para ejecutarlos utilizé la herramienta CMD de Windows, esta no necesita ninguna instalación porque es una herramienta que ya viene incluida.

## **Bibliotecas Utilizadas**

Se utilizaron las siguientes 3 librerias para la realización del proyecto:

1. [Numpy](https://numpy.org/doc/stable/): NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

2. [OpenCV](https://docs.opencv.org/4.x/d0/de3/tutorial_py_intro.html): OpenCV-Python is a library of Python bindings designed to solve computer vision problems.

3. [Matplotlib](https://matplotlib.org/): Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible.

"""
Guía de estudio: lectura y escritura de archivos.

Abrir un archivo u objeto similar a un archivo para leer o escribir es uno de los pasos fundamentales de un programador
de Python. Por ejemplo, es posible que desees leer un archivo .csv y convertirlo al formato JSON. O quizás desee
seleccionar datos de una base de datos y escribirlos en un archivo de salida.

Leer y escribir archivos

Para leer o escribir un archivo, utilice
abierto(). Esta función incluye dos argumentos: la ruta del archivo y el modo.
"""
with open("sample_data/declaration.txt", "rt") as textfile:
    for line in textfile:
        print(line)
"""
En este ejemplo, el primer argumento es una cadena que contiene el nombre del archivo ( sample_data/declaration.txt ). 
El segundo argumento identifica el modo o la forma en que se utilizará el archivo (rt).
"r" significa abierto para lectura y "t" le dice a Python que espere un archivo de texto.
"""

# f = open("sample_data/declaration.txt", “w”)

"""
En este ejemplo, el código le dice a Python que abra este archivo para escribirlo (modo “w”). 

Modo
El argumento modo es opcional y especifica el modo en el que se abre el archivo. Si se omite, el valor predeterminado 
es "r" y eso significa abrir para lectura en modo texto. Los modos comunes incluyen:

    · “r” abierta para lectura (predeterminado)

    · “w” abierto para escritura, truncando el archivo primero

    · “x” abierto para creación exclusiva, fallando si el archivo ya existe

    · “a” abierta para escritura, anexada al final del archivo si existe

    · “+” abierto tanto para lectura como para escritura

Intentar escribir en un archivo abierto para lectura (“r”) provocará un error de tiempo de ejecución.

Codificación

Python distingue entre modo binario (“b”) y modo texto (“t”). De forma predeterminada, los archivos se abren en modo 
texto, lo que significa que usted lee y escribe cadenas desde y hacia el archivo, que están codificadas en una 
codificación específica. Si no se especifica la codificación, el valor predeterminado depende de la plataforma. 
Esto significa que se llama a locale.getencoding() para obtener la codificación local actual. Si necesita abrir el 
texto en una codificación específica, debe especificarla.
"""
f = open('workfile', 'w', encoding="utf-8")

"""
En este ejemplo, la codificación = “utf-8” especifica que el archivo debe abrirse con UTF-8, el estándar moderno de 
facto. Los datos en modo binario se leen y escriben como objetos de bytes. No puede especificar la codificación 
al abrir un archivo en modo binario.

Debes tener permiso para escribir en el directorio donde estás colocando el archivo. Es una buena práctica cerrar 
siempre un archivo .close() cuando haya terminado de trabajar con él.

Conclusiones clave
Para abrir un archivo para leer o escribir, use open(nombre de archivo, modo). Dos argumentos necesarios incluyen el 
nombre del archivo y el modo. Python codificará el archivo como texto (“t”) de forma predeterminada a menos que se 
especifique una codificación específica.

Recursos para más información
Puede encontrar más información sobre la lectura y escritura de archivos en Funciones integradas:

https://docs.python.org/3/library/functions.html#open
"""


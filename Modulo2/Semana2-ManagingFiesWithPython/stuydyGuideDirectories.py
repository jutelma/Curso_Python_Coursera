"""
Guía de estudio: Archivos y directorios

Administrar archivos y directorios incluye crear, eliminar y mover archivos y directorios. También incluye cambiar
la propiedad y los permisos de los archivos y directorios. Hay varias formas de administrar archivos y directorios en
Python. Una de las formas más sencillas es utilizar funciones de bajo nivel en los módulos OS y SYS que imitan
fielmente los comandos estándar de Linux, como os.mkdir() y   os.rmdir() . Alternativamente, puede utilizar el módulo
Pathlib, que proporciona una interfaz orientada a objetos para trabajar con los sistemas de archivos.

Echemos un vistazo a dos ejemplos. El primer ejemplo utiliza el sistema operativo; el segundo usa Pathlib.
Estos dos ejemplos de código hacen lo mismo: crean un directorio llamado test1 y mueven un archivo llamado README.md
de la carpeta sample_data a test1 .

Un ejemplo de uso de la función del sistema operativo para crear un directorio y mover un archivo:
"""
# Create a directory and move a file from one directory to another
# using low-level OS functions.

import os

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:

dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

# Construct source and destination paths:
src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
dest_file = os.path.join(os.getcwd(), "test1", "README.md")

# Move the file from its original location to the destination:
os.rename(src_file, dest_file)

# A continuación se muestra un ejemplo del uso de Pathlib para crear un directorio y mover un archivo:

# Create a directory and move a file from one directory to another
# using Pathlib.

from pathlib import Path

# Check to see if the "test1" subdirectory exists. If not, create it:
dest_dir = Path("./test1/")
if not dest_dir.exists():
    dest_dir.mkdir()

# Construct source and destination paths:
src_file = Path("./sample_data/README.md")
dest_file = dest_dir / "README.md"

# Move the file from its original location to the destination:
src_file.rename(dest_file)

"""
El módulo del sistema operativo
 
El módulo OS de Python, o la interfaz miscelánea del sistema operativo, es muy útil para operaciones de archivos, 
directorios y permisos. Echemos un vistazo a cada uno.

Operaciones de archivos
Los nombres de los archivos se pueden considerar como dos nombres separados por un punto. Por ejemplo, helloworld.txt 
es el nombre del archivo y la extensión define el tipo de archivo. El sistema operativo proporciona funciones para 
crear, leer, actualizar y eliminar archivos. Algunas de las funciones básicas incluyen:

 · Abrir y cerrar archivos

 · Leer y escribir en archivos

 · Agregar a archivos

Directorios

El sistema operativo también proporciona funciones para crear, leer, actualizar y eliminar directorios, así como 
cambiar directorios y enumerar archivos. Saber utilizar estas funciones es clave para trabajar con archivos. 
Por ejemplo, os.listdir(ruta) devuelve una lista de todos los archivos y subdirectorios de un directorio.

Permisos
Tener la capacidad de actualizar los permisos de los archivos es un aspecto importante al realizar instalaciones 
desde una ventana de terminal. os.chmod () brinda la capacidad de crear, leer y actualizar permisos para 
individuos o grupos.

Cosas a tener en cuenta  
Una cosa a tener en cuenta es que Python trata los archivos de texto y binarios de manera diferente. Debido a que 
Python es multiplataforma, intenta manejar automáticamente diferentes finales de línea ASCII. Si está procesando un 
archivo binario, asegúrese de abrirlo en modo binario para que Python no intente "arreglar" nuevas líneas en un 
archivo binario.

Una buena práctica es cerrar siempre () un archivo cuando haya terminado de leerlo o escribirlo. 
Aunque Python generalmente los cierra, es una buena señal para otras personas que lean su código de que ya terminó 
con ese archivo. Asegúrese de detectar cualquier error potencial de las llamadas al sistema de archivos, como permiso 
denegado, archivo no encontrado, etc. Generalmente, los envuelve en try/except para manejar esos errores.

Conclusiones clave
Hay varias formas de administrar archivos y directorios en Python. Una forma es utilizar funciones de bajo nivel en 
los módulos OS y SYS que imiten fielmente los comandos estándar de Linux. Otra forma es utilizar el módulo Pathlib, 
que proporciona una interfaz orientada a objetos para trabajar con los sistemas de archivos. 

Recursos para más información
Puede encontrar más información sobre archivos y directorios en varios recursos que se proporcionan a continuación: 

https://docs.python.org/3/library/os.html

https://docs.python.org/3/library/os.path.html

https://en.wikipedia.org/wiki/Unix_time"""
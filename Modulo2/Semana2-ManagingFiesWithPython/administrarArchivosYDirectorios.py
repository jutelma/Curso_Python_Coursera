# Revisión: Trabajar con archivos

# Introducción
# Esta lectura de seguimiento está organizada para que coincida con el contenido del vídeo que sigue. Contiene el mismo
# código que se muestra en el siguiente vídeo. Estos bloques de código le brindarán la oportunidad de ver cómo
# está escrito el código, le permitirán practicar su ejecución y pueden usarse como referencia para consultar.
#
# Puede seguir la lectura mientras el instructor analiza el código o revisar el código después de ver el video.

import os

os.remove("novel.txt")

# Este código elimina el archivo novel.txt.

import os

os.remove("novel.txt")
os.remove("novel.txt")

# Este código arrojará un error de archivo no encontrado. No puedes eliminar un archivo que no existe.

os.rename("first_draft.txt", "finished_masterpiece.txt")

# Este código se puede utilizar para cambiar el nombre de un archivo.

os.path.exists("finished_masterpiece.txt")
os.path.exists("userlist.txt")

# Este código comprueba si existe o no un archivo. Si el archivo existe, devolverá Verdadero. Si el archivo no existe
# devolverá Falso.

# ¿Cómo podemos comprobar si existe un archivo dentro de un script de Python?

#
#
# Usando la función os.path.exists.

# Correcto
# You got it! The os.path.exists function will return True if the file exists, False if it doesn't.

# Revisión: Más información del archivo

# Introducción
# Esta lectura de seguimiento está organizada para que coincida con el contenido del vídeo que sigue. Contiene el mismo
# código que se muestra en el siguiente vídeo. Estos bloques de código le brindarán la oportunidad de ver cómo está
# escrito el código, le permitirán practicar su ejecución y pueden usarse como referencia para consultar.
#
# Puede seguir la lectura mientras el instructor analiza el código o revisar el código después de ver el video.

# os.path.getsize("spider.txt")
# This code will provide the file size
# os.path.getmtime("spider.txt")
# This code will provide a timestamp for the file
# import datetime
# timestamp = os.path.getmtime("spider.txt")
# datetime.datetime.from timestamp(timestamp)
# #This code will provide the date and time for the file in an easy too understand format
# os.path.abspath("spider.txt")
# #This code takes the file name and turns it into an absolute path

# Algunas funciones más del módulo os.path incluyen getsize() e isfile() que obtienen información sobre el tamaño del
# archivo y determinan si un archivo existe, respectivamente. En el siguiente fragmento de código, ¿qué crees que se
# imprimirá si el archivo no existe?

# import os

file = "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print(os.path.isfile(file))
    print("File not found")

# R FALSO
#
# Archivo no encontrado

# Revisión: Directorios

# Introducción
# Esta lectura de seguimiento está organizada para que coincida con el contenido del vídeo que sigue. Contiene
# el mismo código que se muestra en el siguiente vídeo. Estos bloques de código le brindarán la oportunidad de ver
# cómo está escrito el código, le permitirán practicar su ejecución y pueden usarse como referencia para consultar.
#
# Puede seguir la lectura mientras el instructor analiza el código o revisar el código después de ver el video.

print(os.getcwd())
# Este fragmento de codigo devuelve el directorio de trabajo actual.

os.mkdir("new_dir")
# La function os.mkdir("new_dir") crea un nuevo directorio llamado new_dir

os.mkdir("newer_dir")
os.rmdir("newer_dir")
# Este fragmento de código crea un nuevo directorio llamado newer_dir. la segunda linea elimina el directorio newer_dir

import os

os.listdir("website")
# Este fragmento de código devuelve una lista de todos los archivos y subdirecciones en el directorio,

# dir = "website"
#  for name in os.listdir(dir):
#     fullname = os.path.join(dir, name)
#    if os.path.isdir(fullname):
#        print("{} is a directory".format(fullname))
#   else:
#          print("{} is a file".format(fullname))

# Acerca de este código
# Aquí está el código todo junto. Este código define una variable dir con el nombre del directorio que queremos
# verificar. Esto hace que nuestro código sea más legible y utilizable. Luego, recorre en iteración los nombres de
# archivos devueltos por os.listdir. Sabemos por nuestra ejecución anterior de esta función que estos son solo
# los nombres de los archivos sin directorio. Entonces, usando os.path.join, unimos el directorio a cada uno de esos
# nombres de archivo y creamos una Cadena con un nombre completo válido. Finalmente, usamos ese nombre completo para
# llamar a os.path.isdir y verificar si es un directorio o un archivo.

# ¿Cuál es el propósito de la función os.path.join?

# Crea una cadena que contiene directorios concatenados multiplataformas.


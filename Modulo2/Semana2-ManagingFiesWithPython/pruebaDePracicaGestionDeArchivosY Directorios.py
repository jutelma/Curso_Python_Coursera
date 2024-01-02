# Pregunta 1
# La función create_python_script crea un nuevo script de Python en el directorio de trabajo actual,
# le agrega la línea de comentarios declarada por la variable 'comentarios' y devuelve el tamaño del nuevo archivo.
# Complete los espacios en blanco para crear un script llamado "program.py".

import os


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, 'w') as file:  # Abre el archivo en modo de escritura ('w')
        file.write(comments)  # Escribe los comentarios en el archivo
    filesize = os.path.getsize(filename)  # Obtiene el tamaño del archivo
    return filesize


print(create_python_script("program.py"))

# .
# Pregunta 2
# La función new_directory crea un nuevo directorio dentro del directorio de trabajo actual, luego crea un nuevo
# archivo vacío dentro del nuevo directorio y devuelve la lista de archivos en ese directorio.
# Complete los espacios
# en blanco para crear un archivo "script.py" en el directorio "PythonPrograms".

import os


def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if not os.path.isdir(directory):
        os.mkdir(directory)

        # Create the new file inside the new directory
    os.chdir(directory)
    with open(filename, 'w') as file:
        pass

    # Return the list of files in the new directory
    return os.listdir()


# Pregunta 3
# ¿Cuál de los siguientes métodos del módulo del sistema operativo creará un nuevo directorio?
#
# R mkdir()

# 4.
# Pregunta 4
# La función file_date crea un nuevo archivo en el directorio de trabajo actual, verifica la fecha en que se modificó
# el archivo y devuelve solo la parte de la fecha de la marca de tiempo en el formato aaaa-mm-dd. Complete los
# espacios en blanco para crear un archivo llamado "newfile.txt" y verifique la fecha en que se modificó.

import os
import datetime


def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'w') as file:
        pass
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    date_modified = datetime.datetime.fromtimestamp(timestamp)
    date_string = date_modified.strftime("%Y-%m-%d")
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return "{}".format(date_string)


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd


print(new_directory("PythonPrograms", "script.py"))

# Pregunta 5
# La función parent_directory devuelve el nombre del directorio que se encuentra justo encima del directorio de trabajo
# actual. Recuerde que '..'es un alias de ruta relativa que significa "ir al directorio principal". Complete
# los espacios en blanco para completar esta función.

import os


def parent_directory():
    # Create a relative path to the parent
    # of the current working directory
    relative_parent = os.path.join(os.getcwd(), '..')

    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)


print(parent_directory())

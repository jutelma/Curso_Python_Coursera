# Estamos trabajando con una lista de flores y algo de información sobre cada una. La función create_file escribe
# esta información en un archivo CSV. La función content_of_file lee este archivo en registros y devuelve
# la información en un bloque bien formateado. Complete los espacios en blanco de la función contenido_de_archivo
# para convertir los datos del archivo CSV en un diccionario usando DictReader.

import csv
import os

# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename, "r") as file:
        # Read the rows of the file into a dictionary
        reader = csv.DictReader(file)
        # Process each item of the dictionary
        for row in reader:
            return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
    return return_string


# Call the function
print(contents_of_file("flowers.csv"))

# Usando nuevamente el archivo CSV de flores, complete los espacios en blanco de la función contenido_de_archivo
# para procesar los datos sin convertirlos en un diccionario. ¿Cómo se salta el registro del encabezado con los
# nombres de los campos?

import os
import csv


# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename) as file:
        # Read the rows of the file
        rows = csv.reader(file)
        # Skip the header row
        next(rows)

        # Process each row
        for row in rows:
            name, color, ftype = row
            # Format the return string for data rows only
            return_string += "a {} {} is {}\n".format(color, name, ftype)
    return return_string


# Call the function
print(contents_of_file("flowers.csv"))

# Pregunta 3
# Para utilizar la función writerows() de DictWriter() para escribir una lista de diccionarios en cada línea de un
# archivo CSV, ¿qué pasos debemos seguir? (Marque todo lo que corresponda)

# Importar el módulo del sistema operativo

# Crear una instancia de la clase DictWriter()

# Escriba el parámetro de nombres de campo en la primera fila usando writeheader()



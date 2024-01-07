"""Revisión: Generación de CSV
Introducción
Esta lectura de seguimiento está organizada para que coincida con el contenido del vídeo que sigue.
Contiene el mismo código que se muestra en el siguiente vídeo. Estos bloques de código le brindarán
la oportunidad de ver cómo está escrito el código, le permitirán practicar su ejecución y pueden usarse como
referencia para consultar.

Puede seguir la lectura mientras el instructor analiza el código o revisar el código después de ver el video."""
# import csv

# import csv

# hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]

# with open('hosts.csv', 'w') as hosts_csv:
#    writer = csv.writer(hosts_csv)
#    writer.writerows(hosts)

"""Revisión: lectura y escritura de archivos CSV con diccionarios
 Introducción
 Esta lectura de seguimiento está organizada para que coincida con el contenido del vídeo que sigue.
Contiene el mismo código que se muestra en el siguiente vídeo. Estos bloques de código le brindarán
la oportunidad de ver cómo está escrito el código, le permitirán practicar su ejecución y pueden usarse 
como referencia para consultar.

 Puede seguir la lectura mientras el instructor analiza el código o revisar el código después de ver el video.
 the follow command should be used in the terminal"""

# cat software.csv
# Output name,version, status, users
# MailTree,5.34,production,324
# CalDoor,1.25.1,beta,22
# Chatty Chicken,0.34,alpha,4
# with open('software.csv') as software:
#   reader = csv.DictReader(software)
#   for row in reader:
#       print("{} has {} users".format(row['name'], row["users"]))

"""
Acerca de este código
Aquí el código abre el archivo y crea un DictReader para procesar nuestros datos CSV, luego recorre las filas para 
acceder a la información en cada fila usando las claves tal como lo haríamos al acceder a los datos en el diccionario. 
"""
# users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
# {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
# {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
# keys = ["name", "username", "department"]
#  with open('by_department.csv', 'w') as by_department:
#    writer = csv.DictWriter(by_department, fieldnames=keys)
#    writer.writeheader()
#    writer.writerows(users)

"""
Acerca de este código
Aquí el código crea una lista de diccionarios con los datos que queremos almacenar. Para este ejemplo, 
queremos almacenar datos sobre los usuarios de nuestra empresa y los departamentos en los que trabajan. 
Entonces aquí tenemos nuestra lista de diccionarios y cada uno contiene las claves, el nombre, el nombre de usuario 
y el departamento. Ahora queremos escribir este archivo HTML. Entonces, primero definimos la lista de claves que 
queremos escribir en el archivo y luego abrimos el archivo para escribir. A continuación creamos DictWriter pasando 
las claves que habíamos identificado antes, y luego llamamos a dos métodos diferentes en el escritor. El método del 
encabezado derecho creará la primera línea del CSV según las claves que pasamos, y el método de las filas derecha 
convertirá la lista de diccionarios en líneas en ese archivo. 
"""
# #the follow command should be used in the terminal
#
# cat by_department.csv

# DictReader() nos permite convertir los datos de un archivo CSV en un diccionario estándar. DictWriter() \
# nos permite escribir datos de un diccionario en un archivo CSV. ¿Cuál es el parámetro que debemos pasar para que
# DictWriter() escriba nuestro diccionario en formato CSV?

# R El parámetro de nombres de campo de DictWriter() requiere una lista de claves

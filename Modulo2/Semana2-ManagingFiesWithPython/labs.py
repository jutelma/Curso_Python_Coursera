"""
Cuaderno de práctica: lectura y escritura de archivos
En este ejercicio, pondremos a prueba tus conocimientos sobre lectura y escritura de archivos jugando con algunos
archivos de texto.

Digamos que tenemos un archivo de texto que contiene los visitantes actuales de un hotel. Lo llamaremos invitados.txt.
Ejecute el siguiente código para crear el archivo. El archivo se completará automáticamente con el nombre de cada
huésped inicial en su propia línea.
"""
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()

# No se genera ningún resultado para la celda de código anterior. Para verificar el contenido del archivo guest.txt
# recién creado, ejecute el siguiente código.

with open("guests.txt") as guests:
    for line in guests:
        print(line)

# El resultado muestra que nuestro archivo guest.txt está correctamente completado con el nombre de cada invitado
# inicial en su propia línea. ¡Fresco!
#
# Ahora supongamos que queremos actualizar nuestro archivo a medida que los invitados entran y salen.
# Complete el código que falta en la siguiente celda para agregar invitados al archivo guest.txt a medida que
# se registran.

new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

# Para verificar si su código agregó correctamente los nuevos invitados al archivo guest.txt,
# ejecute la siguiente celda.

with open("guests.txt") as guests:
    for line in guests:
        print(line)

# Los nombres actuales en el archivo guest.txt deben ser: Bob, Andrea, Manuel, Polly, Khalid, Sam, Danielle y Jacob.
#
# ¿Se agregó correctamente el archivo guest.txt con los nuevos invitados? De lo contrario, regrese y edite su código
# asegurándose de completar los espacios en blanco de manera adecuada para que los nuevos invitados se agreguen
# correctamente al archivo guest.txt. Una vez que los nuevos invitados se hayan agregado correctamente,
# habrá completado correctamente el código que falta. ¡Excelente!
#
# Ahora eliminemos a los invitados que ya se han ido. Hay varias formas de hacer esto, sin embargo, el método que
#
# elegiremos para este ejercicio se describe a continuación:
#
# Abra el archivo en modo "lectura".
# Repita cada línea del archivo y coloque el nombre de cada invitado en una lista de Python.
# Abra el archivo una vez más en modo "escritura".
# Agregue el nombre de cada invitado en la lista de Python al archivo uno por uno.
#
# ¿Listo? Complete el código que falta en la siguiente celda para eliminar a los invitados que ya realizaron el
# check out.

checked_out = ["Andrea", "Manuel", "Khalid"]
temp_list = []

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

# Para verificar si su código eliminó correctamente los invitados retirados del archivo guest.txt,
# ejecute la siguiente celda.

with open("guests.txt") as guests:
    for line in guests:
        print(line)

# Los nombres actuales en el archivo guest.txt deben ser: Bob, Polly, Sam, Danielle y Jacob.
#
# ¿Se eliminaron correctamente los nombres de los invitados retirados del archivo guest.txt? De lo contrario,
# regrese y edite su código asegurándose de completar los espacios en blanco de manera adecuada para que los invitados
# retirados se eliminen correctamente del archivo guest.txt. Una vez que los invitados retirados se eliminen con éxito,
# habrá completado correctamente el código que falta. ¡Impresionante!
#
# Ahora comprobemos si Bob y Andrea todavía están registrados. ¿Cómo podríamos hacer esto? Simplemente leeremos
# cada línea del archivo para ver si su nombre está allí. Ejecute el siguiente código para comprobar si Bob y Andrea todavía están registrados.

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt", "r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

# Podemos ver que Bob está registrado mientras que Andrea no. ¡Buen trabajo! ¡Has aprendido los conceptos básicos de
# lectura y escritura de archivos en Python!

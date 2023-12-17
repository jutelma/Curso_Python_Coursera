# 1 Complete los espacios en blanco para completar la función "confirmar_longitud". Esta función debe devolver
# cuántos caracteres contiene una cadena siempre que tenga uno o más caracteres; de lo contrario, devolverá 0.
# Complete las operaciones de cadena necesarias en esta función para que entradas como "lunes" producirá la salida "6".

def confirm_length(word):
    # Complete the condition statement using a string operation.
    if len(word) > 0:
        # Complete the return statement using a string operation.
        return len(word)
    else:
        return 0


print(confirm_length("a"))  # Should print 1
print(confirm_length("This is a long string"))  # Should print 21
print(confirm_length("Monday"))  # Should print 6
print(confirm_length(""))  # Should print 0


# Pregunta 2
# Complete el bucle for y el método de cadena necesarios en esta función para que una llamada de función como
# "alpha_length("Esto tiene 1 número")" devolverá la salida "17". Esta función debería:

# 1 aceptar una cadena a través de los parámetros de la función;

# 2 iterar sobre los caracteres de la cadena;

# 3 determinar si cada carácter es una letra (contando sólo caracteres alfabéticos; se deben ignorar los números,
#  la puntuación y los espacios);

# 4  incrementar el contador;

# 5 Devuelve el recuento de letras de la cadena.


def alpha_length(string):
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for character in string:
        # Complete the if-statement using a string method.
        if character.isalpha():
            count_alpha += 1
    return count_alpha


print(alpha_length("This has 1 number in it"))  # Should print 17
print(alpha_length("Thisisallletters"))  # Should print 16
print(alpha_length("This one has punctuation!"))  # Should print 21


# Pregunta 3
# Considere el siguiente escenario sobre el uso de listas de Python:
#
# Un profesor encomendó a sus dos asistentes, Jaime y Drew, la tarea de mantener una lista de asistencia de los
# estudiantes en el orden en que llegan al salón de clases. Drew fue el primero en notar qué estudiantes llegaron y
# luego Jaime se hizo cargo. Después de la clase, cada uno ingresó sus listas en la computadora y se las enviaron por
# correo electrónico al profesor. El profesor quiere combinar las dos listas en una, en el orden de llegada de cada
# estudiante. Jaime envió un correo electrónico de seguimiento, diciendo que su lista está en orden inverso.
#
# Completa el código para combinar las dos listas en una en el orden de: el contenido de la lista de Drew,
# seguido de la lista de Jaime en orden inverso , para producir una lista precisa de los estudiantes a medida que
# llegaron. Esta función debería:
#
# 1 aceptar dos listas a través de los parámetros de la función;
#
# 2 invertir el orden de “lista1”;
#
# 3 combine las dos listas de modo que "lista2" aparezca primero, seguida de "lista1";
#
# 4 devolver la nueva lista.

def combine_lists(list1, list2):
    combined_list = []  # Initialize an empty list variable
    list1.reverse()  # Reverse the order of "list1"
    list2.extend(list1)  # Combine the two lists
    combined_list = list2
    return combined_list


Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]

print(combine_lists(Jaimes_list, Drews_list))


# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']


# 4. Pregunta 4 Complete el espacio en blanco para completar la función “números_pares”. Esta función debe usar una
# lista de comprensión para crear una lista de números pares usando una declaración if condicional con el operador de
# módulo para probar números divisibles por 2. La función recibe dos variables y debe devolver la lista de números
# pares que ocurren entre " primeras” y “últimas” variablesexclusivamente (es decir, no modifique el comportamiento
# predeterminado del rango para excluir el valor “final” del rango)< /span>

def even_numbers(first, last):
    return [num for num in range(first, last) if num % 2 == 0]


print(even_numbers(4, 14))  # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]


# 5. Pregunta 5 Complete los espacios en blanco para completar la función "animales_en peligro de extinción". Esta
# función acepta un diccionario que contiene una lista de animales en peligro de extinción (claves) y su población
# restante (valores). Para cada clave en el diccionario "animal_dict" dado, formatee una cadena para imprimir el
# nombre del animal, con un nombre de animal por línea.

def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items
    # in the dictionary.
    for animal, population in animal_dict.items():
        # Use a string method to format the required string.
        result += f"{animal}\n"
    return result


print(endangered_animals({"Javan Rhinoceros": 60, "Vaquita": 10, "Mountain Gorilla": 200, "Tiger": 500}))


# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger


# 6.
# Pregunta 6
# Considere el siguiente escenario sobre el uso de diccionarios de Python:
#
# Tessa y Rick están organizando una fiesta. Juntos enviaron invitaciones y recopilaron las respuestas en un
# diccionario, con los nombres de sus amigos y la cantidad de invitados que traerá cada amigo.
#
# Complete la función para que la función "check_guests" recupere el número de invitados (valor) que trae el amigo
# "invitado" (clave) especificado. Esta función debería:
#
# 1 aceptar un diccionario "guest_list" y una variable clave "guest" pasada a través de los parámetros de la función;
#
# 2 Imprime los valores asociados con la variable clave.

def check_guests(guest_list, guest):
    return guest_list.get(guest, "Guest not found")  # Return the value for the given key


guest_list = {"Adam": 3, "Camila": 3, "David": 5, "Jamal": 3, "Charley": 2, "Titus": 1, "Raj": 6, "Noemi": 1,
              "Sakira": 3, "Chidi": 5}

print(check_guests(guest_list, "Adam"))  # Should print 3
print(check_guests(guest_list, "Sakira"))  # Should print 3
print(check_guests(guest_list, "Charley"))  # Should print 2


# Pregunta 7
# Considere el siguiente escenario sobre el uso de diccionarios de Python:
#
# Un profesor utiliza un diccionario para almacenar las calificaciones de los alumnos. Las calificaciones se
# almacenan como un valor de puntos sobre 100. Actualmente, el profesor tiene una configuración de diccionario para
# las calificaciones del primer trimestre y quiere duplicarla para el segundo trimestre. Las claves de nombre de los
# estudiantes en el diccionario deben permanecer iguales, pero los valores de las calificaciones deben restablecerse
# a 0.
#
# Complete la función "setup_grade-book" para que entradas como "{"James": 93, "Felicity": 98, "Barakaa": 80}" generen
# un diccionario resultante que contenga "{"James": 0, "Felicity": 0, "Barakaa": 0}”. Esta función debería:
#
# 1 aceptar una variable del diccionario “old_grade-book” a través de los parámetros de la función;
#
# 2 hacer una copia del diccionario “old_grade-book”;
#
# 3 iterar sobre cada par de clave y valor en el nuevo diccionario;
#
# 4 reemplace el valor de cada clave con el número 0;
#
# 5 devolver el nuevo diccionario.

def setup_gradebook(old_gradebook):
    # Use a dictionary method to create a new copy of the "old_gradebook".
    new_gradebook = old_gradebook.copy()
    # Complete the for loop to iterate over the new gradebook.
    for student in new_gradebook:
        # Use a dictionary operation to reset the grade values to 0.
        new_gradebook[student] = 0
    return new_gradebook


fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}


# Pregunta 8
# ¿Qué devuelven los siguientes comandos cuando car_make = "Lamborghini"?

# print(car_make[3:-5])
# print(car_make[-4:])
# print(car_make[:7])

# R bor, hini, Lamborg


# Pregunta 9
# ¿Qué significa la lista "car_makes" contienen después de ejecutar estos comandos?

# car_makes = ["Ford", "Volkswagen", "Toyota"]
# car_makes.remove("Ford")

# R ['Volkswagen', 'Toyota']


# Pregunta 10
# ¿Qué devuelven los siguientes comandos?

# host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
# host_addresses.keys()

# R dict_keys(['router', 'localhost', 'google'])

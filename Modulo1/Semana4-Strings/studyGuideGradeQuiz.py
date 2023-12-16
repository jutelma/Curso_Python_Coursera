"""
Guía de estudio: Prueba calificada del Módulo 4

Es hora de prepararse para el cuestionario calificado del Módulo 4. Revise los siguientes elementos de este módulo
antes de comenzar la prueba. Si desea refrescar su memoria sobre estos materiales, consulte también las Guías de
estudio ubicadas antes de cada prueba de práctica en el Módulo 4: Guía de estudio: cuerdas , Guía de estudio: enumera
operaciones y métodos , y Guía de estudio: métodos de diccionario .


Conocimiento

 · Cómo generar una lista de claves en un diccionario de Python.

 · Cómo determinar la salida de un rango de índice de cadena utilizado en una cadena.

 · Determine qué debe contener una lista después de utilizar el método .insert() en la lista.

 · Cómo reemplazar una palabra específica en una oración con la misma palabra en todas las letras mayúsculas.

 · Cómo utilizar un diccionario para contar la frecuencia de las letras de una cadena.

Operaciones, métodos y funciones

 · Métodos de cadena, operaciones y funciones

    .superior()

    .más bajo()

    .dividir()

    .formato()

    .isnumeric()

    .isalfa()

    .reemplazar()

    índice de cadena [ ]

    solo()

 ·Listar operaciones y métodos

    .contrarrestar()

    .extender()

    .insertar()

    .adjuntar()

    .eliminar()

    .clasificar()

    lista de comprensiones [ ]

    enumerar comprensiones [ ] con condición if

 ·Operaciones y métodos del diccionario

    .elementos()

    .actualizar()

    .llaves()

    .valores()

    .Copiar()

    diccionario[clave]

    diccionario[clave] = valor



Habilidades de codificación

Habilidad 1: usar métodos de cadena

    · Separe los valores numéricos de los valores de texto en una cadena usando .split() .

    · Iterar sobre los elementos de una cadena.

    · Pruebe si el elemento contiene letras con .isalpha() .

    · Asigne los elementos de la cadena dividida a nuevas variables.

    · Recorte cualquier espacio en blanco adicional usando .strip() .

    · Formatee una cadena usando .format() y { } marcadores de posición variables.


"""


def sales_prices(item_and_price):
    # Initialize variables "item" and "price" as strings
    item = ""
    price = ""
    # Create a variable "item_or_price" to hold the result of the split.
    item_or_price = item_and_price.split()

    # For each element "x" in the split variable "item_or_price"
    for x in item_or_price:

        # Check if the element is a number
        if x.isalpha():

            # If true, assign the element to the "item" string variable and add a space
            # for any item names containing multiple words, like "Winter fleece jacket".
            item += x + " "

        # Else, if x is a number (if x.isalpha() is false):
        else:
            # Assign the element to the "price" string variable.
            price = x

    # Strip the extra space to the right of the last "item" word
    item = item.strip()

    # Return the item name and price formatted in a sentence
    return "{} are on sale for ${}".format(item, price)


# Call to the function
print(sales_prices("Winter fleece jackets 49.99"))


# Should print "Winter fleece jackets are on sale for $49.99"

# · Utilice la función len() para medir una cadena.

# This function accepts a string variable "data_field".
def count_words(data_field):
    # Splits the string into individual words.
    split_data = data_field.split()

    # Then returns the number of words in the string using the len()
    # function.
    return len(split_data)

    # Note that it is possible to combine the len() function and the
    # .split() method into the same line of code by inserting the
    # data_field.split() command into the the len() function parameters.


# Call to the function
count_words("Catalog item 3523: Organic raw pumpkin seeds in shell")


# Output should be 9

# Habilidad 2: Uso de lista métodos
# · Invertir el orden de una lista usando el método .reverse() .

# · Combina dos listas usando el método .extend().

# This function accepts two variables, each containing a list of years.
# A current "recent_first" list contains [2022, 2018, 2011, 2006].
# An older "recent_last" list contains [1989, 1992, 1997, 2001].
# The lists need to be combined with the years in chronological order.
def record_profit_years(recent_first, recent_last):
    # Reverse the order of the "recent_first" list so that it is in
    # chronological order.
    recent_first.reverse()

    # Extend the "recent_last" list by appending the newly reversed
    # "recent_first" list.
    recent_last.extend(recent_first)

    # Return the "recent_last", which now contains the two lists
    # combined in chronological order.
    return recent_last


# Assign the two lists to the two variables to be passed to the
# record_profit_years() function.
recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989, 1992, 1997, 2001]

# Call the record_profit_years() function and pass the two lists as
# parameters.
print(record_profit_years(recent_first, recent_last))


# Should print [1989, 1992, 1997, 2001, 2006, 2011, 2018, 2022]

# Habilidad 3: Usar una lista de comprensión
# Utilice una lista de comprensión [] como acceso directo para crear una nueva lista a partir de un rango.

# Incluir un cálculo con un for bucle in a rango con 2 parámetros (inferior, superior+1).

# The function accepts two parameters: a start year and an end year.
def list_years(start, end):
    # It returns a list comprehension that creates a list of years in a for
    # loop using a range from the start year to the end year (inclusive of
    # the upper range year, using end+1).
    return [year for year in range(start, end + 1)]


# Call the years() function with two parameters.
print(list_years(1972, 1975))


# Should print [1972, 1973, 1974, 1975]

#  Utilice una lista de comprensión [ ] con un bucle for y un if < una i=4>condición.

# The function accepts two variable integers through the parameters and
# returns all odd numbers between x and y-1.
def odd_numbers(x, y):
    # This list comprehension uses a for loop to iterate through values
    # of n in a range from x to y, with the value of y excluded (meaning
    # keep the default range() function behavior to exclude the
    # end-of-range value from the range). Since an incremental value is not
    # specified, the range function uses the default increment of +1.
    # The if condition checks n to test if the number is odd using the
    # modulo operator. This condition is written to check if n is divided
    # by 2, that the remainder is not 0.
    return [n for n in range(x, y) if n % 2 != 0]


# Call the years() function with two parameters.
print(odd_numbers(5, 15))


# Habilidad 4: Uso del diccionario métodos
# · Iterar a través de las claves y valores de un diccionario.
# · Devuelve las claves y los valores en una cadena formateada usando la función .format().

# The network() function accepts a dictionary "servers" as a parameter.
def network(servers):
    # A string variable is initialized to hold the "result".
    result = ""

    # For each "hostname" (key) and "IP address" (value) in the "server" dictionary items...
    for hostname, IP_address in servers.items():
        # A string identifying the hostname and IP address for each server is added
        # to the "result" variable. The string .format() function and is used to plug
        # the hostname and IP_address variables into the designated {} placeholders
        # within the string.
        result += "The IP address of the {} server is {}".format(hostname, IP_address) + "\n"

    # Return the "result" variable string.
    return result


# Call the "network" function with the dictionary.
print(network({"Domain Name Server": "8.8.8.8", "Gateway Server": "192.168.1.1", "Print Server": "192.168.1.33",
               "Mail Server": "192.168.1.190"}))


# Should print:
# The IP address of the Domain Name Server server is 8.8.8.8
# The IP address of the Gateway Server server is 192.168.1.1
# The IP address of the Print Server server is 192.168.1.33
# The IP address of the Mail Server server is 192.168.1.190


# · Crea una copia de un diccionario.
# · Iterar a través de los valores del nuevo diccionario.
# · Cambie cada valor en el nuevo diccionario, manteniendo las mismas claves.

# The scores() function accepts a dictionary "game_scores" as a parameter.
def reset_scores(game_scores):
    # The .copy() dictionary method is used to create a new copy of the "game_scores".
    new_game_scores = game_scores.copy()

    # The for loop iterates over new_game_scores items, with the player as the key
    # and the score as the value.
    for player, score in new_game_scores.items():
        # The dictionary operation to assign a new value to a key is used
        # to reset the grade values to 0.
        new_game_scores[player] = 0

    return new_game_scores


# The dictionary is defined.
game1_scores = {"Arshi": 3, "Catalina": 7, "Diego": 6}

# Call the "reset_scores" function with the "game1_scores" dictionary.
print(reset_scores(game1_scores))
# Should print {'Arshi': 0, 'Catalina': 0, 'Diego': 0}

"""Recordatorio: la sintaxis correcta es fundamental Usar una sintaxis precisa es fundamental al escribir código en 
cualquier lenguaje de programación, incluido Python. Incluso un pequeño error tipográfico puede causar un error de 
sintaxis y el evaluador automatizado de pruebas codificado en Python marcará su código como incorrecto. Esto refleja 
errores de codificación de la vida real en el sentido de que un solo error de ortografía, mayúsculas y minúsculas, 
puntuación, etc. puede provocar que el código falle. Los problemas de codificación causados ​​por una sintaxis 
imprecisa siempre serán un problema, ya sea que esté aprendiendo un lenguaje de programación o esté utilizando 
habilidades de programación en el trabajo. Por lo tanto, es fundamental adquirir el hábito de ser preciso en el 
código ahora.

No se otorgará crédito si hay errores de codificación en las pruebas calificadas automáticamente, incluidos errores 
menores. Afortunadamente, tiene 3 oportunidades opcionales para volver a tomar las pruebas calificadas de este curso. 
Además, tiene repeticiones ilimitadas de cuestionarios de práctica y puede revisar los videos y las lecturas tantas 
veces como necesite para dominar los conceptos de este curso.

Ahora, antes de comenzar la prueba calificada, revise esta lista de errores de sintaxis comunes que cometen los 
codificadores al escribir código.

Errores de sintaxis comunes:

    · Errores ortográficos

    · Sangrías incorrectas

    · Caracteres clave faltantes o incorrectos:

        · Tipos entre paréntesis: (curvo), [cuadrado], {rizado}

        · Tipos de cotización: "directa-doble" o 'rizado-simple', “rizado-doble” o “rizado-simple”

        · Bloquear caracteres de introducción, como dos puntos:

    · No coinciden los tipos de datos

    · Palabras reservadas de Python faltantes, utilizadas incorrectamente o mal colocadas

    · Uso de mayúsculas y minúsculas incorrectas: Python es un lenguaje que distingue entre mayúsculas y minúsculas 

"""

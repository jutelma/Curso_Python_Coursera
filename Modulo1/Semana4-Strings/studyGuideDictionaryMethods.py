""" Guía de estudio: métodos de diccionario

Esta guía de estudio proporciona un resumen de referencia rápida de lo que aprendió en esta lección y sirve como guía
para la próxima prueba de práctica.

En el segmento Diccionario, aprendió sobre las propiedades del tipo de datos del diccionario de Python,
en qué se diferencian los diccionarios de las listas, cómo iterar sobre el contenido de un diccionario y cómo usar
diccionarios con listas y cadenas.


Conocimiento Los diccionarios de Python se utilizan para organizar elementos en colecciones. Los diccionarios
incluyen una o más claves, con uno o más valores asociados a cada clave.

Sintaxis
"""
# my_dictionary = {keyA:value1,value2, keyB:value3,value4}

""" Operaciones
 · len(diccionario) : devuelve el número de elementos de un diccionario.

 · para clave, en diccionario : itera sobre cada clave en un diccionario.

 · para clave, valor en diccionario.items() : itera sobre cada par clave-valor en un diccionario.

 · si la clave está en el diccionario : comprueba si una clave está en un diccionario.

 · diccionario[clave] : accede a un valor utilizando la clave asociada de un diccionario.

 · diccionario[clave] = valor : establece un valor asociado con una clave.

 · del diccionario[clave] : elimina un valor utilizando la clave asociada de un diccionario.


Métodos

 · diccionario.get(clave, predeterminado) : devuelve el valor correspondiente a una clave, o el valor predeterminado 
   si la clave especificada no está presente.

 · Dictionary.keys() : devuelve una secuencia que contiene las claves de un diccionario.

 ·Dictionary.values() : devuelve una secuencia que contiene los valores de un diccionario.

 · diccionario[clave].append(valor) : agrega un nuevo valor para una clave existente.

 · Dictionary.update(other_dictionary) : actualiza un diccionario con los elementos de otro diccionario. Las entradas 
   existentes se actualizan; se añaden nuevas entradas.

 · Dictionary.clear() : elimina todos los elementos de un diccionario.

 · Dictionary.copy() : hace una copia de un diccionario.


Diccionarios versus listas
 
Los diccionarios son similares a las listas, pero existen algunas diferencias:

Tanto diccionarios como listas:

 · se utilizan para organizar elementos en colecciones;

 · se utilizan para inicializar un nuevo diccionario o lista, utilice corchetes vacíos;

 · puede recorrer los elementos o elementos de la colección; y

 · Puede utilizar una variedad de métodos y operaciones para crear y cambiar las colecciones, como eliminar e 
   insertar elementos o elementos.

Sólo diccionarios:

 · son conjuntos desordenados;

 · tener claves que pueden ser una variedad de tipos de datos, incluidas cadenas, números enteros, flotantes, tuplas;

 · puede acceder a los valores del diccionario mediante claves;

 · utilice corchetes dentro de llaves { [ ] };

 · utilice dos puntos entre la clave y los valores;

 · utilice comas para separar cada grupo de claves y cada valor dentro de un grupo de claves;

 · haga que sea más rápido y fácil para un intérprete de Python encontrar elementos específicos, en comparación con 
   una lista.

Ejemplo de diccionario:"""

pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"], "cats": ["Persian", "Scottish Fold", "Siberian"],
                  "rabbits": ["Angora", "Holland Lop", "Harlequin"]}

print(pet_dictionary.get("dogs", 0))
# Should print ['Yorkie', 'Collie', 'Bulldog']

"""
Sólo listas:

 · son conjuntos ordenados;

 · elementos de la lista de acceso por posiciones de índice;

 · requerir que estos índices sean números enteros;

 · utilice corchetes [ ];

 · utilice comas para separar cada elemento de la lista.

Ejemplo de lista:
"""
pet_list = ["Yorkie", "Collie", "Bulldog", "Persian", "Scottish Fold", "Siberian", "Angora", "Holland Lop", "Harlequin"]

print(pet_list[0:3])
# Should print ['Yorkie', 'Collie', 'Bulldog']

"""Habilidades de codificación 
Grupo de habilidades 1 
 · Itere sobre los pares clave y valor de un diccionario usando un 
bucle for con el método Dictionary.items() para calcular la suma de los valores en un diccionario."""


# This function returns the total time, with minutes represented as
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day.


def sum_server_use_time(Server):
    # Initialize the variable as a float data type, which will be used
    # to hold the sum of the total hours and minutes of server usage by
    # end users in a day.
    total_use_time = 0.0

    # Iterate through the "Server" dictionary’s key and value items
    # using a for loop.
    for key, value in Server.items():
        # For each end user key, add the associated time value to the
        # total sum of all end user use time.
        total_use_time += Server[key]

    # Round the return value and limit to 2 decimal places.
    return round(total_use_time, 2)


FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

print(sum_server_use_time(FileServer))  # Should print 20.1

"""Grupo de habilidades 2 

 · Concatene un valor, una cadena y la clave para cada elemento del diccionario y agréguelo al 
   final de una nueva lista [] usando el método list.append(x) .

 · Itere sobre claves con múltiples valores de un diccionario usando bucles for anidados con el método 
   Dictionary.items() ."""


# This function receives a dictionary, which contains common employee
# last names as keys, and a list of employee-first names as values.
# The function generates a new list that contains each employees’ full
# name (First_name Last_Name). For example, the key "Garcia" with the
# values ["Maria", "Hugo", "Lucia"] should be converted to a list
# that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].


def list_full_names(employee_dictionary):
    # Initialize the "full_names" variable as a list data type using
    # empty [] square brackets.
    full_names = []

    # The outer for loop iterates through each "last_name" key and
    # associated "first_name" values, in the "employee_dictionary" items.
    for last_name, first_names in employee_dictionary.items():

        # The inner for loop iterates over each "first_name" value in
        # the list of "first_names" for one "last_name" key at a time.
        for first_name in first_names:
            # Append the new "full_names" list with the "first_name" value
            # concatenated with a space " ", and the key "last_name".
            full_names.append(first_name + " " + last_name)

    # Return the new "full_names" list once the outer for loop has
    # completed all iterations.
    return full_names


print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']

"""
Grupo de habilidades 3  

 · Utilice la operación diccionario[clave] = valor para asociar un valor con una clave en un diccionario.   

 · Itere sobre claves con múltiples valores de un diccionario, usando bucles for anidados y una declaración if , 
   y el método Dictionary.items() .

 · Utilice el método diccionario[clave].append(valor) para agregar la clave, una cadena y la clave para cada elemento 
   del diccionario."""


# This function receives a dictionary, which contains resource
# categories (keys) with a list of available resources (values) for a
# company’s IT Department. The resources belong to multiple categories.
# The function should reverse the keys and values to show which
# categories (values) each resource (key) belongs to.


def invert_resource_dict(resource_dictionary):
    # Initialize a "new_dictionary" variable as a dict data type using
    # empty {} curly brackets.
    new_dictionary = {}
    # The outer for loop iterates through each "resource_group" and
    # associated "resources" in the "resource_dictionary" items.
    for resource_group, resources in resource_dictionary.items():
        # The inner for loop iterates over each "resource" value in
        # the list of "resources" for one "resource_group" key at a time.
        for resource in resources:
            # The if-statement checks if the current "resource" value has
            # been appended as a key to the "new_dictionary" yet.
            if resource in new_dictionary:
                # If True, then append the "resource_group" as a value to the
                # "resource", which is now the key.
                new_dictionary[resource].append(resource_group)
            # If False (else), then add the "resource" as a new key with the
            # "resource_group" as a value for that key.
            else:
                new_dictionary[resource] = [resource_group]
    # Return the new dictionary once the outer for loop has completed
    # all iterations.
    return new_dictionary


print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
                            "PC Parts": ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"],
                            "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video
# cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}

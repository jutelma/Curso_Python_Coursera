"""1. Pregunta 1 Complete los espacios en blanco para completar la función is_palindrome. Esta función comprueba si
una cadena determinada es un palíndromo. Un palíndromo es una cadena que contiene las mismas letras en el mismo
orden, ya sea que la palabra se lea de izquierda a derecha o de derecha a izquierda. Ejemplos de palíndromos son
palabras como kayak y radar, y frases como "Never Odd or Even". La función debe ignorar los espacios en blanco y las
mayúsculas al comprobar si la cadena dada es un palíndromo. Complete esta función para devolver Verdadero si la
cadena pasada es un palíndromo, Falso en caso contrario.
"""


def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""

    for letter in input_string:

        if letter != " ":
            new_string = new_string + letter
            reverse_string = letter + reverse_string
    if new_string.lower() == reverse_string.lower():
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Debería ser Verdadero
print(is_palindrome("abc"))  # Debería ser Falso
print(is_palindrome("kayak"))  # Debería ser Verdadero

"""
2 Usando el método de formato, complete los espacios en la función convert_distance para que devuelva la frase "X 
millas equivalen a Y km", donde Y tiene solo 1 decimal. Por ejemplo, convert_distance(12) debería devolver "12 millas 
equivalen a 19,2 km"."""


def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result


print(convert_distance(12))  # Debería ser: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Debería ser: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Debería ser: 11 miles equals 17.6 km

"""3. Pregunta 3 Si tenemos una variable de cadena llamada Clima = "Lluvia", ¿cuál de las siguientes imprimirá la 
subcadena "Lluvia" o todos los caracteres antes de la "f"?
La opción que imprimirá la subcadena "Lluvia" o todos los caracteres antes de la "f" es la siguiente:

"""
# print(Clima[:4])

"""Pregunta 4 Complete los espacios en blanco en la función de etiqueta de nombre para que utilice el método de 
formato para devolver nombre y la primera inicial de apellido seguido de un punto. Por ejemplo, la etiqueta de nombre 
("Jane", "Smith") debería devolver "Jane S."""


def nametag(first_name, last_name):
    return "{} {}.".format(first_name, last_name[0])


print(nametag("Jane", "Smith"))  # Debería mostrar "Jane S."
print(nametag("Francesco", "Rinaldi"))  # Debería mostrar "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))  # Debería mostrar "Jean-Luc G."


"""5. Pregunta 5 La función replace_ending reemplaza una subcadena especificada al final de una oración determinada 
con una nueva subcadena. Si la subcadena especificada no aparece al final de la oración dada, no se realiza ninguna 
acción y se devuelve la oración original. Si hay más de una aparición de la subcadena especificada en la oración, 
solo se reemplaza la subcadena al final de la oración. Por ejemplo, replace_ending("abcabc", "abc", "xyz") debería 
devolver abcxyz, no xyzxyz o xyzabc. La comparación de cadenas distingue entre mayúsculas y minúsculas, por lo que 
replace_ending("abcabc", "ABC", "xyz") debería devolver abcabc (no se realizaron cambios)."""


def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        i = len(sentence) - len(old)
        new_sentence = sentence[:i] + new
        return new_sentence
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Debería mostrar "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Debería mostrar "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Debería mostrar "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Debería mostrar "The weather is nice in April"

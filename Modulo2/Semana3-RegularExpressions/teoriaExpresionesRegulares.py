# ¿Cuál de las siguientes demuestra cómo se pueden utilizar las expresiones regulares (expresiones regulares)?
# R Encuentra cadenas de texto que coincidan con un patrón

# ¿Por qué utilizar expresiones regulares?
# Introducción

# Estos bloques de código le brindarán
# la oportunidad de ver cómo está escrito el código, le permitirán practicar su ejecución y pueden usarse
# como referencia para consultar.

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index + 1:index + 6])

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# Acerca de este código

# Aquí se usa el módulo re que nos permite usar la función de búsqueda para encontrar expresiones regulares dentro
# de cadenas. Luego, se define una expresión regular r"|[(\d+)\]", que coincide con una cadena encerrada entre
# corchetes seguida de uno o más dígitos. Luego, utiliza la función re.search() para buscar en el registro
# de cadenas una coincidencia con la expresión regular. La función re.search() devuelve un objeto Match si se
# encuentra una coincidencia, o Ninguno si no se encuentra ninguna coincidencia. la función re.search() devuelve un
# objeto Match porque el registro de cadena contiene una coincidencia con la expresión regular. El objeto Match
# tiene un método group() que devuelve los grupos capturados de la coincidencia. En este caso, el único grupo
# capturado es el número, que devuelve la expresión resultado[1].

# En lugar de utilizar la función index() del módulo de cadena, podemos utilizar expresiones regulares,
# que son más flexibles. Después de importar el módulo de expresión regular re, ¿qué función de expresión regular
# podría usarse en lugar de los métodos estándar?

# R re.search()

# Usando la terminal, ¿cuál de los siguientes comandos usará correctamente grep para encontrar las palabras
# “sling” y “sting” (suponiendo que estén en nuestro archivo, file.txt)?

# R user@ubuntu:~$ grep s.ing /usr/file.txt

# Una cosa que recordar que el circumplejo y el signo del dólar coinciden específicamente con el inicio y el final
# de la línea, no con una cadena


# Revisión: coincidencia simple en Python

# Introducción

# Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar
# su ejecución y pueden usarse como referencia para consultar.


import re

result = re.search(r"aza", "plaza")
print(result)

import re

result = re.search(r"aza", "bazaar")
print(result)

import re

result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x", "xenon"))

import re

print(re.search(r"p.ng", "penguin"))

import re

print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))

import re

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

# Complete el código para verificar si el texto pasado contiene las vocales a, e e i, con exactamente una aparición
# de cualquier otro carácter intermedio.

import re


def check_aei(text):
    result = re.search(r"a.e.i", text)
    return result != None


print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False
print(check_aei("paramedic"))  # True

# Revisión: comodines y clases de personajes

# Introducción
# Contiene el mismo código que se muestra en el siguiente vídeo.
# Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código,
# le permitirán practicar su ejecución y pueden usarse como referencia para consultar.


import re

print(re.search(r"[Pp]ython", "Python"))

import re

print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

import re

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

# Complete el código para verificar si el texto pasado contiene símbolos de puntuación: comas, puntos, dos puntos,
# punto y coma, signos de interrogación y signos de exclamación.

import re


def check_punctuation(text):
    result = re.search(r"[\.,;:\?!]", text)
    return result != None


print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?"))  # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False

# Reseña: Clasificatorias de repetición

# Introducción
# Esta lectura de seguimiento.
# Estos bloques de código le brindarán la oportunidad
# de ver cómo está escrito el código, le permitirán practicar su ejecución y pueden usarse como referencia
# para consultar.


import re

print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

import re

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

import re

print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

# La función repetición_letra_a comprueba si el texto pasado incluye la letra "a" (minúscula o mayúscula)
# al menos dos veces. Por ejemplo, repetir_letra_a("plátano") es Verdadero, mientras que repetir_letra_a("piña")
# es Falso. Complete el código para que esto funcione.

import re


def repeating_letter_a(text):
    result = re.search(r"(?i)a.*a", text)
    return result != None


print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True

# Revisión: personajes que escapan
# Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar
# su ejecución y pueden usarse como referencia para consultar.

import re

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

import re

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

# Complete el código para verificar si el texto pasado tiene al menos 2 grupos de caracteres alfanuméricos
# (incluidas letras, números y guiones bajos) separados por uno o más espacios en blanco

import re


def check_character_groups(text):
    result = re.search(r"(\w+\s+)+", text)
    return result != None


print(check_character_groups("One"))  # False
print(check_character_groups("123  Ready Set GO"))  # True
print(check_character_groups("username user_01"))  # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False

# www.regex101.com    recursos para consultar expresiones regulares.

# Revisión: expresiones regulares en acción
# Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar su
# ejecución y pueden usarse como referencia para consultar.

import re

print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

import re

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

# Complete el código para verificar si el texto pasado se parece a una oración estándar, lo que significa que
# comienza con una letra mayúscula, seguida de al menos algunas letras minúsculas o un espacio,
# y termina con un punto, un signo de interrogación o un signo de exclamación.

import re


def check_sentence(text):
    result = re.search(r"^[A-Z][a-z\s]+[.!?]$", text)
    return result != None


print(check_sentence("Is this is a sentence?"))  # True
print(check_sentence("is this is a sentence?"))  # False
print(check_sentence("Hello"))  # False
print(check_sentence("1-2-3-GO!"))  # False
print(check_sentence("A star is born."))  # True

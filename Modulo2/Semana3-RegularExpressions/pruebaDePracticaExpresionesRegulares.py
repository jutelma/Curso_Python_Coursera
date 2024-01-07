# Pregunta 1
# función check_web_address comprueba si el texto pasado califica como una dirección web de nivel superior,
# lo que significa que contiene caracteres alfanuméricos (que incluyen letras, números y guiones bajos),
# así como puntos, guiones y un signo más, seguido de un punto. y un dominio de nivel superior de solo caracteres
# como ".com", ".info", ".edu", etc. Complete la expresión regular para hacerlo, usando caracteres de escape,
# comodines, calificadores de repetición, principio y fin. caracteres fuera de línea y clases de caracteres.

import re


def check_web_address(text):
    pattern = r"^[\w\.\-+]+\.[a-zA-Z]+$"
    result = re.search(pattern, text)
    return result != None


print(check_web_address("gmail.com"))  # True
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True

# 2.
# Pregunta 2
# La función check_time verifica el formato de hora de un reloj de 12 horas, de la siguiente manera: la hora está
# entre 1 y 12, sin cero a la izquierda, seguida de dos puntos, luego minutos entre 00 y 59, luego un espacio
# opcional y luego AM o PM, en mayúsculas o minúsculas. Complete la expresión regular para hacer eso.
# ¿Cuántos de los conceptos que acabas de aprender puedes usar aquí?

import re


def check_time(text):
    pattern = r"^([0-9]|1[0-2]):[0-5][0-9]\s?(AM|am|PM|pm)$"
    result = re.search(pattern, text)
    return result != None


print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False

# 3.
# Pregunta 3
# La función contiene_acronym verifica la presencia de 2 o más caracteres o dígitos entre paréntesis en el texto,
# con al menos el primer carácter en mayúscula (si es una letra), y devuelve Verdadero si se cumple la condición,
# o Falso en caso contrario. Por ejemplo, "La mensajería instantánea (IM) es un conjunto de tecnologías de
# comunicación utilizadas para la comunicación basada en texto" debería devolver Verdadero porque (IM) satisface
# las condiciones de coincidencia". Complete la expresión regular en esta función:

import re


def contains_acronym(text):
    pattern = r"\([A-Z0-9][a-zA-Z0-9]+\)"
    result = re.search(pattern, text)
    return result != None


print(contains_acronym(
    "Instant messaging (IM) is a set of communication technologies used for text-based communication"))  # True
print(contains_acronym(
    "American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication"))  # True
print(contains_acronym("Please do NOT enter without permission!"))  # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)"))  # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!"))  # True

# 4 Pregunta 4
# ¿Qué indica la "r" antes de la cadena de patrón en re.search(r"Py.*n", sample.txt)?

# R Raw strings

# Pregunta 5
# ¿Qué hace el carácter más [+] en expresiones regulares?

# R  Coincide con una o más apariciones del personaje anterior.


# Pregunta 6
# Un pasante implementó un verificador de códigos postales, pero solo funciona con códigos postales de cinco dígitos.
# Su tarea es actualizar el verificador para que incluya los nueve dígitos del código postal; los cinco dígitos
# iniciales y los cuatro opcionales después del guión. Actualiza la expresión regular.

import re


def check_zip_code(text):
    result = re.search(r"\b\d{5}(-\d{4})?\b", text)
    return result is not None


print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False

import re


def check_zip_code(text):
    result = re.search(r"\b\d{5}(?:-\d{4})?\b", text)
    return result is not None


print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False

import re


def check_zip_code(text):
    result = re.search(r"^\d{5}(-\d{4})?$", text)
    return result != None


print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False

import re


def check_zip_code(text):
    result = re.search(r"(?:\D|^)\d{5}(?:[-\s]\d{4})?(?=\D|$)", text)
    return result != None


print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False

# al parecer hay un error en la prueba, ejercicio 6

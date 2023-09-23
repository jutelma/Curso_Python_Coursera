"""Guía de estudio: funciones

Esta guía de estudio proporciona un resumen de referencia rápida de lo que aprendió en esta lección y sirve como guía
para la próxima prueba de práctica.

En el segmento Funciones, aprendió a definir y llamar funciones, utilizar los parámetros de una función y devolver
datos de una función. También aprendió a diferenciar y convertir entre diferentes tipos de datos utilizando variables.
Además, aprendió algunas prácticas recomendadas para escribir código legible y reutilizable.

Términos

valor de retorno : el valor o variable devuelto como resultado final de una función

parámetro (argumento) : un valor pasado a una función para su uso dentro de la función

refactorización de código : un proceso para reestructurar el código sin cambiar la funcionalidad

Conocimiento

El propósito de la palabra clave def() es definir una nueva función.

Mejores prácticas para escribir código que sea legible y reutilizable:

Cree una función reutilizable : reemplace el código duplicado con una función reutilizable para que el código sea más
fácil de leer y reutilizar.

Refactorizar código : actualice el código para que se autodocumente y la intención del código sea clara.

Agregar comentarios : agregar comentarios es parte de la creación de código autodocumentado.
El uso de comentarios le permite dejar notas para usted mismo y/o para otros programadores para aclarar el propósito
del código.

Habilidades de codificación

Grupo de habilidades 1

Utilice una función que acepte múltiples parámetros.

Devolver un valor de resultado"""


# Esta función calcula el número de días en un número variable de
# años, meses y días. Estas variables son proporcionadas por el usuario y
# se pasan a la función a través de los parámetros de la función.
def find_total_days(years, months, days):
    # Asigne una variable para contener los cálculos del número de días en
    # un año (años*365) más el número de días de un mes (meses*30) más
    # el número de días proporcionados a través de la variable del parámetro "días".
    my_days = (years * 365) + (months * 30) + days
    # Utilice la palabra clave "return" para enviar el resultado de "my_days"
    # cálculo de la llamada a la función.
    return my_days

# Llamada a función con valores de parámetros proporcionados por el usuario.

print(find_total_days(2, 5, 23))

#903 resultado.

"""Grupo de habilidades 2

Utilice una función para devolver el resultado de una conversión de medidas

Utilice operadores aritméticos para realizar un cálculo.

Combine texto con una llamada de función dentro de una declaración print()

Convierta el valor de retorno de un tipo de datos flotante a una cadena para la función print()

Llame a la función y realice un cálculo sobre el valor de retorno dentro de una declaración print()"""


# Esta función convierte onzas líquidas a mililitros y devuelve el
# resultado de la conversión.
def convert_volume(fluid_ounce):
    # Calcular el valor de la variable "ml" usando la variable de parámetro
    # "onza_fluida". Hay aproximadamente 29,5 mililitros en 1 líquido.
    # onza.
    ml = fluid_ounce * 29.5
    # Devuelve el resultado del cálculo.
    return ml


# Llame a la conversión desde la función print() usando 2 fluidos
# onzas. Convierta el valor de retorno de un flotante a una cadena.
print("The volume in millimeters is " + str(convert_volume(2)))

# Llame a la función nuevamente y duplique las 2 onzas líquidas desde adentro
# la función de impresión.
print("The volume in millimeters is " + str(convert_volume(2) * 2))
# Alternative calculation:
# print("The volume in millimeters is " + str(convert_volume(4))

#resultado
# The volume in millimeters is 59.0
# The volume in millimeters is 118.0
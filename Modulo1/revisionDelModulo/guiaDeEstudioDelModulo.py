"""

Guía de estudio: Prueba calificada del Módulo 2

Es hora de prepararse para el cuestionario calificado del Módulo 2. Revise los siguientes elementos de este módulo
antes de comenzar el cuestionario calificado del Módulo 2. Si desea refrescar su memoria sobre estos materiales,
vuelva a visitar las Guías de estudio ubicadas antes de cada prueba de práctica en el Módulo 2:

Guía de estudio: expresiones y variables, Guía de estudio: funciones, y Guía de estudio: condicionales.


Conocimiento

· Cómo asignar valores a variables y usarlos en código

· Cómo construir una función y usar parámetros de función

· Cómo se pueden utilizar los operadores lógicos y de comparación,

· Cómo se comportan los operadores lógicos y de comparación con diferentes tipos de datos

· ¿Qué tipo de resultados producen las comparaciones simples y complejas?

· Cómo alfabetizar cadenas usando operadores de comparación

· Qué debe aparecer después de las palabras clave if y elif

· Qué hace la palabra clave  elif

· Cuándo se ejecutará una declaración if, elif o else

· Cómo utilizar los operadores de división de piso // y módulo % y por qué

· Cómo utilizar operadores lógicos con operadores de comparación para desarrollar declaraciones condicionales complejas
  dentro de un bloque if-elif-else

· Mejores prácticas para la codificación y sus beneficios

· Qué significa "código autodocumentado"


Es posible que haya algunas preguntas en el cuestionario que le preguntarán sobre el resultado de un pequeño bloque de
código o el valor de parte del código. Asegúrese de leer atentamente las instrucciones sobre esas preguntas.

Habilidades de codificación

Grupo de habilidades 1

· Utilice una función con la palabra clave def()

· Pasar un parámetro a la función.

· Utilice un bloque if-elif-else para establecer condiciones específicas para una variedad de acciones

· Asignar cadenas a variables

· Usar operadores de comparación

· Devolver un valor

· Llame a la función en una declaración impresa y pase el parámetro a la función

"""


# Se crea una función con la palabra clave def(). El parámetro
# la variable "time_as_string" se pasa a la función a través de un
# llamada a la función.
def task_reminder(time_as_string):
    # El siguiente bloque if-elif-else asigna varias cadenas a
    # la variable "tarea" dependiendo de condiciones específicas. El
    # las condiciones de prueba se establecen usando la comparación de igualdad ==
    # operador. En este caso, el tiempo transcurrido a través del
    # La variable de parámetro "time_as_string" se prueba como
    # condición específica. Entonces, si la hora es "11:30 a.m.", entonces
    # A "tarea" se le asigna el valor: "Ejecutar informe TPS".
    if time_as_string == "8:00 a.m.":
        task = "Check overnight backup images"
    elif time_as_string == "11:30 a.m.":
        task = "Run TPS report"
    elif time_as_string == "5:30 p.m.":
        task = "Reboot servers"
    # La declaración else es un comodín para todos los demás valores de
    # la variable del parámetro "time_as_string" no aparece en el
    # bloque de código if-elif.
    else:
        task = "Provide IT Support to employees"

    # Esta línea devuelve el valor de "tarea" a la llamada a la función.
    return task


# Esta línea llama a la función y pasa un parámetro
# ("10:00 a.m.") a la función.
print(task_reminder("10:00 a.m."))
# Should print "Provide IT Support to employees"

"""
Grupo de habilidades 2

· Predecir el resultado de expresiones escritas con la sintaxis de Python. 

· Requiere comprensión de:

    · Operadores aritméticos y lógicos 

    · Cómo las funciones devuelven e imprimen valores

    · Cómo funcionan las declaraciones if-elif-else

    ·Operadores de comparación
    
"""


# Example 1


def product(a, b):
    return (a * b)


print(product(product(2, 4), product(3, 5)))


#################################

# Example 2
# Evaluate the output of this print statement

def difference(a, b):
    return (a - b)


def sum(a, b):
    return (a + b)


print(difference(sum(2, 2), sum(3, 3)))

#################################

# Example 3
# Evaluate the Boolean output of this comparison


print((5 >= 2 * 4) and (5 <= 4 * 3))

#################################

# Example 4
# Evaluate the value of the comparison in the if statement

x = 3
if x + 5 > x ** 2 or x % 4 != 0:
    print("This comparison is True")

#################################

# Example 5
# Evaluate the output of this if-elif-else statement


number = 6
if number * 2 < 14:
    print(number * 6 % 3)
elif number > 7:
    print(100 / number)
else:
    print(7 - number)

# Click Run to check your answers. If you are having trouble
# calculating the correct answers manually, please review the
# Practice Quiz Study Guides, videos, and readings in this Module.

"""
Grupo de habilidades 3 

    · Cree una declaración if-elif-else con: 

        · una declaración condicional compleja que utiliza operadores lógicos y de comparación

        · valores asignados a las variables 

        · Operadores aritméticos, incluido el operador de módulo %
        
"""


def get_remainder(x, y):
    if x == 0 or y == 0 or x == y:
        remainder = 0
    else:
        remainder = (x % y) / y
    return remainder


print(get_remainder(10, 3))

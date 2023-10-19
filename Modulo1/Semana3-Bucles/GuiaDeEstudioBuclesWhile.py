"""
Guía de estudio: bucles while
Esta guía de estudio proporciona un resumen de referencia rápida de lo que aprendió en este segmento y sirve como guía
para el próximo cuestionario de práctica.

En el segmento de bucles while , aprendió sobre la estructura lógica y la sintaxis de los bucles while . También
aprendió sobre la importancia de inicializar variables y cómo resolver bucles while infinitos con la palabra clave
break .


mientras bucles

Un bucle while ejecuta el cuerpo del bucle mientras una condición especificada permanece verdadera. Se utilizan
comúnmente cuando hay un número desconocido de operaciones por realizar y es necesario verificar una condición en cada
iteración.

Sintaxis:

while specified condition is True:
    body of loop

Example while loop:

"""
multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print("Done")

# Este bucle while imprime los múltiplos de 5 entre 1 y 50. El
# La variable "multiplicadora" se inicializa con el valor inicial de 1.
# La variable "resultado" se inicializa con el valor del
# variable "multiplicadora" multiplicada por 5.

# El bucle while especifica que el bucle debe iterar mientras sea Verdadero
# que el "resultado" es menor o igual a 50. Dentro del ciclo while,
# el código le dice al intérprete de Python que imprima el valor del
# variable "resultado". Luego, el "multiplicador" se incrementa en 1 y el
# Al "resultado" se le asigna el nuevo valor del "multiplicador" multiplicado por 5.

# El final del ciclo while se indica mediante la sangría del siguiente
# línea de código moviendo una pestaña hacia la izquierda. En este punto, Python
# el intérprete vuelve automáticamente al principio del while
# bucle para comprobar la condición nuevamente con el nuevo valor del "resultado"
# variable. Cuando la condición del bucle while se vuelve falsa (es decir,
# "resultado" ya no es menor o igual a 50), el intérprete sale
# el bucle y lee la siguiente línea de código fuera del bucle. En esto
# caso, la siguiente línea le dice al intérprete que imprima la cadena "Listo".

# Haga clic en el botón "Ejecutar" para verificar el resultado de este ciclo while.

"""
Errores comunes en los bucles while

Si recibe un mensaje de error en un bucle o parece bloquearse, su lista de verificación de depuración debe incluir las 
siguientes comprobaciones:

 · Error al inicializar las variables. Asegúrese de que todas las variables utilizadas en la condición del bucle se 
  inicialicen antes del bucle.

 · Bucles infinitos no deseados. Asegúrese de que el cuerpo del bucle modifique las variables utilizadas en la 
  condición, de modo que el bucle finalmente finalice para todos los valores posibles de las variables. A menudo puedes 
  evitar un bucle infinito usando la palabra clave break o agregando criterios de finalización a la parte de condición 
  del bucle while . 

 

Términos del bucle while

 · Bucle while : le indica a la computadora que ejecute un conjunto de instrucciones mientras una condición específica 
   sea verdadera. En otras palabras, los bucles while siguen ejecutando el mismo grupo de instrucciones hasta que la 
   condición se vuelve Falsa.

 · Bucle infinito : falta un método para salir del bucle, lo que hace que el bucle se ejecute para siempre.

break : palabra clave que se puede utilizar para finalizar un bucle en un punto específico. 

 

Conceptos matemáticos en el cuestionario de práctica

Los problemas de codificación del próximo cuestionario de práctica incluirán algunos conceptos matemáticos. No te 
preocupes si estás oxidado en matemáticas. Tendrás mucho apoyo con estos conceptos en el cuestionario. La siguiente es 
una descripción general rápida de los términos matemáticos que encontrará en el cuestionario:  

 · números primos : enteros que tienen solo dos factores, que son el número mismo multiplicado por 1. El número primo más bajo es 2. 

 · factores primos : números primos que son factores de un número entero. Por ejemplo, los números primos 2 y 5 son los factores primos del número 10 (2x5=10). Los factores primos de un número entero no producirán un resto cuando se usen para dividir ese número entero. 

 · divisor : un número (denominador) que se utiliza para dividir otro número (numerador). Por ejemplo, si el número 10 se divide entre 5, el número 5 es el divisor.

 · suma de todos los divisores de un número - El resultado de sumar todos los divisores de un número.  

 · tabla de multiplicar : un número entero multiplicado por una serie de números y sus resultados formateados como una tabla o una lista. Por ejemplo:

                 4x1=4 4x2=8 4x3=12 4x4=16 4x5=20


Habilidades de codificación

Grupo de habilidades 1

 · Inicializar una variable

 · Utilice un bucle while que se ejecute mientras una condición específica sea verdadera

 · Asegúrese de que el bucle while no sea un bucle infinito

 · Incrementar un valor dentro de un bucle while
 
"""

# Esta función cuenta el número de factores enteros para un
# Variable "número_dado", pasada a través de los parámetros de la función.
# El valor de retorno de "recuento" incluye el "número_dado" en sí mismo como un
# factor (n*1).

def count_factors(given_number):
    # Para incluir la variable "número_dado" como "factor", inicialice
    # la variable "factor" con el valor 1 (si la variable "factor"
    # si comenzara en 2, el "número_dado" en sí sería excluido).
    factor = 1
    count = 1

    # Este bloque "si" se ejecutará si el "número_dado" es igual a 0.
    if given_number == 0:
        # Si es Verdadero, el valor de retorno será 0 factores.
        return 0

    # El ciclo while se ejecutará mientras el "factor" sea aún menor que
    # la variable "número_dado".
    while factor < given_number:
        # Este bloque "si" comprueba si el "número_dado" se puede dividir por
        # la variable "factor" sin dejar resto. El módulo
        # operador % se utiliza para probar un resto.
        if given_number % factor == 0:
            # Si es Verdadero, entonces la variable "factor" se agrega al recuento de
            # los factores enteros del "número_dado".
            count += 1
        # Al salir del bloque if, incrementa la variable "factor" en 1
        # para dividir la variable "número_dado" por un nuevo valor de "factor"
        # dentro del bucle while.
        factor += 1

    # Cuando el intérprete sale del bucle while o del if superior
    # bloque, devolverá el valor de la variable "count".
    return count


print(count_factors(0))  # El valor del conteo será 0
print(count_factors(3))  # Debe contar 2 factores (1x3)
print(count_factors(10))  # Debe contar 4 factores (1x10, 2x5)
print(count_factors(24))  # Debe contar 8 factores (1x24, 2x12, 3x8,
# y 4x6).

"""
Grupo de habilidades 2

 · Inicialice variables para asignar tipos de datos antes de que se utilicen en un bucle  while

 · Utilice la palabra clave break como punto de salida para un bucle while
 
"""


# Esta función genera una tabla de suma. Está escrito para terminar después
# imprimiendo 5 líneas de la tabla de suma, pero se saldrá de la
# bucle si la variable "my_sum" excede 20.

# La función acepta una variable "número_dado" a través de su
# parámetros.
def addition_table(given_number):
    # Las variables "iteated_number" y "my_sum" se inicializan con
    # el valor de 1. Aunque la variable "my_sum" no necesita ninguna
    # valor inicial específico, todavía se le debe asignar un tipo de datos
    # antes de ser utilizado en el ciclo while. Inicializando "my_sum"
    # con cualquier número entero, el tipo de datos se establecerá en int.
    iterated_number = 1
    my_sum = 1

    # El bucle while se ejecutará mientras sea cierto que el
    # "número_iterado" es menor o igual a 5.
    while iterated_number <= 5:

        # A la variable "my_sum" se le asigna el valor del
        # "número_dado" más las variables "número_iterado".
        my_sum = given_number + iterated_number

        # Pruebe para ver si la variable "my_sum" es mayor que 20.
        if my_sum > 20:
            # Si es Verdadero, utilice la palabra clave break para salir del ciclo.
            break
        # Si es falso, el intérprete de Python pasará a la siguiente línea.
        # en el bucle while después de que finalice la declaración if.

        # La función de impresión generará el "número_dado" más
        # el "número_iterado" es igual a "mi_suma".
        print(str(given_number), "+", str(iterated_number), "=", str(my_sum))

        # Incrementar el "número_iterado" antes de que comience el ciclo while
        # nuevamente para imprimir un nuevo valor "my_sum".
        iterated_number += 1


addition_table(5)
addition_table(17)
addition_table(30)

# Expected output:
# 5 + 1 = 6
# 5 + 2 = 7
# 5 + 3 = 8
# 5 + 4 = 9
# 5 + 5 = 10
# 17 + 1 = 18
# 17 + 2 = 19
# 17 + 3 = 20
# None

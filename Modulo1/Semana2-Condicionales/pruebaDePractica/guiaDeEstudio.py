"""

    Guía de estudio: condicionales

    Esta guía de estudio proporciona un resumen de referencia rápida de lo que aprendió en esta lección y sirve como
    guía para la próxima prueba de práctica.

    En el segmento Condicionales, aprendió sobre los operadores integrados de Python que se usan para comparar valores
    y los operadores lógicos para realizar comparaciones complejas. También aprendió a utilizar operadores en bloques
    if-else-elif.

    Conocimiento

    Operadores de comparación con valores numéricos

    Las expresiones de comparación devuelven un resultado booleano (Verdadero o Falso).

     · x == y Si x es igual a y, devuelve Verdadero. De lo contrario, devuelva Falso.

     · x != y Si x no es igual a y, devuelve Verdadero. De lo contrario, devuelva Falso.

     · x < y Si x es menor que y, devuelve Verdadero. De lo contrario, devuelva Falso.

     · x <= y Si x es menor o igual que y, devuelve Verdadero. De lo contrario, devuelva Falso.

     · x > y Si x es mayor que y, devuelve Verdadero. De lo contrario, devuelva Falso.

     · x >= y Si x es mayor o igual a y, devuelve Verdadero. De lo contrario, devuelva Falso.


    Operadores de comparación con cadenas

    Las expresiones de comparación con cadenas también devuelven un resultado booleano (Verdadero o Falso).

     · "x" == "y" Si las palabras son iguales, devuelve Verdadero. De lo contrario, devuelva Falso.

     · "x" != "y" Si las palabras no son iguales, devuelve Verdadero. De lo contrario, devuelva Falso.

    Cuando se usan con cadenas, las siguientes expresiones de comparación ordenarán alfabéticamente las cadenas.

     · "x" < "y" Si la cadena "x" tiene un valor Unicode menor que la cadena "y", devuelve Verdadero. De lo contrario,
        devuelva Falso.

     · "x" <= "y" Si el valor Unicode de la cadena "x" es menor o igual que el valor Unicode de la cadena "y", devuelve
        erdadero. De lo contrario, devuelva Falso.

     · "x" > "y" Si la cadena "x" tiene un valor Unicode mayor que la cadena "y", devuelve Verdadero. De lo contrario,
        devuelva Falso.

     · "x" >= "y" Si el valor Unicode de la cadena "x" es mayor o igual que el valor Unicode de la cadena "y", devuelve
        Verdadero. De lo contrario, devuelva Falso.


    Valores Unicode para el alfabeto.

    La numeración Unicode para el alfabeto comienza en 65 para la letra A mayúscula y llega hasta 90 para la letra Z
    mayúscula. Luego, los valores del alfabeto en minúsculas comienzan en 97 para la a minúscula y llegan a 122 para la
    z minúscula. Usando estos números Unicode, el código de la A mayúscula es menor que los códigos de todas las demás
    letras, lo que Python interpreta como el comienzo del alfabeto. El código de la z minúscula es mayor que los
    códigos de todas las demás letras, lo que Python interpreta como el final del alfabeto inglés.


    Operadores logicos

    Los operadores lógicos se utilizan para combinar expresiones de comparación y también devolver resultados booleanos
    (Verdadero o Falso).

     · comparación1 y comparación2

        · Devuelve un resultado Verdadero si tanto la comparación1 como la comparación2 son verdaderas.

        · Si no son ambos verdaderos, devuelve Falso.

     · comparación1 o comparación2

        · Devuelve un resultado Verdadero si comparación1 y/o comparación2 son Verdaderos.

        · Si ninguna de las comparaciones es verdadera, devuelve False.

     · no comparación1

            · Devuelve el valor booleano inverso de la comparación.

                · Devuelve un resultado Verdadero si la comparación1 es falsa.

                · Si la comparación1 es verdadera, devuelve False.



    Sintaxis de un bloque if-elif-else

    if condition1:
        action1
    elif condition2:
        action2
    else:
        action3

   · Si la condición1 es verdadera:

        · Luego realice la acción 1 y salga del bloque if-elif-else

   · Si la condición2 es verdadera:

        · Luego realice la acción 2 y salga del bloque if-elif-else

   · Si ni la condición1 ni la condición2 son verdaderas:

        · Luego realice la acción 3 y salga del bloque if-elif-else



    Habilidades de codificación

    Grupo de habilidades 1

        ·Utilice un operador de comparación con números

        ·Utilice un operador de comparación para ordenar alfabéticamente cadenas

"""
# El valor de 10*4 (40) es mayor que 14+23 (37), por lo tanto esto
# La expresión de comparación devolverá el valor booleano Verdadero.

print(10*4 > 14+23) # Debería imprimirse Verdadero

# La letra "t" tiene un valor Unicode de 116 y la letra "s" tiene un
# Valor Unicode de 115. Dado que 116 no es menor que 115, el
# la comparación de "alto" < "bajo" (o 116 < 115) es falsa.

print("tall" < "short")  # Debería imprimirse Falso

"""
    Grupo de habilidades 2

        · Utilice una función con la palabra clave def()

        · Pasar un parámetro a la función.

        · Utilice una declaración if-elif-else

        ·Asignar cadenas a variables 

        · Usar operadores condicionales

        ·Devolver un valor
    
"""

# La función print() nos permite mostrar la salida del
# función. Para llamar a una función en una declaración impresa, la sintaxis
# es print(n# Esta función acepta una variable como parámetro

def translate_error_code(error_code):
    # El bloque if-elif-else evalúa el valor de la variable
    # pasado a la función como parámetro. La declaración if usa
    # el operador de igualdad == para probar el valor de la variable.
    # Esta prueba devuelve un resultado booleano (Verdadero/Falso).
    if error_code == "401 Unauthorized":
        # Si la comparación anterior devuelve Verdadero, entonces la sangría
        # Se ejecutarán líneas dentro de la declaración if.
        #  En este caso, la acción es asignar una cadena a la variable de traducción.
        # El resto del bloque if-elif-else no se ejecutará.
        # El intérprete de Python saltará a la siguiente línea fuera de
        # el bloque if-elif-else. En este caso, la siguiente línea es la
        # declaración de valor de retorno.

        translation = "Server received an unauthenticated request"

    # Si la declaración if inicial devuelve un resultado Falso, entonces el
    # la primera declaración elif ejecutará una prueba diferente en el valor
    # de la variable.
    elif error_code == "404 Not Found":
        # Si la primera declaración elif devuelve un resultado Verdadero, entonces el
        # líneas sangradas dentro de la primera declaración elif. Se ejecutarán
        # Después de esta línea, el resto del bloque if-elif-else se no correr.
        # El intérprete de Python pasará a la siguiente línea.
        # fuera del bloque if-elif-else.

        translation = "Requested web page not found on server"

    # Si tanto la declaración if inicial como la primera declaración elif
    # devuelve un resultado Falso, luego se ejecutará la segunda declaración elif
    # correr.

    elif error_code == "408 Request Timeout":
        # Si la segunda declaración elif devuelve un resultado Verdadero, entonces el Se ejecutarán
        # líneas sangradas dentro de la segunda declaración elif.
        # Después de esta línea, el resto del bloque if-elif-else se
        # no correr. El intérprete de Python pasará a la siguiente línea.
        # fuera del bloque if-elif-else.

        translation = "Server request to close unused connection"

    # Si las pruebas condicionales anteriores no producen un resultado Verdadero
    # entonces se ejecutará la declaración else.

    else:
        translation = "Unknown error code"
    # El bloque if-elif-else finaliza.

    # Se ejecutará la siguiente línea fuera del bloque if-elif-else
    # después de salir del bloque. En este caso, la siguiente línea devuelve
    # la salida del bloque if-elif-else.
    return translation

# nombre_de_función(parámetro))
print(translate_error_code("404 Not Found"))

# Rendimiento esperado:
# La página web solicitada no se encuentra en el servidor

"""
    Grupo de habilidades 3

        · Utilice una declaración if-elif-else con:

            · operadores de comparación

            · operadores logicos
        
"""
# Establece el valor de la variable "número"
number = 25

# La variable "número" se comparará primero con 5. Dado que es
# Falso que "número" no sea menor o igual a 5, la expresión sangrada
# bajo esta línea será ignorado.

if number <= 5:
    print("The number is 5 or smaller.")

# A continuación, la variable "número" se comparará con 33. Dado que es
# Falso que "número" es igual a 33, la expresión sangrada debajo
# esta línea será ignorada.

elif number == 33:
    print("The number is 33.")

# Luego, la variable "número" se comparará con 32 y 6. Ya que
# es cierto que 25 es menor que 32 y mayor que 6, el Python
# el intérprete imprimirá "El número es menor que 32 y/o mayor
# que 6." Luego, saldrá de la declaración if-elif-else y el resto
# Se ignorará el número de la declaración if-elif-else.

elif number < 32 and number >= 6:
    print("The number is less than 32 and greater than 6.")

else:
    print("The number is " + str(number))

# El resultado esperado es:
# El número es menor que 32 y mayor que 6.

"""
    Grupo de habilidades 4

        · Utilice una declaración if para calcular un valor de retorno

        ·Usar operadores condicionales

        · Recuerde los operadores aritméticos // y %
        
"""

# Esta función redondea un número variable al valor 10x más cercano
def round_up(number):
    x = 10
    # El operador de división de piso calculará el valor entero de
    # "número" dividido por x: 35 // 10 devolverá el número entero 3.

    whole_number = number // x

    # El operador de módulo calculará el valor restante de "número"
    # dividido por x: 35 % 10 devolverá el valor restante 5.

    remainder = number % x

    # Si el resto es mayor que 0:
    if remainder >= 5:
        # Devuelve x multiplicado por (número_entero+1) para redondear
        return x * (whole_number + 1)
    # De lo contrario, devuelve x multiplicado por el número_completo para redondear hacia abajo
    return x * whole_number

# Llama a la función con el valor del parámetro 35.
print(round_up(35))  # Debería imprimir 40
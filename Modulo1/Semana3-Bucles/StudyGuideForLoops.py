"""
Esta guía de estudio proporciona un resumen de lo que aprendió en este segmento y sirve como guía para la próxima
prueba de práctica.

En el segmento de bucles for , aprendió sobre la estructura lógica y la sintaxis de los bucles for . Echaste un vistazo
más de cerca a la función range() . Aprendió sobre los bucles for anidados y los bucles for anidados complejos con
declaraciones if . También aprendió a corregir errores comunes en los bucles for .

Para bucles frente a bucles while

Los bucles for y while comparten varias características. Ambos bucles se pueden usar con una variedad de tipos de datos,
ambos se pueden anidar y ambos se pueden usar con las palabras clave break y continue . Sin embargo, existen
diferencias importantes entre los dos tipos de bucles:

    · Los bucles while se utilizan cuando un segmento de código necesita ejecutarse repetidamente mientras una condición es
      verdadera.

    · Los bucles for iteran sobre una secuencia de elementos, ejecutando el cuerpo del bucle para cada elemento de la
      secuencia.

Sintaxis

La sintaxis de un bucle for con la palabra clave in :

for variable in sequence:
    body of loop

Común para estructuras de bucle

para bucle con rango()

La palabra clave in con la función range() genera una secuencia de números enteros, que se puede usar con un bucle for
para configurar las iteraciones del código. El rango de números [0, 1, 2] se correlaciona con las posiciones del índice
ordinal (1.º, 2.º, 3.º), en lugar de los valores cardinales (cantidad) de los números 0, 1 y 2. Por ejemplo, rango(5)
significa las cinco posiciones del índice en el rango [0, 1, 2, 3, 4].

La función range() puede tomar hasta tres parámetros. Las funciones de los tres posibles parámetros de rango (x,y,z)
son:

    · x = Inicio - Posición de índice inicial del rango

        · La posición del índice predeterminada es 0.

        · La posición inicial del índice está incluida en el rango.

        · Sintaxis de ejemplo: rango( 2 , y, z) o rango( x+3 , y, z)

    · y = Parar - Posición de índice final del rango

        · Sin posición de índice predeterminada. Debe incluir la posición del índice final en los parámetros range().

            · Sintaxis de ejemplo: rango ( y )

        · El valor de la posición del índice final está excluido del rango.

        · Para incluir el número de índice final, utilice la expresión: y+1 (índice + 1)

            · Sintaxis de ejemplo: rango(x, y+1 , z)

            · Alternativamente, si y = 10, puedes escribir: rango(x, 11 , z)

    · z = Paso - Valor incremental

        · El incremento predeterminado es +1.

        · El valor predeterminado se puede anular con cualquier incremento válido.

        · El valor incremental finalizará el bucle for antes de que alcance la posición del índice de fin de rango
          (índice de fin de rango menos 1).

Ejemplo de un bucle for con la palabra clave in y la función range() :

"""
# Este bucle itera sobre el valor de la variable "número" en un rango
# de 1 a 6+1 (el límite superior del rango de 6 está excluido, por lo que +1 tiene
# se le ha agregado para incluir 6 en el rango). El valor incremental
# para el bucle es 2 (número+2). La función print() generará el
# valor resultante de "número" multiplicado por 3.


for number in range(1,6+1,2):
    print(number*3)


# The loop should print 3, 9, 15
"""
Errores comunes al utilizar la función range():

    · Olvidar que el límite superior de un rango() no está incluido en el rango.

    · Iterando sobre no secuencias. Por ejemplo, las cadenas son iterables letra por letra, pero no palabra por palabra.
     
"""
# Este bucle itera sobre el valor de la variable "número" en un rango
# de 2 a 7 (se excluye el límite superior del rango de 8). La impresión()
# La función generará el valor resultante de "número" al cuadrado.


for number in range(2,8):
    print(number**2)


# The loop should print 4, 9, 16, 25, 36, 49

"""
Anidados para bucles 

La sintaxis de los bucles for anidados:

for x in sequence:
    # start of the outer loop body
    for y in sequence:
        # start of the inner loop body

        # end of of the inner loop body
    # continue body of the outer loop
    # end of the outer loop body

9
for x in sequence:
    # start of the outer loop body
    for y in sequence:
        # start of the inner loop body

        # end of of the inner loop body
    # continue body of the outer loop
    # end of the outer loop body

Ejemplo de bucles for anidados:  

"""

# Este código demuestra las iteraciones del bucle externo e interno de un par.
# de bucles for anidados. Haga clic en "Ejecutar" para ver los resultados. El bucle exterior
# se ejecutará dos veces para las posiciones del puntero de rango [0, 1] en el rango (2).
# El bucle interno se ejecutará 4 veces para las posiciones del puntero de rango.
# [0, 1, 2, 3] en rango(3+1) o rango(4) cada vez que se ejecuta el bucle externo.
# Entonces, el bucle interno se ejecutará 8 veces en total.

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop")

"""
for Loop con instrucción if anidada

La sintaxis de un bucle for con instrucción if anidada:


for x in sequence:
    # start of body of for loop
    if condition is true:
        # start of body of if-statement

        # end of body of if-statement
    # continue body of for loop
    # end of body of for loop
    
    Ejemplo de un bucle for con declaración if anidada :  
    
"""
# Este bucle for itera a través de los números del 0 al 6. La declaración if
# usa el operador de módulo para probar si la variable "x" es divisible por
# 2. Si es Verdadero, la declaración if imprimirá el valor de "x" y saldrá
# volver al bucle for para la siguiente iteración de "x". Desde que no
# el valor incremental se especifica en los parámetros range(), el valor predeterminado
# incremento es +1.


for x in range(7):
    if x % 2 == 0:
        print(x)


# The loop should print 0, 2, 4, 6


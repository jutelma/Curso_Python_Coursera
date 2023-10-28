# Pregunta 1

# ¿En qué se diferencian los bucles while y for en Python?

# 1 Si bien los bucles se pueden usar con todo tipo de datos, los bucles for solo se pueden usar con números.

# 2 Los bucles for se pueden anidar, pero los bucles while no.

# 3 Los bucles while iteran mientras una condición es verdadera, los bucles for iteran a través de una secuencia de
# elementos.

# 4 Mientras que los bucles se pueden interrumpir usando break, los bucles for pueden usar continuar.

# Respuesta
# Podemos usar bucles while cuando queremos que nuestro código se ejecute repetidamente
# mientras una condición sea verdadera, y bucles for cuando queremos ejecutar un bloque de código para cada elemento
# de una secuencia.

# Pregunta 2
# ¿Qué opción arreglaría este bucle for para imprimir los números 12, 18, 24, 30, 36?

for n in range(6, 18, 3):
    print(n * 2)

for n in range(6, 18, 3):
    print(n + 2)

for n in range(6, 18 + 1, 3):
    print(n * 2)

for n in range(12, 36, 6):
    print(n * 2)

for n in range(0, 36 + 1, 6):
    print(n)

# Respuesta Para incluir 18 en el rango, agréguele 1. El segundo parámetro podría escribirse como 18+1 o 19.


# Pregunta 3
# ¿Que bucles for imprimiran todos los numeros pares del 0 al 18? Seleccione todas las que correspondan.

for n in range(19):
    if n % 2 == 0:
        print(n)

for n in range(18 + 1):
    print(n ** 2)

for n in range(0, 18 + 1, 2):
    print(n * 2)

for n in range(10):
    print(n + n)

# Respuesta
# Este bucle imprimirá todos los números pares del 0 al 18. El rango de "n" comenzará en 0 y terminará en 18
# (se excluye el valor final del rango de 19). La variable "n" se incrementará de forma predeterminada en 1 en cada
# iteración del bucle. La declaración if utiliza el operador de módulo para probar si la variable "n" es divisible
# por 2. Si es Verdadero, la declaración if imprimirá el valor de "n" y volverá al bucle for para la siguiente
# iteración de "n".

for n in range(0, 18 + 1, 2):
    print(n * 2)

for n in range(10):
    print(n + n)

# Pregunta 4

# Complete los espacios en blanco para que el bucle for imprima los primeros 10 números de cubo (x**3) en un rango que
# comienza con x=1 y termina con x=10.

for x in range(1, 11):
  print(x**3)

# Respuesta Tienes el código para imprimir los primeros 10 cubos.

# Pregunta 5

# Escriba un bucle for con una función range() de tres parámetros que imprima los múltiplos de 7 entre 0 y 100.
# Imprima un múltiplo por línea y evite imprimir números que no sean múltiplos de 7. Recuerde que 0 también es un
# múltiplo de 7 .

for x in range(0, 101, 7):
    print(x)

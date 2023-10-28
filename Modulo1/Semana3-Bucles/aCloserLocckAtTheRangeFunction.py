"""
Una mirada más cercana a la función Range()

La palabra clave in , cuando se usa con la función range() , genera una secuencia de números enteros, que se puede usar
con un bucle for para controlar el punto inicial, el punto final y los valores incrementales del bucle.

Sintaxis:

for n in range(x, y, z):
    print(n)

  La función range() utiliza un conjunto de índices que apuntan a valores enteros, que comienzan en el número 0. Los
  valores numéricos 0, 1, 2, 3, 4 se correlacionan con las posiciones de índice ordinal 1.º, 2.º, 3.º, 4.º, 5.º.
  Entonces, cuando se realiza una llamada de rango a la quinta posición del índice usando el rango (5), el índice
  apunta al valor numérico de 4.

Número de índice    1er índice      2do índice      3er índice     4to índice       5to índice

Valor                  0              1                  2              3                4


La función range() puede tomar hasta tres parámetros:   rango(inicio, parada, paso)

Inicio
 El primer elemento en los parámetros de la función range() es la posición inicial del rango. El valor predeterminado
 es la primera posición del índice, que apunta al valor numérico 0. Este valor está incluido en el rango.

Detener
 El segundo elemento en los parámetros de la función range() es la posición final del rango. No existe una posición de
 índice predeterminada, por lo que este número de índice debe asignarse a los parámetros range() . Por ejemplo, la
 línea para n en range(4) se repetirá 4 veces con la variable n comenzando en 0 y recorriendo 4 posiciones de
 índice: 0, 1, 2, 3. Como puede ver, range(4) (que significa posición de índice 4) termina en el valor numérico
 3. En Python, esta estructura puede expresarse como "el valor de fin de rango está excluido del rango".
 Para incluir el valor 4 en   range(4) , la sintaxis se puede escribir como range(4+1) o range(5) .
 Ambos rangos producirán los valores numéricos 0, 1, 2, 3, 4.

Paso
 El tercer elemento en los parámetros de la función range() es el valor del paso incremental.
 El incremento predeterminado es +1. El valor predeterminado se puede anular con cualquier incremento válido.
 Sin embargo, tenga en cuenta que el bucle seguirá finalizando en la posición del índice de fin de rango,
 independientemente del valor incremental. Por ejemplo, si tiene un bucle con el rango: for n in range(1, 5, 6) ,
 el rango solo producirá el valor numérico 1. Esto se debe a que el valor incremental de 6 excedió el punto final
 del rango.


Ejercicio práctico
Puede utilizar el bloque de código siguiente para probar los valores de n con varios parámetros de rango() .
Algunas sugerencias para probar son:

rango (parada)

 · rango(3)

 · rango(3+1)

rango (inicio, parada)

 · rango(2, 6)

 · rango(5,10+1)

rango (inicio, parada, paso)

 · rango(4, 15+1, 2)

 · rango(2*2, 25, 3+2)

 · rango(10, 0, -2)

"""
for n in range(1, 5, 6):
    print(n)

# Ejemplos de la función range() en código:
# ejemplo 1

# Este bucle itera sobre el valor de la variable "n" en un rango
# de 0 a 10 (se excluye el valor del índice de final de rango 11).
# El valor incremental para el bucle es 2. La función print()
# generar el valor resultante de "n" mientras el bucle cuenta de 0 a 10
# (índice de fin de rango 11) en pasos incrementales de 2. Este es uno
# método que se puede utilizar en Python para imprimir una lista de números pares.


for n in range(0, 11, 2):
    print(n)

# The loop should print 0, 2, 4, 6, 8, 10

# Ejemplo2

# Este bucle itera sobre el valor de la variable "número" en un rango
# de 2 a 7+1 (el valor del índice de final de rango 7 está excluido, por lo que
# Se ha agregado +1 al parámetro para incluir el valor numérico 7 en
# el rango). El valor incremental para el bucle es el predeterminado de +1.
# La función print() generará el valor resultante de "número"
# multiplicado por 3.


for number in range(2, 7 + 1):
    print(number * 3)

# The loop should print 6, 9, 12, 15, 18, 21

# Ejemplo 3

# Este bucle itera sobre el valor de la variable "x" en un rango
# de 2 a -1 (se excluye el índice de final de rango -2). El tercero
# parámetro también es un número negativo, lo que lo convierte en un valor decremental
# de -1. La función print() generará el valor resultante de
# "x" ya que comienza en 2 y cuenta regresivamente hasta -1 (índice -2).

for x in range(2, -2, -1):
    print(x)


# The loop should print 2, 1, 0, -1

"""
Conclusiones clave
Las funciones de los parámetros de función de rango (inicio, parada, paso) son:

    · Inicio - Comienzo de rango

        · valor incluido en el rango

        · predeterminado = 0

    · Parar - Fin del rango

        · valor excluido del rango (para incluir, use stop+1)

        · ningún valor predeterminado

        · debe proporcionar el número de índice final 

    · Paso - Valor incremental 

        · predeterminado = 1
"""

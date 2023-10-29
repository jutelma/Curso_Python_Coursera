# Pregunta 1
# Complete los espacios en blanco para imprimir los números del 15 al 5, contando hacia atrás de cinco en cinco.

number = 15  # Initialize the variable
while number >= 5:  # Complete the while loop condition
    print(number, end=" ")
    number -= 5  # Increment the variable

# Should print 15 10 5

# Pregunta 2
# Busque y corrija el error en el bucle for siguiente. El bucle debe imprimir todos los números pares del 2 al 12.

for number in range(2, 13, 2):
    print(number)


# Should print:
# 2
# 4
# 6
# 8
# 10
# 12

# Complete los espacios en blanco para completar la función "factorial". Esta función aceptará una variable entera
# “n” a través de los parámetros de la función y producirá los factoriales de este número multiplicando este valor
# por cada número menor que el número original [n*(n-1)], excluyendo 0). Para hacer esto, la función debería: aceptar
# una variable entera “n” a través de los parámetros de la función; inicializar una variable “resultado” al valor de
# la variable “n”; iterar sobre los valores de "n" usando un bucle while hasta que "n" sea igual a 0; comenzando en
# n-1, multiplique el resultado por el valor “n” actual; disminuir “n” en -1. Por ejemplo, el factorial 3 devolvería
# el valor de 3*2*1, que sería 6.

def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 1:  # El bucle while debe ejecutarse siempre que n sea mayor que 0
        result *= n  # Multiplicar el resultado actual por el valor actual de n
        n -= 1  # Disminuir la variable apropiada en -1
    return result


print(factorial(3))  # Should print 6
print(factorial(9))  # Should print 362880
print(factorial(1))  # Should print 1


# Pregunta 4 Complete los espacios en blanco para completar la función “tabla_de_multiplicación”. Esta función
# debería imprimir una tabla de multiplicar, donde cada número es el resultado de multiplicar el primer número de su
# fila por el número en la parte superior de su columna. Complete las secuencias de rango en los bucles anidados para
# que se imprima “tabla_de_multiplicación(1, 3)”:
#
# 1 2 3
#
# 2 4 6
#
# 3 6 9

def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start, stop + 1):
        # Complete the inner loop range
        for y in range(start, stop + 1):
            # Prints the value of "x" multiplied by "y"
            # and inserts a space after each value
            print(str(x * y), end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()


multiplication_table(1, 3)


# Should print the multiplication table shown above

# Pregunta 5 Pregunta 5 Complete los espacios en blanco para completar la función "contador". Esta función debe
# realizar una cuenta regresiva desde las variables "inicio" hasta "detener" cuando "inicio" es mayor que "detener".
# De lo contrario, debería contar desde el "inicio" hasta la "parada". Complete el código para que una llamada de
# función como “contador(3, 1)” devuelva “Contando hacia atrás: 3, 2, 1” y “contador(2, 5)” devuelva “Contando hacia
# arriba: 2, 3, 4, 5”.

def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:  # Complete the while loop
            return_string += str(start)  # Add the numbers to the "return_string"
            if start > stop + 1:
                return_string += ","
            start -= 1  # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while start <= stop:  # Complete the while loop
            return_string += str(start)  # Add the numbers to the "return_string"
            if start < stop:
                return_string += ","
            start += 1  # Increment the appropriate variable
    return return_string


print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))  # Should be "Counting down: 2,1"
print(counter(5, 5))  # Should be "Counting up: 5"


# Pregunta 6
# Complete los espacios en blanco para completar la función "todos_números". Esta función debe
# devolver una cadena separada por espacios de todos los números, desde la variable "mínima" inicial hasta la
# variable "máxima" incluida, que se pasa a la función. Complete el bucle for para que una llamada de función como
# "todos_números (3,6)" devuelva los números "3 4 5 6".

def all_numbers(minimum, maximum):
    return_string = ""  # Initializes variable as a string

    # Complete the for loop with a range that includes all
    # numbers up to and including the "maximum" value.
    for num in range(minimum, maximum + 1):
        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        return_string += str(num) + " "

    # This .strip command will remove the final " " space
    # at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2, 6))  # Should be 2 3 4 5 6
print(all_numbers(3, 10))  # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1, 1))  # Should be -1 0 1
print(all_numbers(0, 5))  # Should be 0 1 2 3 4 5
print(all_numbers(0, 0))  # Should be 0


# Pregunta 7
# El siguiente código genera un error cuando se ejecuta. ¿Cuál es el motivo del error?

# def decade_counter():
#    while year < 50:
#        year += 10
#    return year

# Respuesta
# No se pudo inicializar la variable.


# Pregunta 8
# ¿Cuál es el primer número que se imprimirá en la primera iteración de este ciclo? Tu respuesta debe ser
# solo un número.

# for count in range(1, 6):
#    print(count+1)

# Respuesta 2

# Pregunta 9
# ¿Cuál es el valor inicial de la variable "outer_loop" en la primera iteración del "inner_loop" anidado?
# Tu respuesta debe ser solo un número.

# for outer_loop in range(2, 6+1):
#     for inner_loop in range(outer_loop):
#         if inner_loop % 2 == 0:
#             print(inner_loop)

# Respuesta 2
# El siguiente código provoca un bucle infinito. ¿Puedes descubrir qué es lo incorrecto y cómo solucionarlo?

def count_to_ten():
    # Loop through the numbers from first to last
    x = 1
    while x <= 10:
        print(x)
        x = 1


count_to_ten()
# Should print:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# Respuesta
# A la variable "x" se le asigna el valor 1 en cada bucle

"""
1 En Python , ¿ Que hacen los bucles while?

R. En Python, los bucles while son estructuras de control que permiten ejecutar un bloque de código repetidamente
mientras una condición específica se evalúe como verdadera (True).

2 ¿Que técnicas pueden evitar un bucle while infinito? Seleccione todas las que correspondan.

R. De las opciones que proporcionaste, las que son técnicas válidas para evitar un bucle while infinito son:

 · Cambiar el valor de una variable utilizada en la condición while.
 · Utilizar la palabra break.
Estas dos opciones son dos de las técnicas comunes para evitar bucles infinitos. Al actualizar la variable de control y
utilizar break, puedes controlar cuándo se detiene el bucle y evitar que se ejecute indefinidamente.


3 El siguiente codigo contiene un bucle infinito, lo que significa que el interprete de Python no sabe cuando salir
de bucle una vez que se completa la tarea. Para resolver el problema, necesitara :

1 Encuentra el error en el codigo.
2 Arregle el bucle para que haya una condicion de salida.

Sugerencia: intente ejecutar du funcion con el numero 0 como
entrada y observe el resultado. Tenga en cuenta que los bloques de codigo de coursera expiran despues de 5 segundos de
ejecutar un bucle infinito. Si recibes este error de tiempo de espera, significa que el bucle infinito no se ha
solucionado.

"""


# Este bucle while comprueba si el "número" se puede dividir por dos
# sin dejar resto. ¿Cómo se puede cambiar el bucle while a
# ¿Evitar un Python ZeroDivisionError?
# Si después de dividir por 2 "número" es igual a 1, entonces "número" es una potencia de 2.
# Llamadas a la función

def is_power_of_two(number):
    if number == 0:
        return False
    while number % 2 == 0:
        number = number / 2

    if number == 1:
        return True
    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False


"""
4. Completa los espacios en blanco para completar el ciclo while de modo que devuelva la suma de todos los divisores de un 
numero, sin incluir el numero en si. Como recordatorio, un divisor es un numero que divide a otro sin dejar resto. 
Para hacer esto, necesitara: 

1. Inicialice las variables "divisor" y "total" con valores iniciales  
2. Completa la condicion del bucle while.  3. Incrementa la variable "divisor" dentro del bucle while. 
4. Completa la declaracion de devolucion.     
"""


# Complete los espacios en blanco para que el ciclo while continúe ejecutándose mientras el
# La variable "divisor" es menor que el parámetro "número".
# Inicializar las variables apropiadas
# Evite dividir por 0 y números negativos
# en el bucle while saliendo de la función
# si "número" es menor que uno
# Completa el ciclo while
# Incrementar la variable correcta
# Devuelve la variable correcta

def sum_divisors(number):
    divisor = 1
    total = 0
    if number < 1:
        return 0

    while divisor < number:

        if number % divisor == 0:
            total += divisor

        divisor += 1

    return total


print(sum_divisors(0))  # Should print 0
print(sum_divisors(3))  # Should print 1
# 1
print(sum_divisors(36))  # Should print 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should print 1+2+3+6+17+34+51
# 114

"""
5. Complete los espacios en blanco para completar la función, que debería generar una tabla de multiplicar. 
La función, que debería generar una tabla de multiplicar. La función acepta una variable "número" atreves de sus 
parámetros. Esta variable "número" debe multiplicarse por los números del 1 al 5 e imprimirse en un formato similar 
a "1 x 6=6" ("numero" x "multiplicador = "resultado"). El código también debe limitar el "resultado" a no exceder 25. 
Para cumplir estas condiciones, deberá:  
1. Inicialice la variable "multiplicadora" con el valor inicial.  
2. Completa la condición del bucle while.  
3. Agrega un punto de salida para el bucle.  
4. Incrementa la variable "multiplicadora" dentro del bucle while. 
     
"""


# Initialize the appropriate variable
# Complete the while loop condition.
# Enter the action to take if the result is greater than 25
# Increment the appropriate variable
def multiplication_table(number):
    multiplier = 1

    while multiplier:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

multiplication_table(5)
# Should print:
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25

multiplication_table(8)
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24

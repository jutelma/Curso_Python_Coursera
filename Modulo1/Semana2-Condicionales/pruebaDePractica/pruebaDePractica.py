# 1 Cuál es el valor de esta expression dee python : (2**2) == 4?

# R (2**2) == 4 es una expresión que verifica si el resultado de elevar 2 al cuadrado es igual a 4. Dado que esto
# es cierto, la expresión se evalúa como True.

# 2 Complete el guion completando las partes que faltan La fusion recibe un nombre y luego devuelve un saludo segun
# si el nombre es Taylor o no.  def greeting(name):


def greeting(name):
    if name == "Taylor":
        return "¡Bienvenido de nuevo Taylor!"
    else:
        return "¡Hola " + name + "!"


print(greeting("Taylor"))
print(greeting("John"))

# ¿3 Cual es el resultado de este código si el número es igual a 10?


number = 10

if number > 11:
    print(0)
elif number != 10:
    print(1)
elif number >= 20 or number < 12:
    print(2)
else:
    print(3)

# R 2

# 4 ¿Es "Un perro"  mas pequeño o mas grande que "Un ratón"? ¿9999 + 8888 es menor o mayor que 100*100? Remplace el
# signo mas con un operador de comparación en el siguiente código para permitir que Python lo verifique por usted y
# luego responda. El resultado debería devolver Verdadero si se utiliza el operador de comparación correcto.
# print("A dog" + "A mouse")

# R  "Un perro" es mas pequeño que "Un ration" y 9999 + 8888 es mayor que 100 * 100


print("A dog" < "A mouse")
print(9999 + 8888 > 100 * 100)


# 5 Si un sistema de archivos tiene un bloque de 4096 bytes, esto significa que un archivo compuesto por solo un byte
# seguirá utilizando 4096 bytes de almacenamiento.
# Un archivo compuesto por 4097 bytes utilizará  4096*2=8192 bytes de
# almacenamiento.
# Sabiendo esto, ¿ puedes completar los espacios en la function calcular_almacenamiento a continuation,
# que calcula el número de bytes necesarios para almacenar un archivo de un tamaño determinado?


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return full_blocks * block_size


print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192

# 1.
# Pregunta 1
# ¿Para qué se utiliza la recursividad?

# La recursividad se utiliza para llamar a una función desde dentro de la misma función.

# Pregunta 2
# ¿Cuáles de estas actividades son buenos casos de uso para programas recursivos? Marque todo lo que corresponda.

# Pasar por un sistema de archivos recopilando información relacionada con directorios y archivos.

# Gestionar permisos asignados a grupos dentro de una empresa, cuando cada grupo puede contener tanto subgrupos como
# usuarios.

# Pregunta 3 Complete los espacios en blanco para que la función is_power_of devuelva si el número es una potencia de
# la base dada. Nota: se supone que la base es un número positivo. Consejo: para funciones que devuelven un valor
# booleano, puedes devolver el resultado de una comparación.

def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number / base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False


# 4. Pregunta
# 4 La función count_users cuenta recursivamente la cantidad de usuarios que pertenecen a un grupo en el
# sistema de la empresa, pasando por cada uno de los miembros de un grupo y si uno de ellos es un grupo,
# llama recursivamente a la función y cuenta los miembros. ¡Pero tiene un error! ¿Puedes detectar el problema y
# solucionarlo?

# Pregunta 5 Implemente la función sum_positive_numbers, como una función recursiva que devuelve la suma de todos los
# números positivos entre el número n recibido y 1. Por ejemplo, cuando n es 3 debería devolver 1+2+3=6, y cuando n
# es 5 debería devolver 1+2+3+4+5=15.

def sum_positive_numbers(n):
    if n <= 0:
        return 0
    else:
        return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15

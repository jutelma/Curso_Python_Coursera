"""
    Operadores de comparación con ecuaciones

    Los siguientes ejemplos demuestran cómo utilizar operadores de comparación con los tipos de datos int (enteros,
    números enteros) y float (número con punto decimal o valor fraccionario). Los operadores de comparación devuelven
    resultados booleanos. Como aprendiste anteriormente, booleano es un tipo de datos que solo puede contener uno de
    dos valores: Verdadero o Falso .

    Los operadores de comparación incluyen:

    ==     (igualdad)

    !=      (no igual a)

    >        (mayor que)

    <       (menos que)

    >=     (mayor o igual a)

    <=    (menor o igual a)


PARTE 1: Operadores de igualdad == y no igual a !=
         En Python, puedes usar operadores de comparación para comparar valores. Cuando se realiza una comparación,
         Python devuelve un resultado booleano: Verdadero o Falso . Tenga en cuenta que los tipos de datos booleanos
         no son tipos de datos de cadena (Boolean True no es igual a la cadena "True").

            ·Para comprobar si dos valores son iguales, utilice el operador de igualdad : ==

            ·Para comprobar si dos valores no son iguales, utilice el operador distinto de : !=

         La función print() se puede utilizar para mostrar los resultados de las comparaciones.

    Ejemplos:

"""


print(32 == 30+2)   # El operador == comprueba si los 2 valores son
True                # iguales entre sí. Si son iguales,
                     # Python devuelve un resultado Verdadero.


print(5+10 == 6+7)  # Si los dos valores no son iguales, como en el
False               # expresión 5+10 == 6+7 (o 15 == 13), Python
                    # devuelve un resultado Falso.


print(10-4 != 10+4) # El operador != comprueba si los 2 valores son
True                # NO iguales entre sí. Si es cierto, Python
                    # devuelve un resultado Verdadero.


print(9/3 != 3*1)   # En este último ejemplo, 9/3 != 3*1 (o 3 != 3)
False               # Es falso. Entonces, Python devuelve un valor Falso.

"""
    El operador igualdad == versus el operador  igual =
    Es importante tener en cuenta que el operador de comparación igualdad == realiza una tarea diferente a la del
    operador de asignación igual = . El operador igual = asigna el valor en el lado derecho del operador igual = al
    objeto (por ejemplo, una variable) en el lado izquierdo del operador igual = .

    Ejemplos:"""

# El operador de asignación = igual se utiliza para asignar un valor a un
# variable.

my_variable = 3 * 5  # Asigna un valor a mi_variable
print(my_variable)   # Imprimir la variable devuelve el
15                   # valor asignado a la variable.

# El operador de comparación == igualdad comprueba si los valores de los dos
# expresiones a cada lado del operador == son equivalentes a una
# otro.

print(my_variable == 3 * 5)   # Imprimir la variable devuelve un booleano
True                          # Resultado verdadero o falso.

"""
    PARTE 2: Operadores mayor que > y menor que <
    
    Los operadores de comparación mayor que > y menor que < también devuelven un resultado booleano Verdadero o Falso
    después de comparar dos valores.

        ·Para comprobar si un valor es mayor que otro valor, utilice el operador mayor que: > 
        ·Para comprobar si un valor es menor que otro valor, utilice el operador menor que: < 

    Ejemplos:"""

print(11 > 3*3)         # El operador > comprueba si el valor izquierdo es
True                    # mayor que el valor correcto. Si es cierto,
                        # devuelve un resultado Verdadero.


print(4/2 > 8-4)        # Si el operador > encuentra que el valor izquierdo
False                   # NO es mayor que el valor correcto, el
                        # comparación arrojará un resultado Falso.


print(4/2 < 8-4)        # El operador < comprueba si el valor izquierdo es
True                    # menos que el lado derecho. Si es cierto, el
                        # comparación devuelve un resultado Verdadero.


print(11 < 3*3)         # Si el operador < encuentra que el lado izquierdo es Falso
False                   # NO menos que el valor correcto, Python devuelve
                        # un resultado falso.

"""
    PARTE 3: Operadores mayor o igual a >= y menor o igual a <=
    
    Al igual que los otros operadores de comparación, los operadores mayor o igual a >= y menor o igual a <= devuelven 
    un resultado booleano Verdadero o Falso cuando se realiza una comparación.

    ·Para comprobar si un valor es mayor o igual que otro valor, utilice el operador mayor o igual que: >= 

    ·Para comprobar si un valor es menor o igual que otro valor, utilice el operador menor o igual que: <= 

    Ejemplos:"""

print(12*2 >= 24)   # El operador >= comprueba si el valor izquierdo es
True                # mayor o igual al valor correcto.
                    # Si una de estas condiciones es verdadera,
                    # Python devuelve un resultado Verdadero. En este caso
                    # los dos valores son iguales. Entonces, la comparación
                    # devuelve un resultado Verdadero.


print(18/2 >= 15)   # Si la comparación >= determina que la izquierda es Falso
False               # el valor NO es mayor o igual que el
                    # correcto, devuelve un resultado Falso.


print(12*2 <= 30)   # El operador <= comprueba si el valor izquierdo es
True                # menor o igual al valor correcto.
                    # en este caso, el valor izquierdo es menor que el
                    # valor correcto. De nuevo, si uno de los dos
                    # condiciones es verdadera, Python devuelve True
                    # resultado.


print(15 <= 18/2)   # Si la comparación <= determina que la izquierda
False               # valor NO es menor o igual a la derecha
                    # valor, la comparación devuelve un resultado Falso.


"""
    PARTE 4: Práctica
    
    Si desea tener más práctica en el uso de operadores de comparación, no dude en crear sus propias comparaciones
    utilizando el bloque de código a continuación. Tenga en cuenta que no hay comentarios asociados con este bloque 
    de código. """

print(20*3 >= 60)
True

print(25/5 >= 4)
True

print(15*2 <= 30)
True

print(18 <= 36/2)
False

print(11 > 3*3)
True

print(4/2 > 8-4)
False

print(4/2 < 8-4)
True

print(11 < 3*3)
False

""" 
    Conclusiones clave
    
    Los operadores de comparación de Python devuelven resultados booleanos: Verdadero o Falso .

Símbolo  |         Nombre                |  Expresión   |    Descripción
                                                    
  ==     | Operador de igualdad          |    a == b    |  a es igual a b
                                                    
  !=     | No es igual al operador       |    = ba !    |  a no es igual a b
  
  >      | Mayor que el operador         |    a > b     |  a es mayor que b

  >=     | Operador mayor o igual que    |    a >= b    | a es mayor o igual que b
 
  <      | Menos que operador            |    a < b     | a es menor que b

  <=     | Menor o igual que el operador |   a <= b     | a es menor o igual que b

"""


















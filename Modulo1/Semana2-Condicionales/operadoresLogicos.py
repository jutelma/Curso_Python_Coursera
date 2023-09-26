"""
   Operadores logicos
Los operadores lógicos se utilizan para construir expresiones más complejas. Puede realizar comparaciones complejas
uniendo declaraciones de comparación utilizando los operadores lógicos: y , o , no . Las comparaciones complejas
devuelven un resultado booleano ( verdadero o falso ).

 · y

    ·Ambos lados de la declaración que se evalúa deben ser Verdaderos para que toda la declaración sea Verdadera.

    ·Ejemplo: (5 > 1 y 5 < 10) = Verdadero

 · o

    ·Si cualquiera de los lados de la comparación es Verdadero, entonces toda la afirmación es Verdadera.

    ·Ejemplo: (color = "azul" o color = "verde") = Verdadero

 · no

    ·Invierte el resultado booleano de la declaración que le sigue inmediatamente. Entonces, si una declaración se
     evalúa como Verdadera y colocamos el operador not delante de ella, se convertirá en Falsa.

    ·Ejemplo: ( no "A" == "A") = Falso



    PARTE 1: El operador lógico y

    En Python, puedes usar el operador lógico y para conectar más de una comparación. Este tipo de comparación compleja
    se utiliza para comprobar si dos afirmaciones de comparación son verdaderas o no. Puede utilizar el operador and
    cuando necesite ejecutar un bloque de código, pero solo si se cumplen dos condiciones diferentes. Por ejemplo, es
    posible que desee escribir un script que automatice el envío de una alerta de emergencia si un servidor deja de
    responder y hay un aumento inusual de empleados que abren tickets de problemas.

    Ejemplo 1:

    El siguiente modelo demuestra el uso del operador lógico y para unir comparaciones entre dos expresiones
    matemáticas. La descripción debajo del ejemplo explica el orden en el que Python procesará la línea de código.

"""
# Example 1

print((6*3 >= 18) and (9+9 <= 36/2))

"""
    En el ejemplo anterior, Python completó las siguientes actividades en el siguiente orden:  

        1º Python resuelve las expresiones numéricas usando el orden de las operaciones. (6*3 >= 18) y (9+9 <= 36/2) 
        se convierte en (18 >= 18) y (18 <= 18)

        2º Python compara los resultados de las expresiones numéricas utilizando los operadores de comparación (en este 
        caso >= y <=). (18 >= 18) y (18 <= 18) se convierten en Verdadero y Verdadero

        3º Python comprueba si ambos lados del operador lógico "y" son verdaderos. Verdadero y Verdadero se vuelven 
        Verdaderos

        4º Python devuelve un valor booleano: Verdadero o Falso. La comparación compleja devuelve un resultado 
        Verdadero.


    Ejemplo 2:

    En el siguiente ejemplo, "Nairobi" < "Milán" y "Nairobi" > "Hanoi", el operador lógico y conecta dos declaraciones 
    de comparación de cadenas. Anteriormente aprendió que el uso de los operadores mayor que y menor que en cadenas 
    probará el orden alfabético (técnicamente valores Unicode) de las cadenas. Entonces, esta compleja comparación 
    verifica si "Nairobi" está ordenado alfabéticamente antes de "Milán" (Falso) Y después de "Hanoi" (Verdadero). 

    Esta comparación devuelve un resultado Falso porque ambos lados del operador lógico no son Verdaderos. Se podría 
    usar una declaración de comparación como esta para recorrer una lista de nombres y verificar si están ordenados 
    alfabéticamente en el orden correcto.
    
"""

# Example 2

print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")

"""  
        PARTE 2: El operador lógico or

    El operador lógico or prueba dos condiciones para determinar si al menos un lado del operador lógico o es Verdadero. 
    El resultado de la prueba se puede utilizar para activar un bloque de código si al menos una condición está 
    presente.

    Sintaxis:


            1 Expression1 or Expression2


    Devuelve booleanos: 

Expresión1            Expresión2          Devuelve el resultado


Verdadero             Verdadero           Verdadero

Verdadero             FALSO               Verdadero

FALSO                 Verdadero           Verdadero

FALSO                 FALSO               FALSO



    Ejemplos:
"""

# True or True returns True
print((15/3 < 2+4) or (0 >= 6-7))
True

# False or True returns True
country = "New York City"
print(country == "New York City" or country == "New York City")
True

# True or False returns True
print(16 <= 4**2 or 9**(0.5) != 3)
True

# False or False returns False
print("B_name" > "C_name" or "B_name" < "A_name")
False

"""
        PARTE 3: El operador no lógico
        
    El operador no lógico invierte el valor de la expresión de comparación. Esta es una herramienta útil cuando desea 
    ejecutar un bloque de código siempre que no esté presente una determinada condición.

    · Si la expresión condicional es Verdadera, se puede agregar el operador no lógico para que la expresión no sea 
      Verdadera (Falso). 
    
    · Si la expresión condicional es Falsa, se puede agregar el operador no lógico para que la expresión no sea 
      Falsa (Verdadero).  

    Sintaxis:
    
    1  no expression
    
    Ejemplo 1:
    
"""
# Test Example 1:

x = 2*3 > 6
print("The value of x is:")
print(x)

print("")  # Prints a blank line

print("The inverse value of x is:")
print(not x)

"""
    Ejemplo 2:
    
"""
# ¿Qué sucede cuando niegas una afirmación falsa?
# Haga clic en Ejecutar cuando esté listo para verificar su respuesta.


today = "Monday"
print(not today == "Tuesday")


# La variable "hoy" indica que hoy es lunes. Esto hace la comparación
# "hoy == martes" Falso. El operador lógico "no" invierte el Falso
# resultado para convertirse en Verdadero. En otras palabras, esta expresión pregunta si es
#falso que hoy no es martes. De manera más sucinta, "no es falso" significa
# Verdadero."

"""
        PARTE 4: Práctica
        
    Si desea practicar más usando los operadores lógicos ( y , o , no ), no dude en crear sus propias comparaciones 
    usando el bloque de código a continuación. Tenga en cuenta que no hay comentarios asociados con este bloque de 
    código. 
    
"""

result = (3 < 5) and (7 == 7)
print(result)

result = (10 > 20) or (30 != 40)
print(result)

result = not (True and False)
print(result)

result = (15 >= 10) and (20 <= 30)
print(result)

result = (8 > 10) and (15 == 15)
print(result)

"""
        Conclusiones clave
        
    Cuando se utilizan operadores lógicos de Python con operadores de comparación, el intérprete devolverá resultados 
    booleanos ( Verdadero o Falso ):

    Expresión: a == a y a != b  |  Descripción: Verdadero si ambos lados son Verdaderos; en caso contrario, Falso.

    Expresión: a > b o a <= c   |  Descripción: Verdadero si cualquiera de los lados es Verdadero. Falso si ambos lados 
                                   son falsos.
                                   
    Expresión:   no a == b      |  Verdadero si la afirmación es Falsa, Falso si la afirmación es Verdadera.                          


"""




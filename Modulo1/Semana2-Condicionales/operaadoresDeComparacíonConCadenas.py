"""
    Operadores de comparación con cadenas

    En esta lectura, aprenderá más sobre lo que los operadores de comparación pueden y no pueden hacer. Si usa los
    operadores == (igualdad) y != (no igual a) con cadenas, puede verificar si dos cadenas contienen el mismo texto o
    no. También puede alfabetizar cadenas usando operadores de comparación > (mayor que), < (menor que) ,
    >= (mayor o igual que) , <= (menor o igual que). Al igual que con los tipos de datos numéricos, los operadores de
    comparación utilizados con cadenas devolverán resultados   booleanos ( Verdadero , Falso ).



PARTE 1: Operadores de igualdad == y no igual a != con cadenas

En Python, puedes usar operadores de comparación para comparar cadenas. Los operadores igualdad == y no igual a != son
útiles cuando necesita buscar una cadena específica en un cuerpo de texto, un archivo de registro, una hoja de cálculo,
una base de datos y más. También puede verificar las cadenas de entrada del usuario para compararlas con otra cadena.
Tenga en cuenta que los tipos de datos booleanos no son tipos de datos de cadena (Boolean True no es igual a la cadena
"True").

Ejemplos:"""

# El operador == puede comprobar si dos cadenas son iguales entre sí.
# Si son iguales, el intérprete de Python devuelve un resultado Verdadero.
print("a string" == "a string")
True


# En este ejemplo, la igualdad == comparación es entre "4 + 5" y
# 4 + 5. Dado que el tipo de datos de la izquierda es una cadena y el tipo de datos de la derecha
# es un número entero, los dos valores no pueden ser iguales. Entonces, la comparación
# devuelve un resultado Falso.
print("4 + 5" == 4 + 5)
False


# El operador != puede comprobar si las dos cadenas NO son iguales entre sí
# otro. Si realmente no son iguales, Python devuelve un resultado Verdadero.
print("rabbit" != "frog")
True


# En este ejemplo, a la variable event_city se le ha asignado la cadena
# valor "Shanghái". Esta variable se compara con una cadena estática,
# "Shanghai", usando el operador !=. Como, las cadenas "Shanghai" y
# "Shanghai" son iguales, la comparación de "Shanghai"! = "Shanghai"
# Es falso. En consecuencia, Python devolverá un resultado Falso.
event_city = "Shanghai"
print(event_city != "Shanghai")
False

# Este último ejemplo ilustra el resultado de intentar comparar dos
# elementos de diferentes tipos de datos usando el operador igualdad ==. El
# dos elementos no son iguales, por lo que la comparación devuelve Falso.
print("three" == 3)
False

"""PARTE 2: Operadores mayor que > y menor que <
Los operadores de comparación mayor que > y menor que < se pueden usar para alfabetizar palabras en Python. Las letras 
del alfabeto tienen códigos numéricos en Unicode (también conocidos como valores ASCII). Las letras mayúsculas de la A 
a la Z están representadas por los valores Unicode del 65 al 90. Las letras minúsculas de la A a la Z están 
representadas por los valores Unicode del 97 al 122. 


Imagen que contiene los valores Unicode de cada letra del alfabeto.

· Para verificar si las primeras letras de una cadena tienen un valor Unicode mayor (lo que significa que la letra está
más cerca de 122 o z minúscula) que la primera letra de otra cadena, use el operador mayor que: >

· Para verificar si las primeras letras de una cadena tienen un valor Unicode más pequeño (lo que significa que la letra 
está más cerca de 65 o A mayúscula) que la primera letra de otra cadena, use el operador menor que: < 

Al igual que las comparaciones numéricas con los operadores mayor que > y menor que < , las comparaciones entre cadenas
también devuelven resultados   booleanos Verdadero o Falso .

Ejemplos:  """

# El operador mayor que > comprueba si la cadena izquierda tiene un valor mayor
# Valor Unicode que la cadena correcta. Si es verdadero, el intérprete de Python
# devuelve un resultado Verdadero. Dado que W tiene un valor Unicode de 87, puedes
# calcula fácilmente que F tiene un valor Unicode de 70, esta comparación es
# lo mismo que 87 > 70. Como esto es cierto, Python devolverá True
# resultado.
print("Wednesday" > "Friday")
True

# El operador menor que < comprueba si la cadena izquierda tiene un valor inferior
# Valor Unicode que la cadena correcta. Si hace referencia al Unicode
# gráfico de arriba, puedes ver que todas las letras minúsculas tienen mayor
# Valores Unicode que letras mayúsculas. Podemos ver que B tiene un
# Valor Unicode de 66 y b tiene un valor Unicode de 98. Esto
# comparación es lo mismo que 66 <98, lo cual es cierto. Entonces, Python
# devolver un resultado verdadero.
print("Brown" < "brown")
True

# Si las cadenas tienen las mismas primeras letras, la comparación será
# recorrer cada letra de cada cadena, de izquierda a derecha hasta que
# encuentra dos letras que tienen diferentes valores Unicode. En este ejemplo,
# ambas cadenas comparten la subcadena inicial "sol", pero luego tienen
# letras diferentes con diferentes valores Unicode en el cuarto lugar
# en cada cadena. Entonces, las cuartas letras 'b' y 't' de las dos
# cadenas se utilizan para la comparación. Dado que 'b' no tiene un mayor
# Valor Unicode que 't', la comparación devuelve un resultado Falso.
print("sunbathe" > "suntan")
False

# Si se comparan dos cadenas idénticas usando la comparación menor que <
# operador, esto producirá un resultado Falso porque son iguales.
print("Lima" < "Lima")
False

# Este último ejemplo ilustra el resultado de intentar comparar dos
# elementos de diferentes tipos de datos usando el operador menor que <. El
# Los operadores mayor que > y menor que < no se pueden usar para comparar
# dos tipos de datos diferentes.
print("Five" < 6)
"""
Error on line 1:
    print("Five" < 6)
TypeError: '<' not supported between instances of 'str' and 'int'

"""
"""
    PARTE 3: Operadores mayor o igual a >= y menor que o igual a <=
    Los operadores mayor o igual a >= y menor o igual a <= también se pueden usar con cadenas. Al igual que los otros 
    operadores de comparación, devolverán un resultado booleano Verdadero o Falso cuando se realiza una comparación 
    entre dos cadenas. 

        · Para comprobar si una cadena tiene un valor Unicode mayor o igual que las primeras letras de otra cadena, 
          utilice el operador mayor o igual que: > = 

        · Para comprobar si una cadena tiene un valor Unicode menor o igual que las primeras letras de otra cadena, 
          utilice el operador menor o igual que: < =

    En este punto, debería estar familiarizado con cómo funcionan los operadores de comparación en Python. ¿Puedes 
    determinar cuáles serán los resultados de las comparaciones que se enumeran a continuación? Cuando esté listo para 
    verificar sus respuestas, haga clic en Ejecutar.

       1. "mi computadora" >= "mi silla"

       2. "Primavera" <= "Invierno"

       3. "piña" >= "piña"
"""

# Use the Unicode chart in Part 2 to determine if the Unicode values of
# the first letters of each string are higher, lower, or equal to one
# another.


var1 = "my computer" >= "my chair"
var2 = "Spring" <= "Winter"
var3 = "pineapple" >= "pineapple"

print("Is \"my computer\" greater than or equal to \"my chair\"? Result: ", var1)
print("Is \"Spring\" less than or equal to \"Winter\"? Result: ", var2)
print("Is \"pineapple\" less than or equal to \"pineapple\"? Result: ", var3)


"""
    PARTE 4: Práctica
    
    Si desea practicar más usando los operadores de comparación ( == , != , > , < , >= , <= ) con cadenas, no dude en 
    crear sus propias comparaciones usando el bloque de código a continuación. Tenga en cuenta que no hay comentarios 
    asociados con este bloque de código. 
    
    1
    

"""



"""Diccionarios definidos
Los diccionarios son otra estructura de datos en Python. Son similares a una lista en el
sentido de que pueden usarse para organizar datos en colecciones. Sin embargo, no se accede a los datos de un
diccionario en función de su posición. Los datos de un diccionario se organizan en pares de claves y valores. Utiliza
la clave para acceder al valor correspondiente. Cuando un índice de lista es siempre un número, una clave de
diccionario puede ser un tipo de datos diferente, como una cadena, un número entero, un flotante o incluso una tupla.

Al crear un diccionario, utiliza llaves: {} . Al almacenar valores en un diccionario, la clave se especifica primero,
seguida del valor correspondiente, separado por dos puntos. Por ejemplo, animales = { "osos":10, "leones":1,
"tigres":2 } crea un diccionario con tres pares clave-valor, almacenados en la variable animales. La clave "osos"
apunta al valor entero 10, mientras que la clave "leones" apunta al valor entero 1 y "tigres" apunta al valor entero
2. Puede acceder a los valores haciendo referencia a la clave, así: animales [ "osos"] . Esto devolvería el número
entero 10, ya que ese es el valor correspondiente a esta clave.

También puede comprobar si una clave está contenida en un diccionario utilizando la palabra clave in . Al igual que
otros usos de esta palabra clave, devolverá Verdadero si la clave se encuentra en el diccionario; de lo contrario
devolverá Falso.

Los diccionarios son mutables, lo que significa que se pueden modificar agregando, eliminando y reemplazando
elementos en un diccionario, de manera similar a las listas. Puede agregar un nuevo par clave-valor a un diccionario
asignando un valor a la clave, como este: animales["cebras"] = 2 . Esto crea la nueva clave en el diccionario de
animales llamada cebras y almacena el valor 2. Puede modificar el valor de una clave existente haciendo lo mismo.
Entonces animales["osos"] = 11 cambiaría el valor almacenado en la clave osos de 10 a 11. Por último, puedes eliminar
elementos de un diccionario usando la palabra clave del . Al hacer de los animales["leones"] eliminaría el par
clave-valor del diccionario de animales.

Iterando sobre diccionarios

Puedes iterar sobre diccionarios usando un bucle for , al igual que con cadenas,
listas y tuplas. Esto iterará sobre la secuencia de claves en el diccionario. Si desea acceder a los valores
correspondientes asociados con las claves, puede utilizar las claves como índices. O puedes usar el método items en
el diccionario, como Dictionary.items() . Este método devuelve una tupla para cada elemento del diccionario,
donde el primer elemento de la tupla es la clave y el segundo es el valor.

Si solo desea acceder a las claves de un diccionario, puede utilizar el método claves() en el diccionario:
diccionario.claves() . Si solo quisiera los valores, podría usar el método valores() : diccionario.valores() .





"""
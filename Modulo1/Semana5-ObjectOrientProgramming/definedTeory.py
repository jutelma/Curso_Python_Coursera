"""
Definición de programación orientada a objetos

En la programación orientada a objetos, los conceptos se modelan
como clases y objetos. Una idea se define mediante una clase y una instancia de esta clase se denomina objeto. Casi
todo en Python es un objeto, incluidas cadenas, listas, diccionarios y números. Cuando creamos una lista en Python,
estamos creando un objeto que es una instancia de la clase lista, que representa el concepto de lista. Las clases
también tienen atributos y métodos asociados. Los atributos son las características de la clase, mientras que los
métodos son funciones que forman parte de la clase.


Clases y objetos en detalle

Podemos usar la función type() para averiguar a qué clase pertenece una variable o valor.
Por ejemplo, type(" ") nos dice que se trata de una clase de cadena. El único atributo en este caso es el valor de la
cadena, pero hay varios métodos asociados con la clase. Hemos visto el método upper(), que devuelve la cadena en
mayúsculas, así como  isnumeric() que devuelve un valor booleano que nos indica si la cadena es un número o no. Puede
utilizar la función dir() para imprimir todos los atributos y métodos de un objeto. Cada cadena es una instancia de
la clase de cadena y tiene los mismos métodos que la clase principal. Dado que el contenido de la cadena es
diferente, los métodos devolverán valores diferentes. También puede utilizar la función help() en un objeto,
que devolverá la documentación de la clase correspondiente. Esto mostrará todos los métodos de la clase,
junto con los parámetros que reciben los métodos, los tipos de valores de retorno y una descripción de los métodos.

Definición de clases (opcional)
Podemos crear y definir nuestras clases en Python de forma similar a como definimos
funciones. Comenzamos con la palabra clave class, seguida del nombre de nuestra clase y dos puntos. Las pautas de
estilo de Python recomiendan que los nombres de las clases comiencen con una letra mayúscula. Después de la línea de
definición de clase está el cuerpo de la clase, con sangría a la derecha. Dentro del cuerpo de la clase,
podemos definir atributos para la clase.

Tomemos nuestro ejemplo de clase de Apple:

>>> class Apple:
...     color = ""
...     flavor = ""
...

Podemos crear una nueva instancia de nuestra nueva clase asignándola a una variable. Esto se hace llamando al nombre
de la clase como si fuera una función. Podemos configurar los atributos de nuestra instancia de clase accediendo a
ellos usando notación de puntos. La notación de puntos se puede utilizar para establecer o recuperar atributos de
objetos, así como para llamar a métodos asociados con la clase.

>>> jonagold = Apple()
>>> jonagold.color = "red"
>>> jonagold.flavor = "sweet"

Creamos una instancia de Apple llamada jonagold y configuramos los atributos de color y sabor para este objeto de
Apple. Podemos crear otra instancia de una Apple y establecer diferentes atributos para diferenciar dos variedades
diferentes de manzanas.

>>> golden = Apple()
>>> golden.color = "Yellow"
>>> golden.flavor = "Soft"

Ahora tenemos otro objeto de Apple llamado golden que también tiene atributos de color y sabor. Pero estos atributos
tienen valores diferentes.
"""
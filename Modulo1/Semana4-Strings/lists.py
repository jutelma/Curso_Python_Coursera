# Practice
"""Listas definidas
 Las listas en Python se definen usando corchetes, con los elementos almacenados en la lista
separados por comas: list = ["This", "is", "a", "list"] . Puede usar la función len() para devolver el número de
elementos en una lista: len(list) devolvería 4 . También puede utilizar la palabra clave in para comprobar si una
lista contiene un elemento determinado. Si el elemento está presente, devolverá un valor booleano Verdadero. Si el
elemento no se encuentra en la lista, devolverá Falso. Por ejemplo, "Esto" en la lista devolvería Verdadero en
nuestro ejemplo. Al igual que las cadenas, las listas también pueden utilizar la indexación para acceder a elementos
específicos de una lista en función de su posición. Puede acceder al primer elemento de una lista haciendo list[0] ,
lo que le permitiría acceder a la cadena "This" .

En Python, las listas y las cadenas son bastante similares. Ambos son ejemplos de secuencias de datos. Las secuencias
tienen propiedades similares, como (1) poder iterar sobre ellas usando bucles for; (2) apoyar la indexación; (3)
usar la función len para encontrar la longitud de la secuencia; (4) usar el operador más + para concatenar; y (5)
usar la palabra clave in para verificar si la secuencia contiene un valor. Comprender estos conceptos también le
permitirá aplicarlos a otros tipos de secuencias.

Modificar listas

Si bien las listas y las cadenas son secuencias, una gran diferencia entre ellas es que las listas
son mutables. Esto significa que el contenido de la lista se puede cambiar, a diferencia de las cadenas,
que son inmutables. Puede agregar, eliminar o modificar elementos en una lista.

Puede agregar elementos al final de una lista usando el método append . Usted llama a este método en una lista usando
notación de puntos y pasa el elemento que se agregará como parámetro. Por ejemplo, list.append("Nuevos datos")
agregaría la cadena "Nuevos datos" al final de la lista llamada lista.

Si desea agregar un elemento a una lista en una posición específica, puede usar el método insertar . El método toma
dos parámetros: el primero especifica el índice de la lista y el segundo es el elemento que se agregará a la lista.
Entonces list.insert(0, "Nuevos datos") agregaría la cadena "Nuevos datos" al frente de la lista. Esto no
sobrescribiría el elemento existente al comienzo de la lista. Simplemente, cambiaría todos los demás elementos en uno.
Si especifica un índice que es mayor que la longitud de la lista, el elemento simplemente se agregará al final de la
lista.

Puede eliminar elementos de la lista utilizando el método de eliminación . Este método toma un elemento como
parámetro y elimina la primera aparición del elemento. Si el elemento no se encuentra en la lista, recibirá un error
ValueError que explica que el elemento no se encontró en la lista.

También puedes eliminar elementos de una lista usando el método pop . Este método se diferencia del método remove en
que toma un índice como parámetro y devuelve el elemento que se eliminó. Esto puede resultar útil si no sabe cuál es
el valor, pero sabe dónde está ubicado. Esto también puede resultar útil cuando necesita acceder a los datos y
también desea eliminarlos de la lista.

Finalmente, puede cambiar un elemento en una lista utilizando la indexación para sobrescribir el valor almacenado en
el índice especificado. Por ejemplo, puede ingresar lista[0] = "Datos antiguos" para sobrescribir el primer elemento
de una lista con la nueva cadena "Datos antiguos".

Tuples
Como mencionamos anteriormente, las cadenas y las listas son ejemplos de secuencias. Las cadenas son
secuencias de caracteres y son inmutables. Las listas son secuencias de elementos de cualquier tipo de datos y son
mutables. El tercer tipo de secuencia es la tuple. Las tuples son como listas, ya que pueden contener elementos de
cualquier tipo de datos. Pero a diferencia de las listas, las tuples son inmutables. Se especifican mediante
paréntesis en lugar de corchetes.

Quizás se pregunte por qué existen las tuples, dado lo similares que son a las listas. Las tuples pueden resultar
útiles cuando necesitamos asegurarnos de que un elemento esté en una posición determinada y no cambie. Dado que las
listas son mutables, el orden de los elementos se puede cambiar por nuestra cuenta. Dado que el orden de los
elementos de una tuple no se puede cambiar, la posición del elemento en una tuple puede tener significado. Un buen
ejemplo de esto es cuando una función devuelve múltiples valores. En este caso, lo que se devuelve es una tuple,
con los valores devueltos como elementos de la tuple. El orden de los valores devueltos es importante y una tuple
garantiza que el orden no cambiará. Almacenar los elementos de una tuple en variables separadas se llama
desempaquetar. Esto le permite tomar múltiples valores devueltos de una función y almacenar cada valor en su propia
variable.


Iterando sobre listas usando Enumerate

Cuando cubrimos los bucles for , mostramos el ejemplo de iteración sobre una
lista. Esto le permite iterar sobre cada elemento de la lista, exponiendo el elemento al bucle for como una variable.
Pero ¿qué pasa si quieres acceder a los elementos de una lista, junto con el índice del elemento en cuestión? Puedes
hacer esto usando la función enumerar() . La función enumérate() toma una lista como parámetro y devuelve una tuple
para cada elemento de la lista. El primer valor de la tuple es el índice y el segundo valor es el elemento mismo.

Ejemplos de comprensión de listas
Puede crear una lista a partir de una secuencia usando un bucle for , pero hay una
manera más sencilla de hacerlo usando una lista por comprensión. Las listas por comprensión le permiten crear una
nueva lista a partir de una secuencia o un rango en una sola línea.


Comprensión de listas simples
Por ejemplo, [ x*2 for x in range(1,11) ] es una lista de comprensión simple. Esta
única línea de código itera en un rango de 1 a 10, multiplica cada elemento en el rango por 2 y crea una nueva lista
a partir de todos los múltiplos de 2 de 2 a 20.

"""
# Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines
# of code into one line:
print([x * 2 for x in range(1, 11)])

### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1, 11):
    my_list.append(x * 2)
print(my_list)

# Click Run to compare the two results.

"""Comprensión de listas con declaración condicional También puede utilizar condicionales con listas por comprensión 
para crear declaraciones aún más complejas y poderosas. Puede hacer esto agregando una declaración if al final de la 
lista de comprensión. Por ejemplo, [ x for x in range(1,101) if x % 10 == 0 ] genera una nueva lista que contiene 
todos los números enteros divisibles por 10 de 1 a 100. La declaración if evalúa cada valor en el rango de 1 a 100 a 
compruebe si es divisible por 10. Si lo es, el número se agrega a una nueva lista."""

# List Comprehension with Conditional Statement
print("List comprehension result:")

# The following list comprehension compacts multiple lines
# of code into one line:
print([x for x in range(1, 101) if x % 10 == 0])

# Long form for loop with nested if-statement
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code:
my_list = []
for x in range(1, 101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)

# Click Run to observe the two results.

"""Las listas por comprensión pueden ser realmente poderosas, pero también pueden ser complejas, lo que resulta en un 
código difícil de leer. Tenga cuidado al usarlos, ya que podría dificultar que otra persona que mire su código 
comprenda fácilmente lo que está haciendo. Es una buena práctica agregar comentarios descriptivos sobre cualquier 
lista por comprensión utilizada en su código. Esto ayuda a comunicar el propósito de la lista por comprensión a otros 
codificadores. Los comentarios también le ayudarán a recordar el objetivo del código cuando realice futuras adiciones 
y mantenimiento de código.

  

Ejercicio práctico 

Este ejercicio le mostrará cómo escribir una lista de comprensión para crear una lista de números 
al cuadrado (n*n). Debe devolver una lista de cuadrados de números consecutivos entre el "inicio" y el "fin" 
inclusive . Por ejemplo, squares(2, 3) debería devolver una lista que contenga [4, 9].

1 La función recibe las variables “inicio” y “fin” a través de los parámetros de la función.  

2 En la línea de retorno , comience ingresando los corchetes de lista []

3 Entre corchetes [ ], ingrese la expresión aritmética para elevar al cuadrado una variable “n”. 

4 A la derecha de la expresión cuadrada, escriba un bucle for que itere sobre "n" en un rango desde las variables de 
"inicio" hasta "final".

5 Asegúrese de que el valor del rango "final" esté incluido en el rango() añadiéndole 1.

6 ¡Ejecute su código para ver si funciona! Si es necesario, la solución a este código se incluye en el archivo "
Guía de estudio: enumerar operaciones y métodos
”leyendo en “Grupo de habilidades 2” (lista de comprensiones). """


def squares(start, end):
    return [i ** 2 for i in range(start, end + 1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

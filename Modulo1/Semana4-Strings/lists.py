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
hacer esto usando la función enumerar() . La función enumérate() toma una lista como parámetro y devuelve una tupla
para cada elemento de la lista. El primer valor de la tuple es el índice y el segundo valor es el elemento mismo.

"""
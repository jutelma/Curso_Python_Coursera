# Pregunta 1
# Dada una lista de nombres de archivos, queremos cambiar el nombre de todos los archivos con extensión
# hpp a la extensión h. Para hacer esto, nos gustaría generar una nueva lista llamada nuevos nombres de archivos,
# que consta de los nuevos nombres de archivos. Complete los espacios en blanco del código utilizando cualquiera de
# los métodos que ha aprendido hasta ahora, como un bucle for o una lista por comprensión.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newFilenames = []
for filename in filenames:
    newFilenames.append(filename.replace(".hpp", ".h"))

print(newFilenames)


# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# 2. Pregunta
# Creemos una función que convierta el texto en latín: una transformación de texto simple que modifica
# cada palabra moviendo el primer carácter al final y agregando "ay" al final. Por ejemplo, Python termina como
# python.

def pig_latin(text):
    say = []
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        say += word[1:] + word[0] + "ay "
        # Turn the list back into a phrase
    return " ".join(say)


print(pig_latin("hello how are you"))  # Should be "ello hay ow hay ready outlay"
print(pig_latin("programming in python is fun"))  # Should be "programming nay python say unsay"


# 3. Pregunta  ¿Qué método de lista se puede utilizar para agregar un nuevo elemento a una lista en una posición de
# índice específica?

# R lista.insert(índice, x)

# 4. Pregunta Las tuples y las listas son tipos de secuencias muy similares. ¿Qué es lo principal que diferencia
# una tuple de una lista?

# R Una Tupla es inmutable

# 5. Pregunta 5 La función lista_grupo acepta un nombre de grupo y una lista de miembros, y devuelve una cadena con
# el formato: nombre_grupo: miembro1, miembro2,... Por ejemplo, lista_grupo("g", ["a","b","c"] ) devuelve "g: a, b,
# c". Complete los espacios en blanco en esta función para hacerlo.

def group_list(group, users):
    members = ', '.join(users)
    return "{}: {}".format(group, members)


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))  # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"


# 6. Pregunta 6 La función guest_list lee una lista de tuplas con el nombre, edad y profesión de cada invitado a la
# fiesta e imprime la frase "El invitado tiene X años y trabaja como __". Para cada uno. Por ejemplo, guest_list((
# 'Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) debería imprimirse: Ken tiene 30 años. y
# trabaja como Chef. Pat tiene 35 años y trabaja como Abogado. Amanda tiene 25 años y trabaja como Ingeniera.
# Complete los espacios en blanco en esta función para hacerlo.

def guest_list(guests):
    for guest in guests:
        name, age, occupation = guest
        print("{} is {} years old and works as {}".format(name, age, occupation))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

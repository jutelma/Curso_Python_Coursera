"""¿Qué es un método? Llamar a métodos en objetos ejecuta funciones que operan en atributos de una instancia
específica de la clase. Esto significa que llamar a un método en una lista, por ejemplo, solo modifica esa instancia
de una lista, y no todas las listas globalmente. Podemos definir métodos dentro de una clase creando funciones dentro
de la definición de clase. Estos métodos de instancia pueden tomar un parámetro llamado self que representa la
instancia en la que se ejecuta el método. Esto le permitirá acceder a los atributos de la instancia usando notación
de puntos, como self.name, que accederá al atributo de nombre de esa instancia específica de la clase. objeto. Cuando
tiene variables que contienen diferentes valores para diferentes instancias, se denominan variables de instancia.
"""


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)


# Create a new instance with a name of your choice
some_person = Person("John")
# Call the greeting method
print(some_person.greeting())

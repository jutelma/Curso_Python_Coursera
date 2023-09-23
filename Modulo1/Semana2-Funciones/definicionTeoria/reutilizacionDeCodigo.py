"""ejemplo : Este script utiliza la función len, que devuelve la longitud de una cadena. En este ejemplo, el script
    utiliza esa longitud para calcular un número, que estamos llamando al número de la suerte aquí. Y finalmente, imprime
    un mensaje con el nombre y el número."""

name = "Kay"
number = len(name) * 9

print("hello " + name + ". your lucky number is " + str(number))

name = "Cameron"
number = len(name) *9

print("hello " + name + " . Your lucky number is " + str(number))

"""¿Qué tal si reescribimos este código creando una función para agrupar todo el código duplicado?"""

def lucky_number(name):
    number = len(name) * 9
    print ("hello " + name + " . your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Caameron")
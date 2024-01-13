"""
Revisión: lectura de datos de forma interactiva

 Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar su
 ejecución y pueden usarse como referencia para consultar.
"""
# cat hello.py
# !/usr/bin/env python3

name = input("Please enter your name: ")
print("Hello, " + name)

# ./hello.py
# Please enter your name: Roger
# Output will be Hello, Roger

# def to_seconds(hours, minutes, seconds):
#   return hours * 3600 + minutes * 60 + seconds


# print("Welcome to this time converter")

# cont = "y"

# while (cont.lower() == "y"):
#   hours = int(input("Enter the number of hours: "))
#   minutes = int(input("Enter the number of minutes: "))
#   seconds = int(input("Enter the number of seconds: "))

#   print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
#    print()
#   cont = input("Do you want to do another conversion? [y to continue] ")

# print("Goodbye!")

# Acerca de este código
# Para ver cómo funciona el código anterior, cópielo y péguelo en un Colab Notebook en
# https://colab.sandbox.google.com/

# ./seconds.py
# Welcome to this time converter
# Enter the number of hours: 1
# Enter the number of minutes: 2
# Enter the number of seconds: 3

# Do you want to do another conversion? [y to continue] y
# Enter the number of hours: 3
# Enter the number of minutes: 2
# Enter the number of seconds: 1
#
# Do you want to do another conversion? [y to continue] n

# Qué línea de código del script segundos.py convertirá todas las entradas de números enteros en segundos?

# R to_segundos(horas, minutos, segundos)

"""
Revisión: transmisiones estándar

Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar 
su ejecución y pueden usarse como referencia para consultar. 
cat streams.py
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)

./streams.py 
This will come from STDIN: Python Rocks!
Now we write it to STDOUT: Python Rocks!

cat greeting.txt 
Well hello there, STDOUT

cat greeting.txt 
Well hello there, STDOUT

ls -z

cat streams.py
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)

./streams.py 
This will come from STDIN: Python Rocks!
Now we write it to STDOUT: Python Rocks!

cat greeting.txt 
Well hello there, STDOUT

cat greeting.txt 
Well hello there, STDOUT

ls -z

Revisión: variables de entorno

Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar su 
ejecución y pueden usarse como referencia para consultar. 

echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cat variables.py
#!/usr/bin/env python3
import os
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
./variables.py
export FRUIT=Pineapple
./variables.py


Revisión: argumentos de la línea de comandos y estado de salida

 Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar su 
 ejecución y pueden usarse como referencia para consultar. 
 
 cat parameters.py 
#!/usr/bin/env python3
import sys
print(sys.argv)

./parameters.py
['./parameters.py'] 

./parameters.py one two three
['./parameters.py', 'one', 'two', 'three']


wc variables.py
7 19 174 variables.py 	
echo $?
0

wc not-present.sh
wc: not-present.sh: No such file or directory
echo $?
1

#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)

./create_file.py example
echo $?
0

cat example 
New file created
./create_file.py example
Error, the file example already exists!
echo $?
1 
Más acerca de las funciones de entrada

Ahora, habrás notado que la mayoría de los ejemplos de código Python que hemos usado incluyen la línea 

#!/usr/bin/env python3

Ahora bien, esto es importante porque establece la versión de Python en Python 3.

Existen algunas diferencias sutiles en cómo se manejan los flujos de datos en Python 3 y versiones anteriores, 
como Python 2. Centrémonos únicamente en input() y raw_input(), porque funcionan de manera diferente en Python 2 y 3, 
y usted querrá use uno u otro dependiendo de la versión de Python.

En Python 2
Tomando una entrada de un usuario, se debe usar raw_input:

>>> my_number = raw_input('Please Enter a Number: \n')
Please Enter a Number:
1337
>>> print(my_number)
1337
>>>

Ahora bien, esto es importante porque raw_input no evalúa una expresión de Python que de otro modo sería válida. 
En términos simples, raw_input simplemente obtendrá una cadena de un usuario, donde la entrada realmente realizará 
operaciones matemáticas básicas y similares. Vea abajo:

>>> my_raw_input = raw_input('Please Enter a Number: \n')
Please Enter a Number:
123 + 1# This is treated like a raw string.
>>> my_input = input('Please Enter a Number: \n')
Please Enter a Number:
123 + 1 # This is treated like an expression.
>>> print(my_raw_input)
123 + 1
>>> print(my_input)
124 # See that the expression was evaluated!

En Python 2, input(x) es simplemente eval(raw_input(x)). eval() simplemente evaluará una cadena genérica como si 
fuera una expresión de Python.

En Python 3
Al tomar una entrada de un usuario, se debe utilizar la entrada. Vea el siguiente ejemplo:

>>> my_number = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1
>>> print(my_number)
123 + 1
>>> type(my_number)
<class 'str'>

Observe que la expresión se trata como una cadena. No se evalúa. Si queremos, podemos llamar a eval() y eso realmente 
ejecutará la cadena como una expresión:

>>> my_number = input('Please Enter a Number: \n')
Please Enter a Number:
123 + 1
>>> print(my_number)
123 + 1
>>> eval(my_number)
124

finalmente, vale la pena señalar que raw_input no existe de forma nativa en Python 3, pero existen algunas formas complicadas de obligar al intérprete a evaluar raw_input de manera compatible con versiones anteriores. Esto puede resultar útil para modernizar el código Python heredado sin reescribir grandes partes del mismo. Es mejor dejar la investigación sobre este tema en manos del lector, ya que hay muchas formas divertidas (y a veces aterradoras) de hacerlo.

Resumen
Python 2 y Python 3 manejan la entrada y raw_input de manera diferente.

En Python 2

input(x) es más o menos lo mismo que eval(raw_input(x))

Se prefiere raw_input(), a menos que el autor quiera admitir la evaluación de expresiones de cadena.

eval() se utiliza para evaluar expresiones de cadena.

Documentos de biblioteca estándar:

https://docs.python.org/2/library/functions.html#input

https://docs.python.org/2/library/functions.html#raw_input

https://docs.python.org/2/library/functions.html#eval

En Python 3

La entrada maneja la cadena como una cadena genérica. No evalúa la cadena como una expresión de cadena.

raw_input no existe, pero con algunas técnicas complicadas se puede soportar.

eval() se puede utilizar igual que Python 2.

Documentos de biblioteca estándar: 

https://docs.python.org/3/library/functions.html#input

https://docs.python.org/3/library/functions.html#eval

"""

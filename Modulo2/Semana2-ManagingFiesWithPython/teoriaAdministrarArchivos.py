"""
Revisión: lectura de archivos

Introducción

Esta lectura de seguimiento está organizada para que coincida con el contenido del vídeo que sigue. Contiene el mismo
código que se muestra en el siguiente vídeo. Estos bloques de código le brindarán la oportunidad de ver cómo está
escrito el código, le permitirán practicar su ejecución y pueden usarse como referencia para consultar.

Puede seguir la lectura mientras el instructor analiza el código o revisar el código después de ver el video.

archivo = abrir("spider.txt")

Acerca de este código
Esta línea abre el archivo spider.txt en modo lectura. La función open() devuelve un objeto de archivo que se asigna a
la variable archivo .
"""
file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()

"""Acerca de este código 
Estas líneas imprimen las primeras tres líneas del archivo. El método readline() lee una línea del archivo y la 
devuelve como una cadena. El método read() lee el archivo completo y lo devuelve como una cadena. El método close() 
cierra el archivo.
"""
file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()
with open("spider.txt") as file:
    print(file.readline())

""""
¿Cuál es la diferencia entre los métodos readline() y read()?
El método readline() lee una sola línea desde la posición actual, el método read() lee desde la posición actual hasta 
el final del archivo.
"""

"""
Revisión: iteración a través de archivos
Introducción
Esta lectura de seguimiento está organizada para que coincida con el contenido del vídeo que sigue. Contiene el mismo 
código que se muestra en el siguiente vídeo. Estos bloques de código le brindarán la oportunidad de ver cómo está 
escrito el código, le permitirán practicar su ejecución y pueden usarse como referencia para consultar. 

Puede seguir la lectura mientras el instructor analiza el código o revisar el código después de ver el video.
"""

with open("spider.txt") as file:
    for line in file:
        print(line.upper())

"""
Acerca de este código

Salida de código: 

LA ARAÑA PEQUEÑA SUBIÓ A LA TROMBARA.

ABAJO LA LLUVIA

Y LAVÓ LA ARAÑA.

SALIÓ EL SOL

Y SE SECA TODA LA LLUVIA

Y LA ARAÑA PEQUEÑA SUBió DE NUEVO POR EL CAÑO.

Aquí hay espacios entre las líneas en la salida. Esto se debe a que hay un carácter de nueva línea 
al final de cada línea. 
"""

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

"""
Acerca de este código

Salida de código: 

LA ARAÑA PEQUEÑA SUBIÓ A LA TROMBARA.

ABAJO LA LLUVIA

Y LAVÓ LA ARAÑA.

SALIÓ EL SOL

Y SE SECA TODA LA LLUVIA

Y LA ARAÑA PEQUEÑA SUBió DE NUEVO POR EL CAÑO.

Aquí, la tira se usa para eliminar el carácter de nueva línea y obtenemos el resultado sin líneas vacías.
"""

file = open("spider.txt")
lines = file.readlines()
lines.sort()
print(lines)

"""
Acerca de este código

Salida del código: ['Cayó la lluvia\n', 'Salió el sol\n', 'La pequeña araña trepó por la tromba marina.\n', 'y secó 
toda la lluvia\n', 'y el Su diminuta araña subió de nuevo por el pico.\n', 'y lavó la araña.\n'] 

Aquí, las líneas se han ordenado alfabéticamente, por lo que ya no están en el orden en que estaban en el archivo. 
Podemos ver que Python muestra un carácter de nueva línea usando el símbolo "\n" al imprimir una lista de cadenas. 
Esta es una forma de mostrar explícitamente que hay un carácter de nueva línea en esas cadenas. Esto muestra un 
carácter que no se puede imprimir; Python usa secuencias de escape con barra invertida, como \n. Otra secuencia de 
escape común es \t, para tabulación.

"""
# ¿Puedes identificar qué fragmento de código abrirá correctamente un archivo e imprimirá líneas una por una sin
# espacios en blanco?

with open("hello_world.txt") as text:
    for line in text:
        print(line.strip())

"""
Revisión: escritura de archivos

Introducción
Esta lectura de seguimiento está organizada para que coincida con el contenido del vídeo que sigue. Contiene el mismo 
código que se muestra en el siguiente vídeo. Estos bloques de código le brindarán la oportunidad de ver cómo está 
escrito el código, le permitirán practicar su ejecución y pueden usarse como referencia para consultar. 

Puede seguir la lectura mientras el instructor analiza el código o revisar el código después de ver el video.
"""

with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

"""
Acerca de este código
La instrucción with open() crea un objeto de archivo y lo asigna al archivo variable. La función open() toma 
dos argumentos: el nombre del archivo y el modo. En este caso, el modo es w, que significa "escribir". 
Esto le dice a la función open() que cree un nuevo archivo si no existe, o que sobrescriba 
el archivo existente si existe.

El método write() del objeto de archivo toma una cadena como argumento y escribe la cadena en el archivo. En este caso, 
la cadena es "Era una noche oscura y tormentosa".

¿Qué sucede con el contenido anterior de un archivo cuando lo abrimos usando "w" (modo "escritura")?

R Los contenidos antiguos se eliminan tan pronto como abrimos el archivo.


"""
# ¿Cuál de las siguientes demuestra cómo se pueden utilizar las expresiones regulares (expresiones regulares)?
# R Encuentra cadenas de texto que coincidan con un patrón

# ¿Por qué utilizar expresiones regulares?
# Introducción
# Esta lectura de seguimiento está organizada para que coincida con el contenido del vídeo que sigue.
# Contiene el mismo código que se muestra en el siguiente vídeo. Estos bloques de código le brindarán
# la oportunidad de ver cómo está escrito el código, le permitirán practicar su ejecución y pueden usarse
# como referencia para consultar.

# Puede seguir la lectura mientras el instructor analiza el código o revisar el código después de ver el video.

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index + 1:index + 6])

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# Acerca de este código

# Aquí se usa el módulo re que nos permite usar la función de búsqueda para encontrar expresiones regulares dentro
# de cadenas. Luego, se define una expresión regular r"|[(\d+)\]", que coincide con una cadena encerrada entre
# corchetes seguida de uno o más dígitos. Luego, utiliza la función re.search() para buscar en el registro
# de cadenas una coincidencia con la expresión regular. La función re.search() devuelve un objeto Match si se
# encuentra una coincidencia, o Ninguno si no se encuentra ninguna coincidencia. la función re.search() devuelve un
# objeto Match porque el registro de cadena contiene una coincidencia con la expresión regular. El objeto Match
# tiene un método group() que devuelve los grupos capturados de la coincidencia. En este caso, el único grupo
# capturado es el número, que devuelve la expresión resultado[1].

# En lugar de utilizar la función index() del módulo de cadena, podemos utilizar expresiones regulares,
# que son más flexibles. Después de importar el módulo de expresión regular re, ¿qué función de expresión regular
# podría usarse en lugar de los métodos estándar?

# R re.search()

# Usando la terminal, ¿cuál de los siguientes comandos usará correctamente grep para encontrar las palabras
# “sling” y “sting” (suponiendo que estén en nuestro archivo, file.txt)?

# R user@ubuntu:~$ grep s.ing /usr/file.txt

# Una cosa que recordar que el circumplejo y el signo del dolar coinciden específicamente con el inicio y el final
# de la línea, no con una cadena

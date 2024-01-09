# Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar su
# ejecución y pueden usarse como referencia para consultar.

import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])

import re


def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


rearrange_name("Lovelace, Ada")

import re


def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


rearrange_name("Ritchie, Dennis")

import re


def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


rearrange_name("Hopper, Grace M.")

import re


def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


name = rearrange_name("Kennedy, John F.")
print(name)

# Corrija la expresión regular utilizada en la función rerange_name para que pueda coincidir con segundos nombres,
# iniciales del segundo nombre y apellidos dobles.

import re


def rearrange_name(name):
    result = re.search(r"^([\w -]+), ([\w .]+)$", name)
    if result is None:
        return name
    return "{} {}".format(result.group(2), result.group(1))


name = rearrange_name("Kennedy, John F.")
print(name)

# Revisión: Más sobre las eliminatorias de repetición

# Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar su
# ejecución y pueden usarse como referencia para consultar.

import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))

import re

print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

import re

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

import re

re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")

import re

print(re.findall(r"\w{5,}", "I really like strawberries"))

import re

print(re.search(r"s\w{,20}", "I really like strawberries"))

# La función long_words devuelve todas las palabras que tengan al menos 7 caracteres. Complete la expresión regular
# para completar esta función.

# Revisión: Extracción de un PID usando expresiones regulares en PythonRevisión: Extracción de un PID usando
# expresiones regulares en Python

#  Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar
#  su ejecución y pueden usarse como referencia para consultar.

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
if result:
    print(result[1])
result = re.search(regex, "A completely different string that also has numbers [34567]")
if result:
    print(result[1])
result = re.search(regex, "99 elephants in a [cage]")
if result:
    print(result[1])
# Note that this print command results in an error as shown in the video.

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")


def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]


import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")


def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]


print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))

print(extract_pid(log))

# Agregue a la expresión regular utilizada en la función extract_pid, para devolver el mensaje en mayúsculas entre
# paréntesis, después de la identificación del proceso.

import re


def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result.group(1), result.group(2))


print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))  # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]"))  # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message"))  # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))  # 67890 (RUNNING)

# Revisión: dividir y reemplazar
# Estos bloques de código le brindarán la oportunidad de ver cómo está escrito el código, le permitirán practicar su
# ejecución y pueden usarse como referencia para consultar.

import re

re.split(r"[.?!]", "One sentence. Another one? And the last one!")

# ['One sentence', ' Another one', ' And the last one', '']

import re

re.split(r"([.?!])", "One sentence. Another one? And the last one!")

# ['One sentence', '.', 'Another one', '?', 'And the last one', '!', '']

import re

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")

# Received an email for [REDACTED]

import re

re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")

# Ada Lovelace

# Queremos dividir un fragmento de texto por la palabra "a" o "el", como se implementa en el siguiente código.
# ¿Cuál es la lista dividida resultante?

re.split(r"the|a", "One sentence. Another one? And the last one!")

# ['One sentence. Ano', 'r one? And ', ' l', 'st one!']

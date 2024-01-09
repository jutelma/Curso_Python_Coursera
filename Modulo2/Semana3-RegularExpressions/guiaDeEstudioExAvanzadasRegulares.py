"""
Guía de estudio: expresiones regulares avanzadas

Los desarrolladores utilizan expresiones regulares avanzadas, comúnmente denominadas expresiones regulares avanzadas,
para ejecutar coincidencias de patrones complicadas con cadenas. En esta lectura, aprenderá sobre algunos de los ejemplos comunes de expresiones regulares avanzadas.

Alteraciones
Una alteración coincide con cualquiera de las alternativas separadas por la tubería | símbolo. Veamos un ejemplo:

 r"ubicación.*(Londres|Berlín|Madrid)"

Esta línea de código coincidirá. La ubicación del curso es Londres.

Coincidir solo al principio o al final.
Si usa el símbolo circunflejo (también conocido como símbolo de intercalación) ^ como primer carácter de su expresión
regular, coincidirá solo si el patrón ocurre al comienzo de la cadena. Alternativamente, si usa el símbolo del signo
de dólar $ al final de una expresión regular, coincidirá solo si el patrón ocurre al final. Veamos un ejemplo:

r”^Mi nombre es (\w+)”

Esta línea de código coincidirá con Mi nombre es Asha pero no con Hola. Mi nombre es Asha.

Rangos de caracteres
Los rangos de caracteres se pueden utilizar para hacer coincidir un solo carácter con un conjunto de posibilidades.
Veamos un par de ejemplos:

r”[AZ] Esto coincidirá con una sola letra mayúscula.

r”[0-9$-,.] Esto coincidirá con cualquiera de los dígitos del cero al nueve, o el signo de dólar, guión, coma o punto.

Los dos ejemplos anteriores suelen combinarse con los calificadores de repetición. Veamos un ejemplo más:

r”([0-9]{3}-[0-9]{3}-[0-9]{4})”

Esta línea de código coincidirá con un número de teléfono de EE. UU., como 888-123-7612 .

Referencias anteriores
Se utiliza una referencia inversa cuando se usa re.sub() para sustituir el valor de un grupo de captura en la salida.
Veamos un ejemplo:

>>> re.sub(r”([AZ])\.\s+(\w+)”, r”Sra. \2”, “A. Weber y B. Bellmas se han unido al equipo.”)

Esta línea de código producirá que la Sra. Weber y la Sra. Bellmas se unan al equipo .

Mirar hacia el futuro
Una anticipación coincide con un patrón solo si va seguida de otro patrón. Veamos un ejemplo:

Si la expresión regular fuera r”(Prueba\d)-(?=Aprobada)” y la cadena fuera “Prueba1-Pasada, Prueba2-Pasada,
Prueba3-Falla, Prueba4-Pasada, Prueba5-Falla”, el resultado sería:

Prueba1, Prueba2, Prueba4

Conclusiones clave
Los tipos de expresiones regulares avanzadas que se explican en esta lectura son solo algunas de las más utilizadas
por los desarrolladores. Son beneficiosos para la coincidencia de patrones, la manipulación de texto y la validación de datos. Para obtener más información, consulte el siguiente enlace:

https://regexcrossword.com/


"""
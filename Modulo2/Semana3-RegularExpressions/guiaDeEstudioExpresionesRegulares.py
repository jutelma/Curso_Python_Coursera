"""
Guía de estudio: expresiones regulares

Una expresión regular, a veces llamada expresión regular, es una cadena de caracteres que especifica un patrón
para compararlo con algún texto. Además de hacer coincidir patrones, pueden buscar para extraer partes específicas
de texto, validar datos de entrada y son compatibles con editores de código y entornos de desarrollo integrados
(IDE). En esta lectura, verá algunos ejemplos de expresiones regulares comunes utilizadas en la codificación.

Ejemplos de expresiones regulares

    r”\d{3}-\d{3}-\d{4}”   Esta línea de código coincide con números de teléfono de EE. UU. en el formato 111-222-3333.


    r”^-?\d*(\.\d+)?$”   Esta línea de código coincide con cualquier número positivo o negativo, con o sin decimales.


    r”/^(.+)/([^/]+)$/” Esta línea de código coincide con cualquier ruta y nombre de archivo.


Herramienta útil

A veces, las expresiones regulares pueden ser complejas y difíciles de leer y comprender, ¡incluso para programadores
experimentados! Hay herramientas disponibles para ayudar a desglosar la expresión regular y explicar qué hace cada
parte de la expresión. Una herramienta común que puede utilizar para comprender cada etapa de una expresión regular es:

https://regex101.com/

Conclusiones clave

Las expresiones regulares ofrecen potentes capacidades a los programadores pero, en ocasiones, pueden resultar
complejas y difíciles de entender. Cuanto más codifique con expresiones regulares, más cómodo se sentirá usándolas y
comprendiéndolas.

"""
"""
Guía de estudio: archivos .csv

El formato más común para importar y exportar datos para hojas de cálculo es el formato .csv . Un archivo de valores
separados por comas (.csv ) es un archivo de texto sin formato que utiliza (lo adivinó) comas para separar cada dato.
Es posible que ya esté familiarizado con los archivos .csv si ha guardado una hoja de cálculo en formato .csv .
A continuación se muestra un ejemplo sencillo de un archivo .csv que muestra información de los empleados:

    Nombre, Departamento, Salario

    Aisha Khan, Ingeniería, 80000

    Jules Lee, marketing, 67000

    Queenie Corbit, Recursos Humanos, 90000

Observe que cada fila representa la información de un empleado y los valores están separados por comas.

En esta lectura, examinará diferentes comandos para usar cuando trabaje con archivos .csv en Python y recibirá
enlaces adicionales para obtener más información.

Contenido del módulo

El módulo .csv es una funcionalidad integrada de Python que se utiliza para leer y trabajar con archivos .csv .
Veamos cómo el módulo .csv define algunas de estas funciones:

csv.reader Esta función devuelve un objeto lector que itera sobre líneas en el archivo .csv .

csv.writer Esta función devuelve un objeto escritor que es responsable de convertir los datos del usuario en cadenas
delimitadas en el objeto similar a un archivo determinado.

clase csv.DictReader Esta función crea un objeto que funciona como un lector normal, pero asigna la información de
cada fila a un diccionario cuyas claves están dadas por los parámetros de nombre de campo opcionales .

Dialectos y parámetros de formato.

Los dialectos son reglas que definen cómo se estructura un archivo .csv y se forman parámetros para controlar
el comportamiento del lector y escritor de .csv y vivir dentro de los dialectos. Los dialectos admiten
las siguientes funciones:

Dialect.delimiter Este atributo es una cadena de un carácter que se utiliza para separar campos y su valor
predeterminado es una coma.

Dialect.quotechar   Este atributo es una cadena de un carácter que se utiliza para citar campos que contienen
caracteres especiales y su valor predeterminado es ' '' '.

Dialect.strict   El valor predeterminado de este atributo es False, pero cuando es True , se generará la excepción
csv.Error si se detecta un error.

Objetos lectores

Un objeto lector contiene los siguientes métodos y atributos públicos:

csvreader._next_() Este método devuelve la siguiente fila del objeto iterable del lector como una lista o un
diccionario, analizado correctamente en el dialecto actual. Normalmente, lo llamarías siguiente (lector).

csvreader.dialect Este atributo es una descripción de sólo lectura del dialecto utilizado por el analizador.

Objetos del escritor

Los objetos de escritura le brindan la capacidad de escribir datos en un archivo .csv . Veamos un par de métodos y
atributos públicos para objetos de escritura:

csvwriter.writerows(rows) Este método escribe todos los elementos en filas en el objeto de archivo del escritor
y los formatea siguiendo el dialecto actual.

csvwriter.dialect Este atributo es una descripción de solo lectura del dialecto que utiliza el escritor.

Conclusiones clave
Si aún no has trabajado con archivos .csv , es sólo cuestión de tiempo. Familiarícese con los objetos de lectura y
escritura del módulo .csv para trabajar de manera más eficiente con archivos .csv . Los módulos, características y
atributos de esta lectura son solo algunos de los comandos que se pueden utilizar al trabajar con archivos .csv .

"""
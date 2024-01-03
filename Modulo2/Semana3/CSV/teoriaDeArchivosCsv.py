"""
Revisión: lectura de archivos CSV
Introducción
Esta lectura de seguimiento está organizada para que coincida con el contenido del vídeo que sigue. Contiene
el mismo código que se muestra en el siguiente vídeo. Estos bloques de código le brindarán la oportunidad de ver
cómo está escrito el código, le permitirán practicar su ejecución y pueden usarse como referencia para consultar.

Puede seguir la lectura mientras el instructor analiza el código o revisar el código después de ver el video.
"""
import csv

f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()

"""
Acerca de este código
El código anterior leerá los datos del archivo CSV csv_file.txt e imprimirá la siguiente información para cada fila:

 · Nombre

 · Número de teléfono

 · Role

Salida de ejemplo:
Nombre: Sabrina Green, Teléfono: 802-867-5309, Función: Administrador del sistema

Nombre: Eli Jones, Teléfono: 684-3481127, Función: Especialista en TI

Nombre: Melody Daniels, Teléfono: 846-687-7436, Función: Programadora

Nombre: Charlie Rivera, Teléfono: 698-746-3357, Función: Desarrollador web

"""

# ¿Cuál de las siguientes debemos hacer antes de usar la función csv.writer()?
# R Abra el archivo con permisos de escritura.

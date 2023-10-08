"""
1 Completa el código para generar la declaración "192.168.1.10 es la dirección IP del servidor de impresora 1".
Recuerda que se debe utilizar una sintaxis precisa para recibir crédito
"""
IP_address = "192.168.1.10"
host_name = "Printer Server 1"
print(IP_address + " is the IP address of " + host_name)
# Should print "192.168.1.10 is the IP address of Printer Server 1"

"""
2 ¿Cual es el valor de esta expresion de python : 7 < "number"?

R TypeError
La expresión 7 < "number" en Python producirá un error de tipo TypeError. Esto se debe a que estás intentando comparar 
un número (7) con una cadena de texto ("number"), lo cual no es una comparación válida en términos de tipos de datos.

3 ¿Para que se utiliza la palabra elif?

R La palabra clave elif en Python se utiliza para agregar una condición adicional 
en una estructura condicional que ya contiene un if. elif significa "else if" en inglés, lo que indica que es una 
alternativa a la condición del if.

4 Considere el siguiente escenario sobre el uso de declaraciones if-elif-else:
Los estudiantes de una clase reciben sus calificaciones como Aprobado/Reprobado. Las puntuaciones de 60 o más 
(sobre 100) significan que la calificación es "Aprobado". Para puntuaciones más bajas, la calificación es "Suspendido".
Además las puntuaciones superiores a 95 (no incluidas) se califican Como "Puntuación máxima".
Completa los espacios en blancos en esta función para que devuelva la calificación apropiada de "Aprobado", "Reprobado",
o "Puntuación máxima".   def exam_grade(score):

"""


def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade


print(exam_grade(65))  # Debe imprimir Aprobado
print(exam_grade(55))  # en caso de que la impresion falle
print(exam_grade(60))  # Debe imprimir Aprobado
print(exam_grade(95))  # Debe imprimir Aprobado
print(exam_grade(100))  # Debe imprimir la puntuacion mas alta
print(exam_grade(0))  # La impresion deberia fallar

"""
5 Cuando se utiliza una declaracion if, el codigo dentro del bloque if solo se ejecutara si la declaracion condicional 
devuelve ¿que?

R Cuando se utiliza una declaración if en Python, el código dentro del bloque if solo se ejecutará si la condición 
(la expresión booleana) dentro de los paréntesis es evaluada como True.

Si la condición es evaluada como False, el código dentro del bloque if será omitido y el flujo del programa continuará 
con las instrucciones después del bloque if, si las hay.

Por lo tanto, para que el código dentro de un bloque if se ejecute, la condición debe ser verdadera (True). Si es falsa 
(False), el código dentro del bloque if se salta y el programa continúa con las instrucciones siguientes, si las hay.

6 Complete los espacios en blanco para completar la funcion. La funcion "identificar_IP" recibe una "direccion _IP"  
como una cadena atravez de los parametros de la funsion, luego deberia imprimir una descripsion de la direccion IP.
Actulmente, la funsion solo deberia admitir tres direcciones Ip y devolver "desconocido" para todas la demas IP.

"""


def identify_ip(ip_address):
    if ip_address == "192.168.1.1":
        ip_description = "Network router"
    elif ip_address == "8.8.8.8" or IP_address == "8.8.4.4":
        ip_description = "Google DNS server"
    elif ip_address == "142.250.191.46":
        ip_description = "Google.com"
    else:
        ip_description = "unknown"
    return ip_description


print(identify_ip("8.8.4.4"))  # Debe imprimir'Google DNS server'
print(identify_ip("142.250.191.46"))  # Debe imprimir 'Google.com'
print(identify_ip("192.168.1.1"))  # Debe imprimir'  'Network router'
print(identify_ip("8.8.8.8"))  # Debe imprimir' 'Google DNS server'
print(identify_ip("10.10.10.10"))  # Debe imprimir' 'unknown'
print(identify_ip(""))  # Deberia imprimir''unknown'

"""
7 ¿Puedes calcular el resultado de este código?

"""


def greater_value(x, y):
    if x > y:
        return x
    else:
        return y


print(greater_value(10, 3 * 5))

# R  15

"""
8 Cual es el valor de esta expresion de python ?
  
((24 ==  5*2)  and  (24  > 3*5)  and  (2*6 == 12)) 

False and False and True:

Cuando utilizamos el operador and, todas las partes deben ser True para que la expresión completa sea True. En este 
caso, la expresión completa es False.

9 Complete los espacios en blanco para completar la funsion. La funcion "make_positive" toma un numero y lo convierte 
en un equivalente positivo. Complete la funcion para  realizar las siguientes tareas :   
    · use una declaracion if para probar si el numero es negativo,  
    · use un calculo dentro de la declaracion if para cambiar el numero negativo para que sea positivo,  
    · utiloice un calculo en la declaracion else para devolver cualquier "numero" positivo sin cambios


"""


def make_positive(number):
    if number < 0:
        result = number * -1
    else:
        result = number
    return result


print(make_positive(-4))  # Deberia imprimir 4
print(make_positive(0))  # Deberia imprimir 0
print(make_positive(-.25))  # Deberia imprimir 0.25
print(make_positive(5))  # Deberia imprimir 5

"""
10 gitCuales de los siguientes son buenos habitos de estilo de codificacion? 

Refactorizando el codigo.
Agregar comentarios.
limpiar codigo duplicado creando una funcion que se pueda reutilizar.

"""
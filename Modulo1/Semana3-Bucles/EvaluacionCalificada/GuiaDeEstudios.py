# Guía de estudio: Prueba calificada del Módulo 3
"""
Es hora de prepararse para el cuestionario calificado del Módulo 3. Revise los siguientes elementos de este módulo
antes de comenzar el cuestionario calificado del Módulo 3. Si desea refrescar su memoria sobre estos materiales, vuelva
a visitar también elmientras Guía de estudio de bucley elpara Guía de estudio de bucle
ubicado antes de las Pruebas de práctica en el Módulo 3. No se le evaluará el contenido de la lección de Recursión,
que es opcional en este módulo.

Conocimiento

Términos

    · variables : sepa cómo inicializar o incrementar correctamente una variable. También deberá reconocer un error de
      codificación debido a no inicializar o incrementar correctamente una variable.

    · Bucles infinitos : sepa reconocer bucles infinitos y utilice soluciones comunes para evitarlos. Por ejemplo,
      verifique las condiciones del bucle, rangos, iteradores, declaraciones de control, etc. para asegurarse de que al
      menos uno de estos controles esté implementado para evitar un bucle infinito.

    · iteradores : conozca las diversas opciones disponibles para iterar una variable (por ejemplo, usar operadores de
      asignación, usar el tercer parámetro de función range() ). También necesitarás analizar dónde debería ocurrir la
      iteración. Un iterador mal colocado podría producir una salida incorrecta o crear un bucle infinito.

    · declaraciones de control : sepa cómo y cuándo usar las declaraciones de control break y continue para evitar
      bucles infinitos.


Funciones comunes

    · Parámetros de la función range() : conozca las funciones de los tres posibles parámetros de la f
      unción range(x, y, z) :

        · x Inicio de Rango (incluido)

        · y Fin del rango (índice excluido)

            · Para incluir el índice de fin de rango, use la expresión y+1

            · El final del rango debe incluirse en los parámetros del rango() .

        · Valor incremental

        · Ejemplo 1: rango(4, 12 +1 , 2 )

            · Este ejemplo crea un rango que comienza en 4 y termina en 12 (sin +1 , el rango terminaría en 11).

            · El tercer parámetro incrementa la iteración del rango en 2, a diferencia del incremento predeterminado
              de 1. La   expresión rango(4, 12+1, 2) produciría los valores: 4, 6, 8, 10, 12

        · Ejemplo 2: rango(10, 2 -1 , -2 )

            · Este ejemplo crea un rango que comienza en 10 y termina en 2 -1 , con un valor decremental de -2 .
            Al realizar la cuenta atrás, para incluir el valor del índice de final del rango, utilice -1
            (fin del rango menos 1). Este rango produce la secuencia: 10, 8, 6, 4, 2


    · Comportamiento predeterminado de la función print() : conozca que el comportamiento predeterminado
      de la función print() es insertar un carácter de nueva línea después de que se ejecuta la declaración de
      impresión.

        · Para anular la inserción del carácter de nueva línea y reemplazarlo con un espacio, agregue end=" "
        como último elemento en los parámetros print() . Esto hace posible agregar la siguiente salida de impresión a
        la misma línea, separada por un espacio. Puede utilizar esta técnica cuando una función print() sea parte
        de un bucle for o while . Sintaxis de ejemplo:   print(x+1, end=" ")

Habilidades de codificación

Habilidad 1: Usar bucles for con la función range()

    · Utilice un bucle for con la función range() con el valor de fin de rango incluido en el rango.

"""


# Esta función aceptará una variable entera "fin" y contará de 10 en 10
# de 0 al valor "final".
def count_by_10(end):
    # Inicializaq la variable "count" como una cadena.
    count = ""

    # Los parámetros de la función de rango le indican a Python que inicie el conteo
    # en 0 y se detiene en la variable dada como el extremo superior del rango.
    # Dado que el valor del extremo superior de un rango está excluido de forma predeterminada,
    # puedes hacer que Python incluya el valor "final" añadiéndole +1.
    # El tercer parámetro le dice a Python que incremente el recuento en 10.
    for number in range(0, end + 1, 10):
        # Aunque la variable "count" contendrá un recuento de números enteros,
        # este ejemplo se convertirá en una cadena usando "str(número)"
        # para mostrar el conteo incremental desde 0 hasta el "final"
        # valor en la misma línea con un espacio " " separando cada uno
        # número.
        count += str(number) + " "

    # El método .strip() recortará el espacio final " " desde el final de
    # la cadena "cuenta"
    return count.strip()


# Llame a la función con 1 parámetro entero.
print(count_by_10(100))
# Debe imprimir 0 10 20 30 40 50 60 70 80 90 100

"""
    · Utilice un conjunto de bucles for anidados con la función range() para crear una matriz de números. 

    · Incluya el valor del rango superior en la función range() usando end+1.
"""


# Esta función utiliza un conjunto de bucles for anidados con la función range()
# para crear una matriz de números. El valor del rango superior en el rango()
# función debe incluirse en la matriz. La matriz debe consistir
# de un conjunto de números que llenan tanto filas como columnas.
def matrix(initial_number, end_of_first_row):
    # Es un estilo de código opcional para asignar los nombres largos de las variables en el
    # parámetros de función a nombres de variables más cortos.
    n1 = initial_number
    n2 = end_of_first_row + 1  # incluir el valor del rango superior con +1

    # El primer bucle for creará las columnas.
    for column in range(n1, n2):

        # El bucle for anidado creará las filas.
        for row in range(n1, n2):
            # Para que la matriz de números sea más fácil de leer, incluya un espacio
            # entre cada número en las filas hasta que el bucle llegue al
            # final de la fila. Puede anular el comportamiento predeterminado del
            # función print() (que inserta un carácter de nueva línea después
            # se ejecuta el comando de impresión) utilizando el parámetro "end=" "
            # dentro de la función print().
            print(column * row, end=" ")

        # La fila termina cuando se encuentra el valor del rango superior dentro del
        # bucle for anidado. El bucle for externo (columna) debe insertar una nueva línea
        # para crear la siguiente fila. Utilice la función print() nueva línea predeterminada
        # comportamiento con una función print() vacía:
        print()


# Llame a la función con 2 parámetros enteros.
matrix(1, 4)
# Should print:
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16
"""
    · Predice el valor final de un bucle for anidado con funciones range() . 
"""

# Para este ejemplo, el bucle for externo utiliza un índice de fin de rango de
# 10. El valor del índice 10 será 10-1 o 9.
for outer_loop in range(10):

    # Usar la variable "outer_loop" como final del rango para el
    # bucle interno, significa que el índice de final de rango será 9. El valor
    # El número de índice 9 será 9 - 1 u 8
    for inner_loop in range(outer_loop):
        # El resultado impreso es el valor de "inner_loop". Desde
        # no hay ningún cálculo en este bucle, hay un
        # atajo simple para resolver cuál fue el valor final impreso
        # por el "inner_loop" será. La solución es simplemente usar
        # el valor del índice "inner_loop", que es 8.
        print(inner_loop)

"""
   · Encuentre y corrija un error en un bucle for con la función range() .  
"""

# Esta función debe realizar una cuenta regresiva de -2 del 11 al 1, de modo que solo
# imprime números impares.

# Este rango (11, -2) le dice al bucle for que comience en 11 y termine en el índice
# posición -2 (que corresponde al valor numérico de -1). Desde la
# falta el tercer valor incremental o decremental, el bucle
# incremento por defecto de +1 en lugar del decremento previsto de -2.
# Comenzando en la posición de índice 11 e incrementando en +1 finalizará el ciclo
# automáticamente, porque el índice no cuenta atrás hacia -2 como
# el final del rango.

# Para solucionar este problema, range() necesita tres parámetros:
# El primer parámetro debe ser la posición de índice inicial de 11.
# El segundo parámetro debe ser la posición de índice final de 0 (valor 1).
# El tercer parámetro debería disminuir en -2.
# Entonces, el rango debe configurarse como rango (11, 0, -2).

# Corrija este bucle con los parámetros de rango corregidos y haga clic en Ejecutar.
for n in range(11, -2):
    if n % 2 != 0:
        print(n, end=" ")

# Debería imprimir: 11, 9, 7, 5, 3, 1 una vez que se solucione el problema.

"""
Habilidad 2: usar bucles while

    · Utilice un bucle while para imprimir una secuencia de números.
"""
# Para este ejemplo, el bucle while hará una cuenta regresiva de tres en tres comenzando
# desde 18 y terminando en 0.
starting_number = 18

# El bucle while continuará hasta llegar a 0.
while starting_number >= 0:
    # Para facilitar la lectura de la secuencia de números, incluya un espacio
    # entre cada número de la secuencia. Puedes anular el valor predeterminado
    # comportamiento de la función print() usando el parámetro "end=" con
    # la función imprimir(). La sintaxis para agregar un espacio es: end=" "
    print(starting_number, end=" ")

    # Disminuir la variable "número_inicial" en -3.
    starting_number -= 3

# Debería imprimir 18 15 12 9 6 3 0

"""
    · Utilice un bucle while para contar el número de dígitos en un valor numérico 
"""


# Esta función acepta el salario de un CEO como variable.
# Cuenta el número de dígitos del salario y
# devuelve la oración como:
# "El CEO tiene un salario de 6 cifras."
def X_figure(salary):
    # Inicializa el contador como un número entero.
    tally = 0

    # La sentencia if comprueba si la variable "salario"
    # es igual a 0.
    if salary == 0:
        # Si es verdadero, entonces incrementa el contador a
        # muestra que hay 1 dígito en 0.
        tally += 1

    # El bucle while comienza a ejecutarse mientras el "salario"
    # es mayor o igual a 1 (el bucle
    # no se ejecuta si el "salario" es 0).
    while salary >= 1:
        # El cuerpo del bucle while cuenta los dígitos
        # en "salario" contando el número de veces
        # "salario" se puede dividir por 10 hasta "salario"
        # ya no es >= 1.
        salary = salary / 10

        # Suma 1 al contador para contar el número de
        # veces que se ejecuta el bucle.
        tally += 1

    # Devolver los resultados del "recuento" del número
    # de dígitos en "salario".
    return tally


# Llame a la función X_figure con 1 parámetro, convertida en una cadena,
# dentro de una función de impresión con cadenas adicionales.
print("The CEO has a " + str(X_figure(2300000)) + "-figure salary.")

# Debería imprimirse "El CEO tiene un salario de 7 cifras".

"""
Habilidad 3: usar bucles while con declaraciones if-else

    · Utilice una función para aceptar dos números enteros variables. 

    · Utilice sentencias if-else anidadas y bucles while para contar hacia arriba o hacia atrás desde la primera 
      variable hasta la segunda variable. 
 
"""


# Esta función aceptará dos variables enteras: el piso
# número que un pasajero "ingresa" a un ascensor y al piso
# número del pasajero del que va a "salir". Entonces, la función
# cuenta hacia arriba o hacia abajo desde los dos números del piso.
def elevator_floor(enter, exit):
    # La variable "piso" se utilizará como contador y para
    # imprimir los números de piso. La "dirección_elevador"
    # variable contendrá la cadena "Subiendo: " o
    # "Bajando: " más la cuenta ascendente o descendente del
    # números de "piso".
    floor = enter
    elevator_direction = ""

    # Si el pasajero entra al ascensor por un piso que
    # es más alto que el piso de destino:
    if enter > exit:

        # Entonces la cadena "elevator_direction" será
        # inicializado con la cadena "Bajando:".
        elevator_direction = "Going down: "

        # Mientras el número "piso" sea mayor o
        # igual al número del piso de salida:
        while floor >= exit:
            # El número del "piso" se convierte en una cadena
            # y se agrega a la variable de cadena
            # "dirección_ascensor".
            elevator_direction += str(floor)

            # Si el número "piso" sigue siendo mayor que
            # el número del piso de salida:
            if floor > exit:
                # Una tubería | Se añade un carácter entre cada uno.
                # Número de piso en la variable de cadena
                # "elevator_direction" para proporcionar una imagen
                # divisor entre números. La declaración si
                # arriba (si piso > salida) impide que la tubería
                # personaje que no aparece después del "suelo"
                # número ya no es mayor que la "salida"
                # variable.
                elevator_direction += " | "

            # Disminuir el número de "piso" como ascensor
            # baja.
            floor -= 1

    # De lo contrario, se da a entender que el pasajero está ingresando al
    # ascensor en un piso más bajo que el destino
    # piso.
    else:

        # Se inicializará la cadena "elevator_direction"
        # con la cadena "Subiendo:".
        elevator_direction = "Going up: "

        # Mientras que el número "piso" es menor o igual que el
        # número de piso de "salida":
        while floor <= exit:

            # Convierte el número del "piso" en una cadena y añade
            # a la variable de cadena "elevator_direction".
            elevator_direction += str(floor)

            # Si el número del piso de entrada es aún menor que el de salida
            # numero de piso:
            if floor < exit:
                # La pipa | Se añade un carácter entre cada uno.
                # Número de piso en la variable de cadena
                # "elevator_direction" para proporcionar una imagen
                # divisor entre números. La declaración si
                # arriba (si piso <salida) impide que la tubería
                # personaje que no aparece después del "suelo"
                # número ya no es menor que la "salida"
                # variable.
                elevator_direction += " | "

            # Incrementa el número del "piso" a medida que sube el ascensor.
            floor += 1

    # Devuelve la cadena que sostiene la dirección del ascensor (Bajando o
    # Subiendo) junto con la cuenta regresiva o ascendente del piso.
    return elevator_direction


# Llame a la función con 2 parámetros enteros.
print(elevator_floor(1, 4))  # Should print Going up: 1 | 2 | 3 | 4
print(elevator_floor(6, 2))  # Should print Going down: 6 | 5 | 4 | 3 | 2

"""
Recordatorio: la sintaxis correcta es fundamental

Usar una sintaxis precisa es fundamental al escribir código en cualquier lenguaje de programación, incluido Python. 
Incluso un pequeño error tipográfico puede causar un error de sintaxis y el evaluador automatizado de pruebas 
codificado en Python marcará su código como incorrecto. Esto refleja errores de codificación de la vida real en el 
sentido de que un solo error de ortografía, mayúsculas y minúsculas, puntuación, etc. puede provocar que el 
código falle. Los problemas de codificación causados ​​por una sintaxis imprecisa siempre serán un problema, 
ya sea que esté aprendiendo un lenguaje de programación o esté utilizando habilidades de programación en el trabajo. 
Por lo tanto, es fundamental adquirir el hábito de ser preciso en el código ahora. 

No se otorgará crédito si hay errores de codificación en las pruebas calificadas automáticamente, 
incluidos errores menores. Afortunadamente, tiene 3 oportunidades opcionales para volver a tomar las pruebas 
calificadas de este curso. Además, tiene repeticiones ilimitadas de cuestionarios de práctica y puede revisar 
los videos y las lecturas tantas veces como necesite para dominar los conceptos de este curso.  

Ahora, antes de comenzar la prueba calificada, revise esta lista de errores de sintaxis comunes que cometen los 
codificadores al escribir código.

Errores de sintaxis comunes:

    · Errores ortográficos

    · Sangrías incorrectas

    · Caracteres clave faltantes o incorrectos:

        · Tipos entre paréntesis: (curvo), [cuadrado], {rizado}

        · Tipos de cotizaciones: "recto-doble" o "recto-simple", "rizado-doble" o "rizado-simple"

        · Bloquear caracteres de introducción, como dos puntos:

    · No coinciden los tipos de datos

    · Palabras reservadas de Python faltantes, utilizadas incorrectamente o mal colocadas

    · Uso de mayúsculas y minúsculas incorrectas: Python es un lenguaje que distingue entre mayúsculas y minúsculas
     
"""

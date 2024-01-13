"""
Guía de estudio: subprocesos de Python

En Python, normalmente hay muchas formas diferentes de realizar la misma tarea. Algunos son más fáciles de escribir,
otros se adaptan mejor a una tarea determinada y otros tienen una sobrecarga menor en términos de la cantidad de
potencia informática utilizada. Los subprocesos son una forma de llamar y ejecutar otras aplicaciones desde Python,
incluidos otros scripts de Python. En Python, el módulo de subproceso puede ejecutar nuevos códigos y aplicaciones
iniciando los nuevos procesos desde el programa Python. Debido a que el subproceso le permite generar nuevos procesos,
es una forma muy útil de ejecutar múltiples procesos en paralelo en lugar de secuencialmente.

El subproceso de Python puede iniciar procesos para:

    · Abra varios archivos de datos en una carpeta simultáneamente.

    · Ejecute programas externos.

    · Conéctese a canales de entrada, salida y error y obtenga códigos de retorno.

Comparación de subprocesos con OS y Pathlib

Nuevamente, Python tiene múltiples formas de realizar la mayoría de las tareas; El subproceso es extremadamente
poderoso, ya que le permite hacer cualquier cosa que haría desde Python en el shell y recuperar información en Python.
Pero sólo porque puedas usar el subproceso no siempre significa que querrás hacerlo.

Comparemos el subproceso con dos de sus alternativas: OS, que se ha tratado en otras lecturas, y Pathlib. Para tareas
como obtener el directorio de trabajo actual o crear un directorio, OS y Pathlib son más directos (o "Pythonic",
lo que significa que usa el lenguaje como estaba previsto). Usar subprocesos para tareas como estas es como usar
una palanca para abrir una nuez. Es más resistente y puede resultar excesivo para operaciones simples.

Como ejemplo comparativo, los siguientes comandos realizan exactamente las mismas tareas de obtener el directorio de
trabajo actual.

Subproceso:

cwd_subprocess = subproceso.check_output(['pwd'], texto=True).strip()

TÚ:

cwd_os = os.getcwd()

Ruta de acceso:

cwd_pathlib = Ruta.cwd()

Y los siguientes comandos realizan exactamente las mismas tareas de crear un directorio.

Subproceso:

subproceso.run(['mkdir', 'test_dir_subprocess2'])

TÚ:

os.mkdir('test_dir_os2')

Ruta de acceso:

test_dir_pathlib2 = Ruta('test_dir_pathlib2')

test_dir_pathlib2.mkdir(exist_ok=True) #Asegura que el directorio se cree solo si aún no existe

Cuándo utilizar el subproceso
El subproceso se utiliza mejor cuando necesita interactuar con procesos externos, ejecutar comandos de shell
complejos o necesita un control preciso sobre la entrada y salida. El subproceso también genera menos procesos
por tarea que el sistema operativo, por lo que el subproceso puede utilizar menos potencia informática.

Otras ventajas incluyen:

    · El subproceso puede ejecutar cualquier comando de shell, lo que proporciona una mayor flexibilidad.

    · El subproceso puede capturar stdout y stderr fácilmente.

Por otro lado, el sistema operativo es útil para operaciones básicas de archivos y directorios, gestión de variables
de entorno y cuando no se necesita el enfoque orientado a objetos proporcionado por Pathlib.

Otras ventajas incluyen:

    · OS proporciona una forma sencilla de interactuar con el sistema operativo para operaciones básicas.

    · El sistema operativo es parte de la biblioteca estándar, por lo que está ampliamente disponible.

Finalmente, Pathlib es más útil para trabajar extensamente con rutas de archivos, cuando desea una forma intuitiva y
orientada a objetos para manejar las tareas del sistema de archivos, o cuando está trabajando en código donde la
legibilidad y el mantenimiento son cruciales.

Otras ventajas incluyen:

    · Pathlib proporciona un enfoque orientado a objetos para manejar rutas del sistema de archivos.

    · En comparación con el sistema operativo, Pathlib es más intuitivo para operaciones de archivos y directorios.

    · Pathlib es más legible para manipulaciones de rutas.

Donde brilla el subproceso

Las formas básicas de utilizar el subproceso son los métodos .run() y .Popen() . Hay métodos adicionales, .call() ,
.check_output() y .check_call() . Por lo general, solo querrás usar .run() o uno de los dos métodos de verificación
cuando sea apropiado. Sin embargo, cuando genera procesos paralelos o se comunica entre subprocesos, .Popen() tiene
mucho más poder.

Puede pensar en .run() como la forma más sencilla de ejecutar un comando (está todo en el nombre) y en .Popen()
como la forma más completa de llamar comandos externos.

Todos los métodos, .run() , .call() ,  .check_output() y .check_call() son envoltorios de la clase .Popen() .

Correr

El comando .run() es el método recomendado para invocar subprocesos. Ejecuta el comando, espera a que se complete y
luego devuelve una instancia de CompletedProcess que contiene información sobre el proceso.

Usando .run() para ejecutar el comando echo:

result_run = subprocess.run(['echo', '¡Hola mundo!'], capture_output=Verdadero, texto=Verdadero)

result_run.stdout.strip() # Extrayendo la salida estándar y eliminando cualquier espacio en blanco adicional

producción:

'¡Hola Mundo!'

Llamar
El comando call() ejecuta un comando, espera a que se complete y luego devuelve el código de retorno.
Call es más antiguo y .run() debería usarse ahora, pero es bueno ver cómo funciona.

Usando call() para ejecutar el comando echo:

return_code_call = subprocess.call(['echo', '¡Hola desde la llamada!'])

llamada_código_devolución

producción:

0

El valor devuelto 0 indica que el comando se ejecutó correctamente.

check_call y check_output

Utilice check_call() para recibir solo el estado de un comando. Utilice check_output() para obtener también el
resultado. Estos son buenos para situaciones como la E/S de archivos, donde es posible que un archivo no exista o
que la operación falle.

El comando check_call() es similar a call() pero genera una excepción CalledProcessError si el comando devuelve un
código de salida distinto de cero.

Usando check_call() para ejecutar el comando echo:

return_code_check_call = subprocess.check_call(['echo', '¡Hola desde check_call!'])

return_code_check_call

producción:

0

El valor devuelto 0 indica que el comando se ejecutó correctamente.

Usando check_output() para ejecutar el comando echo:

salida_check_output = subprocess.check_output(['echo', '¡Hola desde check_output!'], texto=Verdadero)

output_check_output.strip() # Extrayendo la salida estándar y eliminando cualquier espacio en blanco adicional

producción:

'¡Hola desde check_output!'

Nota: Check_output genera un CalledProcessError si el comando devuelve un código de salida distinto de cero.
Para obtener más información sobre CalledProcessError, consulte
Excepciones
.

popen
Popen() ofrece funciones más avanzadas en comparación con las funciones mencionadas anteriormente.
Le permite generar un nuevo proceso, conectarse a sus canales de entrada/salida/error y obtener su código de retorno.

Usando Popen para ejecutar el comando echo:

Process_popen = subprocess.Popen(['echo', '¡Hola de popen!'], stdout=subprocess.PIPE, text=True)

salida_popen, _ = proceso_popen.comunicar()

output_popen.strip() # Extrayendo la salida estándar y eliminando cualquier espacio en blanco adicional

producción:

'¡Hola de parte de popen!'

Consejo profesional

El comando Popen es muy útil cuando necesita un comportamiento asincrónico y la capacidad de canalizar información
entre un subproceso y el programa Python que ejecutó ese subproceso. Imagine que desea iniciar un comando de ejecución
prolongada en segundo plano y luego continuar con otras tareas en su secuencia de comandos. Más adelante querrás
poder comprobar si el proceso ha finalizado. Así es como lo harías usando Popen.

subproceso de importación

Usando Popen para comportamiento asincrónico:

proceso = subproceso.Popen(['dormir', '5'])

message_1 = "El proceso se está ejecutando en segundo plano..."

# Espere un par de segundos para demostrar el comportamiento asincrónico

tiempo de importación

tiempo.dormir(2)

# Comprobar si el proceso ha finalizado

si process.poll() es Ninguno:

    message_2 = "El proceso aún se está ejecutando."

demás:

    message_2 = "El proceso ha finalizado."

imprimir(mensaje_1, mensaje_2)

producción:

('El proceso se está ejecutando en segundo plano...',

 'El proceso aún está en marcha.')

El proceso se ejecuta en segundo plano mientras el script continúa con otras tareas (en este caso, simplemente
esperando un par de segundos). Luego, el script comprueba si el proceso todavía se está ejecutando. En este caso,
la comprobación se realizó después de 2 segundos de sueño, pero Popen llamó al sueño a los 5 segundos. Entonces el
programa confirma que el subproceso no ha terminado de ejecutarse.

Conclusiones clave

Subprocess es un módulo poderoso que le permite hacer cualquier cosa que pueda en Python desde el shell y luego
recuperar información en Python. Probablemente querrás seguir con OS para operaciones básicas de archivos y
directorios o Pathlib para trabajar extensamente con rutas de archivos. Pero cuando interactúa con procesos
externos, ejecuta comandos de shell complejos o necesita un control preciso sobre la entrada y la salida,
el módulo de subproceso es el camino a seguir.

"""

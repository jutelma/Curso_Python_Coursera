# Pregunta 1
# ¿Cuál de las siguientes es la versión más moderna y actualizada de Python?
#
# R Python 3

# Pregunta 2
# ¿Cuál de los siguientes sistemas operativos es compatible con Python 3?
# R Linux, Windows, MacOs Apple

# ¿Cuál de los siguientes sistemas operativos no se ejecuta en un kernel de Linux?

# R MacOS de Apple

# Si queremos verificar qué versión de Python está instalada, ¿qué escribiríamos en la línea de comando? Seleccione
# todas las que correspondan.
#
# R Python --version, Python -v

# Pregunta 5
# ¿De qué es un ejemplo pip?
#
# R Un administrador de paquetes de Python

"""
Entornos virtuales

Un entorno virtual en Python es una herramienta poderosa que le permite crear entornos aislados para sus proyectos de
Python. Cada entorno actúa como un entorno limitado y contiene su propio intérprete de Python e instalaciones de
biblioteca. Esto significa que puede tener varios proyectos con diferentes dependencias, asegurándose de que no
interfieran entre sí. En esencia, los entornos virtuales proporcionan un borrón y cuenta nueva donde puede trabajar
en sus proyectos sin preocuparse por bibliotecas o versiones en conflicto.

¿Por qué utilizar un entorno virtual en Python?

Imagine que está trabajando en dos proyectos de Python separados: uno requiere una versión específica de una
biblioteca, mientras que el otro depende de una versión más nueva. Sin entornos virtuales, gestionar estas
dependencias podría convertirse en una pesadilla. Aquí es donde brillan los entornos virtuales: le permiten mantener
sus proyectos aislados, asegurando que los cambios en un entorno no afecten a otro.

Al utilizar entornos virtuales, puede:

    · Evite conflictos entre bibliotecas y dependencias.

    · Pruebe diferentes versiones de bibliotecas sin afectar la instalación de Python en todo el sistema.

    · Mantener un entorno de desarrollo limpio y organizado.

    · Colabore con otros mientras garantiza versiones de biblioteca consistentes.

Usando un entorno virtual Python

Crear y utilizar un entorno virtual es un proceso sencillo. Para crear un entorno virtual, abra su terminal y navegue
hasta el directorio de su proyecto. Luego, ejecute el siguiente comando:

pitón -m venv myenv

Este comando crea un entorno virtual llamado "myenv" en el directorio de su proyecto. Para activar el entorno
virtual, utilice el comando apropiado para su sistema operativo:

En Windows:

myenv\Scripts\activar

En macOS y Linux:

myenv/bin/activar

Una vez activado, el mensaje de su terminal cambiará, indicando que ahora está trabajando dentro del entorno virtual.
Ahora puedes instalar paquetes usando pip como lo harías normalmente.

Mejores prácticas y recomendaciones

Mientras se sumerge en el mundo de los entornos virtuales, tenga en cuenta estas mejores prácticas:

Cree un entorno virtual para cada proyecto: cada vez que inicie un nuevo proyecto, cree un nuevo entorno virtual.
Esto asegura un espacio de trabajo limpio y aislado.

Utilice archivos de requisitos: para documentar y administrar las dependencias de su proyecto, cree un archivo de
requisitos.txt. Este archivo enumera todas las bibliotecas y sus versiones. Puede generarlo usando pip congelar >
requisitos.txt y luego instalarlos en un nuevo entorno usando pip install -r requisitos.txt .

Activar y desactivar: active siempre el entorno virtual adecuado antes de trabajar en un proyecto y desactívelo
cuando haya terminado. Esto evita confusiones y posibles conflictos.

Control de versiones: si está colaborando con otras personas, incluya las instrucciones de configuración del entorno
virtual en su sistema de control de versiones. Esto garantiza que todos utilicen el mismo entorno.

Actualice pip y setuptools: cuando crea un nuevo entorno virtual, es una buena práctica actualizar pip y setuptools a
la última versión. Esto garantiza que esté utilizando las herramientas más actualizadas.

Conclusiones clave Los entornos virtuales son la clave para mantener un flujo de trabajo de desarrollo de Python
limpio y eficiente. Al aislar sus proyectos, puede trabajar con confianza, probar varias bibliotecas y garantizar la
coherencia en todo su código base. Con este nuevo conocimiento, estará en camino de dominar el arte de ejecutar
Python localmente y crear aplicaciones sólidas.

https://docs.python.org/3/library/venv.html
"""
# Cuestionario práctico

# 1 Cuando su IDE crea automáticamente una sangría, ¿qué se conoce como esto?
# R Finalización de código

# Pregunta 2
# ¿Puedes identificar el error en el siguiente código?
# #!/usr/bin/env python3
# import numpy as np
#
# def numpyArray():
#     x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
#     y = numpy.array([[3, 6, 2], [9, 12, 8]], np.int32)
#     return x*y
# print(numpyArray())

# R La variable y no llama correctamente al módulo numpy.

# Pregunta 3 ¿Qué tipo de lenguaje de programación se lee y convierte a código de máquina antes del tiempo de
# ejecución, lo que permite un código más eficiente?
# R lenguaje compilado

# ¿Cuál de los siguientes no es un IDE o un editor de código?
#
# R Pepita

# ¿Qué hace la variable RUTA?
#
# R Le dice al sistema operativo dónde encontrar ejecutables.

"""
¿Vale la pena el tiempo?

Piense en una tarea o proceso que haya completado en el trabajo una y otra vez. ¿Alguna vez has pensado que tiene que 
haber una manera más eficiente de ejecutar esta tarea o proceso rutinario? Lo más probable es que tengas razón. Las 
empresas investigan si la automatización de procesos o tareas ahorra tiempo de trabajo (y, por tanto, dinero), 
ofrece un suave retorno de la inversión (ROI) o ambas cosas. Si vale la pena, el proceso automatizado ahorrará tiempo 
de trabajo a la empresa, beneficios de retorno de la inversión (ROI) o ambos.

Retorno de la inversión suave 
El ROI suave a través de la automatización es difícil de medir porque, por lo general, 
no hay cifras ni datos concretos que lo respalden. Las métricas de ROI suave incluyen mejorar:

    · Colaboración en equipo

    · moral del equipo

    · Motivación de empleados

    · Satisfacción del empleado

Piense en la tarea o proceso que completa semanalmente o incluso diariamente. Si esta tarea estuviera automatizada (
como empleado), sería menos probable que se aburriera y, a cambio, estaría más motivado para completar otras tareas 
que no son rutinarias, lo que crearía una alta moral en el lugar de trabajo.

¿Vale la pena la automatización?

Para determinar si la automatización de un proceso ahorraría tiempo de mano de obra, utilice la siguiente fórmula:

Tiempo_para_automatizar < (tiempo_para_realizar * cantidad_de_veces_hechas)

Analicemos esta fórmula y veamos un ejemplo:

Una empresa bancaria busca automatizar uno de sus procesos internos que tarda unos 40 minutos cada semana en 
completarse. El proceso de automatización tardará 10 horas en total en completarse. ¿Cuántas semanas pasarán hasta 
que la empresa bancaria empiece a ahorrar tiempo en el proceso y valga la pena la automatización?

time_to_automate = 10 horas

tiempo_para_realizar = 40 minutos

Cantidad_de_veces_hechas = x 

Consejo profesional: observe que tiene dos medidas de tiempo. Antes de introducir valores en la fórmula, convierta 10 
horas a minutos.

Multiplica 10 por 60 para convertir 10 horas en minutos. Tienes 600 minutos. 

Cuando ingresas tus valores en la fórmula anterior, obtienes:

600 < 40x

Consejo profesional: x representa el número de semanas, por lo que puedes reemplazarlo con x en la fórmula.

Luego, divide ambos lados por 40 para obtener:

15 < semanas

Pasarán 15 semanas antes de que la empresa bancaria comience a ahorrar tiempo en el proceso. Recuerde, 
la automatización de este proceso solo debe realizarse una vez. Además, ayuda a los empleados al eliminar la 
necesidad de pensar en la tarea y mantenerse al día con su seguimiento.

Conclusiones clave
 
Las empresas deben decidir si vale la pena invertir tiempo, esfuerzo y dinero en automatizar 
ciertos procesos que se utilizan comúnmente. Para ello, calcule el ROI para determinar si invertir en la 
automatización del flujo de trabajo es beneficioso para la empresa y sus empleados."""

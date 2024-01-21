"""
Prueba de unidad
Una prueba unitaria proporciona a los desarrolladores un conjunto de herramientas para construir y ejecutar pruebas.
Estas pruebas se pueden ejecutar en componentes individuales o aislando unidades de código para garantizar su
corrección. Al ejecutar pruebas unitarias, los desarrolladores pueden identificar y corregir cualquier error que
aparezca, creando un código más confiable. En esta lectura, aprenderá sobre los conceptos de prueba unitaria, cómo
usarlos y cuándo usarlos, y verá un ejemplo a lo largo del camino.

Conceptos
Unittest se basa en los siguientes conceptos:

    Dispositivo de prueba: Se refiere a la preparación para realizar una o más pruebas. Además, los dispositivos
    de prueba también incluyen cualquier acción involucrada en la limpieza de las pruebas. Esto podría implicar
    la creación de bases de datos, directorios temporales o proxy o el inicio de un proceso de servidor.

    Caso de prueba: esta es la unidad individual de prueba que busca una respuesta específica a un conjunto de entradas.
    Si es necesario, TestCase es una clase base proporcionada por unittest y puede usarse para crear nuevos casos de
    prueba.

    Conjunto de pruebas: es una colección de casos de prueba, conjuntos de pruebas o una combinación de ambos.
    Se utiliza para compilar pruebas que deben ejecutarse juntas.

    Ejecutor de prueba: ejecuta la prueba y proporciona a los desarrolladores los datos del resultado.
    El ejecutor de la prueba puede utilizar diferentes interfaces, como gráfica o textual, para proporcionar al
    desarrollador los resultados de la prueba. También puede proporcionar un valor especial a los desarrolladores
    para comunicar los resultados de las pruebas.

Caso de uso
Veamos un ejemplo de caso de prueba en el que el código Python simula una fábrica de pasteles y realiza diferentes
funciones. Estos incluyen elegir diferentes tamaños y sabores de pastel, incluidos pequeños, medianos y grandes,
y de chocolate o vainilla. Además, la clase simple permite a los desarrolladores agregar chispas o cerezas al pastel,
devolver una lista de ingredientes y devolver el precio del pastel según el tamaño y los ingredientes.



"""


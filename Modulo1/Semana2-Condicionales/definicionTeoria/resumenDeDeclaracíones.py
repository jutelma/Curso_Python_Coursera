"""

    IF resumen de declaraciones

Podemos utilizar el concepto de bifurcación para que nuestro código altere su secuencia de ejecución dependiendo de los
valores de las variables. Podemos usar una declaración if para evaluar una comparación. Comenzamos con la palabra clave
if , seguida de nuestra comparación. Terminamos la línea con dos puntos. El cuerpo de la declaración if tiene sangría
hacia la derecha. Si la comparación es True , se ejecuta el código dentro del cuerpo if . Si la comparación se evalúa
como False , entonces el bloque de código se omite y no se ejecutará.

ejemplo:

"""
def hint_useraname(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")

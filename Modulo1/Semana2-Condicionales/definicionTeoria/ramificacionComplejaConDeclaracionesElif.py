"""
        Ramificación compleja con declaraciones elif

    A partir de los bloques if y else , que nos permiten bifurcar nuestro código dependiendo de la evaluación de una
    declaración, la declaración elif nos permite aún más comparaciones para realizar bifurcaciones más complejas.
    Muy similar a las declaraciones if , una declaración elif comienza con la palabra clave elif , seguida de una
    comparación que se evaluará. A esto le siguen dos puntos y luego el bloque de código en la siguiente línea, con
    sangría a la derecha. Una declaración elif debe seguir a una declaración if y solo se evaluará si la declaración if
    se evaluó como falsa. Puedes incluir múltiples elifdeclaraciones para crear ramificaciones complejas en su código
    para hacer todo tipo de cosas poderosas.

ejemplo:

"""

def hint_username(username):
    if len(username) < 3:
        print("invalid username. must be at most 3 charters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 charters long")
    else:
        print("valid username")
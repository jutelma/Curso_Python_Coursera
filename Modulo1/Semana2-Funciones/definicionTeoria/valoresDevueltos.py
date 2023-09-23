"""Ejemplo"""
def area_triangle(base, heigth):
    return base * heigth/2

area_a = area_triangle (5,4)
area_b = area_triangle (7, 3)
sum = area_a + area_b
print("the sum of both areas is: " + str(sum))

#the sum of both areas is: 20.5

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds= seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds (5000)
print(hours, minutes, seconds)

#1 23 20

"""Devolver valores usando funciones

    A veces no queremos que una función simplemente se ejecute y finalice. Es posible que queramos que una función manipule
    los datos que le pasamos y luego nos devuelva el resultado. Aquí es donde resulta útil el concepto de valores de 
    retorno. Usamos la palabra clave return en una función, que le indica a la función que devuelva datos. Cuando llamamos
    a la función, podemos almacenar el valor devuelto en una variable. Los valores de retorno permiten que nuestras 
    funciones sean más flexibles y potentes, por lo que se pueden reutilizar y llamar varias veces.

    Las funciones pueden incluso devolver múltiples valores. ¡No olvide almacenar todos los valores devueltos en variables!
    También podría hacer que una función no devuelva nada, en cuyo caso la función simplemente sale."""

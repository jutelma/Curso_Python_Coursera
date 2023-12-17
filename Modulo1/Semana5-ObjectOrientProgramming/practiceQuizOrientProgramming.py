# Probemos sus conocimientos sobre el uso de la notación de puntos para acceder a métodos y atributos de un objeto.
# Digamos que tenemos una clase llamada Aves. Los pájaros tienen dos atributos: color y número. Birds también tiene
# un método llamado count() que cuenta el número de pájaros (agrega un valor al número). ¿Cuál de las siguientes
# líneas de código imprimirá correctamente el número de pájaros? ¡Ten en cuenta que el número de pájaros es 0 hasta
# que los cuentes!

# R print(bluejay.number.count())


# Pregunta 2 Crear nuevas instancias de objetos de clase puede ser una excelente manera de realizar un seguimiento de
# los valores utilizando atributos asociados con el objeto. Los valores de estos atributos se pueden cambiar
# fácilmente a nivel de objeto. El siguiente código ilustra una cita famosa de George Bernard Shaw, que utiliza
# objetos para representar personas. Complete los espacios en blanco para que el código satisfaga el comportamiento
# descrito en la cita.


class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


def exchange_apples(you, me):
    # Intercambiamos las manzanas sin usar una variable temporal
    you.apples, me.apples = me.apples, you.apples
    return you.apples, me.apples


def exchange_ideas(you, me):
    # Compartimos nuestras ideas sumándolas
    you.ideas += me.ideas
    me.ideas = you.ideas
    return you.ideas, me.ideas


exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


# 3. Pregunta 3 La clase Ciudad tiene los siguientes atributos: nombre, país (donde se encuentra la ciudad),
#  elevación (medida en metros) y población (aproximada, según estadísticas recientes). Complete los espacios en blanco
# de la función max_elevation_city para devolver el nombre de la ciudad y su país (separados por una coma), al comparar
# las 3 instancias definidas para una población mínima especificada. Por ejemplo, llamar a la función para una
# población mínima de 1 millón: max_elevation_city(1000000) debería devolver "Sofía, Bulgaria".

class City:
    name = ""
    country = ""
    elevation = 0
    population = 0


# Crear instancias de la clase City y definir los atributos para cada ciudad
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):
    # Inicializar la variable que contendrá la información de la ciudad con la elevación más alta
    return_city = City()

    # Evaluar la 1.ª instancia para cumplir con los requisitos:
    # ¿la ciudad #1 tiene al menos min_population y
    # su elevación es la más alta evaluada hasta ahora?
    if city1.population >= min_population and city1.elevation > return_city.elevation:
        return_city = city1

    # Evaluar la 2.ª instancia para cumplir con los requisitos:
    # ¿la ciudad #2 tiene al menos min_population y
    # su elevación es la más alta evaluada hasta ahora?
    if city2.population >= min_population and city2.elevation > return_city.elevation:
        return_city = city2

    # Evaluar la 3.ª instancia para cumplir con los requisitos:
    # ¿la ciudad #3 tiene al menos min_population y
    # su elevación es la más alta evaluada hasta ahora?
    if city3.population >= min_population and city3.elevation > return_city.elevation:
        return_city = city3

    # Formatear la cadena de retorno
    if return_city.name:
        return "{}, {}".format(return_city.name, return_city.country)
    else:
        return ""


# Imprimir los resultados para diferentes poblaciones mínimas
print(max_elevation_city(100000))  # Debería imprimir "Cusco, Peru"
print(max_elevation_city(1000000))  # Debería imprimir "Sofia, Bulgaria"
print(max_elevation_city(10000000))  # Debería imprimir ""


# Pregunta 4
# ¿Qué diferencia a un objeto de una clase?

# R Un objeto es una instancia específica de una clase.


# Pregunta 5
# Disponemos de dos muebles: una mesa de madera marrón y un sofá de cuero rojo. Complete los espacios en
# blanco después de la creación de cada instancia de clase Muebles, de modo que la función describe_furniture pueda
# formatear una oración que describa estas piezas de la siguiente manera: "Este mueble está hecho de {color} {material}"

class Furniture:
    color = ""
    material = ""


table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"


def describe_furniture(piece):
    return "This piece of furniture is made of {} {}".format(piece.color, piece.material)


print(describe_furniture(table))
# Debería imprimir "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Debería imprimir "This piece of furniture is made of red leather"

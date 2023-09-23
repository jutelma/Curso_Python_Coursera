def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculate(5)

"""Es difícil determinar el propósito de este código simplemente mirándolo. Los nombres de las variables no dan mucha
    información al lector y aunque es probable que pueda calcular el resultado del cálculo, no hay pistas sobre para qué
    se podría usar ese resultado. En la jerga de programación, cuando reescribimos el código para ser más 
    autodocumentados, llamamos a este proceso de refactorización. Entonces, ¿cómo se vería si refactorizamos este 
    código?"""

def circle_area(radius) :
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)

"""Con este código refactorizado, la intención debería ser ahora más clara. Los nombres de las variables y la función 
reflejan su propósito, lo que ayuda al lector a entender el código más rápidamente"""

"""Cuando un buen nombre y una organización limpia no pueden aclarar el código, puede agregar un poco de textos 
    explicativos al código.
    En Python, los comentarios se indican mediante el carácter hash , por ejemplo: """

    #Soy un comentario.

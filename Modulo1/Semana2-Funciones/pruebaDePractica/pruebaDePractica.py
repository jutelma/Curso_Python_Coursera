# 1. Esta funsíon convierte millas a kilometros (km)
# 1. Complete el código para devolver el resultado de la conversíon.

# NOTA: Los siguientes elementos ocurren fuera. No intente cambiar las sanggrías en el código asociado o recibira un
#error.
# 2. Llame a la funsíon para convertir la distancia del viaje de millas a kilómetros.
# 3. Complete el espaio en blanco para imprimir el resultado de la vonversíon.
# 4 Calcule el viaje de ida y vuelta en kilómetros duplicando el resultado y complete el espacio en blanco para imprimir
# el resultado.


# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

# Do not indent any of the following lines of code as they are
# meant to be located outside of the function above

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the my_trip_km conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result of
#    my_trip_km. Fill in the blank to print the result.
round_trip_km = my_trip_km * 2
print("The round-trip in kilometers is " + str(round_trip_km))

# resultado:
# The distance in kilometers is 88.0
# The round-trip in kilometers is 352.0

# 2. Esta funsion compara dos números y los devuelve en orden de creciente

# 1. Complete los espacios en blanco para que la declaracíon dde impresíon muestre el resultado de la llamada a la
# funcíon en orden.
# Sugerencia: si una funsion devuelve múltiples valores, no olvide almacenar estos valores en múltiples variables.

# Esta función compara dos números y los devuelve
# en orden creciente.

def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Complete los espacios en blanco para que la declaración impresa muestre el resultado
# de la llamada a la función
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

#resultado: 99 100

# 3. como se llaman los valores pasados a funciones como entrada?

# R. Los valores que se pasan a una función como entrada se denominan "argumentos" o "parámetros"

# 4.Completa la primera línea de la funcíon "print_segundos" para que acepte tres parametros: horas, minutos y
# segundos.
# Recuerde utilizar la palabra clave "def" para indicarle al intérprete de Python que el bloque de código está
# destinado  a definir una funcíon.

def print_seconds(hours, minutes, seconds):
    print(hours * 3600 + minutes * 60 + seconds)


print_seconds(1,2,3)
#output will print to the screen

# Resultado: 3723


# Cual es el proposito de la palabra clave def?

# R. La palabra clave def en Python se utiliza para definir una función.
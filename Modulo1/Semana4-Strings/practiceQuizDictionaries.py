# Pregunta 1 La función email_list recibe un diccionario que contiene nombres de dominio como claves y una lista de
# usuarios como valores. Complete los espacios en blanco para generar una lista que contenga direcciones de correo
# electrónico completas (por ejemplo, diana.prince@gmail.com).


def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user + "@" + domain)
    return emails


print(email_list(
    {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
     "hotmail.com": ["bruce.wayne"]}))


# 2. Pregunta 2 La función groups_per_user recibe un diccionario que contiene nombres de grupos con la lista de
# usuarios. Los usuarios pueden pertenecer a varios grupos. Complete los espacios en blanco para devolver un
# diccionario con los usuarios como claves y una lista de sus grupos como valores.

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of
            user_groups.setdefault(user, []).append(group)

    return user_groups


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))

# Pregunta 3 El método dict.update actualiza un diccionario con los elementos provenientes del otro diccionario,
# de modo que las entradas existentes se reemplazan y se agregan nuevas entradas. ¿Cuál es el contenido del
# diccionario "guardarropa" al final del siguiente código?

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)


# Respuesta
# {'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}

#  Pregunta 4 ¿Cuál es la principal ventaja de utilizar diccionarios sobre listas?

# Respuesta: Es más rápido y sencillo encontrar un elemento específico en un diccionario

# Pregunta 5 La función add_prices devuelve el precio total de todos los alimentos del diccionario. Complete los
# espacios en blanco para completar esta función.

def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for price in basket.values():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += price
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44

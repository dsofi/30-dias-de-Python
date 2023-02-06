# 01 - Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print('nordic_countries : ', nordic_countries)
print('es: ', es)
print('ru: ', ru)


# --- Otro ejercicio
# - Crea una tupla con tres elementos: un nombre, una edad y una lista de hobbies. Desempaqueta los elementos de la tupla en tres variables. Imprime cada variable por separado para verificar que se ha desempaquetado correctamente.
print('''
------ Otro ejercicio ------''')
una_tupla = ('Juan', 25, ['leer','viajar','hacer deporte'])
nombre, edad, hobbies = una_tupla
print('nombre: ', nombre)
print('edad: ', edad)
print('hobbies: ', hobbies)


# - Crea una lista con cinco elementos: tres números enteros y dos strings. Desempaquetar los primeros tres elementos de la lista en tres variables: a, b y c. Desempaquetar los últimos dos elementos de la lista en dos variables: d y e. Imprime cada variable por separado para verificar que se ha desempaquetado correctamente.
print('''
------ Otro ejercicio ------''')
una_lista = [1, 2, 3, 'hola', 'chau']
a, b, c, *resto = una_lista
d, e = resto
print('a: ', a)
print('b: ', b)
print('c: ', c)
print('d: ', d)
print('e: ', e)
# 01 - Explain the difference between map, filter, and reduce.
""" map es una función en Python que se utiliza para aplicar una función dada a cada elemento de un iterable (como una lista, tupla, etc.). Devuelve un objeto iterable, como un map object, que puede ser convertido a una lista o tupla. """
### map aplica una función a todos los elementos de un iterable 
""" filter es una función en Python que se utiliza para filtrar elementos de un iterable en función de una función dada. Devuelve un objeto iterable, como un filter object, que puede ser convertido a una lista o tupla. """
### filter filtra los elementos de un iterable en función de una función dada
""" reduce es una función de la librería functools en Python que se utiliza para aplicar una función binaria a los elementos de un iterable de forma acumulativa. Por ejemplo, puede utilizar la función reduce para calcular el producto de todos los números en una lista. """
### reduce se utiliza para acumular los resultados de una función aplicada a los elementos de un iterable


# 02 - Explain the difference between higher order function, closure and decorator
""" Una función de orden superior es una función que toma otra función como argumento o devuelve otra función. Por ejemplo, map, filter y reduce son funciones de orden superior en Python, ya que toman otras funciones como argumentos. """
### función de orden superior es una función que toma otra función como argumento o devuelve otra función
""" Un closure es una función que recuerda el estado de las variables en el ámbito que se encontraba cuando se definió, incluso si estas variables ya no existen en el ámbito actual. Por ejemplo, una función que devuelve otra función como un closure. """
### closure es una función que recuerda el estado de las variables en el ámbito que se encontraba cuando se definió
""" Un decorador es una función de orden superior que se utiliza para modificar el comportamiento de otra función, agregando funcionalidad adicional sin modificar su código. Los decoradores se utilizan para la reutilización de código y para aplicar patrones de diseño como el patrón de diseño de decorador. """
### decorador es una función de orden superior que se utiliza para modificar el comportamiento de otra función agregando funcionalidad adicional.


# 03 - Define a call function before map, filter or reduce, see examples.
def call(function, *args, **kwargs):
    return function(*args,**kwargs)

def square(x):
    return x ** 2
numbers = [1, 2, 3, 4, 5]
squared_numbers = call(map, square, numbers)
print(list(squared_numbers))    # [1, 4, 9, 16, 25]

def even_filter(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = call(filter, even_filter, numbers)
print(list(even_numbers))   # [2, 4, 6, 8, 10]

from functools import reduce
def multiply(x,y):
    return x*y
numbers=[1, 2, 3, 4, 5]
result = call(reduce, multiply, numbers)
print(result)


# 04 - Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

# 05 - Use for to print each name in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)

# 06 - Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)


# Exercises: Level 2
print('''

--------- * LEVEL 2 * ---------
''')

# 01 - Use map to create a new list by changing each country to uppercase in the countries list
print('-- Exercise 1 --')
mayus_ctries_lst = list(map(lambda country: country.upper(), countries))
print(mayus_ctries_lst)

print('-- Exercise 1 (alternativa)--')
mayus_ctries_lst_alt = list(map(str.upper, countries))
print(mayus_ctries_lst_alt)

# 02 - Use map to create a new list by changing each number to its square in the numbers list
print('-- Exercise 2 --')
square_lst = list(map(lambda x: x*x, numbers))
print(square_lst)

# 03 - Use map to change each name to uppercase in the names list
print('-- Exercise 3 --')
upper_name_lst = list(map(str.upper, names))
print(upper_name_lst)

# 04 - Use filter to filter out countries containing 'land'.
print('-- Exercise 4 --')
cont_land = list(filter(lambda x: 'land' not in x, countries))
print(cont_land)

# 05 - Use filter to filter out countries having exactly six characters.
print('-- Exercise 5 --')
not_six_char = list(filter(lambda x: len(x)!=6,countries))
print(not_six_char)

# 06 - Use filter to filter out countries containing six letters and more in the country list.
print('-- Exercise 6 --')
countries.append('Chile')
not_six_or_more_char = list(filter(lambda x: len(x)<6,countries))
print(not_six_or_more_char)

# 07 - Use filter to filter out countries starting with an 'E'
print('-- Exercise 7 --')
not_start_E = list(filter(lambda x: x[0]!='E', countries ))
print(not_start_E)

# 08 - Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print('-- Exercise 8 --')
chain_num = reduce(lambda x, y: x * y, filter(lambda x: x%2 == 0, map(lambda x: x**2 ,numbers)))
print(chain_num)

chain_ctry = list(filter(lambda x: 'LAND' not in x, map(lambda x: x.upper(), countries)))
print(chain_ctry)

chain_num_2 = reduce(lambda x, y: x + y, list(map(lambda x: x*3, filter(lambda x: x%2 != 0, numbers))))
print(chain_num_2)

# 09 - Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
print('-- Exercise 9 --')
print('-- Filtra los items que son strings --')
my_list = [1,'hola',215,True,'string',41,'prueba']
def get_string_lists(lista):
    return list(filter(lambda x: type(x)==str, lista))
print(get_string_lists(my_list))

print('-- Transforma los items a strings --')
def transf_to_string(lista):
    return list(map(lambda x: str(x),lista))
print(transf_to_string(my_list))

print('-- Transforma los items a strings alternativa --')
def transf_to_string_alt(lista):
    return list(map(str,lista))
print(transf_to_string_alt(my_list))

# 10 - Use reduce to sum all the numbers in the numbers list.
print('-- Exercise 10 --')
total = reduce(lambda x,y:x+y,numbers)
print(total)

# 11 - Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
print('-- Exercise 11 --')
sentence = reduce(
    lambda x,y: x + ', ' + y if y != countries[-1] 
    else x + ' and ' + y + ' are north European countries.',
    countries)
print(sentence)

# 12 - Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
print('-- Exercise 12 --')
import json
with open ("data/countriesdata.json","r", encoding='utf-8') as cjson:
    ctries = json.load(cjson)
def categorize_countries(lista, pattern):
    return list(map(lambda x: x['name'], list(filter(lambda x: pattern in x['name'],lista)))) 
print(categorize_countries(ctries, 'land'))
print(categorize_countries(ctries, 'stan'))

# 13 - Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
print('-- Exercise 13 --')
def ctries_dct(lista):
    dct = {}
    for country in lista:
        inicial = country['name'][0]
        dct[inicial] = dct.get(inicial,0) + 1
    return dct
print(ctries_dct(ctries))

# 14 - Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
print('-- Exercise 14 --')
def get_first_ten_countries(lista):
    return (list(map(lambda x : x['name'], lista)))[:10]
print(get_first_ten_countries(ctries))

# 15 - Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
print('-- Exercise 15 --')
def get_last_ten_countries(lista):
    return (list(map(lambda x : x['name'], lista)))[-10:]
print(get_last_ten_countries(ctries))


# Exercises: Level 3
print('''

--------- * LEVEL 3 * ---------
''')
# Use the countries_data.py file and follow the tasks below:
# 01 - Sort countries by name, by capital, by population
print('-- Exercise 1 --')
def sort_by(lista,key):
    if key != 'name':
        return [{key: x[key], 'country': x['name']} for x in sorted(filter(lambda x: x[key] != '', lista), key=lambda x:x[key])][:10]
    else:
        return list(map(lambda x : x[key], sorted(lista, key = lambda x:x[key])))[:10]

print('**Primeros 10 países en orden alfabético :')
for i in sort_by(ctries, 'name'):
    print(i)
print('**Primeras 10 capitales en orden alfabético :')
for i in sort_by(ctries, 'capital'):
    print(i)
print('**Los 10 países menos poblados :')
for i in sort_by(ctries, 'population'):
    print(i)

# 02 - Sort out the ten most spoken languages by location.
print('-- Exercise 2 --')
print('**Lista de los 10 idiomas más hablados :')
from collections import Counter
def sort_languages(paises):
    all_lang = [lang for pais in paises for lang in pais['languages']]
    lang_count = Counter(all_lang)
    return sorted(lang_count.items(), key=lambda x: x[1], reverse=True)[:10]
top_lang=sort_languages(ctries)
for i in top_lang:
    print(i)

# 03 - Sort out the ten most populated countries.
print('-- Exercise 3 --')
print('**Lista de los 10 países más poblados :')
def sort_population(paises):
    return [{'name': x['name'], 'population': x['population']} for x in sorted(paises, key=lambda x: x['population'])][-10:]
for i in sort_population(ctries):
    print(i)
    



# Exercises: Level 1
print('''

--------- * LEVEL 1 * ---------
''')

# 01 - Declare a function add_two_numbers. It takes two parameters and it returns a sum.
print('-- Exercise 1 --')
def add_two_numbers(n1,n2):
    return n1+n2
print('Suma de 3 y 6 = ', add_two_numbers(3,6))

# 02 - Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
print('-- Exercise 2 --')
def area_of_circle(r):
    return 3.14 * r * r
print('Área de un círculo de radio 10 = ', area_of_circle(10))

# 03 - Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
print('-- Exercise 3 --')
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) == int or type(num) == float:
            total += num
        else:
            print(f'{num} no se ha sumado porque no es un valor correcto.')    
    return total
print('La suma de los números es : ', add_all_nums(2,4,(1,2,3,4),5,9,True,'un string',10,5.5))

# 04 - Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.4
print('-- Exercise 4 --')
def cel_to_fah(cel):
    return (cel * 9/5) + 32
print(f'35° Celsius son: {cel_to_fah(35)}° Fahrenheit')

# 05 - Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
print('-- Exercise 5 --')
primavera = ['septiembre','octubre','noviembre']
verano = ['diciembre','enero','febrero']
otoño = ['marzo','abril','mayo']
invierno = ['junio','julio','agosto']
def check_estacion(mes):    
    if mes in primavera:
        print(f'En el mes de {mes} es primavera.')
    elif mes in verano:
        print(f'En el mes de {mes} es verano.')
    elif mes in otoño:
        print(f'En el mes de {mes} es otoño.')
    elif mes in invierno:
        print(f'En el mes de {mes} es invierno.')
    else:
        print(f'\"{mes}\" no es un mes válido.')   
check_estacion('enero')
check_estacion('septiembre')
check_estacion('cualquier cosa')

# 06 - Write a function called calculate_slope which return the slope of a linear equation
print('-- Exercise 6 --')
def calc_slope(x1, y1, x2, y2):
    m = 0
    b = (x2 - x1)
    d = (y2 - y1)
    if b != 0:
        m = (d)/(b) 
    return m
print('Slope: ', calc_slope(2, 3, 6, 7))
print('Slope: ', calc_slope(2, 4, 8, 4))
print('Slope: ', calc_slope(2, 5, 6, 3))

# 07 - Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
print('-- Exercise 7 --')
def solve_quadratic_eqn(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return "Sin solución"
    elif d == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + (d**0.5)) / (2*a)
        x2 = (-b - (d**0.5)) / (2*a)
        return (x1, x2)
print(solve_quadratic_eqn(1, -3, 2))      # (2.0, 1.0)
print(solve_quadratic_eqn(2, -7, 3))      # (3.0, 0.5)
print(solve_quadratic_eqn(2, 2, 2))       # Sin solución
print(solve_quadratic_eqn(1, 4, 4))       # (-2.0)
print(solve_quadratic_eqn(3, 4, 5))       # Sin solución
print(solve_quadratic_eqn(1, -1, -2))     # (2.0, -1.0)

# 08 - Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
print('-- Exercise 8 --')
def print_list(lista):
    if type(lista) == list:
        for element in lista:
            print(element)
    else:
        print(f'\"{lista}\" no es una lista.')
print_list(['hola','como','estas'])
print_list(('esto','no','es','una','lista'))
print_list('esto tampoco es una lista')

# 09 - Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print('-- Exercise 9 --')
def reverse_list(array):
    reverse_arr = []
    for i in range(len(array) -1, -1, -1):
        reverse_arr.append(array[i])
    return reverse_arr
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

print('-- Exercise 9 (alternativa) --')
def rev_list(arr):
    return arr[::-1]
print(rev_list([1, 2, 3, 4, 5]))
print(rev_list(["A", "B", "C"]))

# 10 - Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
print('-- Exercise 10 --')
def capitalize_list_items(lista):
    capitalized_list = []
    for item in lista:
        capitalized_list.append(item.capitalize())
    return capitalized_list
print(capitalize_list_items(['PoTato', 'tomato', 'mango', 'MILK']))

print('-- Exercise 10 (alternativa) --')
def cap_list_items(lista):
    return [item.capitalize() for item in lista]
print(cap_list_items(['PoTato', 'tomato', 'mango', 'MILK']))

# 11 - Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
print('-- Exercise 11 --')
def add_item(lista,item):
    lista.append(item)
    return lista

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat')) 

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5)) 

# 12 - Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
print('-- Exercise 12 --')
def remove_item(lista,item):
    lista.remove(item)
    return lista

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango')) 

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

# 13 - Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print('-- Exercise 13 --')
def sum_of_numbers(num):
    total = 0
    for n in range(num + 1):
        total += n
    return total
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# 14 - Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
print('-- Exercise 14 --')
def sum_of_odds(num):
    total = 0
    for n in range(num + 1):
        if n%2 != 0:
            total += n
    return total
print(sum_of_odds(5))

# 15 - Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
print('-- Exercise 15 --')
def sum_of_evens(num):
    total = 0
    for n in range(num + 1):
        if n%2 == 0:
            total += n
    return total
print(sum_of_evens(6))


# Exercises: Level 2
print('''

--------- * LEVEL 2 * ---------
''')
# 01 - Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
print('-- Exercise 1 --')
def evens_and_odds(num):
    count_even = 0
    count_odd = 0
    for n in range(num + 1):
        if n%2 == 0:
            count_even +=1
        else:
            count_odd +=1
    print(f'En el rango de {num} hay {count_even} números pares, y {count_odd} números impares.')
evens_and_odds(6)  
print(evens_and_odds(100))

# 02 - Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
print('-- Exercise 2 --')
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

print('-- Exercise 2 (alternativa)--')
def factorial_2(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial_2(5))

# 03 - Call your function is_empty, it takes a parameter and it checks if it is empty or not
print('-- Exercise 3 --')
def is_empty(param):
    if type(param) == int or type(param) == float:
        param = str(param)
    if len(param) == 0:
        print('El parámetro está vacío')
    else:
        print(f'El parámetro es {param}')
is_empty('')
is_empty([])
is_empty(9)

# 04 - Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
print('-- Exercise 4 --')
def calc_mean(lst):
    return sum(lst) / len(lst)
print('mean #01 : ' ,calc_mean([5,6,7,10,8]))
print('mean #02 : ' ,calc_mean([2,9,8,4,7,5,8,5]))

def calc_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]
print('median #01 : ' ,calc_median([1,2,2,2,3,4,5,6]))
print('median #02 : ' ,calc_median([1,2,2,2,3,4,5,6,8,9,10]))

def calc_mode(lst):
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    mode = max(count, key=count.get)
    return mode
print('mode #01 : ' ,calc_mode([1,2,2,2,3,4,5,6]))
print('mode #02 : ' ,calc_mode([1,2,3,3,4,4,4,5,6]))

def calc_range(lst):
    return max(lst) - min(lst)
print('range # 01 : ' ,calc_range([1,2,2,2,3,4,5,6]))
print('range # 02 : ' ,calc_range([3,5,4,8,9,4,6,3]))

def calc_variance(lst):
    mean = calc_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / (len(lst) - 1)

def calc_std(lst):
    variance = calc_variance(lst)
    return variance**(1/2)
print('-- #01--')
lst=[1,2,3]
print('mean : ' ,calc_mean(lst))
print('variance : ' ,calc_variance(lst))
print('std : ',calc_std(lst))
print('-- #02 --')
lst=[5,40,100]
print('mean : ',calc_mean(lst))
print('variance : ',calc_variance(lst))
print('std : ',calc_std(lst))
print('-- #03 --')
lst=[30,20,25]
print('mean : ',calc_mean(lst))
print('variance : ',calc_variance(lst))
print('std : ',calc_std(lst))
print('-- #04 --')
lst=[15,20,10,15]
print('mean : ',calc_mean(lst))
print('variance : ',calc_variance(lst))
print('std : ',calc_std(lst))

def all_func(list):
    print(calc_mean(list))
    print(calc_median(list))
    print(calc_mode(list))
    print(calc_range(list))
    print(calc_variance(list))
    print(calc_std(list))
print('----- PRUEBA TODAS JUNTAS -----')
all_func([7,8,8,9])


# Exercises: Level 3
print('''

--------- * LEVEL 3 * ---------
''')

# 01 - Write a function called is_prime, which checks if a number is prime.
print('-- Exercise 1 --')
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# num = int(input('Ingrese un número: '))
# print(f'El número {num} es un número primo? : {is_prime(num)}')


# 02 - Write a functions which checks if all items are unique in the list.
print('-- Exercise 2 --')
def is_unique(lista):
    copia = []
    repes = []
    for elem in lista:
        if elem not in copia:
            copia.append(elem)
        else:            
            repes.append(elem)            
    if repes == []:
        print('Todos los elementos de la lista son únicos.')
    else:
        print('Hay elementos repetidos: ', repes)

is_unique([1,2,3,4,5,6,8,7,52,9])
is_unique([1,2,3,4,5,6,8,7,8,9,3,7,52,9])

print('-- Exercise 2 (alternativa) --')
def is_unique(lista):
    return len(set(lista)) == len(lista)
print(is_unique([1,2,3,4,5]))
print(is_unique([1,2,2,1,5,9,7,8,]))

# 03 - Write a function which checks if all the items of the list are of the same data type.
print('-- Exercise 3 --')
def same_type(lista):
    dt = type(lista[0])
    for e in lista:
        if type(e) != dt:
            return False
    return True
print('Same data type - Prueba 01 : ', same_type([1, 2, 3, 4, 5]))               # True
print('Same data type - Prueba 02 : ', same_type([1, 'hello', 3.14, True]))      # False
print('Same data type - Prueba 03 : ', same_type([True,False, True, False]))     # True
print('Same data type - Prueba 04 : ', same_type( ['hello', 'world', 'algo']))   # True
print('Same data type - Prueba 05 : ', same_type( [1,2,3,4.5]))                  # False

# 04 - Write a function which check if provided variable is a valid python variable
print('-- Exercise 4 --')
def is_valid_var(var):
    if isinstance(var, str):
        return var.isidentifier()
    else:
        return False
print('Valid var #01: ' , is_valid_var(123))                    # False
print('Valid var #03: ' , is_valid_var('si_es'))                # True
print('Valid var #02: ' , is_valid_var('1noes'))                # False
print('Valid var #02: ' , is_valid_var('no-es'))                # False
print('Valid var #02: ' , is_valid_var('no es'))                # False
print('Valid var #02: ' , is_valid_var('textoSiPuedeSer_6'))    # True

# 05 - Go to the data folder and access the countries-data.py file.
print('-- Exercise 5 --')
from data.countriesdata import get_countries_data
countries_data = get_countries_data()
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
print('-- Exercise 5 - Parte 1 --')
def most_spoken_lan(data):
    lang_all = []
    for country in countries_data:
        lang_all.extend(country['languages'])
    lang_count = {}
    for language in lang_all:
        if language in lang_count:
            lang_count[language] += 1
        else:
            lang_count[language] = 1
    ranking_lang = sorted(lang_count.items(), key=lambda x:x[1], reverse=True)[:10]
    print('Los 10 idiomas más hablados son:')
    for lang, count in ranking_lang:
        print(f'-{lang} : {count}')
most_spoken_lan(countries_data)

# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
print('-- Exercise 5 - Parte 2 --')
def most_popu_ctries(data):
    popu = {}
    for ctry in countries_data:
        popu[ctry['name']] = ctry['population']
    ranking_popu = sorted(popu.items(), key=lambda x:x[1], reverse=True)[:10]
    print('Los 10 países más habitados son:')
    for ctry, population in ranking_popu:
        print(f'-{ctry} : {population}')
most_popu_ctries(countries_data)




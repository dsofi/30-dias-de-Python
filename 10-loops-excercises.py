# Exercises: Level 1
print('------ * LEVEL 1 * ------')

# 01 - Iterate 0 to 10 using for loop, do the same using while loop.
print('* Exercise 1 *')

print('---Exercise 1 with for---')
for number in range(11):
    print(number)

print('---Exercise 1 with while---')
count = 0
while count <= 10:
    print(count)
    count = count + 1

# 02 - Iterate 10 to 0 using for loop, do the same using while loop.
print('* Exercise 2 *')

print('---Exercise 2 with for---')
for number in range(10, -1, -1):
    print(number)

print('---Exercise 2 with while---')
count = 10
while count >= 0:
    print(count)
    count = count - 1

print('---Exercise 2 with for and reversed---')
for number in reversed(range(11)):
    print(number)

# 03 - Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######
print('* Exercise 3 *')
print('---Exercise 3 with while---')
count = 1
simbolo = ''
while count <= 7:
    count = count + 1
    simbolo = simbolo + '#'
    print(simbolo)

print('---Exercise 3 with for---')
simbolo = ""
for i in range(7):
    simbolo += "#"
    print(simbolo)

# 04 - Use nested loops to create the following:
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
print('* Exercise 4 *')
print('---Exercise 4 with for---')
for i in range(8):
    for j in range(8):
        print("# ", end="")
    print()

print('---Exercise 4 with while---')
i = 0
while i < 8:
    j = 0
    while j < 8:
        print("# ", end="")
        j = j + 1
    print()
    i = i + 1

# 05 - Print the following pattern:
    # 0 x 0 = 0
    # 1 x 1 = 1
    # 2 x 2 = 4
    # 3 x 3 = 9
    # 4 x 4 = 16
    # 5 x 5 = 25
    # 6 x 6 = 36
    # 7 x 7 = 49
    # 8 x 8 = 64
    # 9 x 9 = 81
    # 10 x 10 = 100
print('* Exercise 5 *')
for i in range(11):
    print(f'{i} x {i} = {i*i}')

# 06 - Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print('* Exercise 6 *')
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lst:
    print(item)

# 07 - Use for loop to iterate from 0 to 100 and print only even numbers
print('* Exercise 7 *')
for i in range(101):    
    if i % 2 == 0:
        print(i)
    i = i+1

# 08 - Use for loop to iterate from 0 to 100 and print only odd numbers
print('* Exercise 8 *')
for i in range(101):    
    if i % 2 != 0:
        print(i)
    i = i+1


# Exercises: Level 2
print('''
------ * LEVEL 2 * ------''')

# 01 - Use for loop to iterate from 0 to 100 and print the sum of all numbers.
print('* Exercise 1 *')
sum = 0
for i in range(101):
    sum = sum + i
print(f'The sum of all numbers is {sum}.')

# 02 - Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
print('* Exercise 2 *')
sum_evens = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odd += i 
print(f'The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odd}.')


# Exercises: Level 2
print('''
------ * LEVEL 3 * ------''')

# 01 - Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
print('* Exercise 1 *')
from data.countries import get_countries
countries = get_countries()
for country in countries:
    if 'land' in country:
        print(country)

# 02 - This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
print('* Exercise 2 *')
print('---Exercise 2 con reversed---')
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in reversed(fruits):
    print(fruit)

print('---Exercise 2 con range---')
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])

# 03 - Go to the data folder and use the countries_data.py file.
print('* Exercise 3 *')
from data.countriesdata import get_countries_data
countries_data = get_countries_data()
# What are the total number of languages in the data
print('---Exercise 3 / 1---')
languages = []
for country in countries_data:
    for lang in country['languages']:
        if lang not in languages:
            languages.append(lang)
#print(languages)
print(f'El total de idiomas en la data es de: {len(languages)}')

# Find the ten most spoken languages from the data
print('---Exercise 3 / 2---')
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

# Find the 10 most populated countries in the world
print('---Exercise 3 / 3---')
popu = {}
for ctry in countries_data:
    popu[ctry['name']] = ctry['population']
ranking_popu = sorted(popu.items(), key=lambda x:x[1], reverse=True)[:10]
print('Los 10 países más habitados son:')
for ctry, population in ranking_popu:
    print(f'-{ctry} : {population}')

# forma mas corta :
# most_populated_countries = sorted(countries_data, key=lambda x:x["population"], reverse=True)[:10]








# 01 - Declare an empty list
empt_lst = []

# 02 - Declare a list with more than 5 items
receta = ['azúcar', 'científico', 'flores', 'laboratorio', 'muchos colores']
print('receta:', receta)

# 03 - Find the length of your list
length = len(receta)
print('length:', length)

# 04 - Get the first item, the middle item and the last item of the list
first_item = receta[0]
middle_item = receta[2]  # Podría hacerlo con el len / 2 
last_index = length - 1
last_item = receta[last_index]

print(f'''
first item: {first_item}
middle item: {middle_item}
last item: {last_item}
''')

# 05 - Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['sofi','90','1.60','ns/nc','una casita 123']

# 06 - Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 07 - Print the list using print()
print('it companies:', it_companies)

# 08 - Print the number of companies in the list
length_companies = len(it_companies)
print('length companies:', length_companies)

# 09 - Print the first, middle and last company
first_company = it_companies[0]
middle_index = length_companies // 2
middle_company = it_companies[middle_index]  
last_index = length_companies - 1
last_company = it_companies[last_index]

print(f'''
first company: {first_company}
middle company: {middle_company}
last company: {last_company}
''')

# 10 - Print the list after modifying one of the companies
print('it companies:', it_companies)

# 11 - Add an IT company to it_companies
it_companies.append('Accenture')
print('it comp con append:', it_companies)

# 12 - Insert an IT company in the middle of the companies list
new_middle_i = len(it_companies)//2
it_companies.insert(new_middle_i, 'DXC')
print('insert middle:', it_companies)

# 13 - Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print('to uppercase:', it_companies)

# 14 - Join the it_companies with a string '#;  '
str_join = '#;  '.join(it_companies)
print('str join:', str_join)

# 15 - Check if a certain company exists in the it_companies list.
company_to_search =  'Microsoft'
existe = company_to_search in it_companies
print('existe', company_to_search, '?:', existe)

# 16 - Sort the list using sort() method
it_comp_copy = it_companies.copy()
it_comp_copy.sort()
print('sort it comp:', it_comp_copy)

# 17 - Reverse the list in descending order using reverse() method
it_comp_copy.reverse()
print('reverse it comp:', it_comp_copy)

# 18 - Slice out the first 3 companies from the list
print('''
---''')
print('lista original:', it_companies)
first_three = it_companies[:3]
print('first three:', first_three)

# 19 - Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print('last three:', last_three)

# 20 - Slice out the middle IT company or companies from the list
slice_middle = it_companies[3:-3]
print('slice middle:', slice_middle)

# 21 - Remove the first IT company from the list
it_comp_copy = it_companies.copy()
del it_comp_copy[0]
print('remove the first:', it_comp_copy)

# 22 - Remove the middle IT company or companies from the list
length_it_comp_copy = len(it_comp_copy)
middle_index_copy = length_it_comp_copy // 2
del it_comp_copy[middle_index_copy]
print('remove the middle:', it_comp_copy) # Agragar condición para borrar dos en caso de que el len sea par

# 23 - Remove the last IT company from the list
del it_comp_copy[-1]
print('remove last:', it_comp_copy)

# 24 - Remove all IT companies from the list
it_comp_copy.clear()
print('clear:', it_comp_copy)

# 25 - Destroy the IT companies list
del it_comp_copy

# 26 - Join the following lists:
print('''
---''')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_and_back = front_end + back_end
print('join two lists:', front_and_back)

# 27 - After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_and_back.copy()
print('full stack:', full_stack)



# ---
# Exercises: Level 2
print('''
--- LEVEL 2 ---''')

# 01 - The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print('ages sort:', ages)
min = ages[0]
max = ages[-1]
print(f'''
min age: {min}
max age: {max}
''')

# Add the min age and the max age again to the list
ages.append(min)
ages.append(max)
ages.sort()
print('add ages:', ages)

# Find the median age (one middle item or two middle items divided by two)
length_ages = len(ages)
middle_i_ages = length_ages // 2 
if length_ages % 2 == 0:
    print('first median age:', ages[middle_i_ages - 1])
    print('second median age:', ages[middle_i_ages - 1])
else: print('median age:', ages[middle_i_ages])

# Find the average age (sum of all items divided by their number )
suma = sum(ages)
average = suma / length_ages
print(f'''
la suma de todas las edades es: {suma}
la cantidad de edades en la lista es de: {length_ages}
la edad promedio es: {average}
''')

# Find the range of the ages (max minus min)
range = max - min
print('age range:', range)

# Compare the value of (min - average) and (max - average), use abs() method
comp_min_av = abs(min - average)
print('(min - average)', comp_min_av)
comp_max_av = abs(max - average)
print('(max - average)', comp_max_av)


# ---
# Exercises: Part 2
print('''
--- Part 2 ---''')

# Find the middle country(ies) in the countries list
from data.countries import get_countries
countries = get_countries()

len_countries = len(countries)  
# print(len_countries)        # 193
mid_i_countries = len_countries // 2 
# print(mid_i_countries)      # 96
# print(len_countries % 2 )   # 1
if len_countries % 2 == 0:
    print('first middle country:', countries[mid_i_countries - 1])
    print('second middle country:', countries[mid_i_countries - 1])
else: print('middle country:', countries[mid_i_countries])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_divide = countries[:mid_i_countries + 1]
len_firts_div = len(first_divide)
# print(len_firts_div)    # 97
print('primera lista dividida:', first_divide)     # includes Lesotho

second_divide = countries[mid_i_countries + 1:]
len_second_div = len(second_divide)
# print(len_second_div)   # 96
print('segunda lista dividida:', second_divide)    # from  Liberia

# Unpack the first three countries and the rest as scandic countries.
print('''
---''')
list_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print('lista de países', list_countries) 

first_country, second_country, third_country, *scandic_countries = list_countries
print('primer país:', first_country) 
print('segundo país:', second_country) 
print('tercer país:', third_country) 
print('scandic countries:', scandic_countries) 
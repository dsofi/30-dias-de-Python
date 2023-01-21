# 01 - Create an empty tuple
tpl = ()

# 02 - Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Juan','Pedro','Franco')
sisters = ('Martina','Julieta','María')

# 03 - Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print('siblings:', siblings)

# 04 - How many siblings do you have?
len_sibl = len(siblings)
print(f'I have: {len_sibl} siblings')

# 05 - Modify the siblings tuple and add the name of your father and mother and assign it to family_members
lst_sibl = list(siblings)
lst_sibl.append('Homero')
lst_sibl.append('Marge')
family_members = tuple(lst_sibl)
print('family_members:',family_members)


# ---
# Exercises: Level 2
print('''
--- LEVEL 2 ---''')
# 01 - Unpack siblings and parents from family_members
siblings, *parents = family_members[:-2], family_members[-2:]
print('siblings',siblings)
print('parents',parents)

# 02 - Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
print('''
---''')
fruits = ('apple', 'banana', 'orange', 'mango', 'kiwi')
vegetables = ('carrot', 'cabbage', 'broccoli', 'spinach', 'cucumber')
animal_products = ('milk', 'cheese', 'beef', 'chicken', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
print('food stuff tp:',food_stuff_tp)

# 03 - Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
food_stuff_lt.append('algo')

# 04 - Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
len_food = len(food_stuff_lt)
middle_index = len_food // 2
if len_food % 2 == 0:
    second_middle_index = middle_index - 1
    print('Middle item 1:',food_stuff_lt[middle_index])
    print('Middle item 2:',food_stuff_lt[second_middle_index])
else: print ('Middle item:',food_stuff_lt[middle_index])

# 05 - Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
print('first three:', first_three)
last_three = food_stuff_lt[-3:]
print('last three:', last_three)

# 06 - Delete the food_staff_tp tuple completely
del food_stuff_tp

# 07 - Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('nordic countries', nordic_countries)

# Check if 'Estonia' is a nordic country
country_search = 'Estonia'
print(f'Is {country_search} a nordic country?: {country_search in nordic_countries} ')


# Check if 'Iceland' is a nordic country
country_search = 'Iceland'
print(f'Is {country_search} a nordic country?: {country_search in nordic_countries} ')




# 01 - Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
print('''
--- 01 ---''')
age = int(input('Ingrese su edad: '))
var = 'años'
if 18-age == 1:
    var = 'año'
if age >= 18:
    print('Tienes edad suficiente para manejar.')    
else:
    print(f'Eres menor de edad. En {18-age} {var} podrás manejar.')

# 02 - Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
print('''
--- 02 ---''')
my_age = 20
your_age = int(input('Ingrese su edad: '))
if your_age > my_age:
    print('Eres mayor que yo.')
elif your_age < my_age:
    print('Eres menor que yo.')
else:
    print('Tenemos la misma edad.')

# 03 - Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
print('''
--- 03 ---''')
num_one = int(input('Ingrese el primer número: '))
num_two = int(input('Ingrese el segundo número: '))
if num_one > num_two:
    print(f'{num_one} es mayor que {num_two}.')
elif num_one < num_two:
    print(f'{num_one} es menor que {num_two}.')
else:
    print('Los números ingresados son iguales.')


### Exercises: Level 2
print('''

------ *Level 2* ------''')
# 01 - Write a code which gives grade to students according to theirs scores:
'''
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''
print('''
--- 01 ---''')
nota = int(input('Ingrese su nota: '))
if nota >= 0 and nota <=100:
    if nota >= 80:
        print('Su nota es: A')
    elif nota >= 70:
        print('Su nota es: B')
    elif nota >= 60:
        print('Su nota es: C')
    elif nota >= 50:
        print('Su nota es: D')
    else:
        print('Su nota es: F')
else:
    print('Ingrese un número del 0 al 100.')    

# 02 - Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
print('''
--- 03 ---''')
season = str(input('Ingrese el mes: '))
primavera = ['septiembre','octubre','noviembre']
verano = ['diciembre','enero','febrero']
otoño = ['marzo','abril','mayo']
invierno = ['junio','julio','agosto']
if season in primavera:
    print('Estás en primavera.')
elif season in verano:
    print('Estás en verano.')
elif season in otoño:
    print('Estás en otoño.')
elif season in invierno:
    print('Estás en invierno.')
else:
    print('Ingrese un mes válido, en minúsculas.')    

# 03 - The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
print('''
--- 03 ---''')
print('Lista de frutas:', fruits)
fruta = str(input('Ingrese una fruta: '))
if fruta in fruits:
    print('La fruta ya existe en la lista.')
else:
    fruits.append(fruta)
    print('Lista de frutas:', fruits)


### Exercises: Level 3
print('''

------ *Level 3* ------''')
# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 01 - Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
print('''
--- 01 ---''')
if 'skills' in person:
    skills_mid_i = len(person.get('skills')) // 2
    print('Skill del medio:', person.get('skills')[skills_mid_i])
else:
    print('La persona no tiene skills.')

# 02 - Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
print('''
--- 02 ---''')
if 'skills' in person:
    if 'Python' in person.get('skills'):
        print('La persona tiene skills, incluyendo el de Python.')
    else:
        print('La persona tiene skills, pero no el de Python.')
else:
    print('La persona no tiene skills.')

# 03 - If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
print('''
--- 03 ---''')
front_end = ['JavaScript','React']
back_end = ['Node', 'Python', 'MongoDB']
fullstack = ['React', 'Node', 'MongoDB']
if set(front_end).issubset(person.get('skills')) and len(person.get('skills'))==2:
    print('He is a front end developer.')
elif set(fullstack).issubset(person.get('skills')):
    print('He is a fullstack developer.')
elif set(back_end).issubset(person.get('skills')):
    print('He is a backend developer.')
else:
    print('unknown title')

# 04 - If the person is married and if he lives in Finland, print the information in the following format:     
# Asabeneh Yetayeh lives in Finland. He is married.
print('''
--- 04 ---''')
if person['is_marred'] and person['country'] == 'Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married. ')
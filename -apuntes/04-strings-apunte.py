
#Multiline string 
multiline_string = '''Hola !
Esto es ...
un texto de múltiples líneas !'''
print(multiline_string)


# String Concatenation
first_name = 'Loca'
last_name = 'Isaura'
space = ' '
full_name = first_name  +  space + last_name
print('El nombre de mi gatita es: ', full_name)


# Escape Sequences in Strings
print('''
----- Escape Sequences in Strings -----''') 
# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")
print('This is \na line break') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t2\t5')
print('Day 2\t6\t8')
print('Day 3\t4\t6')
print('Day 4\t5\t7')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# String formatting - New Style String Formatting (str.format)
print('''
----- String Formatting -----''') 
saludo = 'Hola'
nombre = 'Sofi'
lenguaje = 'Python'
formated_string = '{}! mi nomnre es {}. Estoy aprendiendo {}'.format(saludo, nombre, lenguaje)
print(formated_string)

a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

radio = 10
pi = 3.14
area = pi * radio ** 2
formated_string = 'El área de un círculo con un radio de {} es {:.2f}.'.format(radio, area) # 2 digits after decimal
print(formated_string)


# String Interpolation
print('''
----- String Interpolation -----''') 
a = 2
b = 4
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')


# Python Strings as Sequences of Characters
# Unpacking Characters
print('''
----- Unpacking Characters -----''')
lenguaje = 'Python'
a,b,c,d,e,f = lenguaje # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Accessing Characters in Strings by Index
print('''
----- Accessing by Index -----''')
lenguaje = 'Python'
first_letter = lenguaje[0]
print(first_letter) # P
second_letter = lenguaje[1]
print(second_letter) # y
last_index = len(lenguaje) - 1
last_letter = lenguaje[last_index]
print(last_letter) # n

# If we want to start from right end we can use negative indexing. -1 is the last index.
print('''
----- from right end with negative index -----''')
lenguaje = 'Python'
last_letter = lenguaje[-1]
print(last_letter) # n
second_last = lenguaje[-2]
print(second_last) # o

# Slicing Python Strings
print('''
----- Slicing Python Strings -----''')
lenguaje = 'Python'
first_three = lenguaje[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = lenguaje[3:6]
print(last_three) # hon
# Another way
last_three = lenguaje[-3:]
print(last_three)   # hon
last_three = lenguaje[3:]
print(last_three)   # hon

# Reversing a String
print('''
----- Reversing a String -----''')
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

# Skipping Characters While Slicing
print('''
----- Skipping Characters While Slicing -----''')
lenguaje = 'Python'
pto = lenguaje[0:6:2] #
print(pto) # Pto


# String Methods
print('''
**
----- String Methods -----''')

# capitalize(): Converts the first character of the string to capital letter
challenge = 'thirty days of python'
print('capitalize :', challenge.capitalize()) # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count
challenge = 'thirty days of python'
print('count \"y\": ', challenge.count('y')) # 3
print('count \"y, 7 ,14\": ', challenge.count('y', 7, 14)) # 1, 
print('count \"th\": ', challenge.count('th')) # 2

# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print('ends with \"on\"?: ', challenge.endswith('on'))   # True
print('ends with \"tion\"?: ', challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print('expandtabs: ', challenge.expandtabs())   # 'thirty  days    of      python'
print('expandtabs: ', challenge.expandtabs(10)) # 'thirty    days      of        python'

#find(): Returns the index of the first occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print('find \"y\": ', challenge.find('y'))  # 5
print('find \"th\": ', challenge.find('th')) # 0

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print('rfind \"y\": ', challenge.rfind('y'))  # 16
print('rfind \"th\": ', challenge.rfind('th')) # 17

# format(): formats string into a nicer output
# como en los ejemplos de arriba

# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
challenge = 'thirty days of python'
sub_string = 'da'
print('index \"da\": ', challenge.index(sub_string))  # 7
# print('index \"da, 9\": ', challenge.index(sub_string, 9)) # ValueError

# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print('index \"da\": ', challenge.rindex(sub_string))  # 8
# print('index \"da, 9\": ', challenge.rindex(sub_string, 9)) # ValueError

# isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print('is alphanumeric?', challenge, ': ', challenge.isalnum()) # True

challenge = '30DaysPython'
print('is alphanumeric?', challenge, ': ', challenge.isalnum()) # True

challenge = 'thirty days of python'
print('is alphanumeric?', challenge, ': ', challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print('is alphanumeric?', challenge, ': ', challenge.isalnum()) # False

# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print('is alpha?', challenge, ': ', challenge.isalpha()) # False, space is once again excluded

challenge = 'ThirtyDaysPython'
print('is alpha?', challenge, ': ', challenge.isalpha()) # True

num = '123'
print('is alpha?', challenge, ': ', num.isalpha())      # False

# isdecimal(): Checks if all characters in a string are decimal (0-9)
challenge = 'thirty days of python'
print('is decimal?', challenge, ': ', challenge.isdecimal())  # False

challenge = '123'
print('is decimal?', challenge, ': ', challenge.isdecimal())  # True

challenge = '\u00B2'
print('is decimal?', challenge, ': ', challenge.isdigit())   # False

challenge = '12 3'
print('is decimal?', challenge, ': ', challenge.isdecimal())  # False, space not allowed

# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = 'Thirty'
print('is digit?', challenge, ': ', challenge.isdigit()) # False

challenge = '30'
print('is digit?', challenge, ': ', challenge.isdigit())   # True

challenge = '\u00B2'
print('is digit?', challenge, ': ', challenge.isdigit())   # True

# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print('is numeric?', challenge, ': ', num.isnumeric()) # True

num = '\u00BD' # ½
print('is numeric?', challenge, ': ', num.isnumeric()) # True

num = '10.5'
print('is numeric?', challenge, ': ', num.isnumeric()) # False

# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print('is indentifier?', challenge, ': ', challenge.isidentifier()) # False, because it starts with a number

challenge = 'thirty_days_of_python'
print('is indentifier?', challenge, ': ', challenge.isidentifier()) # True

# islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print('is lower?', challenge, ': ', challenge.islower()) # True

challenge = 'Thirty days of python'
print('is lower?', challenge, ': ', challenge.islower()) # False

# isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print('is upper?', challenge, ': ', challenge.isupper()) #  False

challenge = 'THIRTY DAYS OF PYTHON'
print('is upper?', challenge, ': ', challenge.isupper()) # True

# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print('concatenated string: ', result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print('concatenated string: ', result) # 'HTML# CSS# JavaScript# React'

# strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print('strip', challenge, ': ', challenge.strip('noth')) # 'irty days of py'

# replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print('replace', challenge, ': ', challenge.replace('python', 'coding')) # 'thirty days of coding'

# split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print('split', challenge, ': ', challenge.split()) # ['thirty', 'days', 'of', 'python']

challenge = 'thirty, days, of, python'
print('split ,', challenge, ': ', challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# title(): Returns a title cased string
challenge = 'thirty days of python'
print('title', challenge, ': ', challenge.title()) # Thirty Days Of Python

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print('swapcase', challenge, ': ', challenge.swapcase())   # THIRTY DAYS OF PYTHON

challenge = 'Thirty Days Of Python'
print('swapcase', challenge, ': ', challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print('starts with?', challenge, ': ', challenge.startswith('thirty')) # True

challenge = '30 days of python'
print('starts with?', challenge, ': ', challenge.startswith('thirty')) # False

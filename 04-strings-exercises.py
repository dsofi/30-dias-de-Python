# 01 : Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
palabras = ['Thirty', 'Days', 'Of', 'Python']
concatenate = ' '.join(palabras)
print('01-Concatenate:', concatenate) 

# 02 : Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
palabras = ['Coding', 'For' , 'All']
concatenate = ' '.join(palabras)
print('02-Concatenate:', concatenate) 

# 03 : Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# 04 : Print the variable company using print().
print(company)

# 05 : Print the length of the company string using len() method and print().
print('company len :', len(company))

# 06 : Change all the characters to uppercase letters using upper() method.
to_upper = company.upper()
print('uppercase : ', to_upper)

# 07 : Change all the characters lowercase letters using lower() method.
to_lower = company.lower()
print('lowercase : ', to_lower)

# 08 : Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.to_lower = company.lower()
to_capitalize = company.capitalize()
print('capitalize : ', to_capitalize)

to_title = company.title()
print('titlecase : ', to_title)

to_swapcase = company.swapcase()
print('swapcase : ', to_swapcase)

# 09 : Cut(slice) out the first word of Coding For All string.
first_word = company[:6]
print('first word : ', first_word)

# 10 : Check if Coding For All string contains a word Coding using the method index, find or other methods.
to_find = company.find('Coding')
print('Find \"Coding\" index : ', to_find)

to_find = company.index('Coding')
print('Index \"Coding\" index : ', to_find)

print('Contiene la palabra \"Coding\"?', 'Coding' in company)

# 11 : Replace the word coding in the string 'Coding For All' to Python.
to_replace = company.replace('Coding','Python')
print('Replace \"Coding\" to \"Python\": ', to_replace)

# 12 : Change Python for All to Python for Everyone using the replace method or other methods.
to_replace_12 = to_replace.replace('All','Everyone')
print('Replace \"All\" to \"Everyone\": ', to_replace_12)

# 13 : Split the string 'Coding For All' using space as the separator (split()) .
to_split = company.split()
print('Split : ', to_split)

# 14 : "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
texto_ejemplo = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
to_split_comma = texto_ejemplo.split(', ')
print('Split comma : ', to_split_comma)

# 15 : What is the character at index 0 in the string Coding For All.
first_char = company[0]
print('First char in \"Coding For All\": ', first_char)

# 16 : What is the last index of the string Coding For All.
last_index = len(company) - 1
last_char = company[last_index]
print('Last char in \"Coding For All\": ', last_char)

# 17 : What character is at index 10 in "Coding For All" string.
char_index_10 = company[10]
print('Char at index 10 in \"Coding For All\": ', char_index_10)

# 18 : Create an acronym or an abbreviation for the name 'Python For Everyone'.
split_to_replace = to_replace_12.split()
# opción 1 :
abbr = split_to_replace[0][0] + split_to_replace[1][0] + split_to_replace[2][0]
print('Abbreviation for \"Python For Everyone\":', abbr)
# opción 2 :
acronym = "".join([palabra[0] for palabra in split_to_replace])
print('Acronym for \"Python For Everyone\":', acronym)

# 19 : Create an acronym or an abbreviation for the name 'Coding For All'.
acronym_19 = "".join([palabra[0] for palabra in to_split])
print('Acronym for \"Coding For All\":', acronym_19)

# 20 : Use index to determine the position of the first occurrence of C in Coding For All.
position_first_C = company.find('C')
print('Position of the first \"C\": ', position_first_C) 

# 21 : Use index to determine the position of the first occurrence of F in Coding For All.
position_first_F = company.find('F')
print('Position of the first \"F\": ', position_first_F) 

# 22 : Use rfind to determine the position of the last occurrence of l in Coding For All People.
frase_22 = 'Coding For All People'
position_last_l = frase_22.rfind('l')
print('Position of the first \"l\": ', position_last_l) 

# 23 : Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
frase_23 = 'You cannot end a sentence with because because because is a conjunction'
position_first_because = frase_23.find('because')
print('Position of the first \"because\" in', frase_23, ': ', position_first_because) 

# 24 : Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
position_last_because = frase_23.rfind('because')
print('Position of the last \"because\": ', position_last_because) 

# 25 : Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start_i = position_first_because
end_i = position_last_because + len('because')
phrase_sliced = frase_23[start_i:end_i]
print('Sliced phrase becauses: ', phrase_sliced) 

# 26 : Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# es igual a la 23

# 27 : Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# es igual a la 25

# 28 : Does ''Coding For All' start with a substring Coding?
start_with_Coding = company.startswith('Coding')
print('Does \"Coding For All\" start with a substring \"Coding\":', start_with_Coding) 

# 29 : Does 'Coding For All' end with a substring coding?
end_with_coding = company.endswith('coding')
print('Does \"Coding For All\" end with a substring \"coding\":', end_with_coding) 

# 30 : '   Coding For All      '  , remove the left and right trailing spaces in the given string.
frase_30 = '   Coding For All      '
to_strip = frase_30.strip()
print('Remove left and right trailing spaces', frase_30, ':', to_strip) 

# 31 : Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
var_1 = '30DaysOfPython'
var_2 = 'thirty_days_of_python'
is_ident_1 = var_1.isidentifier()
is_ident_2= var_2.isidentifier()
print(f'\"{var_1}\" is identifier? : {is_ident_1}')
print(f'\"{var_2}\" is identifier? : {is_ident_2}')

# 32 : The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
list_with_hash = '# '.join(librerias)
print(list_with_hash)

# 33 : Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge. \nI just wonder what is next.')

# 34 : Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\t\tAge\tCountry\t\tCity')  
print('Asabeneh\t250\tFinland\t\tHelsinki')

# 35 : Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area:.0f} meters square.')

# 36 : Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')



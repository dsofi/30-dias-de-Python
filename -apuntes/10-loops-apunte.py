# Loops

# While Loop
#  It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.
print('---While Loop---')
count = 0
while count < 5:
    print(count)
    count = count + 1       #prints from 0 to 4
# If we are interested to run block of code once the condition is no longer true, we can use else.
print('---Else---')
count = 0
while count < 5:
    print(count)
    count = count + 1  
else:
    print(count)

# Break and Continue - Part 1
print('---Break---')
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

print('---Continue---')
count = 0
while count < 5:
    #if count == 3:
        #continue
    print(count)
    count = count + 1   # Dice que The above while loop only prints 0, 1, 2 and 4 (skips 3). 
    # Pero solo imprime hasta el 2 (?)

# For Loop
# Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
print('---For Loop (list)---')
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:  # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

print('---For Loop (string -1)---')
language = 'Python'
for letter in language:
    print(letter)
    
print('---For Loop (string -2)---')
for i in range(len(language)):
    print(language[i])

print('---For Loop (tuple)---')
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

print('---For Loop (dictionary -keys)---')
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

print('---For Loop (dictionary -keys + values)---')
for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

print('---For Loop (set)---')
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# Break and Continue - Part 2
print('---Break in a For---')
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

print('---Continue in a For---')
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')


# The Range Function
print('---The Range Function---')
# The range() function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

for number in range(11):
    print(number)   # prints 0 to 10, not including 11


# Nested For Loop
print('---Nested For Loop---')
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# For Else
print('---For Else---')
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# Pass
# In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
for number in range(6):
    pass



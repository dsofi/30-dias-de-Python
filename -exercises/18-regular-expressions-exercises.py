# Exercises: Level 1
print('''

--------- * LEVEL 1 * ---------''')
# 01 - What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

import re
from collections import defaultdict
def most_frequent_words(paragraph):
    word_counts = defaultdict(int)
    for word in re.findall(r'\w+', paragraph):
        word_counts[word] += 1
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
print(most_frequent_words(paragraph))
most_freq_word = most_frequent_words(paragraph)[0][0]
print('La palabra más frecuent es:', most_freq_word)

# 02 - Extract these numbers from this whole text and find the distance between the two furthest particles.
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
points = re.findall(r'-?\d+', txt)
points = [int(x) for x in points]
points = sorted(points)
print(points)
distance = points[-1] - points[0]
print('distancia:',distance)


# Exercises: Level 2
print('''

--------- * LEVEL 2 * ---------''')
# 01 - Write a pattern which identifies if a string is a valid python variable
# Debe comenzar con una letra o un guión bajo.
# No puede ser una palabra reservada de Python.
# No puede contener espacios en blanco.
# Sólo puede contener letras, números y guiones bajos.
# No puede ser un número.
pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
def is_valid_variable(string):
    return pattern.match(string) is not None
print(is_valid_variable('first_name'))     # True
print(is_valid_variable('first-name'))     # False
print(is_valid_variable('1first_name'))    # False
print(is_valid_variable('firstname'))      # True

# Exercises: Level 3
print('''

--------- * LEVEL 3 * ---------''')
# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean_text = re.sub('[%@$&#;]', '', sentence)
print(clean_text)
most_freq_word = most_frequent_words(clean_text)[:3]
print(most_freq_word)

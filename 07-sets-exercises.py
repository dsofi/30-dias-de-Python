# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 01 - Find the length of the set it_companies
print('it_comp:', it_companies)
print('length of it_comp:', len(it_companies))

# 02 - Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('add Twitter:', it_companies)

# 03 - Insert multiple IT companies at once to the set it_companies
other_it_comp = ('Accenture', 'SAP', 'TCS', 'DXC', 'Delloite', 'Capgemini')
it_companies.update(other_it_comp)
print('multiple insert:', it_companies)

# 04 - Remove one of the companies from the set it_companies
it_companies.remove('TCS')
print('remove TCS:', it_companies)

# 05 - What is the difference between remove and discard
#  If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
it_companies.discard('algo que no existe')
print('prueba discard:', it_companies)
#it_companies.remove('algo que no existe')
#print('prueba remove error:', it_companies)


# ---
# Exercises: Level 2
print('''
--- LEVEL 2 ---''')
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print ('A:',A)
print ('B:',B)

# 01 - Join A and B
join = A.union(B)
print('01-Join:', join)

# 02 - Find A intersection B
print('02-Intersection', A.intersection(B))

# 03 - Is A subset of B
print('03-A subset of B?:', A.issubset(B))

# 04 - Are A and B disjoint sets
print('04-Are disjointed?:', A.isdisjoint(B))

# 05 - Join A with B and B with A
A.update(B)
print('05-A join with B:', A)
B.update(A)
print('05-B join with A:', B)

# 06 - What is the symmetric difference between A and B
print('06-Symetric dif:', A.symmetric_difference(B))

print('''
--- con los sets originales ---''')
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print ('A:',A)
print ('B:',B)
print('06-Symetric dif:', A.symmetric_difference(B))

# 07 - Delete the sets completely
del A
del B


# ---
# Exercises: Level 3
print('''
--- LEVEL 3 ---''')
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 01 - Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print('age list:', age)
print('01-length list:', len(age),'\n')      # 8 - is bigger
print('age set:', age_set)
print('01-length set:', len(age_set),'\n')   # 5


# 02 - Explain the difference between the following data types: string, list, tuple and set

# String - es una secuencia de caracteres, encerrados entre comillas dobles o simples. Por ejemplo 'hello world' o "hello world" ---TEXT DATA---

# List - es una collection de items, encerrados entre corchetes y se separan por comas. Son editables, se pueden cambiar luego de ser creadas. Por ejemplo [1,2,3,4] o ['hola','mundo'] ---ORDERED COLLECTIONS OF ITEMS---

# Tuple - es similar a la list, pero se encierran con paréntesis. No son editables, no pueden ser cambiadas luego que son creadas. Por ejemplo (1,2,3,4) o ('hola','mundo') ---ORDERED COLLECTION OF ITEMS THAT CANNOT BE CHANGED---

# Set - es una collection desordenada de items únicos, se encierran con llaves y se separan con comas. No admiten valores duplicados. Al ser desordenado no son indexables. Por ejemplo {1,2,3,4} o {'hola','mundo'} ---UNORDERED COLLECTIONS OF UNIQUE ITEMS---


# 03 - I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
frase = 'I am a teacher and I love to inspire and teach people'
split = frase.split()
print('03-split:', split)
print('03-length split:', len(split),'\n')
split_set = set(split)
print('03-split_set:', split_set)
print('03-length split_set:', len(split_set))

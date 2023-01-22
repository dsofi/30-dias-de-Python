# Dictionaries
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# Creating a Dictionary
empty_dict = {}
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# Could be any data types:string, boolean, list, tuple, set or a dictionary.
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

# Dictionary Length
# It checks the number of 'key: value' pairs in the dictionary.
print(len(dct))     # 4
print(len(person))  # 7

# Accessing Dictionary Items
print(dct['key1']) # value1
print(dct['key4']) # value4

print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
# print(person['city'])       # KeyError

# Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

# Adding Items to a Dictionary
dct['key5'] = 'value5'
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

# Modifying Items in a Dictionary
dct['key1'] = 'value-one'
person['first_name'] = 'Eyob'
person['age'] = 252

# Checking Keys in a Dictionary
print('key2' in dct) # True
print('key5' in dct) # False

# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name
print('dct:', dct)
dct.pop('key1') # removes key1 item
print('pop key1:', dct)
dct.popitem() # removes the last item
print('popitem:', dct)
del dct['key2'] # removes key2 item
print('del key2:', dct)

print('---')
print('person:', person)
person.pop('first_name')   # Removes the firstname item
print('pop first name:', person)
person.popitem()           # Removes the job_title item
print('pop item:', person)
del person['is_married']   # Removes the is_married item
print('del is_married:', person)

# Changing Dictionary to a List of Items
# The items() method changes dictionary to a list of tuples.
print('---')
print(dct.items())  # dict_items([('key3', 'value3'), ('key4', 'value4')])

# Clearing a Dictionary
print(dct.clear()) # None

# Deleting a Dictionary
del dct

# Copy a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()

# Getting Dictionary Keys as a List
# The keys() method gives us all the keys of a a dictionary as a list.
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

# Getting Dictionary Values as a List
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])






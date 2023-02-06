
'''
There are four collection data types in Python :
** List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
** Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
** Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
** Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.
'''

# How to Create a List
# Using list built-in function
empty_list = list() # this is an empty list, no item in the list
print('Tamaño de lista vacía:', len(empty_list)) # 0
# Using square brackets, []
empty_list = [] # this is an empty list, no item in the list
print('Tamaño de lista vacía:', len(empty_list)) # 0

#Lists with initial values. We use len() to find the length of a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
animal_products = ['milk', 'meat', 'butter', 'yoghurt'] 
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] 
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Lists can have items of different data types
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]

# Accessing List Items Using Positive Indexing
first_fruit = fruits[0] # we are accessing the first item using its index
print('first_fruit :',first_fruit)
second_fruit = fruits[1]
print('second_fruit :',second_fruit)
last_fruit = fruits[3]
print('last_fruit :',last_fruit) 
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing List Items Using Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.
last_fruit = fruits[-1]
second_last = fruits[-2]
print('last_fruit :',last_fruit)     
print('second_last :',second_last)     


# Unpacking List Items
print('''
----- Unpacking List Items -----''') 

# First Example
lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print('first_item :',first_item)      # item1
print('second_item :',second_item)    # item2
print('third_item :',third_item)      # item3
print('rest :',rest)                  # ['item4', 'item5']

# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)       # Germany
print(fr)       # France
print(bg)       # Belgium
print(sw)       # Sweden
print(scandic)  # ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es)       # Estonia


# Slicing Items from a List
print('''
----- Slicing Items from a List -----''') 
# Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

# Negative Indexing: We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']


# Modifying Lists
print('''
----- Modifying Lists -----''')
fruits[0] = 'avocado'
print('modificando primer elemento:',fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print('modificando segundo elemento:',fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print('modificando ultimo elemento:',fruits)        #  ['avocado', 'apple', 'mango', 'lime']


# Checking Items in a List
print('''
----- Checking Items in a List -----''')
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print('does exist \"banana\" in fruits?',does_exist)  # True
does_exist = 'lime' in fruits
print('does exist \"lime\" in fruits?',does_exist)  # False


# Adding Items to a List
print('''
----- Adding Items to a List -----''')
# To add item to the end of an existing list we use the method append().
fruits.append('apple')
print('append apple:', fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print('append lime:', fruits)

# Inserting Items into a List
print('''
----- Inserting Items into a List -----''')
# The insert() methods takes two arguments:index and an item to insert.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print('insert apple (2):', fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print('insert lime (3):', fruits)


# Removing Items from a List
print('''
----- Removing Items from a List -----''')
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print('remove banana:', fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print('remove lemon:', fruits)  # ['orange', 'mango', 'banana']

# Removing Items Using Pop
print('''
----- Removing Items Using Pop -----''')
# The pop() method removes the specified index, (or the last item if index is not specified):
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print('pop last:', fruits)       # ['banana', 'orange', 'mango']
fruits.pop(0)
print('pop 0:', fruits)       # ['orange', 'mango']

# Removing Items Using Del
print('''
----- Removing Items Using Del -----''')
# The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
print('frutas:', fruits)
del fruits[0]
print('del[0]:', fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print('del[1]:', fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print('del[1:3]:', fruits)     # ['orange', 'lime']
# del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined

# Clearing List Items
print('''
----- Clearing List Items -----''')
# The clear() method empties the list:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print('clear:', fruits)       # []


# Copying a List
print('''
----- Copying a List -----''')
# It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. But there are lots of case in which we do not like to modify the original instead we like to have a different copy. One of way of avoiding the problem above is using copy().
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print('frutas:', fruits)       # ['banana', 'orange', 'mango', 'lemon']
print('copia:', fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']


# Joining Lists
print('''
----- Joining Lists -----''')
# Plus Operator (+)
# list3 = list1 + list2
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print('vegetales:', vegetables)
print('frutas y vegetales con (+):', fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

# Joining using extend() method The extend() method allows to append list in a list.
# list1.extend(list2)
fruits.extend(vegetables)
print('frutas y vegetales con extend():', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']


# Counting Items in a List
print('''
----- Counting Items in a List -----''')
print('count orange:', fruits.count('orange'))   # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print('edades:', ages)
print('count 24:', ages.count(24))           # 3


# Finding Index of an Item
print('''
----- Finding Index of an Item -----''')
print('index orange:', fruits.index('orange'))   # 1
print('index 24:', ages.index(24))           # 2, the first occurrence


# Reversing a List
print('''
----- Reversing a List -----''')
fruits.reverse()
print('fruit reverse:', fruits) # ['lemon', 'mango', 'orange', 'banana']

ages.reverse()
print('edades reverse:', ages) # [24, 25, 24, 26, 25, 24, 19, 22]


# Sorting List Items
print('''
----- Sorting List Items -----''')
# To sort lists we can use sort() method or sorted() built-in functions. The sort() method reorders the list items in ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.
# syntax
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending

# sort(): this method modifies the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print('frutas sort asc', fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print('frutas sort desc', fruits)            # ['orange', 'mango', 'lemon', 'banana']

ages.sort()
print('edad sort asc', ages) #  [19, 22, 24, 24, 24, 25, 25, 26]
ages.sort(reverse=True)
print('edad sort desc', ages) #  [26, 25, 25, 24, 24, 24, 22, 19]

# sorted(): returns the ordered list without modifying the original list.
fruits = ['banana', 'orange', 'mango', 'lemon']
print('------frutas inicio:', fruits) 
print('frutas sorted asc', sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
print('------frutas medio:', fruits) 
# Reverse order
fruits_sorted = sorted(fruits,reverse=True)
print('frutas sort desc', fruits_sorted)     # ['orange', 'mango', 'lemon', 'banana']
print('------frutas final:', fruits) 





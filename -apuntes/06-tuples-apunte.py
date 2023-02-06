
# Tuples
#  collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, ().

# Creating Empty tuple: Creating an empty tuple
empty_tuple = ()
empty_tuple = tuple() # or using the tuple constructor

# Creating Tuple with initial values
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

# Tuple length
len(tpl)
len(fruits)

# Accessing Tuple Items
first_item = tpl[0]
second_item = tpl[1]

first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

# Negative indexing Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last and the negative of the list/tuple length refers to the first item.
first_item = tpl[-3]
second_item = tpl[-2]

first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

# Slicing tuples
all_items = tpl[0:4]            # all items
all_items = tpl[0:]             # all items
middle_two_items = tpl[1:3]     # does not include item at index 3

all_fruits = fruits[0:4]        # all items
all_fruits= fruits[0:]          # all items
orange_mango = fruits[1:3]      # doesn't include item at index 3
orange_to_the_rest = fruits[1:]


# Changing Tuples to Lists
# We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.
lst = list(tpl)

fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']

fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# Checking an Item in a Tuple
print('item2' in tpl)       # True
print('orange' in fruits)   # True
print('banana' in fruits)   # False
# fruits[0] = 'apple'       # TypeError: 'tuple' object does not support item assignment

# Joining Tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

# Deleting Tuples
# It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
del tpl
del fruits
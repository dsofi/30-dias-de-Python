# Sets
# Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

# Creating an empty set
st = {}
st = set()

# Creating a set with initial items
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('set:', fruits)

# Getting Set's Length
len(fruits)

# Accessing Items in a Set
# We use loops to access items. We will see this in loop section

# Checking an Item
print('existe mango?:', 'mango' in fruits ) # True

# Adding Items to a Set
# Once a set is created we cannot change any items and we can also add additional items.
fruits.add('lime')
print('add:', fruits)


# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print('update with vegetables:', fruits)

# Removing Items from a Set
# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
fruits.remove('onion')
print('remove onion:', fruits)

# The pop() methods remove a random item from a list and it returns the removed item.
fruits.pop()    # removes a random item from the set
print('pop:', fruits)

# If we are interested in the removed item.
removed_item = fruits.pop() 
print('removed item:', removed_item)

# Clearing Items in a Set
fruits.clear()
print(fruits) # set()

# Deleting a Set
del fruits

# Converting List to Set
# Converting list to set removes duplicates and only unique items will be reserved.
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
print('List fruits:', fruits)
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
print('Set fruits:', fruits)

# Joining Sets
# Union This method returns a new set
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fru_veg = fruits.union(vegetables)
print('union fruits + vegetables:', fru_veg)

# Update This method inserts a set into a given set
fruits.update(vegetables)
print('update fruits + vegetables:', fruits)

# Finding Intersection Items
# Intersection returns a set of items which are in both the sets. 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}

# Checking Subset and Super Set
# A set can be a subset or super set of other sets:
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

# Checking the Difference Between Two Sets
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}

# Finding Symmetric Difference Between Two Sets
# It returns the the symmetric difference between two sets. It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

# Joining Sets
# If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False

odd_numbers = {0, 2, 4 ,6, 8}
even_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}




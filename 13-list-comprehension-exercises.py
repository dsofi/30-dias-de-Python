# Exercises: Level 1
print('''

--------- * LEVEL 1 * ---------
''')

# 01 - Filter only negative and zero in the list using list comprehension
print('-- Exercise 1 --')
numbers = [-4, -3, -2, -1, 0, 2, 4, 6, -8]
filt_neg_and_zero = [i for i in numbers if i<=0]
print(filt_neg_and_zero)

# 02 - Flatten the following list of lists of lists to a one dimensional list :
print('-- Exercise 2 --')
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [i for row in list_of_lists for second in row for i in second]
print(flatten)

# 03 - Using list comprehension create the following list of tuples:
print('-- Exercise 3 --')
lst_of_tuples = [(i,1,i,i*i,i**3,i**4,i**5) for i in range(11)]
for i in lst_of_tuples:
    print(i)

# 04 - Flatten the following list to a new list:
print('-- Exercise 4 --')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat = [[i[0][0].upper(), i[0][0][0:3].upper(), i[0][1].upper()] for i in countries]
print(flat)

# 05 - Change the following list to a list of dictionaries:
print('-- Exercise 5 --')
lst_dct = [{'country':i[0][0].upper(), 'city':i[0][1]} for i in countries]
for i in lst_dct:
    print(i)

# 06 - Change the following list of lists to a list of concatenated strings:
print('-- Exercise 6 --')
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
conc_strings = [i[0][0] + ' ' + i[0][1] for i in names]
print(conc_strings)

# 07 - Write a lambda function which can solve a slope or y-intercept of linear functions.
print('-- Exercise 7 --')

slope = lambda x1, y1, x2, y2 : (y2 - y1) / (x2 - x1)
print(slope(0,0,4,8))

y_intercept = lambda x, y, m: y - (m * x)
print(y_intercept(3,9,2))


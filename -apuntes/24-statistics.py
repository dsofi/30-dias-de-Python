# Statistics
# Statistics is the discipline that studies the collection, organization, displaying, analysing, interpretation and presentation of data. Statistics is a branch of Mathematics that is recommended to be a prerequisite for data science and machine learning. Statistics is a very broad field but we will focus in this section only on the most relevant part. After completing this challenge, you may go onto the web development, data analysis, machine learning and data science path. Whatever path you may follow, at some point in your career you will get data which you may work on. Having some statistical knowledge will help you to make decisions based on data, data tells as they say.

# Data
# What is data? Data is any set of characters that is gathered and translated for some purpose, usually analysis. It can be any character, including text and numbers, pictures, sound, or video. If data is not put in a context, it doesn't make any sense to a human or computer. To make sense from data we need to work on the data using different tools.

# The work flow of data analysis, data science or machine learning starts from data. Data can be provided from some data source or it can be created. There are structured and unstructured data.

# Data can be found in small or big format. Most of the data types we will get have been covered in the file handling section.

# Statistics Module
# The Python statistics module provides functions for calculating mathematical statistics of numerical data. The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy, or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab. It is aimed at the level of graphing and scientific calculators.

# NumPy
# In the first section we defined Python as a great general-purpose programming language on its own, but with the help of other popular libraries as(numpy, scipy, matplotlib, pandas etc) it becomes a powerful environment for scientific computing.

# NumPy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with arrays.

# So far, we have been using vscode but from now on I would recommend using Jupyter Notebook. To access jupyter notebook let's install anaconda. If you are using anaconda most of the common packages are included and you don't have install packages if you installed anaconda.

# pip install numpy


# Importing NumPy
# Jupyter notebook is available if your are in favor of jupyter notebook (https://github.com/Asabeneh/data-science-for-everyone/blob/master/numpy/numpy.ipynb)
import numpy as np
# How to check the version of the numpy package
print('numpy:', np.__version__)
# Checking the available methods
print(dir(np))


# Creating numpy array using

# Creating int numpy arrays
python_list = [1,2,3,4,5]   # Creating python List
print('Type:', type (python_list)) # <class 'list'>
print(python_list) # [1, 2, 3, 4, 5]

# Creating Numpy(Numerical Python) array from python list
numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1 2 3 4 5])


# Creating float numpy arrays from list with a float data type parameter
numpy_array_from_list2 = np.array(python_list, dtype=float)
print(numpy_array_from_list2) # array([1. 2. 3. 4. 5.])


# Creating boolean numpy arrays from list
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False  True  True False False])


# Creating multidimensional array using numpy
# A numpy array may have one or multiple rows and columns
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list)) # <class 'numpy.ndarray'>
print(numpy_two_dimensional_list)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
 '''


 # Converting numpy array to list
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())


# Creating numpy array from tuple
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]


# Shape of numpy array
# The shape method provide the shape of the array as a tuple. The first is the row and the second is the column. If the array is just one dimensional it returns the size of the array.
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)

print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)

three_by_four_array = np.array([[0, 1, 2, 3],
    [4,5,6,7],
    [8,9,10, 11]])
print(three_by_four_array)
print('shape of three_by_four_array: ',three_by_four_array.shape)


# Data type of numpy array
# Type of data types: str, int, float, complex, bool, list, None
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)      # int32
print(float_array)
print(float_array.dtype)    # float64


# Size of a numpy array
# In numpy to know the number of items in a numpy array list we use size
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 9



# Mathematical Operation using numpy
# NumPy array is not like exactly like python list. To do mathematical operation in Python list we have to loop through the items but numpy can allow to do any mathematical operation without looping. Mathematical Operation:

# Addition (+)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
math_op_result = numpy_array_from_list  + 10
print(math_op_result) # [11 12 13 14 15]

# Subtraction (-)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
math_op_result = numpy_array_from_list  - 10
print(math_op_result) # [-9 -8 -7 -6 -5]

# Multiplication (*)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
math_op_result = numpy_array_from_list * 10
print(math_op_result) # [10 20 30 40 50]

# Division (/)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
math_op_result = numpy_array_from_list / 10
print(math_op_result) # [0.1 0.2 0.3 0.4 0.5]

# Modules (%)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
math_op_result = numpy_array_from_list % 3
print(math_op_result) # [1 2 0 1 2]

# Floor Division(//)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
math_op_result = numpy_array_from_list // 10
print(math_op_result) # [0 0 0 0 0]

# Exponential(**)
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
math_op_result = numpy_array_from_list  ** 2
print(math_op_result) # [ 1  4  9 16 25]


# Checking data types
numpy_int_arr = np.array([1,2,3,4]) 
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype)    # int32
print(numpy_float_arr.dtype)  # float64
print(numpy_bool_arr.dtype)   # bool



# Converting types
# We can convert the data types of numpy array

# Int to Float
numpy_float_arr = np.array([1,2,3,4], dtype = 'float')
print(numpy_float_arr) # [1. 2. 3. 4.]
print(numpy_float_arr.dtype)

# Float to Int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
print(numpy_int_arr) # [1 2 3 4]
print(numpy_int_arr.dtype)

# Int to boolean
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_bool_arr) # [ True  True False  True  True  True]
print(numpy_bool_arr.dtype)

# Int to str
numpy_str_arr = np.array([1,2,3,4]).astype('str') 
print(numpy_str_arr)        # ['1' '2' '3' '4']
print(numpy_str_arr.dtype)  # <U11

# Float to str
numpy_str_arr = np.array([1., 2., 3., 4.]).astype('str')
print(numpy_str_arr)        # ['1.0' '2.0' '3.0' '4.0']
print(numpy_str_arr.dtype)  # <U32


# Multi-dimensional Arrays
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type(two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)


# Getting items from a numpy array
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)


# Slicing Numpy array
# Slicing in numpy is similar to slicing in python list
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)


# How to reverse the rows and the whole array?
print(two_dimension_array[::])

# Reverse the row and column positions
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(two_dimension_array[::-1,::-1])


# How to represent missing values ?
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)

numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)

numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)

twoes = numpy_ones * 2
print(twoes)


# Reshape
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)
flattened = reshaped.flatten()
print(flattened)


## Horitzontal Stack
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print('suma:', np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))

## Vertical Stack
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))



# Generating Random Numbers

# Generate a random float  number
random_float = np.random.random()
print(random_float)

random_floats = np.random.random(5)
print(random_floats)

# Generating a random integers between 0 and 10
random_int = np.random.randint(0, 11)
print(random_int)

# Generating a random integers between 2 and 11, and creating a one row array
random_int = np.random.randint(2,10, size=4)
print(random_int)

# Generating a random integers between 0 and 10
random_int = np.random.randint(2,10, size=(3,3))
print(random_int)

# np.random.normal(mu, sigma, size)
# mu: media de la distribución normal. 
# sigma: desviación estándar de la distribución normal. 
# size: tamaño del array a generar. 
normal_array = np.random.normal(79, 15, 80)
print(normal_array)


'''
# Numpy and Statistics
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)
'''


# Matrix in numpy
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)


# Numpy numpy.arange()
# What is Arrange?
# Sometimes, you want to create values that are evenly spaced within a defined interval. For instance, you want to create values from 1 to 10; you can use numpy.arange() function
lst = range(0, 11, 2) # creating list using range(starting, stop, step)
print(lst)
for l in lst:
    print(l)

# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)

odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)

even_numbers = np.arange(2, 20, 2)
print(even_numbers)


# Creating sequence of numbers using linspace
# numpy.linspace()
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
linspace = np.linspace(1.0, 5.0, num=10)
print(linspace)

# not to include the last value in the interval
linspace_notend = np.linspace(1.0, 5.0, num=5, endpoint=False)
print(linspace_notend)

# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.
# Syntax:
# numpy.logspace(start, stop, num, endpoint)
logspace = np.logspace(2, 4.0, num=4)
print(logspace)


# to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)
print(x)
print(x.itemsize)



# # indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1,2,3), (4,5,6)])
print(np_list)
print('First row: ', np_list[0])
print('Second row: ', np_list[1])
print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])



# NumPy Statistical Functions with Example
# NumPy has quite useful statistical functions for finding minimum, maximum, mean, median, percentile,standard deviation and variance, etc from the given elements in the array. The functions are explained as follows − Statistical function Numpy is equipped with the robust statistical function as listed below

# Numpy Functions
# Min np.min()
# Max np.max()
# Mean np.mean()
# Median np.median()
# Varience
# Percentile
# Standard deviation np.std()

np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)

## min, max, mean, median, sd
print('min: ', np_normal_dis.min())
print('max: ', np_normal_dis.max())
print('mean: ',np_normal_dis.mean())
# print('median: ', np_normal_dis.median())
print('sd: ', np_normal_dis.std())

print(two_dimension_array)
print('=== Col ==')
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))


# How to create repeating sequences?
a = [1,2,3]

# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))


# How to generate random numbers?
# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random ## ?
print(one_random_num)

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

## Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
print(rand)

# Random integers between [0, 10) of shape 5,3
rand_int = np.random.randint(0, 10, size=[5,3])
print(rand_int)


'''
from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()
'''

# numpy.dot(): Dot Product in Python using Numpy
# Dot Product
# Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot

# Syntax
# numpy.dot(x, y, out=None)

## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,6])
### 1*4+2*5 + 3*6
print(np.dot(f, g))  # 32


# NumPy Matrix Multiplication with np.matmul()
### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5 + 2*7 = 19
### 1*6 + 2*8 = 22
### 3*5 + 4*7 = 43
### 3*6 + 4*8 = 50
print(np.matmul(h, i)) ### [[19 22] [43 50]]


## Determinant 2*2 matrix
### 5*8-7*6np.linalg.det(i)
print(np.linalg.det(i))

Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)

new_list = [ x + 2 for x in range(0, 11)]
print(new_list)

np_arr = np.array(range(0, 11))
print(np_arr + 2)


# We use linear equation for quantities which have linear relationship. Let's see the example below:
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)

'''
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
'''

# To draw the Gaussian normal distribution using numpy. As you can see below, the numpy can generate random numbers. To create random sample, we need the mean(mu), sigma(standard deviation), mumber of data points.
'''
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()
'''


# Summery
# To summarize, the main differences with python lists are:

# Arrays support vectorized operations, while lists don’t.
# Once an array is created, you cannot change its size. You will have to create a new array or overwrite the existing one.
# Every array has one and only one dtype. All items in it should be of that dtype.
# An equivalent numpy array occupies much less space than a python list of lists.
# numpy arrays support boolean indexing.
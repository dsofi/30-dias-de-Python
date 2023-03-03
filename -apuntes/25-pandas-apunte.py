# Installing Pandas
# For Mac:
""" 
pip install conda
conda install pandas
"""
# For Windows:
""" 
pip install conda
pip install pandas
"""

# Pandas data structure is based on Series and DataFrames.
# A series is a column and a DataFrame is a multidimensional table made up of collection of series. In order to create a pandas series we should use numpy to create a one dimensional arrays or a python list.
import pandas as pd
import numpy  as np

# Creating Pandas Series with Default Index
nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

# Creating Pandas Series with custom index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# Creating Pandas Series from a Dictionary
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s)

# Creating a Constant Pandas Series
s = pd.Series(10, index = [1, 2, 3])
print(s)

# Creating a Pandas Series Using Linspace
s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)

# DataFrames
# Creating DataFrames from List of Lists
data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

# Creating DataFrame Using Dictionary
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

# Creating DataFrames from a List of Dictionaries
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)

# Reading CSV File Using Pandas
df = pd.read_csv('data\weight-height.csv')
print(df)

# Data Exploration
# Let us read only the first 5 rows using head()
print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method

# Let us also explore the last recordings of the dataframe using the tail() methods.
print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method

# As you can see the csv file has three rows: Gender, Height and Weight. If the DataFrame would have a long rows, it would be hard to know all the columns. Therefore, we should use a method to know the colums. we do not know the number of rows. Let's use shape meathod.
print(df.shape) # as you can see 10000 rows and three columns

# Let us get all the columns using columns.
print(df.columns)

# Now, let us get a specific column using the column key
heights = df['Height'] # this is now a series
print(heights)

weights = df['Weight'] # this is now a series
print(weights)

print(len(heights) == len(weights))

# The describe() method provides a descriptive statistical values of a dataset.
print(heights.describe()) # give statisical information about height data

print(weights.describe())

print(df.describe())  # describe can also give statistical information from a dataFrame

# Similar to describe(), the info() method also give information about the dataset.
print(df.info())


# Modifying a DataFrame
# * We can create a new DataFrame
# * We can create a new column and add it to the DataFrame, 
# * we can remove an existing column from a DataFrame, 
# * we can modify an existing column in a DataFrame, 
# * we can change the data type of column values in the DataFrame

# Creating a DataFrame
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)

# Adding a column to a DataFrame is like adding a key to a dictionary.
# First let's use the previous example to create a DataFrame. After we create the DataFrame, we will start modifying the columns and column values.

# Adding a New Column
# Let's add a weight column in the DataFrame
weights = [74, 78, 69]
df['Weight'] = weights
print(df)
# Let's add a height column into the DataFrame aswell
heights = [173, 175, 169]
df['Height'] = heights
print(df)

# As you can see in the DataFrame above, we did add new columns, Weight and Height. Let's add one additional column called BMI(Body Mass Index) by calculating their BMI using thier mass and height. BMI is mass divided by height squared (in meters) - Weight/Height * Height.
# As you can see, the height is in centimeters, so we shoud change it to meters. Let's modify the height row.
# Modifying column values
df['Height'] = df['Height'] * 0.01
print(df)

# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi    
bmi = calculate_bmi()
df['BMI'] = bmi
print(df)

# Formating DataFrame columns
# The BMI column values of the DataFrame are float with many significant digits after decimal. Let's change it to one significant digit after point.
df['BMI'] = round(df['BMI'], 1)
print(df)

# The information in the DataFrame seems not yet complete, let's add birth year and current year columns.
birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2023, index=[0,1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)

# Checking data types of Column values
print(df.Weight.dtype)

print(df['Birth Year'].dtype) # it gives string object , we should change this to number
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # let's check the data type now

# Now same for the current year:
df['Current Year'] = df['Current Year'].astype('int')
print(df['Current Year'].dtype)

# Now, the column values of birth year and current year are integers. We can calculate the age.
ages = df['Current Year'] - df['Birth Year']
print(ages)

df['Ages'] = ages
print(df)

# The person in the first row lived so far for 251 years. It is unlikely for someone to live so long. Either it is a typo or the data is cooked. So lets fill that data with average of the columns without including outlier.
mean = (38 + 33)/ 2
print('Mean: ',mean)	#it is good to add some description to the output, so we know what is what


# Boolean Indexing
print(df[df['Ages'] > 120])
print(df[df['Ages'] < 120])

# Replace the outlier age with the mean age
df['Ages'].replace(254, mean, inplace=True)
print(df)

# Agregando valores:
nuevas_filas = [{"Name": "Emily", "Country": "USA", "City": "New York", "Weight": 62, "Height": 1.65, "BMI": 22.8, "Birth Year": 1789, "Current Year": 2023, "Ages": 234},
{"Name": "Sofi", "Country": "ARG", "City": "Ciudad", "Weight": 60, "Height": 1.60, "BMI": 23.4, "Birth Year": 1492, "Current Year": 2023, "Ages": 531}]
df = df.append(nuevas_filas, ignore_index=True)
print(df)

# Calculate the mean of the Ages column excluding the outlier
mean = df.loc[df['Ages'] < 120, 'Ages'].mean()

# Replace the values greater than 120 with the mean
df.loc[df['Ages'] > 120, 'Ages'] = mean
print(df)


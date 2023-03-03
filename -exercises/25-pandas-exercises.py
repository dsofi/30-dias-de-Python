# Read the hacker_news.csv file from data directory
import pandas as pd
df = pd.read_csv('data\hacker_news.csv')

# 01 - Get the first five rows
print('01 - First five rows :')
print(df.head(5))

# 02 - Get the last five rows
print('02 - Last five rows :')
print(df.tail(5))

# 03 - Get the title column as pandas series
print('03 - Columns')
s = pd.Series(df.columns)
print(s)

# 04 - Count the number of rows and columns
print('04 - Number of rows and columns')
print(df.shape)

# 05 - Filter the titles which contain python
print('05 - Titles containing python')
tit_py = df[df['title'].str.contains('python', case=False)]
print(tit_py['title'])

# 06 - Filter the titles which contain JavaScript
print('06 - Titles containing JavaScript')
tit_js = df[df['title'].str.contains('JavaScript', case=False)]
print(tit_js['title'])

# 07 - Explore the data and make sense of it
print('07 - Exploring data')
print(df.describe())
print(df['author'].unique())

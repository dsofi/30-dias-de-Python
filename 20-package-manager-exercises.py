import requests

# 01 - Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
print(response)


# 02 - Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
print(response)
##### the min, max, mean, median, standard deviation of cats' weight in metric units.
##### the min, max, mean, median, standard deviation of cats' lifespan in years.
##### Create a frequency table of country and breed of cats



# 03 - Read the countries API and find
url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)
print(response)
##### the 10 largest countries
##### the 10 most spoken languages
##### the total number of languages in the countries API



# 04 - UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
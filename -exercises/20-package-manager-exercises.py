import requests

# 01 - Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
from collections import Counter
print('------------ Ejercicio 1 ------------')
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
txt = response.text
words = txt.split()
words_count = Counter(words)
most_freq = sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:10]
print('Las 10 palabras más frecuentes en Romeo and Juliet :')
for x in most_freq:
    print(x)


# 02 - Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
from statistics import mean, median, stdev
print('------------ Ejercicio 2 parte 1 ------------')
url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cats = response.json()

##### the min, max, mean, median, standard deviation of cats' weight in metric units.
weights = [float(x['weight']['metric'].split(' ')[0]) for x in cats]
min_weight = round(min(weights), 2)
max_weight = round(max(weights), 2)
mean_weight = round(mean(weights), 2)
median_weight = round(median(weights), 2)
stdev_weight = round(stdev(weights), 2)

print(f'min weight : {min_weight} kg.')
print(f'max weight : {max_weight} kg.')
print(f'mean weight : {mean_weight} kg.')
print(f'median weight : {median_weight} kg.')
print(f'stdev weight : {stdev_weight} kg.')


##### the min, max, mean, median, standard deviation of cats' lifespan in years.
print('------------ Ejercicio 2 parte 2 ------------')
lifespans = [(int(x['life_span'].split(' ')[0]) + int(x['life_span'].split(' ')[2])) / 2 for x in cats]
min_lifespan = round(min(lifespans), 2)
max_lifespan = round(max(lifespans), 2)
mean_lifespan = round(mean(lifespans), 2)
median_lifespan = round(median(lifespans), 2)
stdev_lifespan = round(stdev(lifespans), 2)

print(f'min lifespan : {min_lifespan} years.')
print(f'max lifespan : {max_lifespan} years.')
print(f'mean lifespan : {mean_lifespan} years.')
print(f'median lifespan : {median_lifespan} years.')
print(f'stdev lifespan : {stdev_lifespan} years.')

##### Create a frequency table of country and breed of cats
from collections import defaultdict
print('------------ Ejercicio 2 parte 3 ------------')
freq = defaultdict(int)
for cat in cats:
    country = cat['country_code']
    breed = cat['name']
    freq[(country, breed)] +=1
print('Country\tBreed\t\t\tFrequency')
for (country, breed), count in freq.items():
    breed_len = len(breed)
    spaces = '\t' * (3 - (breed_len // 8))
    print(f'{country}\t{breed}{spaces}{count}')

print('------------ Ejercicio 2 parte 3 alternativa ------------')
agrupado = defaultdict(list)
for cat in cats:
    country = cat.get('origin')
    breed = cat.get('name')
    agrupado[country].append(breed)

print('Country\tBreed')
for country, breeds in agrupado.items():
    for breed in breeds:
        print(f'{country}\t{breed}')

print('------------ Ejercicio 2 parte 3 alternativa con pandas ------------')
import pandas as pd
df = pd.DataFrame.from_dict(cats)
grouped = df.groupby('origin')['name'].apply(list)
grouped_df = pd.DataFrame({'origin': grouped.index, 'breeds': grouped.values})
grouped_df['frequency'] = grouped_df['breeds'].apply(lambda x: len(x))

print('Country\t\t\tFrequency\tBreeds')
for i, row in grouped_df.iterrows():
    country_len = len(row.origin)
    spaces = '\t' * (3 - (country_len // 8))
    print(f'{row.origin}{spaces}{row.frequency}\t\t{row.breeds}')


# 03 - Read the countries API and find
print('------------ Ejercicio 3 ------------')
url = 'https://restcountries.eu/rest/v2/all'
#response = requests.get(url)       # no funciona
##### the 10 largest countries
##### the 10 most spoken languages
##### the total number of languages in the countries API



# 04 - UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
print('------------ Ejercicio 4 ------------')
# pip install beautifulsoup4
from bs4 import BeautifulSoup
response = requests.get("https://archive.ics.uci.edu/ml/datasets.php")
links = set()
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    for td in soup.find_all('td'):
        for p in td.find_all('p', class_='normal'):
            for b in p.find_all('b'):
                for a in b.find_all('a'):
                    link = a.text
                    links.add(link)

    print(sorted(links))
else:
    print('No se pudo acceder a la página web')

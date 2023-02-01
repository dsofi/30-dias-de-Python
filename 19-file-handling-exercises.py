# 01 - Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
def count_lines_and_words(file):
    nombre = open(file)
    lines = len(nombre.read().splitlines())
    nombre.close()
    nombre = open(file)
    words = len(nombre.read().split())
    nombre.close()
    return lines, words

# a) Read obama_speech.txt file and count number of lines and words 
lines, words = count_lines_and_words('data/obama_speech.txt')
print(f'''
Obama: 
- cant. de líneas: {lines} 
- cant. de palabras : {words}''')

# b) Read michelle_obama_speech.txt file and count number of lines and words 
lines, words = count_lines_and_words('data/michelle_obama_speech.txt')
print(f'''
Michelle: 
- cant. de líneas: {lines} 
- cant. de palabras : {words}''')

# c) Read donald_speech.txt file and count number of lines and words 
lines, words = count_lines_and_words('data/donald_speech.txt')
print(f'''
Donald: 
- cant. de líneas: {lines} 
- cant. de palabras : {words}''')

# d) Read melina_trump_speech.txt file and count number of lines and words
lines, words = count_lines_and_words('data/melina_trump_speech.txt')
print(f'''
Melina: 
- cant. de líneas: {lines} 
- cant. de palabras : {words}''')


# 02 - Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
from collections import Counter
import json

def most_spoken_lang(file, cant):
    with open (file,"r", encoding='utf-8') as cjson:
        data = json.load(cjson)
        all_lang = [lang for pais in data for lang in pais['languages']]
        lang_count = Counter(all_lang)
        return sorted(lang_count.items(), key=lambda x: x[1], reverse=True)[:cant]    

print('''
------  IDIOMAS MÁS HABLADOS - TOP 10 ------''')
for i in most_spoken_lang('data/countriesdata.json', 10):
    print(i)

print('''
------  IDIOMAS MÁS HABLADOS - TOP 3 ------''')
for i in most_spoken_lang('data/countriesdata.json', 3):
    print(i)

# 03 - Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_popu(file, cant):
    with open (file,"r", encoding='utf-8') as cjson:
        data = json.load(cjson)
        return [{'nombre':x['name'],'popu':format(x['population'], ',').replace(",", ".")} for x in sorted(data, key=lambda x: x['population'], reverse=True)][:cant]    

print('''
------  PAÍSES MÁS POBLADOS - TOP 10 ------''')
for i in most_popu('data/countriesdata.json', 10):
    print(i)

print('''
------  PAÍSES MÁS POBLADOS - TOP 3 ------''')
for i in most_popu('data/countriesdata.json', 3):
    print(i)



# Exercises: Level 2
print('''

--------- * LEVEL 2 * ---------''')
# 04 - Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
def extract_emails(txt):
    email_addresses = []
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    with open(txt, 'r', encoding='utf-8') as txt:
        lines = txt.read().splitlines()
        for line in lines:
            if line.startswith("From "):
                match = re.search(email_pattern, line)
                if match:
                    email_addresses.append(match.group())
    return set(email_addresses)

print('''
------  LISTA DE EMAILS ------''')
for i in extract_emails('data/email_exchanges_big.txt'):
    print(i)
print(f'''
---------------------------------------------
Cantidad de direcciones de email: {len(extract_emails("data/email_exchanges_big.txt"))}
---------------------------------------------
''')


# 05 - Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
import os
def find_most_common_words(txt, cant):
    if os.path.exists(txt):
        with open (txt,"r", encoding='utf-8') as txt:
            palabras = txt.read().split()
    else:
        palabras = txt.split()
    words_count = Counter(palabras)
    return sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:cant]

print('TOP DE PALABRAS MÁS USADAS :')
print('------ Constitución Argentina (20): ')
for i in find_most_common_words('data/constitucion_de_la_nacion_argentina.txt', 20):
    print(i)
print('------ Himno Argentino (10): ')
for i in find_most_common_words('''
Sean eternos los laureles
que supimos conseguir:
Coronados de gloria vivamos
O juremos con gloria morir. Oid ¡mortales! el grito sagrado:
¡Libertad, libertad, libertad!
Oid el ruido de rotas cadenas:
Ved en trono a la noble Igualdad. Se levanta a la faz de la tierra
Una nueva y gloriosa Nación:
Coronada su sien de laureles
Y a su planta rendido un León. Coro De los nuevos campeones los rostros
Marte mismo parece animar;
La grandeza se anida en sus pechos,
A su marcha todo hacen temblar. Se conmueven del Inca las tumbas
Y en sus huesos revive el ardor,
Lo que ve renovando a sus hijos
De la Patria el antiguo esplendor. Coro Pero sierras y muros se sienten
Retumbar con horrible fragor:
Todo el país se conturba con gritos
de venganza, de guerra y furor. En los fieros tiranos la envidia
Escupió su pestífera hiel
Su estandarte sangriento levantan
Provocando a la lid más cruel. Coro ¿No los veis sobre Méjico y Quito
Arrojarse con saña tenaz?
¿Y cual lloran bañados en sangre
Potosí, Cochabamba y la Paz?
¿No los veis sobre el triste Caracas
Luto y llanto y muerte esparcir?
¿No los veis devorando cual fieras
todo pueblo que logran rendir? Coro A vosotros se atreve ¡Argentinos!
El orgullo del vil invasor,
Vuestros campos ya pisa contando
Tantas glorias hollar vencedor. Mas los bravos que unidos juraron
Su feliz libertad sostener. A esos tigres sedientos de sangre
Fuertes pechos sabrán oponer. Coro El valiente argentino a las armas
Corre ardiendo con brío y valor,
El clarín de la guerra cual trueno
En los campos del Sud resonó;
Buenos Aires se pone a la frente
De los pueblos de la ínclita Unión,
Y con brazos robustos desgarran
Al ibérico altivo León. Coro San José, San Lorenzo, Suipacha,
Ambas Piedras, Salta y Tucumán,
La Colonia y las mismas murallas
Del tirano en la Banda Oriental;
Son letreros eternos que dicen:
"Aquí el brazo argentino triunfó."
"Aquí el fiero opresor de la patria
Su cerviz orgullosa dobló." Coro La victoria al guerrero argentino
Con sus alas brillantes cubrió,
Y azorado a su vista el tirano
Con infamia a la fuga se dio;
Sus banderas, sus armas se rinden
Por trofeos a la Libertad.
Y sobre alas de gloria alza el pueblo
Trono digno a su gran majestad. Coro Desde un polo hasta el otro resuena
De la fama el sonoro clarín.
Y de América el nombre enseñado,
Les repite ¡mortales! Oíd:
¡Ya su trono dignísimo abrieron
las Provincias Unidas del Sud!
Y los libres del mundo responden:
¡Al Gran Pueblo Argentino, Salud!
''', 20):
    print(i)


# 06 - Use the function, find_most_frequent_words to find: 
# a) The ten most frequent words used in Obama's speech 
print('Obama -most frequent words : ', find_most_common_words('data/obama_speech.txt', 10))
# b) The ten most frequent words used in Michelle's speech 
print('Michelle -most frequent words : ', find_most_common_words('data/michelle_obama_speech.txt', 10))
# c) The ten most frequent words used in Trump's speech 
print('Donald -most frequent words : ', find_most_common_words('data/donald_speech.txt', 10))
# d) The ten most frequent words used in Melina's speech
print('Melina -most frequent words : ', find_most_common_words('data/melina_trump_speech.txt', 10))


# 07 - Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
import string
def clean_text(txt):
    if os.path.exists(txt):
        with open (txt,"r", encoding='utf-8') as txt:
            txt = txt.read().lower()
    else:
        txt = txt.lower()    
    txt = "".join(x for x in txt if x not in string.punctuation)
    return txt

def remove_support_words(txt):
    from data.stop_words import stop_words  
    words = txt.split()
    words = [word for word in words if word not in stop_words]
    return words

def check_text_similarity(txt1, txt2):
    cl_txt1 = clean_text(txt1)
    cl_txt2 = clean_text(txt2)
    txt1_words = set(remove_support_words(cl_txt1))
    txt2_words = set(remove_support_words(cl_txt2))
    similarity = round(len(txt1_words & txt2_words) / len(txt1_words | txt2_words)*100, 2)
    return similarity

def compare_texts(txt1, txt2, name1, name2):
    similarity = check_text_similarity(txt1, txt2)
    print(f'Similitud entre los textos de {name1} y {name2} : {str(similarity)+"%"}')

compare_texts('data/donald_speech.txt','data/obama_speech.txt','Donald','Obama')
compare_texts('data/michelle_obama_speech.txt','data/melina_trump_speech.txt', 'Michelle','Melina')
compare_texts('data/michelle_obama_speech.txt','data/obama_speech.txt', 'Michelle','Obama')
compare_texts('data/donald_speech.txt','data/melina_trump_speech.txt', 'Donald','Melina')
compare_texts('data/constitucion_de_la_nacion_argentina.txt','data/constitucion_de_la_nacion_argentina.txt', 'Constitución Arg.','Constitución Arg.')
compare_texts('data/obama_speech.txt','data/constitucion_de_la_nacion_argentina.txt','Obama','Constitución Arg.')
compare_texts('data/obama_speech.txt','data/obama_speech_prueba_similitud.txt','Obama','Prueba Obama')


# 08 -Find the 10 most repeated words in the romeo_and_juliet.txt
print('10 palabras mas comunes en Romeo y Julieta : ', find_most_common_words('data/romeo_and_juliet.txt', 10))
print('------------------')
palabras_clean = remove_support_words(clean_text('data/romeo_and_juliet.txt'))
conteo_palabras = Counter(palabras_clean)
palabras_comunes = sorted(conteo_palabras.items(), key=lambda x: x[1], reverse=True)[:10]
print('10 palabras mas comunes en Romeo y Julieta LIMPIO : ', palabras_comunes)


# 09 - Read the hacker news csv file and find out: 
# a) Count the number of lines containing python or Python 
# b) Count the number lines containing JavaScript, javascript or Javascript 
# c) Count the number lines containing Java and not JavaScript
import csv
def count_lines(txt,pattern):
    count = 0
    with open(txt, 'r') as archivo:
        reader = csv.reader(archivo)
        for line in reader:
            line = ' '.join(line)
            if re.search(pattern, line):
                count += 1
    return count
    
print('------------------')

pattern = r'[Pp]ython'
cant_lineas = count_lines('data/hacker_news.csv', pattern)
print(f'Cantidad de líneas que contienen [Pp]ython : ', cant_lineas)

pattern = r'JavaScript|javascript|Javascript'
cant_lineas = count_lines('data/hacker_news.csv', pattern)
print(f'Cantidad de líneas que contienen JavaScript, javascript or Javascript : ', cant_lineas)

pattern = r'Java(?!Script)'
cant_lineas = count_lines('data/hacker_news.csv', pattern)
print(f'Cantidad de líneas que contienen Java and not JavaScript : ', cant_lineas)




    



    

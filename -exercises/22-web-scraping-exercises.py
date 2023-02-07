# 01 - Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)

if response.status_code == 200:
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')    
    section = soup.find('section', class_='facts-categories')
    desc = []
    value = []
    facts_cat = []
    for h in section.find_all('h5'):
        ul = h.find_next_sibling('ul')
        h_desc = []
        h_value = []
        for li in ul.find_all('li'):
            p = li.find('p')
            h_desc.append(p.text)
            span = li.find('span')
            h_value.append(span.text)
        facts = dict(zip(h_desc, h_value))
        facts_cat.append({h.text: facts})
    with open("./data/22-exercise-1.json", "w") as f:
        json.dump(facts_cat, f)
else:
    print("Error al descargar la página")


# 02 - Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)

if response.status_code == 200:
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', {'cellpadding':'5'})
    header = []
    header_row = table.find('tr')
    for td in header_row.find_all('td'):
        header.append(td.text)
    rows = []
    for tr in table.find_all('tr')[1:]:
        row = {}
        for i, td in enumerate(tr.find_all('p')):
            if i < len(header)-1:
                row[header[i]] = td.text.replace("\u00a0", "")
        if row:
            if not any(d.get('Name', None) == row.get('Name', None) for d in rows):
                rows.append(row)
    with open("./data/22-exercise-2.json", "w") as f:
        json.dump(rows, f)


# 03 - Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.




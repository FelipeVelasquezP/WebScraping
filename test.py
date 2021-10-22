from bs4 import BeautifulSoup
import requests
import csv

# Newspaper url's
tiempoURL = "https://www.eltiempo.com/"
espectadorURL = "https://www.elespectador.com/"

# Newspaper HTML
tiempoHTML = requests.get(tiempoURL)
espectadorHTML = requests.get(espectadorURL, timeout=5000, stream=True)

# Conversion HTML to BS
tiempoBS = BeautifulSoup(tiempoHTML.content, 'html.parser')
espectadorBS = BeautifulSoup(espectadorHTML.content, 'html.parser')

# Utils
def normalize(s): #Function to 
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

""" El Tiempo """

#News titles
titleClass = tiempoBS.find_all('a', class_='title')
titles = list()
for title in titleClass:
    titles.append(title.text)


# Category 
categoryClass = tiempoBS.find_all('a', class_='category')
categories = list()

for category in categoryClass:
    currentCategory = category.text
    if currentCategory != currentCategory.upper():
        categories.append(currentCategory)

#News urls

urls = list()

for index, url in enumerate(titleClass):
    scrapedURL = url['href']
    urls.append(scrapedURL)
    txt = scrapedURL.split(sep='/')
    hasCategory = True
 
    for texto in txt:
        normalizeCatedory = normalize(categories[index].lower())
        newTxt = texto.replace('-', ' ')
        if normalizeCatedory in newTxt.split() or normalizeCatedory.split()[0] in newTxt.split():
            hasCategory = False
            break

    if hasCategory: 
        categories.insert(index, "Category Null")



#CSV
fields = ['Category', 'Title', 'Url']
rows = []

for i in range(len(categories)):
    row = [categories[i], titles[i], urls[i]]
    rows.append(row)

with open('El Tiempo.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)
    print("Scraping 'El Tiempo' successful")


""" El Espectador """

#News titles
titleClass = espectadorBS.find_all('h2', class_='Card-Title')
titles = list()

for title in titleClass:
    # title = title.find('a')
    titles.append(title.text)


# News Categries
categoryClass = espectadorBS.find_all('h4', class_='Card-Section')
categories = list()

for category in categoryClass:
    category = category.find('a')
    categories.append(category.text)

# News Urls
urls = list()

for index, url in enumerate(titleClass):
    scrapedURL = url.find('a')['href']
    urls.append(scrapedURL)

    txt = scrapedURL.split(sep='/')
    hasCategory = True
 
    for texto in txt:
        normalizeCatedory = normalize(categories[index].lower())
        newTxt = texto.replace('-', ' ')
        if normalizeCatedory in newTxt.split() or normalizeCatedory.split()[0] in newTxt.split():
            hasCategory = False
            break

    if hasCategory: 
        categories.insert(index, "Category Null")

#CSV
fields = ['Category', 'Title', 'Url']
rows = []

for i in range(len(categories)):
    row = [categories[i], titles[i], urls[i]]
    rows.append(row)

with open('El Espectador.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)
    print("Scraping 'El Espactador' successful")
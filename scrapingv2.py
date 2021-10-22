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

# Lists
titles = list()
categories = list()
urls = list()

def newsTitles (titleClass):
    for title in titleClass:
        titles.append(title.text)

def newsCategories (categoryClass, newspaper = ""):
    for category in categoryClass:
        if newspaper == "ET": category = category.text
        else: category = category.find('a').text
        if category != category.upper():
            categories.append(category)

def newsUrls (urlClass):
    for index, url in enumerate(urlClass): 
        scrapedURL = url.find('a')['href']
        urls.append(scrapedURL)
      
        # Process to check if a news has category
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

def generateCSV(categories, titles, urls, fileName):
    print(len(categories),len(titles), len(urls))
    fields = ['Category', 'Title', 'Url']
    rows = []

    for i in range(len(categories)):
        row = [categories[i], titles[i], urls[i]]
        rows.append(row)

    with open(fileName, 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(rows)
        print("Scraping successful.\nFinal file: ", fileName)

    titles.clear()
    categories.clear()
    urls.clear()

""" El Tiempo """
titleClass = tiempoBS.find_all('a', class_='title')
categoryClass = tiempoBS.find_all('a', class_='category')
urlClass = tiempoBS.find_all('h3', class_='title-container')

# Begins the scraping for "El Tiempo"
newsTitles(titleClass)
newsCategories(categoryClass, "ET")
newsUrls(urlClass)
generateCSV(categories, titles, urls, "El Tiempo.csv")

""" El Espectador """
titleClass = espectadorBS.find_all('h2', class_='Card-Title')
categoryClass = espectadorBS.find_all('h4', class_='Card-Section')

# Begins the scraping for "El Espectador"
newsTitles(titleClass)
newsCategories(categoryClass)
newsUrls(titleClass)

generateCSV(categories, titles, urls, "El Espectador.csv")
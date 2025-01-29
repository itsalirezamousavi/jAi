from bs4 import BeautifulSoup                                                                   # importing libs
import requests

def cityInfo(cityName):                                                                         # info func

    if len(cityName.split()) != 0:
        cityName = cityName.replace(' ','_')

    adress = requests.get(f'https://en.wikipedia.org/wiki/{cityName}')                          # creating url

    soup = BeautifulSoup(adress.text, 'lxml')                                                   # instans of bs4

    paragraphs = soup.find_all('p')                                                             # curling data

    cityInformation = ''
    numberOfParagraph = 5
    for paragraph in paragraphs:                                                                # finding all paragraphs
        if paragraph.text == '' or paragraph.text == '\n':
            continue
        elif not numberOfParagraph:
            break
        else:
            cityInformation += textCleaner(paragraph.text)
            numberOfParagraph -= 1
    
    return cityInformation

def textCleaner(string):                                                                        # cleaning text from ...
    listBasedOnString = string.split()
    for item in listBasedOnString:
        if item[0] == '[' and item[-1] == ']':
            listBasedOnString.remove(item)
    return ' '.join(listBasedOnString)
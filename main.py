import requests
from bs4 import BeautifulSoup

baseUrl = "https://www.vttrando.fr"
uri = "/rando-vtt-departements/rando-vtt-38/"
tempo = ""
tabDonnees = []

response = requests.get(baseUrl+uri)

if response.ok:
    swoup=BeautifulSoup(response.text, 'html.parser')
    
    divs = swoup.findAll("a")
    for div in divs:
        if str(div["href"]) != tempo:
            tempo = str(div["href"])
            if "evenement" in str(div["href"]):
                response = requests.get(div["href"])
                if response.ok:
                    swoup = BeautifulSoup(response.text, 'html.parser')
                    headers = swoup.findAll("header",{"class":"entry-header"})
                    for header in headers:
                        print(header)
                        nomRando = str(header.find('h1'))
                        fin = len(str(nomRando))
                        fin = fin - 5
                        #nomRando[4:fin]
#Ajoute les données dans un tableau
                        tabDonnees.append(nomRando[4:fin])
                        print(tabDonnees)
                        #nom = header[index+5:-1]   
                    with open("F:\DEV\Python\sites.csv","w") as fo:
                        fo.write(div["href"])
                    
    fo.close

for div in divs:
    fo = open("F:\DEV\Python\sites.csv","r")
    #liens = fo.readlines()
    #print(liens)

    for lien in fo:
        #print(lien)
#pk lien bug ?
        response = requests.get(lien)
        print(response)
        if response.ok:
            swoup=BeautifulSoup(response.text, 'html.parser')
#P1 - Récupérer le nom de la sortie
            divs = swoup.findAll("header",{"class":"entry-header"})
            for div in divs:
                print(div)
    fo.close
    #refs = div.findAll("a")
    #divs = swoup.findAll("div",{"class": "js-scroll-to-top-anchor css-6xup2u"})
    



    #print(swoup)

#print(response)

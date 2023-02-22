import requests
from bs4 import BeautifulSoup
import functions

baseUrl = "https://www.vttrando.fr"
uri = "/rando-vtt-departements/rando-vtt-38/"
tempo = ""
tabDonnees = []
recherche = ""

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
                    recherche = "href"
                    tabDonnees.append(functions.decoupage_header(response))
                    # swoupBis = BeautifulSoup(response.text, 'html.parser')
                    # headers = swoupBis.findAll("header",{"class":"entry-header"})
                    # for header in headers:
                    #     print(header)
                    #     nomRando = str(header.find('h1'))
                    #     fin = len(str(nomRando))
                    #     fin = fin - 5
#Ajoute les données dans un tableau
                    #tabDonnees.append(header.text)
                        #print(tabDonnees)
                #print(tabDonnees)
                with open("sites.csv","a+") as fo:
                    fo.write(div["href"]+",")
                    
    fo.close
    print(tabDonnees[1])
    i = 5
    valeur = tabDonnees[i]
    decoupe = ""+valeur[0]
    tabValeurs = []
    # for a in decoupe.split("\n"):
    #     valeur = 
# for div in divs:
#     fo = open("sites.csv","r")
#     #liens = fo.readlines()
#     #print(liens)

#     for lien in fo:
#         #print(lien)
# #pk lien bug ?
#         response = requests.get(lien)
#         print(response)
#         if response.ok:
#             swoup=BeautifulSoup(response.text, 'html.parser')
# #P1 - Récupérer le nom de la sortie
#             divs = swoup.findAll("header",{"class":"entry-header"})
#             for div in divs:
#                 print(div)
#     fo.close
    #refs = div.findAll("a")
    #divs = swoup.findAll("div",{"class": "js-scroll-to-top-anchor css-6xup2u"})
    



    #print(swoup)

#print(response)

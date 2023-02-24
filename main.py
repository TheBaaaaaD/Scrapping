import requests
from bs4 import BeautifulSoup
import csv
import os
from Data import Data

departement = 1
baseUrl = 'https://www.vttrando.fr'
uri = "/rando-vtt-departements/rando-vtt-"


def getEndpoints(swoup):
    liens = []

    refs = swoup.find("div", {"class": "em-view-container"})
    links = refs.findAll("a", {"class": "link-danger"})
    for link in links:
        liens.append(link["href"])
    
    # for link in links:
    #     a = link.find("a")
    #     liens.append(a["href"])
    return liens

def getInfoByPage(swoup):
    infosTriees = [swoup]
    return infosTriees

def swoup(url, process):
    response = requests.get(url)
    if response.ok:
        print("yes")
        soup = BeautifulSoup(response.text, 'html.parser')
        return process(soup)
    return []


def fileReader(file):
    result = []
    with open(file, 'r', encoding="UTF8", newline="") as f:
        reader = csv.DictReader(f)
        for line in reader:
           result.append(line) 
    return result

def fileWriterLinks(file, fieldnames, data):
    with open(file, 'w', encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in data:
            f.write(i+"\n")
    return fileReader(file)

def fileWriterLinksAlreadyExist(file, data):
    with open(file, 'a+', encoding="UTF8", newline="") as f:
        # writer = csv.DictWriter(f, fieldnames=fieldnames)
        # writer.writeheader()
        for i in data:
            f.write(i+"\n")
    return fileReader(file)

def fileWriterData(file, fieldnames, data):
    with open(file, 'w', encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    return fileReader(file)

def tryToCleanOrReturnBlank(str):
    try:
        result = str.getText().strip()
    except:
        result = ''
    return result

# def getElements(lien):
#     data = []
#     response = requests.get(lien)

#     soup = BeautifulSoup(response.text,'html.parser')
#     nom = tryToCleanOrReturnBlank(soup.find("h1"))
#     date = tryToCleanOrReturnBlank(soup.find("span",{"class":"fs-5"}))
#     heure = tryToCleanOrReturnBlank(soup.find("div",{"class":"em-event-time"}))
#     adresse = soup.find("div",{"class":"em-event-location"})
#     typeEvenement = tryToCleanOrReturnBlank(soup.find("ul",{"class":"event-categories"}))
#     informations = tryToCleanOrReturnBlank(soup.find("section",{"class":"em-event-content"}))
#     contacts = tryToCleanOrReturnBlank(soup.find("div",{"class":"border-start ps-3"}))

#     try:
# #Adresses
#         adress = adresse.getText()
#         cleanArrAdress = []
#         for ele in str(adress).split("\n"):
#             if ele != "":
#                     cleanArrAdress.append(ele.strip())
        
#         realAdresse = cleanArrAdress[0] + cleanArrAdress[1]
#         realDepartment = cleanArrAdress[2]
#         realRegion = cleanArrAdress[3]
#         realCountry = cleanArrAdress[4]
#     except:

#         adress = ""
#         realAdress =""
#         realCountry =""
#         cleanArrAdress = []

# #Contacts
#     try:
#         cleanContact = []
#         for ele in str(contacts).split("\n"):
#             if ele != "":
#                     cleanContact.append(ele.strip())

#         del cleanContact[0]        
#         personneContact = cleanArrAdress[0]
#         telephone = cleanContact[1]
#         mail = cleanContact[2]
#         club = cleanContact[3]
#         siteInternet = cleanContact[4]
#     except:   
#         personneContact = ""
#         telephone =""
#         mail =""
#         club = ""
#         siteInternet = ""
#         cleanContact = []

#     adresse = " ".join(cleanArrAdress)

#     cleanInformations = []
#     for ele in str(informations).split("\n"):
#             if ele != "":
#                     cleanInformations.append(ele.lstrip("\n").lstrip(","))
    
#     cleanTypeEvt = []
#     for ele in str(typeEvenement).split("\n"):
#             if ele != "":
#                     cleanTypeEvt.append(ele.lstrip(" "))

#     typeEvenement = " ".join(cleanTypeEvt)

#     informations = " ".join(cleanInformations)
# #passer data en objets
#     fiche = {
#         "nom" : nom,
#         "date" : date,
#         "heure" : heure,
#         "adresse" : adresse,
#         "typeEvenement" : typeEvenement,
#         "departement" : realDepartment,
#         "region" : realRegion,
#         "informations" : informations,
#         "contact" : personneContact,
#         "telephone" : telephone,
#         "mail" : mail,
#         "club" : club,
#         "siteInternet" : siteInternet
#     }
    
#     data.append(fiche)

#     return data

for compteurD in range(1,99):
    if compteurD < 10:
        departement = "0"+str(compteurD)
        response = requests.get(baseUrl + uri + str(departement)+"/")
    else:
        departement = str(compteurD)
        response = requests.get(baseUrl + uri + str(departement)+"/")

    print("réponse = " + str(response))
    if response.ok:
        fields = ['lien']
        liens = []
        infos = []
        liens = swoup(baseUrl + uri + str(departement)+"/",getEndpoints)
        #print(liens)

        print(os.path.exists("links.csv"))

        if os.path.isfile("links.csv"):
            fileWriterLinksAlreadyExist('links.csv', liens)
            print("exist")

        else:
            fileWriterLinks('links.csv', fields, liens)
            print("exist pas")

        lignes = []
        for link in fileReader('links.csv'):
            data = Data(link["lien"])
            data.getElements()
            lignes.extend(data.data)

        fileWriterData('infos.csv',data.fieldsNames,lignes)

        if compteurD == 10:
            exit()        
exit()
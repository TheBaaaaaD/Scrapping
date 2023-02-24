from bs4 import BeautifulSoup
import requests

class Data:
    def __init__(self, lien):
        self.lien = lien
        self.fieldsNames = ["nom","date","heure","adresse","typeEvenement", "departement","region","informations","contact","telephone","mail","club","siteInternet"]
        self.data = []

    def getElements(self):
        self.data = []
        response = requests.get(self.lien)

        soup = BeautifulSoup(response.text,'html.parser')
        nom = self.tryToCleanOrReturnBlank(soup.find("h1"))
        date = self.tryToCleanOrReturnBlank(soup.find("span",{"class":"fs-5"}))
        heure = self.tryToCleanOrReturnBlank(soup.find("div",{"class":"em-event-time"}))
        adresse = soup.find("div",{"class":"em-event-location"})
        typeEvenement = self.tryToCleanOrReturnBlank(soup.find("ul",{"class":"event-categories"}))
        informations = self.tryToCleanOrReturnBlank(soup.find("section",{"class":"em-event-content"}))
        contacts = self.tryToCleanOrReturnBlank(soup.find("div",{"class":"border-start ps-3"}))

        try:
    #Adresses
            adress = adresse.getText()
            cleanArrAdress = []
            for ele in str(adress).split("\n"):
                if ele != "":
                        cleanArrAdress.append(ele.strip())
            
            realAdresse = cleanArrAdress[0] + cleanArrAdress[1]
            realDepartment = cleanArrAdress[2]
            realRegion = cleanArrAdress[3]
            realCountry = cleanArrAdress[4]
        except:

            adress = ""
            realAdress =""
            realCountry =""
            cleanArrAdress = []

    #Contacts
        try:
            cleanContact = []
            for ele in str(contacts).split("\n"):
                if ele != "":
                        cleanContact.append(ele.strip())

            del cleanContact[0]        
            personneContact = cleanArrAdress[0]
            telephone = cleanContact[1]
            mail = cleanContact[2]
            club = cleanContact[3]
            siteInternet = cleanContact[4]
        except:   
            personneContact = ""
            telephone =""
            mail =""
            club = ""
            siteInternet = ""
            cleanContact = []

        adresse = " ".join(cleanArrAdress)

        cleanInformations = []
        for ele in str(informations).split("\n"):
                if ele != "":
                        cleanInformations.append(ele.lstrip("\n").lstrip(","))
        
        cleanTypeEvt = []
        for ele in str(typeEvenement).split("\n"):
                if ele != "":
                        cleanTypeEvt.append(ele.lstrip(" "))

        typeEvenement = " ".join(cleanTypeEvt)

        informations = " ".join(cleanInformations)
    #passer data en objets
        fiche = {
            "nom" : nom,
            "date" : date,
            "heure" : heure,
            "adresse" : adresse,
            "typeEvenement" : typeEvenement,
            "departement" : realDepartment,
            "region" : realRegion,
            "informations" : informations,
            "contact" : personneContact,
            "telephone" : telephone,
            "mail" : mail,
            "club" : club,
            "siteInternet" : siteInternet
        }
        
        self.data.append(fiche)

    def tryToCleanOrReturnBlank(self,str):
        try:
            result = str.getText().strip()
        except:
            result = ''
        return result
import requests
from bs4 import BeautifulSoup

def decoupage_header(response):
    tabDonnees = []
    swoupBis = BeautifulSoup(response.text, 'html.parser')
    headers = swoupBis.findAll("header",{"class":"entry-header"})
    for header in headers:
        nomRando = str(header.find('h1'))
        fin = len(str(nomRando))
        fin = fin - 5
        nomRando = nomRando[4:fin:1]
    return nomRando

def decoupage_lien():
    
    return 0

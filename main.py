import requests
from bs4 import BeautifulSoup

baseUrl = "https://www.komoot.com/fr-fr"
uri = "/discover/Bourgoin-Jallieu/@45.5872259%2C5.2828123/tours?max_distance=20000&sport=hike"

response = requests.get(baseUrl+uri)

if response.ok:
    swoup=BeautifulSoup(response.text, 'html.parser')
    
    div = swoup.find("div",{"class=":"js-scroll-to-top-anchor css-6xup2u"})
    print(div)
    #refs = div.findAll("a")
    #divs = swoup.findAll("div",{"class=": "js-scroll-to-top-anchor css-6xup2u"})
    



    #print(swoup)

print(response)
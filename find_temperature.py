import requests
from bs4 import BeautifulSoup

def find_temperature(query):
    url = f"https://www.google.com/search?q={query}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    data.find("div",class_="BNeawe").text
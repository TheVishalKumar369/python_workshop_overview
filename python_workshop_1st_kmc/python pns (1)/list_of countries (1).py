import requests
from bs4 import BeautifulSoup

resp = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population")

soup = BeautifulSoup(resp.text,"html.parser")

table = soup.find("")
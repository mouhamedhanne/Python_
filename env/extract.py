# Extraction des données sur le web
import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")

description_text = []

for desc in descriptions :
    description_text.append(desc.string)

print(description_text)
   
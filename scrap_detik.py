import requests
from bs4 import BeautifulSoup

url = "https://www.detik.com/terpopuler"

html = requests.get(url, params={"tag_from": "framebar"})

soup = BeautifulSoup(html.text, "html.parser")

content = soup.find('div', attrs={'grid-row list-content'})

titles = content.findAll('h3', attrs={'class': 'media__title'})
images = content.findAll('div', attrs={'class': 'media__image'})

# for title in titles:
#     print(title.text)

for image in images:
    print(image.find('a').find('img'))

# print(content)

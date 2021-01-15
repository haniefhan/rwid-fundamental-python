import requests
from bs4 import BeautifulSoup

url = 'https://jadwalsholat.pkpu.or.id/?id=98'
content = requests.get(url)

response = BeautifulSoup(content.text, features="html.parser")

tds = response.select("table.table_adzan tr.table_highlight td")

jadwal = {}

for i, td in enumerate(tds):
    if i > 0:
        switcher = {
            1: "Subuh",
            2: "Dhuhur",
            3: "Ashar",
            4: "Maghrib",
            5: "Isya",
        }
        jadwal[switcher.get(i, None)] = td.get_text()

print(jadwal)
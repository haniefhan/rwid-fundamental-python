import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/detik-populer')
def detik_populer():
    url = "https://www.detik.com/terpopuler"

    html = requests.get(url, params={"tag_from": "framebar"})

    soup = BeautifulSoup(html.text, "html.parser")

    content = soup.find('div', attrs={'grid-row list-content'})

    titles = content.findAll('h3', attrs={'class': 'media__title'})
    images = content.findAll('div', attrs={'class': 'media__image'})

    return render_template('detik_populer.html', images=images)


@app.route('/idr-rates')
def idr_rates():
    url = "http://www.floatrates.com/daily/idr.json"
    json = requests.get(url)

    rates = json.json().values()

    return render_template('idr_rates.html', rates=rates)


if __name__ == "__main__":
    app.run(debug=True)

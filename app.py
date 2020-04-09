# app.py
from flask import Flask, render_template, url_for
from db import Schema
from requests import Session
import json

'''TICKER_API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
  'start':'1',
  'limit':'5',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'de6429f1-c45b-4f68-9e80-5c5cc5cf215c',
}

posts = [
    {
        'author': 'Quentin Panger',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 6, 2020'
    },
    {
        'author': 'Quentin Panger',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 6, 2020'
    }
]

#session = Session()
#session.headers.update(headers)

response = session.get(TICKER_API_URL, params=parameters)
coins = json.loads(response.text)
val = coins['data'][0]['quote']['USD']['price']
coin = coins['data'][0]['name']
print(coin)'''

app = Flask(__name__)             # create an app instance

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True)
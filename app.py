# app.py
from flask import Flask, render_template
from db import Schema
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint

TICKER_API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
  'start':'1',
  'limit':'5',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'de6429f1-c45b-4f68-9e80-5c5cc5cf215c',
}

session = Session()
session.headers.update(headers)

app = Flask(__name__)             # create an app instance

try:
    response = session.get(TICKER_API_URL, params=parameters)
    coins = json.loads(response.text)
    # print("test")
    # print(data['data'][0]['quote']['USD']['price'])
    # pprint.pprint(data)
    val = coins['data'][0]['quote']['USD']['price']
    coin = coins['data'][0]['name']
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=coins)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True)
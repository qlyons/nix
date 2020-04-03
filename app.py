# app.py
from flask import Flask
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

@app.route("/")                   # at the end point /
def hello():
    try:
        response = session.get(TICKER_API_URL, params=parameters)
        data = json.loads(response.text)
        #print("test")
        #print(data['data'][0]['quote']['USD']['price'])
        #pprint.pprint(data)
        val = data['data'][0]['quote']['USD']['price']
        coin = data['data'][0]['name']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    return str(coin) + ' : ' + str(val)
if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True)
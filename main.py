import requests
import os
import yfinance as yf


def send_txt(price):
    req = requests.post(os.environ["MAILGUN_URL"],
                        auth=("api", os.environ["MAILGUN_API_KEY"]),
                        data={"to": os.environ["MAILGUN_TO"],
                              "from": os.environ["MAILGUN_FROM"],
                              "text": price})
    print(req.content)


bond = yf.Ticker("^TNX")

send_txt(bond.info['open'])

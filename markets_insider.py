# B"H
# function to request stocks data

import requests, json, urllib3
from lxml import html
urllib3.disable_warnings()

def get_prices(stock):
    base_url = "https://markets.businessinsider.com/stocks/"
    stock_url = f"{base_url}{stock}-stock"
    
    try:
        stock_prices = requests.get(stock_url, verify = False)
    except:
        return {"error": "web not accesible"}

    root = html.document_fromstring(stock_prices.text)

    for x in root.findall(".//"):
        if str((x.text)).find("historicalPrices:")>0:
            stock_values = json.loads(str(x.text)[str(x.text).find("[{"):str(x.text).find("}]")+2])

    return stock_values

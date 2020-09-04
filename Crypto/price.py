import requests 
import json 
import pandas as pd
import time
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
api_key = "0d563c71-d2bd-42da-a5f4-d9dddd3a06af"
header = {'Accepts':'application/json',
          'X-CMC_PRO_API_KEY': api_key}

response = requests.get(url, headers= header)
#df = pd.DataFrame(response)
#df_json = df.to_json()
res_json = response.json()
last_price_BTC = 0 
last_price_ETH = 0
updated_price_BTC = res_json['data'][0]['quote']['USD']['price']
updated_price_ETH = res_json['data'][1]['quote']['USD']['price']
while True:
    print('Time: ', time.ctime())
    if last_price_BTC != updated_price_BTC:
        print('price BTC: ',updated_price_BTC)
        last_price_BTC = updated_price_BTC
    if last_price_ETH != updated_price_ETH:
        print('price ETH: ', updated_price_ETH)
        last_price_ETH = updated_price_ETH
    time.sleep(10)
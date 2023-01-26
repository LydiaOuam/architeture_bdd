from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import json
from datetime import datetime

from pymongo import MongoClient
import csv
import pandas as pd
from pprint import pprint

# code moodle jfk5fm
def get_database():
   # CONNECTION_STRING = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.1"
    CONNECTION_STRING = "mongodb+srv://lydia:1234@cluster0.y5rw0az.mongodb.net"
    client = MongoClient(CONNECTION_STRING)
    return client
    
myclient = get_database()
mydb = myclient["ProjectBase"]
collection_name = mydb["projectCollection"]
# print(mydb)
# print(collection_name)


"""
Les cryptos qui nous interessent : 
    Bitcoin
    Wrapped Bitcoin
    PAX Gold
    Tether Gold
    Lido Staked Ether
    Maker
    Monero
    Quant
    Bitcoin Cash
    Litecoin

Les indices qu'on va suivre:
    l'historique du prix d'une crypto sur un mois
    les differnets changement sur 1h 24h 7j
    les prix sont en dollars
    pttr ajouter le min et le max des prix
"""



#data = cg.get_coin_history_by_id(id='bitcoin',date='10-11-2020', localization='false')

# Cette requete va nous servire surtt pour les update et le real time
# """'bitcoin', 'wrapped-bitcoin','staked-ether', 'pax-gold','tether-gold','maker', 'monero',,  'quant-network','bitcoin-cash', 'litecoin'"""
listCrypto = ['bitcoin', 'wrapped-bitcoin','staked-ether', 'pax-gold','tether-gold','maker', 'monero']
data = {}
for crypto in listCrypto:
    data = cg.get_price(ids=crypto, vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    data['crypto_data'] = data[crypto]
    data['_id'] = crypto
    data['usd'] = data['crypto_data']['usd'] 
    data['usd_market_cap'] =  data['crypto_data']['usd_market_cap'] 
    data['usd_24h_vol'] = data['crypto_data']['usd_24h_vol']
    data['usd_24h_change'] = data['crypto_data']['usd_24h_change']
    data['last_updated_at'] = data['crypto_data']['last_updated_at']
    # data['crypto_data']["id_crypto"] = crypto
    del(data[crypto])
    del(data['crypto_data'])

    # data.append(cg.get_coin_history_by_id(id=crypto, localization='false', date = '30-04-2021',vs_currency='usd'))
    historical__ = cg.get_coin_market_chart_by_id(id=crypto,vs_currency='usd',days='47')
    for price in historical__['prices']:
        a = datetime.fromtimestamp(price[0]/1000)
        price[0] = a
    data["prices"]= historical__['prices']
    print(data)
    collection_name.insert_one(data)
    print(crypto)
    
    # with open(crypto+".json", "w") as fp:
    #     json.dump(data, fp, default = str, indent  = 4)
    # break


# To filter 
# db.projectCollection.find({"crypto_data.id_crypto":"bitcoin"})


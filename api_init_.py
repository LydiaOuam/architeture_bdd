from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import json
from datetime import datetime

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

listCrypto = ['bitcoin', 'wrapped-bitcoin','staked-ether', 'pax-gold','tether-gold','maker', 'monero', 'quant-network','bitcoin-cash', 'litecoin']
data = {}
for crypto in listCrypto:
    data = cg.get_price(ids=crypto, vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    # data.append(cg.get_coin_history_by_id(id=crypto, localization='false', date = '30-04-2021',vs_currency='usd'))
    historical__ = cg.get_coin_market_chart_by_id(id=crypto,vs_currency='usd',days='40')
    for price in historical__['prices']:
        a = datetime.fromtimestamp(price[0]/1000)
        price[0] = a
    data["prices"]= historical__['prices']
    with open(crypto+".json", "w") as fp:
        json.dump(data, fp, default = str, indent  = 4)


#data = cg.get_price(ids=['bitcoin', 'wrapped-bitcoin','PAX-Gold', 'Tether-Gold', 'Lido-Staked-Ether', 'Maker', 'Monero', 'Quant', 'Bitcoin-Cash', 'Litecoin'], vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true', date = '10-11-2022')

# Cette requete sert a avoir le prix d'une crypto a une date pricise

#data = cg.get_coin_history_by_id(id='bitcoin', localization='false', date = "30/04/2023")


# suivre les evol des prix sur un mois en detail
# on utilisera ceci aussi pour fixer un laps de temps pour comparer entre les tweets et les prix
#data = cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days='3')

#with open("exemple.json", "w") as fp:
    #json.dump(data, fp)


# timestamp is number of seconds since 1970-01-01 
#timestamp =    1673276528168

# convert the timestamp to a datetime object in the local timezone
#dt_object = datetime.fromtimestamp(timestamp/1000.0) 

# print the datetime object and its type
#print("dt_object =", dt_object)
#print("type(dt_object) =", type(dt_object))
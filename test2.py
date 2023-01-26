## Connexion BD 

from pymongo import MongoClient
from datetime import datetime
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development



def get_database():
    CONNECTION_STRING = "mongodb+srv://lydia:1234@cluster0.y5rw0az.mongodb.net"
    client = MongoClient(CONNECTION_STRING)
    return client
    
myclient = get_database()
mydb = myclient["ProjectBase"]
collection_name = mydb["projectCollection"]
print(mydb.test)

# Update the Data
listCrypto = ['bitcoin', 'wrapped-bitcoin','staked-ether', 'pax-gold','tether-gold','maker', 'monero','quant-network','bitcoin-cash', 'litecoin']
data = {}
for crypto in listCrypto:
    data = cg.get_price(ids=crypto, vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    data_myBD = pd.DataFrame((collection_name.find({'_id' : crypto})))
    data['crypto_data'] = data[crypto]
    data['usd'] = data['crypto_data']['usd'] 
    data['usd_market_cap'] =  data['crypto_data']['usd_market_cap'] 
    data['usd_24h_vol'] = data['crypto_data']['usd_24h_vol']
    data['usd_24h_change'] = data['crypto_data']['usd_24h_change']
    data['last_updated_at'] = data['crypto_data']['last_updated_at']
    # data['crypto_data']["id_crypto"] = crypto
    del(data[crypto])
    del(data['crypto_data'])
    collection_name.update_one({'_id':str(crypto) },{"$set" : data})
    collection_name.update_one({'_id':str(crypto) },{"$push" : {"prices": [datetime.fromtimestamp(data['last_updated_at']),data['usd']]}})

df = pd.DataFrame(collection_name.find({ "usd": { "$exists": True} }))



# creating a single-element container
placeholder = st.empty()


for i in range(10):
    df['last_updated_at'][i] = datetime.fromtimestamp(df['last_updated_at'][i])

df1 = df['prices']
df2 = df.drop('prices', axis = 1)
st.markdown("### Detailed Data View")
st.dataframe(df2)
time.sleep(1)

# One exemple

for j in range(10):
    price = []
    hour = []
    crypto = []
    myCrypto = df1[j]
    print(len(myCrypto))
    for i in range(19):
        crypto.append(df['_id'][j])
        hour.append(myCrypto[len(myCrypto) - i - 1][0].hour)
        price.append(myCrypto[len(myCrypto) - i - 1][1])
    mydata = pd.DataFrame(list(zip(hour, price, crypto)), columns= ['hour', 'price', 'crypto'])
    st.markdown(str(crypto[0]))
    fig2 = px.treemap(data_frame=mydata, path=['crypto','hour', 'price'],  values='price',
                  color='price', hover_data=['hour'],
                  color_continuous_scale='burgyl',
                 )
    st.write(fig2)


<<<<<<< HEAD
## cap_market and volume market
=======

>>>>>>> 119954c69bcd96aab2d255a33090a7087ea8fa41


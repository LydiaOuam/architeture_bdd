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

# result=collection_name.aggregate([
#     {"$match": {"_id": {"$eq": ObjectId("63c1428ccc2e8146e3ea3b41")}}},
#     {"$project": {"text": 1}}
# ])

# # result = mydb..find({'_id': '63c1428ccc2e8146e3ea3b41'})
# print('--------------------------')
# print('--------------------------')
# for i in result:
#     print(i)
# print('--------------------------')
# deleteResu = mydb.collection_name.delete_many({ "usd": { "$exists": True} })
# deleteResu
# df =  ',User,Date Created,Number of Likes,Source of Tweet,Tweet,Number of Retweet 0,#EndSARS,2023-01-13 09:28:37+00:00,0,Twitter for Android,"RT @PeterObi: Fellow Nigerians, we are one step closer to victory. In order to exercise your constitutional right to elect me as your Presi…",269 1,Aian.91,2023-01-13 09:28:36+00:00,0,Twitter for Android,"RT @NounaGAW: I will send $100 to 2 random person if #BITCOIN hit $24k in 24 hours  Like +RT",908'

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

    # data['last_updated_at'] = datetime.fromtimestamp(data['last_updated_at'])
    # print(data_myBD['prices'])
    # data_myBD['prices'].append([(data['last_updated_at']), data['usd']])
    # print(data)
    # collection_name.insert_one(data)
    # print(crypto)





# df = get_data()
df = pd.DataFrame(collection_name.find({ "usd": { "$exists": True} }))
# for i in range(10):
#     mylength_ = len(df['prices'][i])
#     for j in range(mylength_):
#         df['prices'][i][j][0] = str(df['prices'][i][j][0])


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
    for i in range(20):
        crypto.append(df['_id'][j])
        hour.append(myCrypto[len(myCrypto) - i - 1][0].hour)
        price.append(myCrypto[len(myCrypto) - i - 1][1])
    mydata = pd.DataFrame(list(zip(hour, price, crypto)), columns= ['hour', 'price', 'crypto'])
    st.markdown(str(crypto[0]))
    fig2 = px.treemap(data_frame=mydata, path=['crypto','hour', 'price'],  values='price',
                  color='price', hover_data=['hour'],
                  color_continuous_scale='Purpor',
                 )
    st.write(fig2)



# print(hour)
# print(price)

# mydata = pd.DataFrame(list(zip(hour, price, crypto)), columns= ['hour', 'price', 'crypto'])

# print(mydata)
# # create two columns for charts
# placeholder = st.empty()

# with placeholder.container():


#     st.markdown("### Second Chart")
#     fig2 = px.treemap(data_frame=mydata, path=['crypto','hour', 'price'],  values='price',
#                   color='price', hover_data=['hour'],
#                   color_continuous_scale='RdBu',
#                  )
#     st.write(fig2)


# for d in df:
#     print(d)

    # for i in d :
    #     print(i)

# # dashboard title
# st.title("Real-Time / Live Data Science Dashboard")

# # # top-level filters
# # job_filter = st.selectbox("Select the Job", pd.unique(df["job"]))

# # # creating a single-element container
# placeholder = st.empty()

# # # dataframe filter
# # df = df[df["job"] == job_filter]

# # # near real-time / live feed simulation
# for seconds in range(3):
#     with placeholder.container():

#         for d in df:
#             print(d)
#             st.markdown("### Detailed Data View")
#             st.dataframe(d)
#             time.sleep(1)

# #     df["age_new"] = df["age"] * np.random.choice(range(1, 5))
# #     df["balance_new"] = df["balance"] * np.random.choice(range(1, 5))

# #     # creating KPIs
# #     avg_age = np.mean(df["age_new"])

# #     count_married = int(
# #         df[(df["marital"] == "married")]["marital"].count()
# #         + np.random.choice(range(1, 30))
# #     )

# #     balance = np.mean(df["balance_new"])

# #     with placeholder.container():

# #         # create three columns
# #         kpi1, kpi2, kpi3 = st.columns(3)

# #         # fill in those three columns with respective metrics or KPIs
# #         kpi1.metric(
# #             label="Age ⏳",
# #             value=round(avg_age),
# #             delta=round(avg_age) - 10,
# #         )
        
# #         kpi2.metric(
# #             label="Married Count 💍",
# #             value=int(count_married),
# #             delta=-10 + count_married,
# #         )
        
# #         kpi3.metric(
# #             label="A/C Balance ＄",
# #             value=f"$ {round(balance,2)} ",
# #             delta=-round(balance / count_married) * 100,
# #         )




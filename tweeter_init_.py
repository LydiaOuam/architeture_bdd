import tweepy
import pandas as pd
import json



## Connexion BD 

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
print(mydb)
print(collection_name)



API_KEY="H8qzKivjZxiGaJIdCxFr3QX49"
API_SECRET_KEY="NKQgoaIFONVeSEwXuE4aNabVuqF3wW5QByPJFFoy9UkoQmtBkV"
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAACCUiwEAAAAATxG9gm6pEQ6VpDzT3jFnjch5O3Q%3De3oYwPK7rDqn783iXorV1HcS3ScWHj7vVgTxuDZShVMsxrUlQw"
ACCESS_TOKEN="1588115651989848066-tN1jcTK3lcHFEjVJ99VKOc9zITndRv"
ACCESS_TOKEN_SECRET="Ek58DFJLvJWh6xWNurmH4gZSiKxVEALVL55bZb3wIwMeR"

# Authenticate to Twitter
auth = tweepy.OAuthHandler("H8qzKivjZxiGaJIdCxFr3QX49", "NKQgoaIFONVeSEwXuE4aNabVuqF3wW5QByPJFFoy9UkoQmtBkV")
auth.set_access_token("1588115651989848066-tN1jcTK3lcHFEjVJ99VKOc9zITndRv", "Ek58DFJLvJWh6xWNurmH4gZSiKxVEALVL55bZb3wIwMeR")

# Create API object
api = tweepy.API(auth)

MyCurrencies_list = ['crypto','Bitcoin','Wrapped Bitcoin','PAX Gold','Tether Gold', 'Lido Staked Ether', 'Maker', 'Monero', 'Quant','Bitcoin','Cash', 'Litecoin' ]
date_list = ["2023-01-16", "2023-01-14","2023-01-15", "2023-01-17","2023-01-18"]
for currency in MyCurrencies_list:
    for mydate in date_list:
        q= str(currency)+ " filter:retweets"
        # print(q)
        #The number of tweets we want to retrieved from the user
        tweets = api.search_tweets(q= str(currency)+ " filter:retweets",count=100,until = mydate)

        print("collect tweets")   
            #Pulling Some attributes from the tweet
        #crypto OR Bitcoin OR Wrapped Bitcoin OR PAX Gold OR Tether Gold OR Lido Staked Ether OR Maker OR Monero OR Quant OR  Bitcoin Cash OR Litecoin 
        for tweet in tweets:
            data = {}
            data["user_name"] = tweet.user.name
            data['date_creation'] = str(tweet.created_at) 
            data["favorite_count"] = tweet.favorite_count
            data["source"] = tweet.source
            data["text"] = tweet.text
            data["retwet_count"] = tweet.retweet_count
            # print(tweet.text)
            # insert in tweeter
            collection_name.insert_one(data)

# Reste a faire les requetes qui vont collecter les données en temps reel (reflechir a cela
# plus les differentes visualization)
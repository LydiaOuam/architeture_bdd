from pymongo import MongoClient
import csv
import pandas as pd
from pprint import pprint

# code moodle jfk5fm
def get_database():
    CONNECTION_STRING = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.1"
    client = MongoClient(CONNECTION_STRING)
    return client
    
myclient = get_database()
mydb = myclient["IMDbBase"]
collection_name = mydb["collectionNameBasics"]
print(mydb)
print(collection_name)

# # Name Basis File 
# tsvfile = pd.read_csv("DATAIMDb/name.basics.tsv",delimiter = "\t", na_values="\\N")
# #tsvfile["column_name"].replace('',None, inplace=True)
# tsvfile["knownForTitles"] = tsvfile["knownForTitles"].str.split(',')
# tsvfile["primaryProfession"] = tsvfile["primaryProfession"].str.split(',')

# tsvfile = tsvfile.to_dict('records')
# for dict_ in tsvfile:
#     collection_name.insert_one(dict_)

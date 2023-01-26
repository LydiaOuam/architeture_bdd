from warnings import catch_warnings
from flask import Flask, render_template, request, redirect, request, url_for, flash, send_from_directory, jsonify, send_file, make_response
from markupsafe import escape
import os
import re
import numpy as np
import json
from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId
import logging
# pip install Flask-JSON
# pip install Flask pymongo

# --------------------------------------------------------------------------------------

app = Flask(__name__)

app.secret_key = 'Boutaina12345'

def get_database():
    #mongo atlas lien de connexion
    CONNECTION_STRING = "mongodb+srv://lydia:1234@cluster0.y5rw0az.mongodb.net/"
    # Connexion avec MongoClient
    client = MongoClient(CONNECTION_STRING)
    return(client)

# Create database
def create_db_collection(client):
    db = client["ProjectBase"]
    collection_name = db["projectCollection"]
    return(collection_name)

client = get_database()
collection_name = create_db_collection(client)
# ---------------------------------------------------------------------------------------
# ENDPOINTS
# ---------------------------------------------------------------------------------------

# ENDPOINTS WITHOUT METHODS
@app.route("/")
def home():
    return render_template('/index.html')

@app.route("/add_element", methods=['GET', 'POST'])
def add_element():
    # msg = '' 
    # if all labels exists, add them to bdd
    if request.method == 'POST' and 'user_name' in request.form and 'number_of_like' in request.form and 'number_of_retweet' in request.form and 'source_of_tweet' in request.form and 'tweet' in request.form :
        user_name = request.form['user_name']
        number_of_like = request.form['number_of_like']
        number_of_retweet = request.form['number_of_retweet']
        source_of_tweet = request.form['source_of_tweet']
        tweet = request.form['tweet']
        date_created = datetime.now()
        if number_of_like.isdigit() and number_of_retweet.isdigit():
            data = {"user_name":user_name,"date_creation":date_created,"favorite_count":number_of_like,"source":source_of_tweet,"text":tweet,"retwet_count":number_of_retweet}
            collection_name.insert_one(data)
            print("update success")
            logging.info('Document successfully created ;)')
            return redirect(url_for('home'))
    else :         
        print('Number of like and number of retweet must be integer')
        logging.error('Number of like and number of retweet must be integer')
        # flash('Not int entered')
        return render_template('/add_element.html')
    return redirect(url_for('home'))


@app.route("/add_element_bitcoin", methods=['GET', 'POST'])
def add_element_bitcoin():
    # msg = '' 
    # if all labels exists, add them to bdd
    if request.method == 'POST' and 'bitcoin_name' in request.form and 'usd' in request.form and 'usd_market_cap' in request.form and 'usd_24h_vol' in request.form and 'usd_24h_change' in request.form :
        bitcoin_name = request.form['bitcoin_name']
        usd = request.form['usd']
        usd_market_cap = request.form['usd_market_cap']
        usd_24h_vol = request.form['usd_24h_vol']
        usd_24h_change = request.form['usd_24h_change']
        last_update_at = datetime.now()
        if usd_market_cap.isdigit() and usd_24h_vol.isdigit() and usd_24h_change.isdigit() and usd.isdigit():
            data = {"_id":bitcoin_name, "usd":usd,"usd_market_cap":usd_market_cap,"usd_24h_vol":usd_24h_vol,"usd_24h_change":usd_24h_change, "last_updated_at":last_update_at}
            collection_name.insert_one(data)
            collection_name.update_one({'_id':bitcoin_name },{"$push" : {"prices": [last_update_at,usd]}})
            # collection_name.insert_one(data)
            print("Add success")
            return redirect(url_for('home'))
    else :         
        print('Usd, Usd market cap, Usd change and Usd Vol must be a number')
        # flash('Not int entered')
        logging.error('Please dont leave any of the fields empty')
        return render_template('/add_element_bitcoin.html')
    return redirect(url_for('home'))


@app.route("/delete_element", methods = ['GET', 'POST'])
def delete_element():
    # msg = ''
    # if id exists, delete them to bdd
    if request.method == 'POST' and 'bitcoin_name' in request.form :
        bitcoin_name = request.form['bitcoin_name']
        filter = {"_id" : bitcoin_name}
        collection_name.delete_one(filter)
        # collection_name.delete_one(filter)
    elif request.method == 'POST' and 'id_tweet'in request.form :
        id_tweet = request.form['id_tweet']
        filter = {"_id" : ObjectId(id_tweet)}
        collection_name.delete_one(filter)
    else :
        # flash('You have entered an invalid id')
        logging.error('Please dont leave any of the fields empty')
        return render_template('/delete_element.html')

    return redirect(url_for('home'))

@app.route("/update_element", methods=['GET', 'POST'])
def update_element():
    # error = None
    # msg = ''
    # if all labels exists, update them to bdd
    if request.method == 'POST' and 'id_tweet'in request.form and 'user_name' in request.form and  'number_of_like' in request.form and 'number_of_retweet' in request.form and 'source_of_tweet' in request.form and 'tweet' in request.form :
        id_tweet = request.form['id_tweet']
        user_name = request.form['user_name']
        number_of_like = request.form['number_of_like']
        number_of_retweet = request.form['number_of_retweet']
        source_of_tweet = request.form['source_of_tweet']
        tweet = request.form['tweet']
        date_created = datetime.now()
        if number_of_like.isdigit() and number_of_retweet.isdigit(): 
            filter = {"_id" : ObjectId(id_tweet)}
            data = {"$set": {"user_name":user_name,"date_creation":date_created,"favorite_count":number_of_like,"source":source_of_tweet,"text":tweet,"retwet_count":number_of_retweet}}
            collection_name.update_one(filter, data)
            print("update success")
            logging.warning('Update success for you')
            return redirect(url_for('home'))
        else :
            print('Number of like and number of retweet must be integer')
            flash('Not int entered')
            logging.error('Number of like and number of retweet must be integer')
            return render_template('/update_element.html')
        # Filter on Id and update data / verifies if id_tweet has 12 characters
        # filter = {"_id" : ObjectId(id_tweet)}
        # data = {"$set": {"User":user_name,"Date Created":date_created,"Number of Likes":number_of_like,"Source of Tweet":source_of_tweet,"Tweet":tweet,"Number of Retweet":number_of_retweet}}
        # collection_name.update_one(filter, data)
        # return(render_template('/deleted_element.html'), flash)
    else :
        # flash('No update found')
        logging.error('Please dont leave any of the fields empty')
        return render_template('/update_element.html')


@app.route("/update_element_bitcoin", methods=['GET', 'POST'])
def update_element_bitcoin():
    # error = None
    # msg = ''
    # if all labels exists, update them to bdd
    if request.method == 'POST' and 'bitcoin_name' in request.form and 'usd' in request.form and 'usd_market_cap' in request.form and 'usd_24h_vol' in request.form and 'usd_24h_change' in request.form :
        bitcoin_name = request.form['bitcoin_name']
        usd = request.form['usd']
        usd_market_cap = request.form['usd_market_cap']
        usd_24h_vol = request.form['usd_24h_vol']
        usd_24h_change = request.form['usd_24h_change']
        last_update_at = datetime.now()
        if usd_market_cap.isdigit() and usd_24h_vol.isdigit() and usd_24h_change.isdigit() and usd.isdigit():
            filter = {"_id" : bitcoin_name}
            data = {"$set" : {"usd":usd,"usd_market_cap":usd_market_cap,"usd_24h_vol":usd_24h_vol,"usd_24h_change":usd_24h_change, "last_updated_at":last_update_at}}
            collection_name.update_one(filter, data)
            collection_name.update_one(filter,{"$push" : {"prices": [last_update_at,usd]}})
            # collection_name.insert_one(data)
            # print("update success")
            logging.warning('Update success for you')
            return redirect(url_for('home'))
        else :
            # print('Usd, Usd market cap, Usd change and Usd Vol must be a number + Bitcoin name is CASE SENSITIVE')
            # flash('Not int entered')
            logging.error('Usd, Usd market cap, Usd change and Usd Vol must be a number + Bitcoin name is CASE SENSITIVE')
            return render_template('/update_element_bitcoin.html')
        # Filter on Id and update data / verifies if id_tweet has 12 characters
        # filter = {"_id" : ObjectId(id_tweet)}
        # data = {"$set": {"User":user_name,"Date Created":date_created,"Number of Likes":number_of_like,"Source of Tweet":source_of_tweet,"Tweet":tweet,"Number of Retweet":number_of_retweet}}
        # collection_name.update_one(filter, data)
        # return(render_template('/deleted_element.html'), flash)
    else :
        # flash('No update found')
        logging.error('Please dont leave any of the fields empty')
        return render_template('/update_element_bitcoin.html')


# ENDPOINTS WITH METHODS POST

#RECUPERER DATA WITH ID
# @app.route("/length_data_id", methods=['POST', ])
# def index_count():
#     db.collection.findall( {} ).count()

@app.route("/update_api_live")
def update_api():
    return render_template('/update_api_live.html')
    # return redirect(url_for('home'))



# ENDPOINTS WITH METHODS GET
# print my json data
@app.route("/data", methods=['POST', 'GET'])
def get_jsondata():
    # Opening JSON file
    with open('./templates/public/crypto_tweets.json') as json_file:
        donnees = json.load(json_file)
        # print(donnees)
    return jsonify(donnees)
    
@app.route("/data/<int:number>", methods=['GET'])
def get_jsondata_number(number):
    # Opening JSON file
    with open('./templates/public/crypto_tweets.json') as json_file:
        donnees = json.load(json_file)
        # print(donnees)
    return jsonify(donnees[number])
        

        
    


# ENDPOINTS WITH METHOD PUT 

# return render_template('/index.html')
# ENDPOINTS WITH METHODS DELETE


@app.route("/updated", methods = ['GET', 'POST'])
def updated():
    # msg = ''
    # if id exists, delete them to bdd
    return  render_template('/updated.html')

# Error endpoints
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# ---------------------------------------------------------------------------------------------
# RUNNING APP
# --------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
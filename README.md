# Ce projet est réalisé dans le cadre du TP noté du module Architecture BDD
---------------------------------------------------------------
# La Data
---------------------------------------------------------------
Deux Sources de données sont utilisé pour ce projet : 
1. Des données de twitter collecté en utilisant l'API tweepy de python
2. Des données de CoinGecko collecté aussi en utilisant l'API proposé
-> on a utilisé ces API car on a utilisé python comme language de programmation
- _La description des données Twitter :_  
    - __"user_name"__ :ce champs décrit l'utilisateur qui a publié le tweet : type String
    - __"date_creation"__ : ce champs décrit la date dont laquelle l'utilisateur a publié son tweet : type String
    - __"favorite_count"__ : ce champs décrit le nombre de fois que le tweet a été liké et aimé : type Int
    - __"source"__ : ce champs décrit la source du tweet, (app web, téléphone mobile, ...) : type String
    - __"text"__ : ce champs contient le text du tweet, peut etre utilisé dans une analyse plus poussé en se basant sur les sentiments, dans le sens s'agit il de _good comments or bad ones_ et comment ça influence les prix des cryptos
    - __"retwet_counts"__: ce champs décrit le nombre de fois un tweet a été repartagé : type Int

- _La description des données Coingecko :_  
Pour commencer on a choisit 10 crypto pour les suivre en près s'agit :  
    __['bitcoin', 'wrapped-bitcoin','staked-ether', 'pax-gold','tether-gold','maker', 'monero','quant-network','bitcoin-cash', 'litecoin']__
    - __"id"__ : ce champs contient l'id qui est une des crypto ci-dessus, fait de cette maniére pour faciliter les différente recherche: type __String__
    - __"usd"__ : ce champ représente le prix en __dollars $__, ce champs est mis à jours constamment : type __Int__
    - __usd_market_cap__ : ce champs représent plus ou moins la polpularité d'une crypto, il permet de faire des analyses pour investissement : type __double__
    - __usd_24h_vol__ :ce champs présente la masse de transaction sur une crypto, permet également de faire des analyses techniques : type __double
    - __usd_24h_change__ : le changement des prix durant les derniéres 24 heures type : __double__
    - __last_updated_at__ : ce champs nous informe de la date du dernier update, toutes les infos ci-dessous sont eu a cette date : type __Int__
    - __prices__ : une liste de liste qui en forme de couple ['date', 'price'] qui contient l'historqie des prix des différentes cryptos
 
---------------------------------------------------------------
# Installation Nécessaire
---------------------------------------------------------------
Afin de pouvoir assurer le bon focntionnement du code pusher dans ce git il va falloir installer quelques bibliothéques python :  
-le script __api_init.py__ utilise la bibliothéque __pycoingecko__ :  
``` 
pip install -U pycoingecko
```  

Source : [Installer pycoingecko](https://pypi.org/project/pycoingecko/)   
-le script __tweeter_init.py__ utilise la bibliothéque __tweepy__ :  

``` 
pip install tweepy
```  
Source : [Installer tweepy](https://docs.tweepy.org/en/stable/install.html). 
-le script __streaming.py__ utilise la bibliothéque __streamlit__:  
```
pip install streamlit
```
Source : [Installer streamlit](https://docs.streamlit.io/library/get-started/installation). 
 
-le script __app.py__ utilise la bibliothéque __flask-json__ et __flask-pymongo__:  
```
pip install Flask-JSON

pip install Flask-PyMongo
```
Source : [Installer Flask](https://pypi.org/project/Flask-JSON/).   
Source : [Installer pyMongo](https://pypi.org/project/Flask-PyMongo/). 




---------------------------------------------------------------
# Collaborateurs : 
---------------------------------------------------------------
    Lydia 
    Kafia 
    Boutaina 
    Shadrack

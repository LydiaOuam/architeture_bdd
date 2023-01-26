# Projet Architecture BDD
---------------------------------------------------------------
# La description du projet
---------------------------------------------------------------
Ce projet est réalisé dans le cadre du TP noté du module Architecture BDD.
L'essence même de ce projet est de pouvoir manipuler des bases de données non relationnelle (MongoDB), envoyer des requêtes à l'aide desaggregates. De même, pouvoir aussi appliquer un CRUD,  commencer _from scratch_, collecter, nettoyer, traiter et analyser les données.
De plus, A l'aide du framework Flask, faire un CRUD pour notre base de donnée.
De même avec streamlit, Mettre en place une interface qui permet d'afficher des données live en utilisant des bibliothéque comme stremalit, et enfin faire des petites visualisations en utilisant des bibliothéques comme matplotlib.

Notre But est de collecter des données sur Twitter et CoinGecko et et montrer la correlation entre les données, repondant à la problematique : est ce que les tweets influence le prix des cryptos ?

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
    - __prices__ : une liste de liste qui en forme de couple ['date' : __timestamp__, 'price' : __double__] qui contient l'historqie des prix des différentes cryptos
 
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
pip install tweepy. 
```  
Source : [Installer tweepy](https://docs.tweepy.org/en/stable/install.html)  

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

-le script __bitcoinplot__ utilise la bibliothéque __matplotlib__ :    
```
python -m pip install matplotlib
```
Source : [Installer MatPlotLib](https://matplotlib.org/stable/users/installing/index.html). 

---------------------------------------------------------------
# Visualisations
---------------------------------------------------------------
Sur ce graphe on peut voir en orange les prix des bitcoins et en bleu le nombre de tweets, on peut remarquer que l'augmentation des prix des bitcoins suit la hausse des nombre des tweets.

Faut aussi savoir que les prix des cryptos sont influencé par plusieurs autre éléments comme : l'offre et la demande, incertitudes politiques et économiques, ...

<img width="900" alt="Capture d’écran 2023-01-20 à 12 08 36" src="https://user-images.githubusercontent.com/84903904/214848632-d64eae7d-e3ac-4a26-9d20-46c9c74798e2.png">

Cette Image on peut voir l'évolution de prix de 4 différentes cryptos. 

<img width="900" alt="Capture d’écran 2023-01-20 à 12 08 36" src="https://user-images.githubusercontent.com/84903904/214862466-56445bb0-713f-4b3a-90d9-d476e962db6d.png">



Cette figure montre un _treemap_ composé de trois couches la premiére représente le nom de la crypto, la deuxiéme est l'heure et la troisiéme c'est le prix, les informations qu'on voit sur le _treemap_ sont les données des derniéres 24H.

<img width="835" alt="Capture d’écran 2023-01-26 à 14 56 34" src="https://user-images.githubusercontent.com/84903904/214854013-728054cf-a773-42a6-b906-1278ab07d4fe.png">


---------------------------------------------------------------
# Perspectives
---------------------------------------------------------------
On peut faire une analyse des émotions sur les tweets et cela en les séparant en tweets négatifs et positifs et puis par la suite faire la meme analyse.
Est ce que des tweets écrits pas des gens qui ont de l'influence ça aide a changé les prix des cryptos.
Aussi utilisé les données comme le market cap et market vol pour suivre la circulation des cryptos et pouvoir voir l'influence des tweets sur les décisions prises par les _traders_ à savoir l'achat ou la vente.  


---------------------------------------------------------------
# Collaborateurs
---------------------------------------------------------------
    Lydia 
    Kafia 
    Boutaina 
    Shadrack

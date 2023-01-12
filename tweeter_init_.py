import tweepy

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


tweets = api.search_tweets(q="crypto")

# Affichez les 10 premiers tweets
for tweet in tweets[:10]:
    print(f"{tweet.user.name} a tweeté : {tweet.text}")


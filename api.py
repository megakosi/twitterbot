from pytwitter import Api

api_key = "G8uCFLZY6kYKmxMo2gUpMLvIR"
api_key_secret = "6HjOgjGE7tZh4uMcAFS9u5za4bUfTRmF4lE0ZIux0P9zMhOfOS"

api = Api(consumer_key=api_key, consumer_secret=api_key_secret, oauth_flow=True)

print(api.search_tweets(query="python"))
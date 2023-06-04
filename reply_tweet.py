import json
import requests
from requests_oauthlib import OAuth1
from config import *

consumer_key = api_key
consumer_secret = api_key_secret
access_token = access_token
access_token_secret = access_token_secret


def replyTweet(tweet_id: int, message: str):
    # URL and data for the POST request
    url = 'https://api.twitter.com/2/tweets'
    data = {'text': message, "reply": {"in_reply_to_tweet_id": str(tweet_id)}}

    # Set the Content-Type header to application/json
    headers = {'Content-Type': 'application/json'}

    # Serialize the data as JSON
    json_data = json.dumps(data)

    # Create an OAuth1 session
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
    session = requests.Session()
    session.auth = auth

    try:
        # Make the POST request
        response = session.post(url, data=json_data, headers=headers)
        print(response.text)
    except Exception as ex:
        print(str(ex))

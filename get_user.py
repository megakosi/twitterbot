import json
import requests
from requests_oauthlib import OAuth1
from config import *

consumer_key = api_key
consumer_secret = api_key_secret
access_token = access_token
access_token_secret = access_token_secret


def getTwitterUser(user_id: int):
    # URL and data for the POST request
    url = 'https://api.twitter.com/2/users/' + str(user_id)

    # Set the Content-Type header to application/json
    headers = {'Content-Type': 'application/json'}

    # Create an OAuth1 session
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
    session = requests.Session()
    session.auth = auth

    # Make the POST request
    response = session.get(url, headers=headers)
    # Check the response
    if response.status_code == 200:
        json_response = response.json()
        response_data = json.dumps(json_response, indent=4, sort_keys=True)
        user_data = json.loads(response_data)
        name = user_data['data']['name']
        username = user_data['data']['username']
        return {'name': name, 'username': username}
    else:
        print('Failed to Reply to Tweet, Reason: ' + response.text)

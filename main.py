import time

import requests

import json
from spamfilter.filters import Length, Symbols
from spamfilter.machines import Machine
from config import *
from reply_tweet import replyTweet
from get_user import getTwitterUser

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
# bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/search/recent"

keyword_to_search = 'metamask'
hashtag_to_search = '#metamask'

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,

# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields


file_path = 'id.txt'

with open(file_path, 'r') as file:
    since_id = int(file.read())

query_params = {'query': 'Metamask (entity:metamask)', 'tweet.fields': 'author_id',
                'user.fields': 'username', 'max_results': 10, 'since_id': since_id}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_to_search_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def getRecentTweets():
    json_response = connect_to_search_endpoint(search_url, query_params)
    data = json.dumps(json_response, indent=4, sort_keys=True)
    tweets_data = json.loads(data)

    if 'data' in tweets_data:

        newest_id = tweets_data['meta']['newest_id']
        tweets = tweets_data['data']

        for data in tweets:
            text = data['text']
            tweet_id = data['id']
            author_id = data['author_id']

            author = getTwitterUser(int(author_id))

            author_name = author['name']
            author_username = author['username']

            m = Machine([
                Length(min_length=10, max_length=200, mode="crop"),
                Symbols(mode="normal")
            ])

            if m.check(text).passed:
                replyTweet(tweet_id,
                           f'Hi {author_name}, @{author_username} your Ticket ID is {tweet_id}, Kindly send us an email via metamaskcustomercare.io@gmail.com our online customer service is always ready to respond to your complaint and provide more information about product/services.')

        with open(file_path, 'w') as f:
            f.write(newest_id)


while True:
    getRecentTweets()
    time.sleep(5)

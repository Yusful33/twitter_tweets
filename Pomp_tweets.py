# import Twitter_Creds
import datetime
from datetime import datetime, timedelta
import os
import pandas as pd
import itertools
import collections
import tweepy as tw
import nltk
from nltk.corpus import stopwords
import re
import networkx
import warnings
import json

import yaml

with open("auth.yaml", "r") as creds:
    try:
        twitter_auth = yaml.safe_load(creds)
    except yaml.YAMLError as exc:
        print(exc)

print(twitter_auth['consumer_key'])


# # Authenticate to Twitter
auth = tw.OAuthHandler(twitter_auth['consumer_key'], twitter_auth['consumer_secret'])
auth.set_access_token(twitter_auth['access_token'], twitter_auth['access_token_secret'])

# # Create API object
api = tw.API(auth, 
wait_on_rate_limit=True)
#,
  #  wait_on_rate_limit_notify=True)

#Getting Info On Twitter Users
user = api.get_user("APompliano")


search_term = "best article you read this week -filter:retweets"

#Getting today's date
current = date.today()
d1 = current.strftime("%Y-%m-%d")

#Ten Days Ago
days_ago = 10
d2 = str(current - timedelta(days=days_ago))


tweets = tw.Cursor(api.search,
                   q=search_term,
                   lang="en",
                   since=d2,
                   until=d1
).items(1000)

all_tweets = [tweet.text for tweet in tweets]

all_tweets[:5]


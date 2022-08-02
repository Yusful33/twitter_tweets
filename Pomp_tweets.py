# import Twitter_Creds
import datetime
from datetime import datetime, timedelta, date 
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

_NAME = "APompliano"
with open("auth.yaml", "r") as creds:
    try:
        twitter_auth = yaml.safe_load(creds)
    except yaml.YAMLError as exc:
        print(exc)


# # # Authenticate to Twitter
auth = tw.OAuthHandler(twitter_auth['consumer_key'], twitter_auth['consumer_secret'])
auth.set_access_token(twitter_auth['access_token'], twitter_auth['access_token_secret'])

# # # Create API object
api = tw.API(auth, wait_on_rate_limit=True)


tweets = api.user_timeline(screen_name=_NAME, 
                           # 200 is the maximum allowed count
                           count=100,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
for info in tweets[:1]:
  print(info)

# #Getting Info On Twitter Users
# user = api.get_user(screen_name=_NAME)

# search_term = "best article you read this week -filter:retweets"

# #Getting today's date
# current = date.today()
# d1 = current.strftime("%Y-%m-%d")

# #Ten Days Ago
# days_ago = 10
# d2 = str(current - timedelta(days=days_ago))


# tweets = tw.Cursor(api.search_tweets,
#                    q=search_term,
#                    lang="en",
#                    until=d1
# ).items(100)

# replies = []
# for tweet in tweets:
#   if tweet.user.id_str == '339061487':
#     print(tweet.id, tweet.user.screen_name, tweet.text, tweet.created_at, tweet.in_reply_to_status_id_str, tweet.in_reply_to_user_id, tweet.retweet_count, tweet.favorite_count)

#     for tweet in tw.Cursor(api.search_tweets,q='to:'+_NAME, since_id='339061487', tweet_mode='extended').items():
#       if hasattr(tweet, 'in_reply_to_status_id_str'):
#         replies.append(tweet)
# print(replies[:1])



# replies = []
# for full_tweet in all_tweets:
#   for tweet in tw.Cursor(api.search_tweets,q='to:'+_NAME, since_id=tweet_id, tweet_mode='extended').items():
#     if hasattr(tweet, 'in_reply_to_status_id_str'):
#       if (tweet.in_reply_to_status_id_str==full_tweet.id_str):
#         replies.append(tweet.text)
#   for elements in replies:
#        print("Replies :",elements)
#   replies.clear()
# sample = all_tweets[0]


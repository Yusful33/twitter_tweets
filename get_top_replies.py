import pymongo
from gather_tweets_utils import (MONGOCLIENT, MONGO_ID, 
                            REPLY_TO_STATUS_ID,
                            FROM_NUMBER, TO_NUMBER, extract_url, get_full_url)
from twilio_message import TwilioClient
import logging 
logging.basicConfig(level=logging.INFO)

_THIS_LINK = "This link: "
_MOST_RESPONSES = " had the most likes in response to APompliano latest tweet "
_CREATED_AT = "created_at"
_FAVORITE_COUNT = "favorite_count"

cluster = pymongo.MongoClient(MONGOCLIENT)
db = cluster.twitter
orig_collection = db.original_tweets
reply_collection = db.reply_tweets

# Getting the latest tweet 
latest_tweet = orig_collection.find({}).sort(_CREATED_AT, -1).limit(1)
for tweet in latest_tweet:
    latest_tweet_id = int(tweet[MONGO_ID])

# Getting the highest favorited reply for a given tweet
max_favorites = reply_collection.find({REPLY_TO_STATUS_ID: latest_tweet_id}).sort(_FAVORITE_COUNT, -1).limit(1)
max_fav = next(max_favorites)

# Twilio does not support sending shortened_url links
## So we are extracting the url and then converting it into its full form
tweet_url = extract_url(max_fav['text'])
full_url = get_full_url(tweet_url)
twilio_client = TwilioClient(FROM_NUMBER, TO_NUMBER)
message = str(_THIS_LINK + full_url + _MOST_RESPONSES + str(latest_tweet_id))
twilio_client.send_message(message)
# twilio_client.send_message('This link: https://www.globenewswire.com/en/news-release/2022/07/07/2476303/0/en/Security-Token-Market-Launches-First-Tokenized-Crowdfund-on-Avalanche-Blockchain.html had the most likes in response to APompliano latest tweet 1550821177693769729')



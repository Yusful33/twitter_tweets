import pymongo
from gather_tweets_utils import MONGOCLIENT, MONGO_ID, REPLY_TO_STATUS_ID

cluster = pymongo.MongoClient(MONGOCLIENT)
db = cluster.twitter
orig_collection = db.original_tweets
reply_collection = db.reply_tweets

# Getting the latest tweet 
latest_tweet = orig_collection.find({}).sort("created_at", -1).limit(1)
for tweet in latest_tweet:
    latest_tweet_id = int(tweet[MONGO_ID])

# Getting the highest favorited reply for a given tweet
max_favorites = reply_collection.find({REPLY_TO_STATUS_ID: latest_tweet_id}).sort("favorite_count", -1).limit(1)

for tweet in max_favorites:
    print(tweet['text'])
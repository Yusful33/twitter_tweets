from twitter_setup import TwitterClient, create_subdict_from_dict
from gather_tweets_utils import (date_cleanup, 
                            create_subdict_from_dict, 
                            NAME, 
                            get_id_into_mongo_format) 
from datetime import datetime, timedelta, date 
import logging 
import pymongo
import json
from bson import ObjectId
logging.basicConfig(level=logging.INFO)


# _SEARCH_TERM = "best article you read this week -filter:retweets AND -filter:replies -from: APompliano"
_SEARCH_TERM = "best article you read this week from: APompliano"
_ORG_TWEET_FIELDS = ['id', 'created_at', 'text', 'user.name', 'user.screen_name']
_TO = "to:"
_LINK = " has:links"
_YAML_FILE = "auth.yaml"
_MongoClient = "mongodb+srv://ycattaneo:yusuf33@cluster0.ridin.mongodb.net/?retryWrites=true&w=majority"


client = TwitterClient(_YAML_FILE, NAME)

# Using next as this is an item iterator
orig_tweet = next(client.search_tweets(_SEARCH_TERM))

# This is where I would call the get_latest_tweet_dict if necessary

# If we find a tweet, go looking for replies
if orig_tweet:
    orig_record = create_subdict_from_dict(orig_tweet._json, _ORG_TWEET_FIELDS)
    # Need to rename id to _id before loading to mongo
    orig_record = get_id_into_mongo_format(orig_record)
    # Establishing connection to mongo
    cluster = pymongo.MongoClient(_MongoClient)
    db = cluster.twitter
    # Writing values to Mongo
    orig_collection = db.original_tweets
    # orig_collection.insert_one(orig_record)
    orig_collection.replace_one({"_id": orig_record['_id']}, orig_record, upsert=True)
    logging.info(orig_record)
    # Establishing Timespan
    from_date, to_date = date_cleanup(orig_tweet.created_at)
    search_response_query = _TO+NAME+_LINK
    replies = client.get_tweet_responses(search_response_query, 
                        orig_tweet.id, 
                        from_date,
                        to_date
                        )
    # Establishing mongo collection
    reply_collection = db.reply_tweets
    logging.info(replies)
    for reply in replies:
        reply = get_id_into_mongo_format(reply)
        # Loading data to Mongo
        reply_collection.replace_one({"_id": reply['_id']}, reply, upsert=True)
    

# Viewing Results
# all_results = reply_collection.find({})
# for record in all_results:
#     print(record)

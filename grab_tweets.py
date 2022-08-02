from twitter_setup import TwitterClient, create_subdict_from_dict
from gather_tweets_utils import date_cleanup, create_subdict_from_dict, NAME
from datetime import datetime, timedelta, date 
import logging 
logging.basicConfig(level=logging.INFO)


# _SEARCH_TERM = "best article you read this week -filter:retweets AND -filter:replies -from: APompliano"
_SEARCH_TERM = "best article you read this week from: APompliano"
_ORG_TWEET_FIELDS = ['id', 'created_at', 'text', 'user.name', 'user.screen_name']
_TO = "to:"
_LINK = " has:links"
_YAML_FILE = "auth.yaml"


client = TwitterClient(_YAML_FILE, NAME)

# Using next as this is an item iterator
orig_tweet = next(client.search_tweets(_SEARCH_TERM))

# This is where I would call the get_latest_tweet_dict if necessary

# If we find a tweet, go looking for replies
if orig_tweet:
    orig_record = create_subdict_from_dict(orig_tweet._json, _ORG_TWEET_FIELDS)
    logging.info(orig_record)
    from_date, to_date = date_cleanup(orig_tweet.created_at)
    search_response_query = _TO+NAME+_LINK
    # Need to determine the amount of replies to check for??
    # How can I isolate the orig_record.id??
    num_replies = client.number_of_replies(search_response_query, orig_record.id)
    print(num_replies)
    # replies = client.get_tweet_responses(search_response_query, 
    #                     orig_record.id, 
    #                     from_date,
    #                     to_date
    #                     )
    # logging.info(replies)

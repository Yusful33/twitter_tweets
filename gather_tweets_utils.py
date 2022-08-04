from datetime import datetime
import logging 
import yaml
import tweepy as tw
import re
import requests


NAME = "APompliano"
MONGOCLIENT = "mongodb+srv://ycattaneo:yusuf33@cluster0.ridin.mongodb.net/?retryWrites=true&w=majority"
_ZEROS = '0000'
_CONSUMER_SECRET = 'consumer_secret'
_CONSUMER_KEY = 'consumer_key'
_ACCESS_TOKEN_SECRET = 'access_token_secret'
_ACCESS_TOKEN = 'access_token'
ORG_TWEET_FIELDS = ['id', 'created_at', 'text', 'user']
ORIG_ID = "id"
MONGO_ID = "_id"
REPLY_TO_STATUS_ID = 'in_reply_to_status_id'
_USER = "user"
_SCREEN_NAME = "screen_name"
FROM_NUMBER = '+15106942739'
TO_NUMBER = '+12025805993'
TWILIO_ACCOUNT_SID = 'TWILIO_ACCOUNT_SID'
TWILIO_AUTH_TOKEN = 'TWILIO_AUTH_TOKEN'
STATUS_CALLBACK = 'https://eobfwh9i22csmq9.m.pipedream.net'
URL_REGEX = "https://t\.co/\S+"

def twt_auth(yaml_file):
    """Authenticating to Twitter."""
    key_dict = read_yaml(yaml_file)
    auth = tw.OAuthHandler(key_dict[_CONSUMER_KEY], key_dict[_CONSUMER_SECRET])
    auth.set_access_token(key_dict[_ACCESS_TOKEN], key_dict[_ACCESS_TOKEN_SECRET])
    return auth

def read_yaml(yaml_file):
    """Read Yaml file."""
    with open(yaml_file, "r") as creds:
        try:
            twitter_auth = yaml.safe_load(creds)
            return twitter_auth
        except yaml.YAMLError as exc:
            logging.WARNING(exc)

def date_cleanup(date):
    """Converting datetime to string to be feed into 30_day search param."""
    from_date = datetime.strftime(date, '%Y%m%d')
    to_date = str(int(from_date) + 1) + _ZEROS
    from_date+= _ZEROS
    return from_date, to_date

def get_id_into_mongo_format(sub_dict):
    """Updates the id key to _id to be inline with mongodb format."""
    sub_dict[MONGO_ID] = sub_dict[ORIG_ID]
    del sub_dict[ORIG_ID]
    return sub_dict

def create_subdict_from_dict(big_dict, target_fields):
    """Creates a sub dictionary by targetting a few fields in a dictionary."""
    field_dict = dict((k, big_dict[k]) for k in target_fields if k in big_dict)
    return field_dict

def get_screen_name(tweet_dict):
    """Gets the screen name of the user and deletes the remaining user contents."""
    tweet_dict[_SCREEN_NAME] = tweet_dict[_USER][_SCREEN_NAME]
    del tweet_dict[_USER]
    return tweet_dict

def extract_url(tweet_text):
    """Extracts a url from tweet."""
    get_url = re.findall(URL_REGEX, tweet_text)
    # Returning first element in list
    return get_url[0]

def get_full_url(short_url):
    """Converts a shortened url into its full form."""
    # Using string indexing as we are actually receiving a list
    response = requests.get(short_url)
    return response.url

# Might not be necessary but further testing required keep for now.
# def get_latest_tweet_dict(tweets):
#         """Creates a dicitonary from key items in the latest tweet."""
#         for tweet in tweets:
#             if tweet.user.screen_name == NAME:
#         # This should be a seperate table/document model than the responses
#                 orig_tweet = create_subdict_from_dict(tweet._json, ORG_TWEET_FIELDS)
#                 logging.info(orig_tweet)
#                 return orig_tweet
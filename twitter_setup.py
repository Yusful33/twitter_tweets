import yaml
import logging
import tweepy as tw
from datetime import datetime, timedelta, date 
import datetime

_CONSUMER_SECRET = 'consumer_secret'
_CONSUMER_KEY = 'consumer_key'
_ACCESS_TOKEN_SECRET = 'access_token_secret'
_ACCESS_TOKEN = 'access_token'
_SEARCH_TERM = "best article you read this week -filter:retweets"

def read_yaml(yaml_file):
    """Read Yaml file."""
    with open(yaml_file, "r") as creds:
        try:
            twitter_auth = yaml.safe_load(creds)
            return twitter_auth
        except yaml.YAMLError as exc:
            logging.info(exc)
def twt_auth(yaml_file):
    """Authenticating to Twitter."""
    key_dict = read_yaml(yaml_file)
    auth = tw.OAuthHandler(key_dict[_CONSUMER_KEY], key_dict[_CONSUMER_SECRET])
    auth.set_access_token(key_dict[_ACCESS_TOKEN], key_dict[_ACCESS_TOKEN_SECRET])
    return auth

class TwitterClient():
    def __init__(self, yaml_file, twitter_user=None):
        self.auth = twt_auth(yaml_file)
        self.twitter_client = tw.API(self.auth, wait_on_rate_limit=True)
        self.twitter_user = twitter_user 

    def user_name(self):
        user = self.twitter_client.get_user(screen_name=self.twitter_user)
        print(type(user))
        return user 

    def search_tweets(self, _SEARCH_TERM):
        current = date.today()
        d1 = current.strftime("%Y-%m-%d")
        tweets = tw.Cursor(self.twitter_client.search_tweets,
                   q=_SEARCH_TERM,
                   lang="en",
                   until=d1
                    ).items(1)
        return tweets
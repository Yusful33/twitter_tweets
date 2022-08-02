import yaml
import logging
import tweepy as tw

_CONSUMER_SECRET = 'consumer_secret'
_CONSUMER_KEY = 'consumer_key'
_ACCESS_TOKEN_SECRET = 'access_token_secret'
_ACCESS_TOKEN = 'access_token'
_IMPORTANT_FIELDS = ['id', 'created_at', 'in_reply_to_status_id', 'text', 'retweet_count', 'favorite_count'] 

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
        return user.screen_name

    def search_tweets(self, search_term):
        tweets = tw.Cursor(self.twitter_client.search_30_day,
                    label='dev',
                   query=search_term,
                    ).items(1)
        return tweets
    
    def get_tweet_responses(self, filter_param, tweet_id, from_date, to_date):
        replies=[]
        for tweet in tw.Cursor(self.twitter_client.search_30_day, 
                                label='dev', 
                                query=filter_param, 
                                fromDate=from_date, toDate=to_date).items(50):
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                if tweet.in_reply_to_status_id == tweet_id:
                    field_dict = dict((k, tweet._json[k]) for k in _IMPORTANT_FIELDS if k in tweet._json)
                    replies.append(field_dict)
        return replies
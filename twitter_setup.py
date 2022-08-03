import yaml
import logging
import tweepy as tw
from gather_tweets_utils import read_yaml, twt_auth, create_subdict_from_dict, NAME

_IMPORTANT_FIELDS = ['id', 'created_at', 'in_reply_to_status_id', 'text', 'retweet_count', 'favorite_count'] 

class TwitterClient():
    def __init__(self, yaml_file, twitter_user=None):
        self._auth = twt_auth(yaml_file)
        self._twitter_client = tw.API(self._auth, wait_on_rate_limit=True)
        self._twitter_user = twitter_user 

    def user_name(self):
        """Gives you the screen name of a user."""
        user = self._twitter_client.get_user(screen_name=self._twitter_user)
        print(type(user))
        return user.screen_name

    def search_tweets(self, search_term):
        """Gets most recent tweet asking for articles."""
        tweets = tw.Cursor(self._twitter_client.search_30_day,
                    label='dev',
                   query=search_term).items(1)
        return tweets

    def most_recent_tweet(self, tweets):
        """Most recent tweet by a user."""
        latest = max(tweets['id'], key=lambda ev: ev['id'])
        return latest
    
    def get_tweet_responses(self, filter_param, tweet_id, from_date, to_date):
        """Responses to a particular tweet within a given date range."""
        replies=[]
        for tweet in tw.Cursor(self._twitter_client.search_30_day, 
                                label='dev', 
                                query=filter_param, 
                                fromDate=from_date, toDate=to_date,
                                maxResults = 10
                                ).items():
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                if tweet.in_reply_to_status_id == tweet_id:
                    field_dict = create_subdict_from_dict(tweet._json, _IMPORTANT_FIELDS)
                    replies.append(field_dict)
        return replies
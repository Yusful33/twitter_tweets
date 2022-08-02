from twitter_setup import TwitterClient
from datetime import datetime, timedelta, date 


_NAME = "APompliano"
# _SEARCH_TERM = "best article you read this week -filter:retweets AND -filter:replies -from: APompliano"
_SEARCH_TERM = "best article you read this week from: APompliano"

_TO = "to:"
_LINK = " has:links"

def date_cleanup(date):
    """Converting datetime to string to be feed into 30_day search param."""
    from_date = datetime.strftime(date, '%Y%m%d')
    to_date = str(int(from_date) + 1) + '0000'
    from_date+= '0000'
    return from_date, to_date



client = TwitterClient("auth.yaml", _NAME)

tweets = client.search_tweets(_SEARCH_TERM)
result_dict = dict()
for tweet in tweets:
    # Added b/c the _SEARCH_TERM will include instances where users tag him in an original tweet
    if tweet.user.screen_name == 'APompliano':
        print(tweet.created_at, tweet.id, tweet.text, 
                tweet.user.screen_name, tweet.user.name)
        from_date, to_date = date_cleanup(tweet.created_at)
        responses = client.get_tweet_responses(_TO+_NAME+_LINK, 
                            tweet.id, 
                            from_date,
                            to_date
                            )
        print(responses)

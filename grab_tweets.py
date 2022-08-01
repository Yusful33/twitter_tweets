from twitter_setup import TwitterClient


_NAME = "APompliano"
_SEARCH_TERM = "best article you read this week -filter:retweets"

client = TwitterClient("auth.yaml", _NAME)
tweets = client.search_tweets(_SEARCH_TERM)
for tweet in tweets:
    print(tweet.created_at,
        tweet.id, 
        tweet.text, 
        tweet.in_reply_to_status_id, 
        tweet.retweet_count,
        tweet.favorite_count)

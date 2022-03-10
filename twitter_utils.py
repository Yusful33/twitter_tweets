def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

#Utilizing the above function to remove urls

all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]
all_tweets_no_urls[:5]

#Reading Tweets 
timeline = api.home_timeline()
for tweet in timeline:
    print(tweet.text)


today = datetime.today().strftime('%Y/%m/%d') 
last_month = datetime.timedelta(days=10)
last_month = last_month.strftime('%Y/%m/%d')
print(last_month)
print(today)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.user_timeline, since=last_month, until=today).items():
    print( "ID TWEET: " + str(tweet.id), tweet.text)

##################################################################################################

#Getting Info On Twitter Users
user = api.get_user("APompliano")
print("User details:")
print(user.name)
print(user.description)
print(user.location)
for follower in user.followers():
    print(follower.name)
    

    
#Searching twitter
for tweet in api.search(q="Python", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")
    
#printing an ad at regular intervals (does not work yet, need to find the package for get_ad())

import ad
import tweepy
interval = 15
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)
while True:
    print("This is a test, to generate a random ad on my TL")
    ad = get_ad()
    api.update_status(ad)
    time.sleep(intervals)
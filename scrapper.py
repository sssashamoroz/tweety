import tweepy
import credentials as APICredentials

#from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#setup API access
auth = tweepy.OAuthHandler(APICredentials.consumer_key, APICredentials.consumer_secret)
auth.set_access_token(APICredentials.access_key, APICredentials.access_secret)
api = tweepy.API(auth)

#Search and Load
def load_tweets(search_words, date_since):
    tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since).items(5)
    tweet_text = []

    for tweet in tweets:
        #discarting retweets
        if tweet.text[0:2] != "RT":
            tweet_text.append(tweet.text)

    return tweet_text
 
#Main
def main():
    #setup analizer
    analyzer = SentimentIntensityAnalyzer()
    

    search_words = "#Bitcoin"
    date_since = "2020-01-16"

    loaded_tweets = load_tweets(search_words, date_since)
    print(analyzer.polarity_scores(loaded_tweets[0]))
    print(loaded_tweets[0])

main()
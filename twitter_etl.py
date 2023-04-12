import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

def run_twitter_etl():
    # Authenticate with Twitter API
    consumer_key = '****'
    consumer_secret = '******'
    access_token = '******'
    access_token_secret = '******'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    # Extract 100 tweets from user's timeline
    tweets = api.user_timeline(screen_name='@Tech_Impact', 
    count=100,
    include_rts = False,
    tweet_mode = 'extended')

    # Print each tweet's text
    # for tweet in tweets:
    #     print(tweet.text)
        
    tweets_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        
        tweets_list.append(refined_tweet)

    df = pd.DataFrame(tweets_list)
    df.to_csv('s3://myetlbucket-rkg/Tech_Impact_tweets.csv')

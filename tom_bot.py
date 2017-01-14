# Import Libraries
import markovify
import tweepy
import time
import os

# Import auth keys
from auth import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Generate Tweet
def generate_tweet():

    with open(os.path.dirname(__file__) + "lyrics.txt") as f:
        text = f.read()

    text_model = markovify.NewlineText(text)

    output_text = text_model.make_short_sentence(121) + " #TomTale #TomWaits"

    return output_text

# Post the tweet to Twitter
api.update_status(status=generate_tweet())
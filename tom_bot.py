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

    text_model = markovify.NewlineText(text, state_size=3)

    output_text = text_model.make_short_sentence(130) + " #TomWaits"

    return output_text

# Post tweet to Twitter every 4 hours
while True:
    api.update_status(status=generate_tweet())
    time.sleep(14400)
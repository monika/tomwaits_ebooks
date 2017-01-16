# Import Libraries
import markovify
import tweepy
import time
import os

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)

# Generate Tweet
def generate_tweet():

    with open(os.path.dirname(__file__) + "lyrics.txt") as f:
        text = f.read()

    text_model = markovify.NewlineText(text, state_size=3)

    output_text = text_model.make_short_sentence(140)

    return output_text

# Post tweet to Twitter every 4 hours
while True:
    api.update_status(status=generate_tweet())
    time.sleep(14400)
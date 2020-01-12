import tweepy
import csv
import pandas as pd
import re
from datetime import datetime
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# input your credentials here
consumer_key = 'LX8ZLqqQ85mJGmtH8F4F9ot5j'
consumer_secret = 'rvPUTaUrB0zFvAFPhUoJWPzISSD6ENGNHPWNWhRR5ZWx8x7reM'
access_token = '235853049-53rQOhJmrt0RCEuTiVmtxWlcIMyo6aVnXkoLKzSq'
access_token_secret = '4qjpfn5SHIQ4b4WvyIyHo7Iqa7WSRsF2cfSms3h9xHSEv'

client = language.LanguageServiceClient()
text = u'Hello, world!'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
# United Airlines
# Open/Create a file to append data
# csvFile = open('ua.csv', 'a')
# Use csv Writer
# csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, q="#rbc",
                           lang="en",
                           since="2020-01-03").items(1):
    tweetText = tweet.text.encode(
        'ascii', 'ignore').decode('utf-8').replace("/n", '')
    result = re.sub(r"http\S+", "", tweetText)
    # print(type(tweetText))
    # print(tweet.created_at, tweetText)
    # print(result)
    # print("-----------------")
    # print(tweet.user.screen_name)
    # csvWriter.writerow([tweet.created_at, result])
    # csvWriter.writerow([tweet])

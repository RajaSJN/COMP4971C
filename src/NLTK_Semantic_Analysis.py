#Vader is Semantic analyser designed for social media, so we can judge title of posts in finance subreddits
from math import ceil
from urllib import request
from nltk.collocations import TrigramCollocationFinder
from nltk.sentiment import SentimentIntensityAnalyzer
import json
import requests
from datetime import date
import pandas as pd
import matplotlib as plt
sia = SentimentIntensityAnalyzer()
today = date.today()
#To determine number of days from start, to last scan 
startDate = date(2020,1,22)
numberOfDays= today-startDate
print(str(numberOfDays.days))
numberofRequestsNeeded = numberOfDays.days%100 + ceil((numberOfDays.days-(numberOfDays.days%100)*100)/100)*1
comments =[]
# for testing time we shall just use 100 days of data
for i in range(0,1):
    textDays = str(numberOfDays.days-100*i)
    tempUrl = f"https://api.pushshift.io/reddit/search/comment/?q=science&subreddit=wallstreetbets&after="+textDays+"d&size=100"
    request=requests.get(tempUrl)
    json_response = request.json()
    tempComments = json_response['data']
    comments.append(tempComments)
print(len(comments))
print(sia.polarity_scores("Wow, Sid is great!"))
print(sia.polarity_scores("This is not sucky"))
print("Look above")
totalPolarity = 0.0
df = pd.DataFrame(comments)
# df.to_csv("src/RedditPosts.csv")
print(comments[0][0].keys())
count = 0
# for testing time we shall just use 100 days of data
for j in range(0,1):
    for i in comments[j]:
        totalPolarity+= sia.polarity_scores(comments[j][0]["body"])['compound'] 
        count +=1
print(totalPolarity/count)
#there is a key 'created_utc' which can be used to find out which date a post was posted    

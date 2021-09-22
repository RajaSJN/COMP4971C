#Vader is Semantic analyser designed for social media, so we can judge title of posts in finance subreddits
from math import ceil
from urllib import request
from nltk.collocations import TrigramCollocationFinder
from nltk.sentiment import SentimentIntensityAnalyzer
import json
import requests
from datetime import date
import pandas as pd
from matplotlib import pyplot as plt
sia = SentimentIntensityAnalyzer()
today = date.today()
#Currentlty we can see that we can only get a maximum of 100 data points 
#However, a new solution is that we extract the first 100 posts (later all the posts) of each day and then calculate a cummulative semantic value 
#Then we can plot the trend of the change of semantics to determine if there is a correlation
#To determine number of days from start, to last scan 
startDate = date(2020,1,22)
#for testing purposes we set the enddate to a much lower value
endDate = today
numberOfDays= endDate-startDate
print(str(numberOfDays.days))
numberofRequestsNeeded = numberOfDays.days%100 + ceil((numberOfDays.days-(numberOfDays.days%100)*100)/100)*1
comments =[]
# for testing time we shall just use 100 days of data
for i in range(0,1):
    textDays = str(numberOfDays.days-100*i)
    tempUrl = f"https://api.pushshift.io/reddit/search/comment/?q=science&subreddit=wallstreetbets&after="+textDays+"d&size=1000"
    request=requests.get(tempUrl)
    json_response = request.json()
    tempComments = json_response['data']
    comments.append(tempComments)
# print(len(comments))
# print(sia.polarity_scores("Wow, Sid is great!"))
# print(sia.polarity_scores("This is not sucky"))
# print("Look above")
totalPolarity = 0.0
print(comments[0][0].keys())
count = 0
compoundPolarity = []
datePosting = []
# for testing time we shall just use 100 days of data
for j in range(0,1):
    for i in comments[j]:
        totalPolarity+= sia.polarity_scores(comments[j][count]["body"])['compound'] 
        datePosting.append(count)
        print(comments[j][count]["body"])
        compoundPolarity.append(sia.polarity_scores(comments[j][count]["body"])['compound'])
        count +=1
print(totalPolarity/count)
print(count)
plt.plot(datePosting, compoundPolarity)
print(datePosting)
# plt.ylim(-0.3600, -0.3612)
plt.show()
#there is a key 'created_utc' which can be used to find out which date a post was posted    

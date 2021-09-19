#Vader is Semantic analyser designed for social media, so we can judge title of posts in finance subreddits
from urllib import request
from nltk.collocations import TrigramCollocationFinder
from nltk.sentiment import SentimentIntensityAnalyzer
import json
import requests
sia = SentimentIntensityAnalyzer()
# url = f"https://api.pushshift.io/reddit/search/comment/?author=MockDeath&sort=asc&size=100"
#all you have to do is just create multiple requests, split into sizes of 100 days max
url = f"https://api.pushshift.io/reddit/search/comment/?q=science&subreddit=wallstreetbets&after=365d&size=100"
request=requests.get(url)
#this gives the json as a python dictionary
json_response = request.json()
#there is one data key in the dictionarity where all the information from the json is stored as a list
comments = json_response['data']
# print(type(comments))
#each comment is an element in the list
print(len(comments))
# #each element itself is a dictionary
# print(type(comments[0]))
# #here are the parameters I want
# print(comments[0].keys())
# #lets gooo
# print(comments[0]["body"])
# print(sia.polarity_scores("Wow, Sid is great!"))
print(sia.polarity_scores("This is so sucky"))
from datetime import datetime
print(datetime.fromtimestamp(comments[0]["created_utc"]))
totalPolarity = 0.0
for i in comments:
    totalPolarity+= sia.polarity_scores(comments[0]["body"])['compound'] 
print(totalPolarity/len(comments))
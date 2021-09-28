import json
import urllib.request
from nltk.sentiment import SentimentIntensityAnalyzer
from matplotlib import pyplot as plt
sia = SentimentIntensityAnalyzer()
from psaw import PushshiftAPI 
import datetime as dt
def get_posts_data(author, last_utc):
    url = 'https://api.pushshift.io/reddit/search/comment/?q=science&subreddit=wallstreetbets&after='+textDays+'d&size=1000'
    web_url = urllib.request.urlopen(url)
    contents = web_url.read()
    encoding = web_url.info().get_content_charset('utf-8')
    data = json.loads(contents.decode(encoding))
    return data


def semantic_analysis(comments):
	totalPolarity = 0
	count = 0
	compoundPolarity = []
	datePosting = []
	# for testing time we shall just use 100 days of data
	for j in range(0, 1):
		for i in comments[j]:
			totalPolarity += sia.polarity_scores(
            comments[j][count]["body"])['compound']
        	datePosting.append(count)
        	print(comments[j][count]["body"])
        	compoundPolarity.append(sia.polarity_scores(
            comments[j][count]["body"])['compound'])
        	tempDate = comments[j][count]["created_utc"]
        	print(str(tempDate))
        	count += 1
	print(totalPolarity/count)
	print(count)
	plt.plot(datePosting, compoundPolarity)
	print(datePosting)
	return

def psaw_search():
	
	return
def continous_data_collection():
	
	return

def main():
    print("Hello World")
    return


if __name__ == "main":
    main()

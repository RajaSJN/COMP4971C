from datetime import date, datetime
from psaw import PushshiftAPI
import json
import urllib.request
from nltk.sentiment import SentimentIntensityAnalyzer
from matplotlib import pyplot as plt
import pandas as pd
sia = SentimentIntensityAnalyzer()
api = PushshiftAPI()


def get_posts_data(author, last_utc):
    url = 'https://api.pushshift.io/reddit/search/comment/?q=science&subreddit=wallstreetbets&after=' + \
        textDays+'d&size=1000'
    web_url = urllib.request.urlopen(url)
    contents = web_url.read()
    encoding = web_url.info().get_content_charset('utf-8')
    data = json.loads(contents.decode(encoding))
    return data


def semantic_analysis(titles, count):
    totalPolarity = 0
    compoundPolarity = []
    # for testing time we shall just use 100 days of data
    for i in titles:
        totalPolarity += sia.polarity_scores(i)['compound']
        compoundPolarity.append(sia.polarity_scores(i)['compound'])
    print(totalPolarity/count)
    return


def psaw_search():
    # starting from the first covid case date in the USA
    #initial is 2020 1, 22
    start_time = int(datetime(2020, 4, 22).timestamp())
    # end training time for the time of the last day of summer
    end_time = int(datetime(2021, 4, 22).timestamp())
    submissions = api.search_submissions(after=start_time, before=end_time,
                       subreddit='wallstreetbets', filter=['score', 'title', 'author'])
    temp = []
    for submission in submissions:
        # time = datetime.fromtimestamp(submission.created_utc).strftime("%Y-%m-%d %H:%M:%S")
        # print(time)
        print(submission.created_utc)
        temp.append(submission)
    df = pd.DataFrame(temp)
    # print(df)
    df.to_csv('April-April202021.csv')
    return


def continous_data_collection():

    return

# def main():
#     print("Hello World")
# 	psaw_search()
#     return


# if __name__ == "main":
#     main()
psaw_search()

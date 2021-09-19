import requests
#using the prawn reddit api
SECRET_KEY = "n1mj4nsUKr_7pc18CTRDyFYH9hbfBQ"
CLIENT_ID = "-Wr_Tsz9_e8qGSy8qVvh_g"
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

# here we pass our login method (password), username, and password
#HAVE TO BE VERY CAREFUL HERE THAT WHEN I LATER MAKE THIS ACCOUNT PUBLIC THAT THE USERNAME AND PASSWORD INFORMATION IS GONE
data = {'grant_type': 'password',
        'username': 'FinanceGur',
        'password': 'COMP4971C'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
res = requests.get("https://oauth.reddit.com/r/wallstreetbets/hot",
                   headers=headers)

# print(res.json())  # let's see what we get
import pandas as pd
df = pd.DataFrame()  # initialize dataframe

# loop through each post retrieved from GET request
for post in res.json()['data']['children']:
    # append relevant data to dataframe
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score']
    }, ignore_index=True)
print(df.head())
df.to_csv("src/RedditPosts.csv")
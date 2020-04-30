import praw
import configparser
import requests
from urllib.parse import urlparse
from datetime import datetime, timezone

def api_call(subreddit, before, after, sort_type):
    return "http://api.pushshift.io/reddit/submission/search/?subreddit={0}&after={1:.0f}&before{2:.0f}&sort_type={3}".format(subreddit, before, after, sort_type)



def main_pushshift():
    subreddit = 'politics'
    before = datetime(2020, 4, 30).replace(tzinfo=timezone.utc).timestamp()
    after = datetime(2020, 4, 1).replace(tzinfo=timezone.utc).timestamp()
    sort_type = 'score'


    response = requests.get(api_call(subreddit, before, after, sort_type))

    if response:
        print('Success!')
        print(response.json())

def main_praw():
    # Initialize connection to reddit
    config = configparser.ConfigParser()
    config.read('praw.ini')
    creds = config['webcredbot']

    # Connect to reddit
    reddit = praw.Reddit(client_id=creds['client_id'],
                         client_secret=creds['client_secret'],
                         username=creds['username'],
                         password=creds['password'],
                         user_agent=creds['user_agent'])

    subreddit = reddit.subreddit('politics')

    for submission in subreddit.hot(limit=10):
        print(submission.title)
        print(submission.url)
        print(submission.id)


if __name__ == "__main__":
    main_pushshift()
    #main_praw()

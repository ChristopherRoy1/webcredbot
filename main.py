import praw
import configparser

config = configparser.ConfigParser()
config.read('praw.ini')

creds = config['webcredbot']


reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     username=creds['username'],
                     password=creds['password'],
                     user_agent=creds['user_agent'])

print(reddit.read_only)

subreddit = reddit.subreddit('politics')

for submission in subreddit.hot(limit=10):
    print(submission.title)
    print(submission.url)
    print(submission.id)

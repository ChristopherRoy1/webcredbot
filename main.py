import praw
import configparser

config = configparser.ConfigParser()
config.read('praw.ini')

creds = config['webcredbot']

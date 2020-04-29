import praw
import configparser

config = configparser.ConfigParser()
config.read('praw.ini')

print(str(config.sections()))

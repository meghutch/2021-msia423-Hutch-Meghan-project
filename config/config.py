from os import path

# Getting the parent directory of this file. That will function as the project home.
PROJECT_HOME = path.dirname(path.dirname(path.abspath(__file__)))
print(PROJECT_HOME)

# App config
APP_NAME = "lda_tweets"
DEBUG = True

# Logging
LOGGING_CONFIG = path.join(PROJECT_HOME, 'config/logging.conf')

# Database connection config
#DATABASE_PATH = path.join(PROJECT_HOME, 'data/sportco.db')
#SQLALCHEMY_DATABASE_URI = 'sqlite:////{}'.format(DATABASE_PATH)
#SQLALCHEMY_TRACK_MODIFICATIONS = True
#SQLALCHEMY_ECHO = False  # If true, SQL for queries made will be printed

# API configs
#HOST = "host.docker.internal"
#PORT = 10000
#API_SENTIMENT_PATH = 'sentiment'
#API_ENDPOINT = "http://{}:{}/{}".format(HOST, PORT, API_SENTIMENT_PATH)

# Acquire and process config
#MAX_RECORDS_READ = 100
#SENTIMENT_RAW_LOCATION = path.join(PROJECT_HOME, 'data/tweet_sentiment.json')
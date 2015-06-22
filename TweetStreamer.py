#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import json

#Variables that contains the user credentials to access Twitter API 

PATH_TO_CONFIG = 'Resources/config.json'
tweetlist =[]
MAX = 1000

def parse_config(path):
    config ={}
    if os.path.exists(path):
        with open(path) as f:
                config.update(json.load(f))
    else:
            print "Cannot find config.json"
    return config


#This is a basic listener that just prints received tweets to stdout.
class Listener(StreamListener):

     def on_status(self, status):
        text = status.text
        print "Getting tweets %s of %s" % (len(tweetlist), MAX)
        if len(tweetlist) < MAX:
            tweetlist.append(text)
            return True
        else:
            return False

     def on_error(self, status):
        print status




def get_tweets(keyword, maxTweets = 1000):
        global MAX
        MAX = maxTweets
        
        # Authenticating
        print "Authenticating..."
        config = parse_config(PATH_TO_CONFIG)
        auth = OAuthHandler(config.get('consumer_key'), config.get('consumer_secret'))
        auth.set_access_token(config.get('access_token'), config.get('access_token_secret'))
        print "OK"

        # Streaming
        l = Listener()
        stream = Stream(auth, l)
        stream.filter(track=[keyword], languages=['en'])

        print "OK"        
        return tweetlist




if __name__ == '__main__':
     get_tweets('nutella', 10)

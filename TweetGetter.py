import oauth2
import tweepy
import urllib
import urllib2
import json
from datetime import timedelta
import os
import datetime
from tweepy import OAuthHandler


PATH_TO_CONFIG = 'Resources/config.json'

end = datetime.date.today()
defaultPeriod = timedelta(days = -30)
start = end + defaultPeriod
end = end.strftime("%Y-%m-%d")
start = start.strftime("%Y-%m-%d")
       

# Loads keys and tokens from file
def parse_config(path):
    config ={}
    if os.path.exists(path):
        with open(path) as f:
                config.update(json.load(f))
    else:
            print "Cannot find config.json"
    return config


# Handles twitter authentication
def oauth_request_handler(url, http_method="GET", post_body=None, http_headers=None):
        config = parse_config(PATH_TO_CONFIG)
        consumer = oauth2.Consumer(config.get('consumer_key'), config.get('consumer_secret'))
        token = oauth2.Token(config.get('access_token'), config.get('access_token_secret'))
        client = oauth2.Client(consumer, token)
        resp, content = client.request( url, method=http_method,
                                        body=post_body or '',
                                        headers=http_headers)
        return content
        
# Retrieves tweets from twitter 
def get_tweets(keyword, maxTweets = 5000, from_date = None , to_date = None):
        print "Getting tweets... "
        from_date = from_date or start
        to_date = to_date or end
        url = url = 'https://api.twitter.com/1.1/search/tweets.json?'    
        data = {'q': keyword, 'lang': 'en', 'result_type': 'recent', 'count': maxTweets, 'since': from_date, 'until': to_date}
        url += urllib.urlencode(data)
        
        response = oauth_request_handler(url)
        jsonData = json.loads(response)
        tweetlist = []
        if 'errors' in jsonData:
            print "API Error"
            print jsonData['errors']
        else:
            for item in jsonData['statuses']:
                tweetlist.append(item['text'])            
        print "OK"
        return tweetlist

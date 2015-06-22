import csv
import re
import numpy
from numpy import mean
from math import *

PATH_TO_DICTIONARY = 'Resources/labMTfinal.csv'

# Load dictionary into the program
def load_dictionary(path):
        dictionary = {}
        try:
            reader = csv.DictReader(open(path))
        except:
            print "Could not read file!"
        
        for row in reader:
            key = row.pop('word')
            dictionary[key] = row
        return dictionary


labMT = load_dictionary(PATH_TO_DICTIONARY)
  
        
    

def sentiment_calc(keywords):
        X = 0.0
        avgs = sigmas = probs = numpy.array([])
        for w in keywords:
            avgs = numpy.append(avgs, float(labMT[w]['avg']))
            sigmas = numpy.append(sigmas, float(labMT[w]['std_dev']))

        X = avgs.mean() 
        #print avgs
        
        for i in range(0, len(keywords)):
                prob = normpdf(X, avgs[i], sigmas[i])
                probs = numpy.append(probs, prob)

        #print self.normpdf(7, 6, 1)    #0.655
        #print self.normpdf(7, 8, 3)    #0.813
        
        sentiment = sum(avgs*probs)/sum(probs)
        #print sentiment
        return sentiment


# Normal probability distribution function
def normpdf(x, mu, sigma):
        prob = 0.5 * (1 + erf(abs(x - mu)/sqrt(2 * sigma**2)))
        return prob 



    # Use dictionary to tweet sentiment
def get_tweet_sentiment(tweet):
        # Split tweet into individual words
        count = 0;
        words = tweet.split()
        
        #words = re.compile(r'/W+').split(tweet)
        
        for word in words[:]:
                if word in labMT and not 4 <= float(labMT[word]['avg']) <= 6:
                        count += 1
                else:
                        words.remove(word)
        
        #print words        
        if count >= 2:
            return sentiment_calc(words)
            #print "count =", count
            
        #else:
            #print "Sentiment indeterminant/neutral"

def classify_tweetlist(tweetlist):
        print "Classifying tweets..."
        tweettable = {}
        for tweet in tweetlist:
                sentiment = get_tweet_sentiment(tweet)
                if sentiment is not None:
                        if sentiment <= 4:
                                tweettable[tweet] = [sentiment, 'BAD']
                        elif sentiment <= 6:
                                tweettable[tweet] = [sentiment, 'NEUTRAL']
                        else:
                                tweettable[tweet] = [sentiment, 'GOOD']
        print "OK"           
        return tweettable
        

        

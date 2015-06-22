import re
import nltk

        
# Creates a generalized tweet list by calling clean_tweet()
def  process_tweetlist(myList):
        print "Cleaning tweets..."
        cleanlist = []
        for tweet in myList:
            cleanlist.append(clean_tweet(tweet))
        print "OK"
        return cleanlist
        #self.classifier.classify_tweetlist(finallist)
    
# Generalizes tweets
def clean_tweet(t):
        # Change to lowercase
        t = t.lower()
        # Replace hyperlink with "URL" 
        t = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',t)
        # Replace twitter handle with "USERNAME"
        t = re.sub('@[^\s]+', 'USERNAME', t)
        # Remove additional spaces
        t = re.sub('[\s]+', ' ', t)
        # Remove "RT" 
        #t = re.sub(r'\brt','XXXXXXX', t)        
	# Trim
        t = t.strip()
        # Remove quotation marks ""
        #remove first/last " or 'at string end
        t = t.rstrip('\'"')
        t = t.lstrip('\'"')
        
        return t

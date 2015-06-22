import barplot as bp
import pieplot as pp
import scatterplot as sp
import TweetStreamer as ts
import TweetGetter as tg
import TweetCleaner as tc
import TweetClassifier as tcf


def visualize_sentiment(word,n = 100, method = 'search'):
    if method is 'streaming':
        # Get tweets using Streaming API
        tweetlist = ts.get_tweets(word,n)
    else:
        # Get tweets using Search API
        tweetlist = tg.get_tweets(word,n)
                
    tweetlist = tc.process_tweetlist(tweetlist)
    tweetlist = tcf.classify_tweetlist(tweetlist)

    # Visualize sentiment
    bp.bar_plot(tweetlist)
    sp.scatter_plot(tweetlist)
    pp.pie_plot(tweetlist)




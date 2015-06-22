import numpy as np
import matplotlib.pyplot as plt


def bar_plot(table):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # The Data
    sentlabel = zip(*table.values())
    good= sentlabel[1].count('GOOD')
    neutral = sentlabel[1].count('NEUTRAL')
    bad = sentlabel[1].count('BAD')
    
    N = 3
    sentvals = [good, neutral, bad]

    ## necessary variables
    ind = np.arange(N)                # the x locations for the groups
    width = 0.40                      # the width of the bars

    ## the bars
    rects1 = ax.bar(ind, sentvals, width,
                color='black')

    # axes and labels
    ax.set_xlim(-width,len(ind)+width)
    ax.set_ylim(0,len(table))
    ax.set_ylabel('No. of tweets')
    ax.set_title('Sentiment classification')
    xTickMarks = ['Good', 'Neutral', 'Bad']
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=0, fontsize=10)

    ## add a legend
        #ax.legend( (rects1[0]), ('Men') )
 




 
   # plt.draw()
    plt.show()

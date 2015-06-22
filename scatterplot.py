import numpy as np
import matplotlib.pyplot as plt



def scatter_plot(table):
    plt.style.use('ggplot')
    fig = plt.figure()
    ax2 = fig.add_subplot(111)
    total = len(table)

    # The data
    x = range(len(table))
    y = zip(*table.values())[0]
    
    # x,y range
    ax2.set_ylim([1,9])
    ax2.set_xlim([1,len(table)])

    plt.axhline(y=4, color='red')
    plt.axhline(y=6, color= 'green')
    
    
    ax2.set_title('Scatter chart for tweet sentiment')
    ax2.set_xlabel('Number of tweets')
    ax2.set_ylabel('Sentiment value')
    ax2.scatter(x, y, color= 'blue')

    #plt.draw()
    plt.show()

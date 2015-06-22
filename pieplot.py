import matplotlib.pyplot as plt

def pie_plot(table):
    fig = plt.figure()
    
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'POSITIVE', 'NEUTRAL', 'NEGATIVE'

    # The Data
    sentlabel = zip(*table.values())
    pos= sentlabel[1].count('GOOD')
    neut = sentlabel[1].count('NEUTRAL')
    neg = sentlabel[1].count('BAD')
    
    sizes = [pos, neut, neg]
    colors = ['green', 'lightskyblue', 'red']
    if neg > pos:
        explode = (0, 0, 0.1)
    else:
        explode = (0.1, 0, 0)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=45)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

    #plt.draw()
    plt.show()



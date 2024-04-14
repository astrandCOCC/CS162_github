import matplotlib.pyplot as plot
# set up your lists
numlist = [4, 5, 2, 3, 1]
namelist = ['dogs', 'cats', 'fish', 'birds', 'reptiles']
colorlist = ['brown', 'red', 'blue', 'yellow', 'green']
explodelist = [0.1, 0.1, 0.1, 0.1, 0.1]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 90)
plot.axis('equal')
plot.savefig('piechart2.png')
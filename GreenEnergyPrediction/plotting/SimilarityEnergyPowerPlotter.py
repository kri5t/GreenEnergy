__author__ = 'Brian'

import csv
import matplotlib.pyplot as plt
import numpy as np

#plt.plotfile('C:\Users\Brian\Desktop\Brian\Universitetet\Kandidat\Master Thesis\WeLoveGREEN-ENERGY\DATASET_FOR_GREEN_ENERGY_PLOTTING\wind_vs_prices.csv', delimiter=';', cols=(0, 1),
 #   names=('Wind Speed', 'Electricity Price'), linestyle='None', marker='.')

N = 11
ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

month=[]
y=[]
x=[]
z=[]

with open('C:\Users\Brian\Desktop\Brian\Universitetet\Kandidat\Master Thesis\WeLoveGREEN-ENERGY\DATA_FOR_STATION_SIMILARITY\STATION_LIST_COMBINING.csv', 'rb') as csvfile:
    dat = csv.reader(csvfile, delimiter=';')
    for row in dat:
        month.append(int(row[0]))
        x.append(int(row[1]))
        y.append(int(row[3]))
        z.append(int(row[5]))

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, x, width, color='r')

rects2 = ax.bar(ind+width, y, width, color='y')

rects3 = ax.bar(ind+(width*2), z, width, color='b')

# add some
ax.set_ylabel('Wind Speed Compare')
ax.set_title('Wind Speed from different stations')
ax.set_xticks(ind+(width*2))
ax.set_xticklabels( month )

ax.legend( (rects1[0], rects2[0], rects3[0]), ('Aarhus Lufthavn', 'Karup', 'Aarhus Syd') )


#def autolabel(rects):
    # attach some text labels
 #   for rect in rects:
  #      height = rect.get_height()
   #     ax.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%d'%int(height),
    #        ha='center', va='bottom')

#autolabel(rects1)
#autolabel(rects2)
#autolabel(rects3)

plt.show()
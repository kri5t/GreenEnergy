__author__ = 'Brian'

import csv
import matplotlib.pyplot as plt
import numpy as np

plt.plotfile('C:\Users\Brian\Desktop\Brian\Universitetet\Kandidat\Master Thesis\WeLoveGREEN-ENERGY\DATASET_FOR_GREEN_ENERGY_PLOTTING\wind_vs_prices.csv', delimiter=';', cols=(0, 1),
    names=('Wind Speed', 'Electricity Price'), linestyle='None', marker='.')

y=[]
x=[]

with open('C:\Users\Brian\Desktop\Brian\Universitetet\Kandidat\Master Thesis\WeLoveGREEN-ENERGY\DATASET_FOR_GREEN_ENERGY_PLOTTING\wind_vs_prices.csv', 'rb') as csvfile:
    dat = csv.reader(csvfile, delimiter=';')
    for row in dat:
        y.append(int(row[1]))
        x.append(int(row[0]))

m,b = np.polyfit(x,y,1)
plt.plot(x, np.array(x) * m +b, color='red')

plt.show()
import csv

__author__ = 'Brian'

from pybrain.datasets import SupervisedDataSet, ImportanceDataSet


class GreenEnergyDataSet(SupervisedDataSet):
    """ A dataset for the XOR function."""
    def __init__(self):
        SupervisedDataSet.__init__(self, 2, 1)

        with open('C:\Users\Brian\Desktop\Brian\Universitetet\Kandidat\Master Thesis\WeLoveGREEN-ENERGY\DATASET_FOR_GREEN_ENERGY_PLOTTING\WIND_TEMP_PRODUCTION_AVERAGE.csv', 'rb') as csvfile:
            dat = csv.reader(csvfile, delimiter=';')
            for row in dat:
              #  print 'sample 0: ' + row[0] + ' sample 1: ' + row[1]
                self.addSample([int(row[1]),int(row[2])],[int(row[0])])

class XORDataSet(SupervisedDataSet):
    """ A dataset for the XOR function."""
    def __init__(self):
        SupervisedDataSet.__init__(self, 2, 1)
        self.addSample([7,28],[743])
        self.addSample([5,28],[701])
        self.addSample([8,28],[676])
        self.addSample([8,28],[641])
        self.addSample([7,28],[642])
        self.addSample([8,28],[671])
        self.addSample([8,28],[659])
        self.addSample([8,29],[629])
        self.addSample([8,30],[596])
        self.addSample([8,29],[550])
        self.addSample([10,30],[533])
        self.addSample([11,30],[499])
        self.addSample([413,28],[528])
        self.addSample([12,30],[567])
        self.addSample([10,29],[574])




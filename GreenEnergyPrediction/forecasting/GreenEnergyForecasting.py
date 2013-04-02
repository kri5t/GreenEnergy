import csv
from BuildDataSet import XORDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer


__author__ = 'Brian'

def testTraining():
    d = XORDataSet()
    n = buildNetwork(d.indim, 5, d.outdim, recurrent=True)
    t = BackpropTrainer(n, learningrate = 0.1, momentum = 0.1, verbose = True)
    t.trainOnDataset(d, 1000)
    t.testOnData(verbose= True)

if __name__ == '__main__':
    testTraining()
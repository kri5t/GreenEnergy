import csv
from BuildDataSet import GreenEnergyDataSet,XORDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer


__author__ = 'Brian'


def testTraining():
    d = XORDataSet()
    n = buildNetwork(d.indim, 4, d.outdim, recurrent=True)
    t = BackpropTrainer(n, learningrate = 0.01, momentum = 0.99, verbose = True)
    t.trainOnDataset(d, 200)
    t.testOnData(verbose= True)

if __name__ == '__main__':
    testTraining()
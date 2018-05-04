##from keras.models import Sequential
##from keras.layers import Dense
import numpy as np
from sklearn import GaussianNB
def Naive_Bayes():
    print("Loading Data")
    dataset = numpy.loadtxt("responses_cleaned2.csv", delimiter=",")
    #split into input(X) and output(Y) variables
    X = dataset
Naive_Bayes()

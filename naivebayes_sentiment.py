##from keras.models import Sequential
##from keras.layers import Dense
################################
#HW5 Implementation            #
#Made for UIC:CS412            #
#Liam Edelman, Nikhil Shankar  #
#Uses tools form Scikit, Keras #
################################
import numpy as np
from sklearn.naive_bayes import GaussianNB
def Naive_Bayes():
    print("Loading Data")
    labels = np.loadtxt("labels_sentiment.csv")
    features = np.loadtxt("features_sentiment.csv", delimiter=",")
    #split into input(X) and output(Y) variables
    X = features[0:760,:]
    X_test = features[761:,:]
    Y = labels[0:760] 
    Y_test = labels[761:]
    clf = GaussianNB()
    clf.fit(X,Y)
    print("score", clf.score(X_test,Y_test))
Naive_Bayes()

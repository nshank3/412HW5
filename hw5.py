##from keras.models import Sequential
##from keras.layers import Dense
import numpy
numpy.random.seed(8)
#Loading Data#
dataset = numpy.loadtxt("responses_cleaned2.csv", delimiter=",")
#split into input(X) and output(Y) variables
X = dataset[1:8, 141]
print(X)

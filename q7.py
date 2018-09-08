import NeuralNet
import Testing
import random

possibleExamples = [([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])]


def createExamples(size):
    numTrain = size * 4 / 5
    numTest = size / 5
    training = []
    testing = []
    for i in range(numTrain):
        training.append(random.choice(possibleExamples))
    for i in range(numTest):
        testing.append(random.choice(possibleExamples))

    print "Generated " + str(size) + " Examples \n"
    return training, testing


def xor():
    examples = createExamples(1000)
    result = []
    # no hidden layer
    for i in range(5):
        result.append(NeuralNet.buildNeuralNet(examples, maxItr=400, hiddenLayerList=[])[1])
    print "Perceptrons in Hidden Layer: 0 \n"
    print "Max: " + str(max(result)) + " Average: " + str(Testing.average(result)) +\
          " Std Dev: " + str(Testing.stDeviation(result)) + "\n"

    # 1 in hidden layer
    result = []
    for i in range(5):
        result.append(NeuralNet.buildNeuralNet(examples, maxItr=400, hiddenLayerList=[1])[1])
    print "Perceptrons in Hidden Layer: 1 \n"
    print "Max: " + str(max(result)) + " Average: " + str(Testing.average(result)) +\
          " Std Dev: " + str(Testing.stDeviation(result)) + "\n"

    # 2 in hidden layer
    result = []
    for i in range(5):
        result.append(NeuralNet.buildNeuralNet(examples, maxItr=400, hiddenLayerList=[2])[1])
    print "Perceptrons in Hidden Layer: 2 \n"
    print "Max: " + str(max(result)) + " Average: " + str(Testing.average(result)) +\
          " Std Dev: " + str(Testing.stDeviation(result)) + "\n"

    # 3 in hidden layer
    result = []
    for i in range(5):
        result.append(NeuralNet.buildNeuralNet(examples, maxItr=400, hiddenLayerList=[3])[1])
    print "Perceptrons in Hidden Layer: 3 \n"
    print "Max: " + str(max(result)) + " Average: " + str(Testing.average(result)) +\
          " Std Dev: " + str(Testing.stDeviation(result)) + "\n"

xor()

import math
import random


# Divide the data into training set, validation set, testing set by proportion 2:1:1
f = open("ANN_Iris data.txt","r")
line = f.readlines()
line.pop()
f.close()
line = [i.split(",") for i in line]
for i in line:
    for j in range(4):
        i[j] = float(i[j])
    if i[-1] == 'Iris-setosa\n':
        i[-1] = [1, 0, 0]
    elif i[-1] == 'Iris-versicolor\n':
        i[-1] = [0, 1, 0]
    else:
        i[-1] = [0, 0, 1]
data = line[:]

Training_set = []
Validation_set = []
Testing_set = []

for i in range(75):
    n = random.randrange(len(line))
    Training_set.append(line.pop(n))
for i in range(38):
    n = random.randrange(len(line))
    Validation_set.append(line.pop(n))
Test_set = line[:]


# Use sigmoid function as activation function
def sigmoid(p):

    return 1/(1 + math.exp(-p))


class Neuron:

    def __init__(self, n):
        self.input_weight = None
        self.number_of_input = n
        self.value = None
        self.error = None

    def evaluate(self, i):
        weight = self.input_weight
        potential = sum([i[n] * weight[n] for n in range(len(i))])
        self.value = sigmoid(potential)

    def evaluate2(self, i):
        weight = self.input_weight
        potential = sum([i[n] * weight[n] for n in range(len(i))])
        return sigmoid(potential)

    def getvalue(self):
        return self.value

    def set_error(self, e):
        self.error = e

    def get_error(self):
        return self.error

    def set_weight(self, w):
        self.input_weight = w

    def get_weight(self):
        return self.input_weight

    def initialise(self):
        # self.input_neurons = input_neurons
        self.input_weight = [ 0.01 + 0.499 * random.random() for i in range(self.number_of_input+1)]


class ANN():
    def __init__(self, lr = 0.2):
        self.hidden_neurons = 5
        self.wij = None
        self.wi = None
        self.hidden = [Neuron(4) for i in range(self.hidden_neurons)]
        self.output = [Neuron(self.hidden_neurons) for i in range(3)]
        self.lr = lr

    def initialize(self):
        for i in self.hidden:
            i.initialise()
        for i in self.output:
            i.initialise()

    def back_propagation(self, s):
        expected_out = s[-1]
        for i in range(3):
            o = self.output[i].getvalue()
            error = o * (1-o) * (expected_out[i] - o)
            self.output[i].set_error(error)

        for j in range(self.hidden_neurons):
            i = self.hidden[j]
            o = i.getvalue()
            error = o * (1-o) * sum([k.get_weight()[j] * k.get_error() for k in self.output])
            i.set_error(error)

        o = [i.getvalue() for i in self.hidden]
        o.append(1)
        for i in self.output:
            w = i.get_weight()
            for j in range(self.hidden_neurons+1):
                d = self.lr * o[j] * i.get_error()
                w[j] += d
            i.set_weight(w)

        sb = s[0:-1]
        sb.append(1)
        for i in self.hidden:
            w = i.get_weight()
            for j in range(5):
                d = self.lr * sb[j] * i.get_error()
                w[j] += d
            i.set_weight(w)

    def evaluate(self, s):
        inputs = s[0:-1]
        inputs.append(1)
        outputs = []
        for i in self.hidden:
            a = i.evaluate2(inputs)
            outputs.append(a)
        o = []
        for i in self.output:
            a = i.evaluate2(outputs)
            o.append(a)
        return o

    def train_on_one_sample(self, s):
        inputs = s[0:-1]
        inputs.append(1)
        outputs = []
        for i in self.hidden:
            i.evaluate(inputs)
            outputs.append(i.getvalue())
        o = []
        for i in self.output:
            i.evaluate(outputs)
            o.append(i.getvalue())

        self.back_propagation(s)

    def train(self, T, V):
        # Stop training as soon as the accuracy rate on validation set is decreasing

        over_trained = False
        accuracy = 0
        i = 0

        while not over_trained:
            i += 1
            for t in T:
                self.train_on_one_sample(t)

            new_accuracy = self.accuracy(V)
            if new_accuracy >= accuracy and i < 1000:
                accuracy = new_accuracy

            else:
                over_trained = True

    def accuracy(self, S):
        # Calculate the accuracy on classifying data from set S
        accuracy = 0
        for i in S:
            o = a.evaluate(i)
            m = max(o)
            if m == o[0]:
                r = [1,0,0]
            elif m == o[1]:
                r = [0,1,0]
            elif m == o[2]:
                r = [0,0,1]

            if r == i[-1]:
                accuracy += 1
        return accuracy/len(S)

    def classify(self, i):
        # Classify i and comment on the correctness of this classification
        print(i)
        o = a.evaluate(i)
        m = max(o)
        if m == o[0]:
            r = [1,0,0]
            print("classified as Iris-setosa")
        elif m == o[1]:
            r = [0,1,0]
            print("classified as Iris-versicolor")
        elif m == o[2]:
            r = [0,0,1]
            print("classified as Iris-virginica")

        if r == i[-1]:
            print("classified in the right category")
        else:
            print("classified in the wrong category")

        print()


if __name__ == "__main__":
    a = ANN()
    a.initialize()

    print("Training Neural network")
    a.train(Training_set, Validation_set)
    print("Finished training, achieve a accuracy rate of ", a.accuracy(Test_set), "on testing set")
    print()

    print("Now, we will try to classify the class of some Iris with our trained network")
    for i in range(5):
        d = random.choice(data)
        a.classify(d)




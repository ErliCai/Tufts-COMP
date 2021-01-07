from numpy import random as randnormal
from numpy.lib.scimath import logn
import matplotlib.pyplot as plt
import random
import math
from math import e as exp
from datetime import datetime


class Bandit:

    def __init__(self):
        self._mean = 0

    def update(self):
        self._mean += randnormal.normal(loc=0, scale=0.01)

    def get_next_value(self):
        # return self._value
        return randnormal.normal(loc=self._mean, scale=1)


class TenArmBandits:
    def __init__(self, epsilon=0.1, a=0.1):
        self._bandits = [Bandit() for i in range(10)]
        self._qvalues = [0] * 10
        self._a = a
        self._n = 1
        self._epsilon = epsilon

    def update(self):
        for j in range(10):
            self._bandits[j].update()

    def _MaxQ(self):
        q = max(self._qvalues)
        MaxPos = self._qvalues.index(q)
        return MaxPos

    def get_next_value(self, i):
        return self._bandits[i].get_next_value()

    def greedy(self, UpdateFunction):
        i = self._MaxQ()
        q = self.get_next_value(i)
        UpdateFunction(i, q)
        return q

    def explore(self,UpdateFunction):
        i = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        q = self.get_next_value(i)
        UpdateFunction(i, q)
        return q

    def updateq(self, i, q):
        raise NotImplementedError("To be implemented in subclass")

    def next_step(self):
        self.update()
        if random.uniform(0, 1) < (1 - self._epsilon):
            print(1)
            q = self.greedy(self.updateq)
        else:
            print(2)
            q = self.explore(self.updateq)
        return q


class Constant_Step(TenArmBandits):

    def __init__(self):
        super().__init__()

    def updateq(self, i, q):
        self._qvalues[i] += self._a * (q - self._qvalues[i])

class Sample_Average(TenArmBandits):

    def __init__(self):
        super().__init__()

    def updateq(self, i, q):
        self._qvalues[i] += (1/self._n) * (q - self._qvalues[i])
        self._n += 1




def f():
    # This function takes about 10 seconds to complete
    s = Sample_Average()
    total = 0
    for i in range(11):
        q = s.next_step()
        total += q
        print(s._qvalues)
        print(q)
    print(s._n)
    print(s._n)
    return total

def g():
    c = Constant_Step()
    total = 0
    for i in range(11):
        q = c.next_step()
        total += q
        print(c._qvalues)
        print([b._mean for b in c._bandits])
        print(q)
    return total


print(f())
print(g())
from numpy import random as randnormal
from numpy.lib.scimath import logn
import matplotlib.pyplot as plt
import random
import math
from math import e as exp
import numpy as np
import seaborn as sns
from scipy.stats import norm
from datetime import datetime


class Bandit:

    def __init__(self):
        self._mean = 0

    def update(self):
        self._mean += randnormal.normal(loc=0, scale=0.01)

    def get_next_value(self):
        # return self._value
        return randnormal.normal(loc=self._mean, scale=1)


class Non_Stationary_Ten_armed_Bandit:

    def __init__(self):
        self.bandits = [Bandit() for i in range(10)]

    def update(self):
        for bandit in self.bandits:
            bandit.update()

    def getvalue(self):
        return [b.get_next_value() for b in self.bandits]


class Constant_Step:
    def __init__(self):
        self._q = [0]*10
        self._optimal = False

    def greedy(self,L,n):
        i = self._q.index(max(self._q))
        q = L[i]
        if q == max(L):
            self._optimal = True
        else:
            self._optimal = False
        return i, q

    def explore(self,L,n):
        q = L[n]
        if q == max(L):
            self._optimal = True
        else:
            self._optimal = False
        return n, q

    def step(self, L, n):
        if n == 11:
            i, q = self.greedy(L, n)
        else:
            i, q = self.explore(L, n)
        self._q[i] += 0.1 * (q-self._q[i])
        return q

class Sample_Average:
    def __init__(self):
        self._q = [0]*10
        self._n = 1
        self._optimal = False

    def greedy(self, L, n):
        i = self._q.index(max(self._q))
        q = L[i]
        if q == max(L):
            self._optimal = True
        else:
            self._optimal = False
        return i, q

    def explore(self, L, n):
        q = L[n]
        if q == max(L):
            self._optimal = True
        else:
            self._optimal = False
        return n, q

    def step(self, L, n):
        if n == 11:
            i, q = self.greedy(L, n)
        else:
            i, q = self.explore(L, n)
        self._q[i] += (q-self._q[i])/self._n
        self._n += 1
        return q


Xaxis = [1, 3, 5, 10, 15, 20] + [50 * i for i in range(1,201)]


def f(steps):
    B = Non_Stationary_Ten_armed_Bandit()
    C = Constant_Step()
    S = Sample_Average()
    total1 = 0
    total2 = 0
    optimal1 = [0]
    optimal2 = [0]
    Number_of_steps = steps
    Result = [[],[]]
    for i in range(Number_of_steps):
        n = 11
        if random.uniform(0, 1) > 0.9:
            n = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        B.update()
        L = B.getvalue()
        q1 = C.step(L, n)
        q2 = S.step(L, n)
        total1 += q1
        total2 += q2
        if C._optimal:
            optimal1.append(optimal1[-1] + 1)
        else:
            optimal1.append(optimal1[-1])
        if S._optimal:
            optimal2.append(optimal2[-1] + 1)
        else:
            optimal2.append(optimal2[-1])
        if (i+1) in Xaxis:
            Result[0].append(total1/(i+1))
            Result[1].append(total2/(i+1))

    #     print(q1, q2)
    #     print(C._q)
    #     print(S._q)
    # print([b._mean for b in B.bandits])
    # print(total1, total2)

    return total1/Number_of_steps,total2/Number_of_steps, Result, [optimal1, optimal2], L


if __name__ == '__main__':
    start = datetime.now()
    t = [0,0]
    t1 = [0] * 206
    t2 = [0] * 206
    o1 = [0] * 206
    o2 = [0] * 206
    L = []
    number_of_trials = 1000
    for i in range(number_of_trials):
        result = f(10000)
        t[0] += result[0]
        t[1] += result[1]
        t1 = [t1[m] + result[2][0][m] for m in range(len(t1))]
        t2 = [t2[m] + result[2][1][m] for m in range(len(t1))]
        o1 = [o1[m] + result[3][0][m] for m in range(len(o1))]
        o2 = [o2[m] + result[3][1][m] for m in range(len(o2))]
        L += result[4]
    for i in range(len(t1)):
        t1[i] = t1[i]/number_of_trials
        t2[i] = t2[i]/number_of_trials
        o1[i] = o1[i]/((i+1) * number_of_trials)
        o2[i] = o2[i]/((i+1) * number_of_trials)
    print(t1)
    print(t)
    print(L)
    # print(len(Xaxis),len(t1))
    print(datetime.now() - start)
    plt.plot(Xaxis, t1, label='Constant step')
    plt.plot(Xaxis, t2, label='Sample average')
    plt.xlabel('number of steps')
    plt.ylabel('Average rewards')
    plt.legend()
    plt.show()


    sns.distplot(L, bins = 100)
    plt.xlabel('Bandits real value after 10000 steps')
    plt.ylabel('probability density')

    plt.show()





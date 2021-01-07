import Non_stationary
from Non_stationary import Non_Stationary_Ten_armed_Bandit, Sample_Average, Constant_Step
import math
from bisect import bisect
from random import random, uniform, choice
from numpy.lib.scimath import logn
import matplotlib.pyplot as plt
from datetime import datetime


# Implementation of Optimistic Initial value method
class Optimistic_Initial_Values:
    def __init__(self):
        self._q = [4] * 10
        self._n = 1

    def greedy(self, L, n):
        i = self._q.index(max(self._q))
        q = L[i]
        return i, q

    def explore(self, L, n):
        q = L[n]
        return n, q

    def step(self, L, n):
        if n == 11:
            i, q = self.greedy(L, n)
        else:
            i, q = self.explore(L, n)
        self._q[i] += (q - self._q[i]) / self._n
        self._n += 1
        return q


# Implementation of Upper Confidence Bound method
class UCB:
    def __init__(self):
        self._q = [0] * 10
        self._n = 1
        self._count = [1] * 10

    def find_next_step(self, L, n):
        Values = [self._q[i] + math.sqrt(logn(math.e, self._n) / self._count[i]) for i in range(10)]
        i = Values.index(max(Values))
        q = L[i]
        return i, q

    def step(self, L, n):
        i, q = self.find_next_step(L, n)
        self._q[i] += (q - self._q[i]) / self._n
        self._n += 1
        return q


# Implementation of Gradient Bandit method
class Gradient_Bandit:
    def __init__(self):
        self._H = [0] * 10
        self._prob = [0.1] * 10
        self._r = 0
        self._n = 1

    def find_next_step(self, L, n):
        Values = [(math.e) ** (self._H[i]) for i in range(10)]
        s = sum(Values)
        Values = [Values[i] / s for i in range(10)]
        cdf = [Values[0]]
        for i in range(1, len(Values)):
            cdf.append(cdf[-1] + Values[i])

        self._prob = cdf
        i = bisect(cdf, random())
        q = L[i]
        return i, q

    def step(self, L, n):

        i, q = self.find_next_step(L, n)
        self._r += (q - self._r) / self._n
        self._H[i] += 0.25 * (q - self._r) * (1 - self._prob[i])
        for j in range(10):
            if j != i:
                self._H[j] -= 0.25 * (q - self._r) * self._prob[j]
        self._n += 1

        return q


Xaxis = [1, 3, 5, 10, 15, 20] + [50 * i for i in range(1, 201)]


def f(steps):
    B = Non_Stationary_Ten_armed_Bandit()
    O = Optimistic_Initial_Values()
    U = UCB()
    G = Gradient_Bandit()
    S = Sample_Average()
    C = Constant_Step()
    total = [0] * 5
    Q = [0] * 5
    total1 = total2 = total3 = total4 = total5 = 0
    Number_of_steps = steps
    Result = [[], [], [], [], []]
    for i in range(Number_of_steps):
        n = 11
        if uniform(0, 1) > 0.9:
            n = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        B.update()
        L = B.getvalue()
        Q[0] = O.step(L, n)
        Q[1] = U.step(L, n)
        Q[2] = G.step(L, n)
        Q[3] = S.step(L, n)
        Q[4] = C.step(L, n)
        for z in range(5):
            total[z] += Q[z]
        if (i + 1) in Xaxis:
            for j in range(5):
                Result[j].append(total[j] / (i + 1))
    return total1 / Number_of_steps, total2 / Number_of_steps, Result, 1, L


if __name__ == '__main__':
    start = datetime.now()
    t = [0, 0]
    T = [[0] * 206] * 5
    t1 = [0] * 206
    t2 = [0] * 206
    L = []
    number_of_trials = 1000
    for i in range(number_of_trials):
        result = f(10000)
        t[0] += result[0]
        t[1] += result[1]
        for j in range(5):
            T[j] = [T[j][m] + result[2][j][m] for m in range(len(T[j]))]
        L += result[4]
    for i in range(len(t1)):
        for j in range(5):
            T[j][i] = T[j][i] / number_of_trials
    print(T[0])
    print(t)
    print(L)
    # print(len(Xaxis),len(t1))
    print(datetime.now() - start)
    plt.plot(Xaxis, T[0], label='Optimistic_Initial_Values')
    plt.plot(Xaxis, T[1], label='UCB')
    plt.plot(Xaxis, T[2], label='Gradient_Bandit')
    plt.plot(Xaxis, T[3], label='Sample Average')
    plt.plot(Xaxis, T[4], label='Constant Step Size')
    plt.xlabel('number of steps')
    plt.ylabel('Average rewards')
    plt.legend()
    plt.show()

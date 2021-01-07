import random

# Most of the codes are copied from Pancake Problem
# only a few changes are made so we no longer calculate forward cost and backward cost
# It runs slower than A* Algorithm
# Heuristic is not removed in this implementation
# It still works as an examination of termination of the algorithm
def item_with_min_value(d):
    return min(d.items(), key=lambda x: x[1])


class PanCake:

    def __init__(self, state, backwardcost=0, paststates=[], n=0):
        self._state = state
        self._backwardcost = backwardcost
        self._paststates = paststates
        self._n = n

    def getstate(self):
        return self._state

    def getcost(self):
        return self._backwardcost

    def getpaststates(self):
        return self._paststates

    def get_Number_of_Steps(self):
        return self._n

    # Heuristic is not removed in this implementation
    # It still works as an examination of termination of the algorithm
    def heuristic(self):
        h = 0
        for i in range(10):
            if self._state[i] != 10-i:
                h += 5
        return h

    def flip(self, n):
        cost = 10 - n
        p1 = self._state[:n]
        p2 = self._state[n:]
        p2.reverse()
        return p1 + p2, cost

    def __hash__(self):
        a = 31
        n = 0
        for i in range(10):
            n += (31**i) * self._state[i]
        return n

    def __eq__(self, other):
        return repr(self.getstate()) == repr(other.getstate())


# Only change here is how we no longer need to calculate the cost from the heuristic function and cost function
class Uniform_Cost_Search:

    def __init__(self, pancake):
        p = PanCake(pancake)
        self._searchingfront = {p: 0}
        self._StatesAlreadySeen = set()
        self._StatesAlreadySeen.add(repr(p.getstate()))

    def action(self):
        p = item_with_min_value(self._searchingfront)[0]
        state = p.getstate()
        backwardcost = p.getcost()
        paststates = p.getpaststates()
        n = p.get_Number_of_Steps()
        for i in range(9):
            next_pancake = p.flip(i)
            new_paststates = paststates[:]
            new_paststates.append(state)
            new_cost = backwardcost + 1
            new_pancake = PanCake(next_pancake[0], new_cost, new_paststates, n+1)
            if new_pancake not in self._searchingfront and repr(new_pancake.getstate()) not in self._StatesAlreadySeen:
                self._searchingfront[new_pancake] = new_cost
                self._StatesAlreadySeen.add(repr(new_pancake.getstate()))
        self._searchingfront.pop(p)
        return p

    # Test if we have reach the terminate state
    def finish(self, p):
        if p.heuristic() == 0:
            return True
        return False

    def findoptimal(self):
        while True:
            p = self.action()
            if self.finish(p):
                paststates = p.getpaststates()
                paststates.append(p.getstate())
                return p.get_Number_of_Steps(), paststates


def test(pancakes):
    # Input should be a list representing pancakes in order of size
    # The list should have length 10 and each number between 1 and 10 should appear exactly once
    if not (len(pancakes) == 10 and sum(pancakes) ==55):
        raise ValueError("Invalid input")

    print('We are starting from: ', pancakes)
    p = Uniform_Cost_Search(pancakes)
    optimal_strategy = p.findoptimal()
    print('We get to correct order in ', optimal_strategy[0], ' steps')
    for i in optimal_strategy[1]:
        print(i)
    print()
    print()


if __name__ == '__main__':

    print('1st Test')
    pancakes1 = [i+1 for i in range(10)]
    test(pancakes1)

    print('2nd Test')
    pancakes2 = [1,2,3,5,6,7,4,8,9,10]
    test(pancakes2)

    print('3th Test')
    pancakes3 = [10,9,8,1,2,3,7,6,5,4]
    test(pancakes3)

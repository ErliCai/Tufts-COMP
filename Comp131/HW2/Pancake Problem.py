import random


# Viewing the pancake problem as a searching problem, we have
# Initial state: the order of pancake now
# Possible Actions: flip under n-th pancake
# Successor function: order of pancakes after flipping
# Goal state: [10,9,8,7,6,5,4,3,2,1]
# Path cost function: number of pancakes being flipped

# I define the cost to be the number of pancakes being flipped

# I define heuristic function to be 5 times the number of pancake that is not in the correct position

# Implementation of A* algorithm starts here

# Function that return item with minimum value
# Later used to find the state to perform next action
def item_with_min_value(d):
    return min(d.items(), key=lambda x: x[1])


# Pancake object(actually Pancakes would be more appropriate) represent the current order of the pancakes
# it also keeps in record the backward cost and states it been through from initial state
# and the number of flips to get to this state
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

    # define heuristic function to be 5 times the number of pancake that is not in the correct position
    def heuristic(self):
        h = 0
        for i in range(10):
            if self._state[i] != 10-i:
                h += 5
        return h

    # flip after n-th pancake
    # Define the cost to be the number of pancakes being flipped
    def flip(self, n):
        cost = 10 - n
        p1 = self._state[:n]
        p2 = self._state[n:]
        p2.reverse()
        return p1 + p2, cost

    # make the object hashable
    # I think this hash function would work but did not examine/proof it
    def __hash__(self):
        a = 31
        n = 0
        for i in range(10):
            n += (31**i) * self._state[i]
        return n

    def __eq__(self, other):
        return repr(self.getstate()) == repr(other.getstate())


class A_star_algorithm:

    def __init__(self, pancake):
        p = PanCake(pancake)
        # should be named frontier, the value represents heuristic plus backward cost
        self._searchingfront = {p: p.heuristic()}
        self._StatesAlreadySeen = set()
        self._StatesAlreadySeen.add(repr(p.getstate()))

    # choosing from a node in frontier with minimum
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
            new_cost = backwardcost+ next_pancake[1]
            new_pancake = PanCake(next_pancake[0], new_cost, new_paststates, n+1)
            if new_pancake not in self._searchingfront and repr(new_pancake.getstate()) not in self._StatesAlreadySeen:
                self._searchingfront[new_pancake] = new_cost + new_pancake.heuristic()
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
    p = A_star_algorithm(pancakes)
    optimal_strategy = p.findoptimal()
    print('We get to correct order in ', optimal_strategy[0], ' steps')
    for i in optimal_strategy[1]:
        print(i)
    print()
    print()


# Some tests to demonstrate the correctness of the algorithm
# I guess my choice of cost function and heuristic are not very good
# since it is slow in solving these problems
if __name__ == '__main__':

    print('1st Test')
    pancakes1 = [i+1 for i in range(10)]
    test(pancakes1)

    print('2nd Test')
    pancakes2 = [1,2,3,5,6,7,4,8,9,10]
    test(pancakes2)

    print('3nd Test')
    pancakes3 = [1,2,3,4,5,6,7,8,9,10]
    random.shuffle(pancakes3)
    test(pancakes3)

    print('4th Test')
    pancakes4 = [1,5,3,4,7,9,10,2,8,6]
    test(pancakes4)

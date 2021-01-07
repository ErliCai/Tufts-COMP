import random


# Behaviour_Tree_Template is a template for behaviour tree
# it has one private inner class, _Node, which is a base class of all kinds of node we implement
# Condition_Node, Task_Node, Composite_Node and Decorator_Node all inherit from _Node
# they represent nodes performing different functions
class Behavior_Tree_Template:

    # _Node is a private class and is prototype of every nodes we implement
    class _Node:
        def __init__(self):
            self._children = []

        def add_child(self, child):
            self._children.append(child)

    # Condition_Node represents condition in a behaviour tree
    # It checks if data from blackboard satisfies some conditions and return True or False
    class Condition_Node(_Node):

        def __init__(self, Blackboard=None):
            super().__init__()
            self._blackboard = Blackboard

        def run(self):
            return NotImplementedError

    # Task_Node represent task in a behaviour tree
    # it perform certain task
    class Task_Node(_Node):

        def __init__(self, Blackboard=None):
            super().__init__()
            self._blackboard = Blackboard

        def run(self):
            return NotImplementedError

    # Composite_Node represent composite in a behaviour tree
    # it return True, False, Running based on the return of it child nodes
    class Composite_Node(_Node):

        def __init__(self, Blackboard=None):
            super().__init__()
            self._blackbard = Blackboard

    # A decoratoralters the basic behavior of the tree-node it is associated with
    class Decorator_Node(_Node):

        def run(self):
            return NotImplementedError

    # Children are evaluated in order of priority
    # It fails if all children have failed, otherwise it succeeds
    class Priority_Node(Composite_Node):

        def __init__(self):
            self._children = {}

        def add_child(self, child, priority=0):
            self._children[child] = priority

        def _sort_child(self):
            return [k for k, v in sorted(self._children.items(), key=lambda item: item[1])]

        def run(self):
            for child in self._sort_child():
                if child.run():
                    return True
            return False

    # Children are evaluated in order (left to right).
    # It fails if all children have failed, otherwise it succeeds
    class Selection_Node(Composite_Node):

        def run(self):
            for child in self._children:
                if child.run():
                    return True
            return False

    # Children are evaluated in order (left to right)
    # It fails as soon as one of the children fails, otherwise it succeeds
    class Sequence_Node(Composite_Node):

        def __init__(self):
            super().__init__()

        def run(self):
            for child in self._children:
                if not child.run():
                    return False
            return True

    # It executes the attached node for a specific amount of time
    # It returns RUNNING while the timer is running
    # It returns SUCCEEDED after the expiration
    class Timer(Decorator_Node):

        def __init__(self, time):
            super().__init__()
            self.time = time

        def run(self):
            print('For', self.time, 's: ', end='')
            self._children[0].run()
            return True

    # It executes the attached node and then it negates its result
    class Logical_negation(Decorator_Node):

        def run(self):
            return not self._children[0].run()

    # It executes the attached node while it succeeds returning RUNNING
    # It returns SUCCEEDED at the first failure
    class Until_Fails(Decorator_Node):

        def run(self):
            if not self._children[0].run():
                return True
            else:
                return 'Running'


# This class implement tasks and conditions specific to roomba
class Roomba_Template:

    # check if battery is above 30
    class Battery(Behavior_Tree_Template.Condition_Node):
        def run(self):
            return self._blackboard['BATTERY_LEVEL'] < 30

    # check if spot clean is requested
    class Spot(Behavior_Tree_Template.Condition_Node):
        def run(self):
            return self._blackboard['SPOT']

    # check if general clean is requested
    class General(Behavior_Tree_Template.Condition_Node):
        def run(self):
            return self._blackboard['GENERAL']

    # check if dusty spot is detected
    class Dusty_spot(Behavior_Tree_Template.Condition_Node):
        def run(self):
            return self._blackboard['DUSTY_SPOT']

    # Generate a home path and write it to blackboard
    class Find_Home(Behavior_Tree_Template.Task_Node):

        def run(self):
            Directions = ['up', 'down', 'left', 'right']
            path = [random.choice(Directions) for i in range(random.randrange(1, 6))]
            self._blackboard['HOME_PATH'] = ' '.join(path)
            print('FIND_HOME: path is', self._blackboard['HOME_PATH'] )
            return True

    # Get home path from blackboard
    class Go_Home(Behavior_Tree_Template.Task_Node):

        def run(self):
            print('GO_HOME:', self._blackboard['HOME_PATH'])
            return True

    # Go back to dock and charge itself
    class Dock(Behavior_Tree_Template.Task_Node):

        def run(self):
            print('DOCK')
            return True

    # perform task clean spot
    class Clean_spot(Behavior_Tree_Template.Task_Node):

        def run(self):
            print('CLEAN_SPOT')
            return True

    # change the state of SPOT in blackboard to False
    class Done_spot(Behavior_Tree_Template.Task_Node):

        def run(self):
            self._blackboard['SPOT'] = False
            print('DONE_SPOT')
            return True

    # change the state of General in blackboard to False
    class Done_general(Behavior_Tree_Template.Task_Node):

        def run(self):
            self._blackboard['GENERAL'] = False
            print('DONE_GENERAL')
            return True

    # perform task clean
    class Clean(Behavior_Tree_Template.Task_Node):

        def run(self):
            print('CLEAN')
            return True

    # perform task do nothing
    class Do_Nothing(Behavior_Tree_Template.Task_Node):

        def run(self):
            print('DO_NOTHING')
            return True


# Implementing roomba by connecting nodes defined above
# Roomba will take a parameter board(short for blackboard)
# with information about the state of the roomba
def roomba(board):
    # Root of the tree
    start = Behavior_Tree_Template.Priority_Node()

    # first child of root
    # check if charging is needed and performing corresponding task
    charge = Behavior_Tree_Template.Sequence_Node()
    charge.add_child(Roomba_Template.Battery(Blackboard=board))
    charge.add_child(Roomba_Template.Find_Home(Blackboard=board))
    charge.add_child(Roomba_Template.Go_Home(Blackboard=board))
    charge.add_child(Roomba_Template.Dock())

    # second child of root
    # check if clean is needed
    # it further divides into general clean and spot clean
    clean = Behavior_Tree_Template.Selection_Node()

    # check if spot needed and performing corresponding task
    spotclean = Behavior_Tree_Template.Sequence_Node()
    spotclean.add_child(Roomba_Template.Spot(board))
    timer1 = Behavior_Tree_Template.Timer(20)
    timer1.add_child(Roomba_Template.Clean_spot())
    spotclean.add_child(timer1)
    spotclean.add_child(Roomba_Template.Done_spot(board))

    # check if general needed and performing corresponding task
    generalclean = Behavior_Tree_Template.Sequence_Node()
    generalclean.add_child(Roomba_Template.General(board))

    subtree1 = Behavior_Tree_Template.Sequence_Node()
    generalclean.add_child(subtree1)
    uf = Behavior_Tree_Template.Until_Fails()

    subtree2 = Behavior_Tree_Template.Sequence_Node()
    uf.add_child(subtree2)
    subtree1.add_child(uf)
    subtree1.add_child(Roomba_Template.Done_general(board))
    negation = Behavior_Tree_Template.Logical_negation()
    negation.add_child(Roomba_Template.Battery(board))
    subtree2.add_child(negation)
    subtree3 = Behavior_Tree_Template.Sequence_Node()

    subtree4 = Behavior_Tree_Template.Selection_Node()
    subtree2.add_child(subtree4)
    subtree4.add_child(subtree3)
    subtree4.add_child(Roomba_Template.Clean())

    subtree3.add_child(Roomba_Template.Dusty_spot(board))
    time2 = Behavior_Tree_Template.Timer(35)
    subtree3.add_child(time2)
    time2.add_child(Roomba_Template.Clean_spot())

    # Connecting all parts of clean
    clean.add_child(spotclean)
    clean.add_child(generalclean)

    # Connecting all parts of the behaviour tree
    start.add_child(charge, 1)
    start.add_child(clean, 2)
    start.add_child(Roomba_Template.Do_Nothing(), 3)
    return start.run()


# Below is five testings of the behaviour tree
# Although there could be infinitely many different kinds of tests
# These five tests will cover all the different output of behaviour tree
def Test1():
    print('Test case 1:')
    T1 = {'BATTERY_LEVEL': 19, 'HOME_PATH': 'up,up,down,down', 'SPOT': True,
          'GENERAL': True, 'DUSTY_SPOT': True}
    print('Roomba condition:', T1)
    roomba(T1)


def Test2():
    print('Test case 2:')
    T2 = {'BATTERY_LEVEL': 35, 'HOME_PATH': 'up,up,down,down', 'SPOT': True,
          'GENERAL': True, 'DUSTY_SPOT': True}
    print('Roomba condition:', T2)
    roomba(T2)
    print('SPOT now has boolean value', T2['SPOT'])


def Test3():
    print('Test case 3:')
    T3 = {'BATTERY_LEVEL': 35, 'HOME_PATH': 'up,up,down,down', 'SPOT': False,
          'GENERAL': True, 'DUSTY_SPOT': True}
    print('Roomba condition:', T3)
    roomba(T3)
    print('GENERAL now has boolean value', T3['GENERAL'])


def Test4():
    print('Test case 4:')
    T4 = {'BATTERY_LEVEL': 35, 'HOME_PATH': 'up,up,down,down', 'SPOT': False,
          'GENERAL': True, 'DUSTY_SPOT': False}
    print('Roomba condition:', T4)
    roomba(T4)


def Test5():
    print('Test case 5:')
    T5 = {'BATTERY_LEVEL': 35, 'HOME_PATH': 'up,up,down,down', 'SPOT': False,
          'GENERAL': False, 'DUSTY_SPOT': False}
    print('Roomba condition:', T5)
    roomba(T5)


# Uncomment tests below to test roomba
# Test1()
# Test2()
# Test3()
# Test4()
# Test5()

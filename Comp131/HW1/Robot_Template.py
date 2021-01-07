

class Robot_Template:

    class Node:
        def __init__(self):
            self._children = []

    class Condition_Node(Node):

        def __init__(self):
            super()

    class Task_Node(Node):
        pass

    class Composite_Node(Node):
        pass

    class Decorator_Node(Node):
        pass

    def p(self):
        return 1

class A:
    def __init__(self, b ):
        self.b = b
    def p(self):
        print(self.b)


class B(A):
    def q(self):
        return 2


if 'Running':
    print(2)

# b = B(1)
# b.p()
# L = {1:2,3:4,414:0}
# a = [k for k, v in sorted(L.items(), key=lambda item: item[1])]
# print(a)
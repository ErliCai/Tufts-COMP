##########################################################################
#
#    randSelect.py
#    randomized selection
#
#    includes functions provided and function students need to implement
#
##########################################################################

import random


# TODO: implement this function
# ray is a list of ints
# index is an int
def randSelect(array, rank):
    print('Looking for value with rank', rank, 'in the array:')
    print(array)
    index = random.randint(0, len(array)-1)
    (L, R, num) = partition(array, index)
    if len(L) > rank:
        print('Thus, we recurse on left')
        print()
        return randSelect(L, rank)
    elif len(L) < rank:
        print('Thus, we recurse on right')
        print()
        return randSelect(R, rank - len(L) - 1)
    else:
        print('Thus, we recurse on nothing. We are done.')
        print('The number we are looking for is ', num)
        return num


def partition(array, index):

    L = []
    R = []
    for i in range(len(array)):
        if i != index and array[i] <= array[index]:
            L.append(array[i])
        elif i != index and array[i] > array[index]:
            R.append(array[i])
    print('Selected ', array[index], ' as the pivot; its rank is ', len(L))
    return L, R, array[index]


if __name__ == '__main__':
    a = [7,6,5,4,3,2,1,0]
    print(randSelect(a, 5))
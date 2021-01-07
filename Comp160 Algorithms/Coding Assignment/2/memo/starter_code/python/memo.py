##########################################################################
#
#    Tufts University, Comp 160 DP coding assignment
#
#    memo.py
#    DP
#
#   Includes functions students need to implement and benchmark tests
#
##########################################################################

import time
from random import choice, randint
from string import ascii_lowercase


##########################################################################
#   Recursive + memoized functions

def rob(houses, i):
    if i < 0:
        return 0
    elif i == 0:
        return houses[0]
    else:
        return max(rob(houses, i - 1), houses[i] + rob(houses, i - 2))


def memo_rob(houses, i):
    Memo = dict()
    Memo[-1] = 0
    Memo[0] = houses[0]
    for j in range(1,i+1):
        Memo[j] = max(Memo[j-1], Memo[j-2] + houses[j])
    return Memo[i]


def SBS(A, target, i):
    if target == 0:
        return True
    elif i < 0 and target != 0:
        return False
    elif A[i] > target:
        return SBS(A, target, i - 1)
    else:
        return SBS(A, target - A[i], i - 1) or SBS(A, target, i - 1)


def _memo_SBS(A, target, i, memo):
    #print(target,i)
    if target == 0:
        print(1)
    if repr([target, i]) in memo:
        return memo[repr([target, i])]
    else:
        if A[i] <= target:
            memo[repr([target, i])] = (_memo_SBS(A, target, i-1, memo) or
                                       _memo_SBS(A, target-A[i], i-1, memo))
        else:
            memo[repr([target, i])] = _memo_SBS(A, target, i - 1, memo)
    return memo[repr([target, i])]

def memo_SBS(A, target, i):
    memo = dict()
    for m in range(target+1):
        memo[repr([m, 0])] = False
    for m in range(i):
        memo[repr([0, m])] = True

    return _memo_SBS(A, target, i, memo)

##########################################################################
#   Benchmarking tests

def benchmark_rob():
    # sizes of tests
    vals = [20, 30, 35, 37]

    for val in vals:

        # generate test case
        houses = [randint(0, 100) for _ in range(val)]

        # benchmarking recursive solution
        t1 = time.time()
        r = rob(houses, val - 1)
        t2 = time.time()
        print("#" * 80)
        print(f"Recursive rob({houses}, {val - 1}): {r}; took {t2 - t1} seconds")
        
        # benchmarking memo solution
        t1 = time.time()
        r = memo_rob(houses, val - 1)
        t2 = time.time()
        print(f"Memoized  rob({houses}, {val - 1}): {r}; took {t2 - t1} seconds")


def benchmark_SBS():
    # sizes of tests
    vals = [10, 20, 25, 27]
    vals = [20]
    for val in vals:

        # generate test case
        # A = [randint(0, 50) for _ in range(val)]
        # target = randint(0, 1000)
        A = [40, 48, 42, 19, 28, 15, 0, 5, 7, 39, 6, 49, 28, 24, 22, 43, 11, 8, 24, 0]
        target = 425

        # benchmarking recursive solution
        t1 = time.time()
        r = SBS(A, target, val - 1)
        t2 = time.time()
        print("#" * 80)
        print(f"Recursive SBS({A}, {target}, {val - 1}): {r}; took {t2 - t1} seconds")
        
        # benchmarking memo solution
        t1 = time.time()
        r = memo_SBS(A, target, val - 1)
        t2 = time.time()
        print(f"Memoized  SBS({A}, {target}, {val - 1}): {r}; took {t2 - t1} seconds")


def run_benchmarks():
    print("-" * 80)
    #benchmark_rob()
    print("-" * 80)
    benchmark_SBS()


if __name__ == "__main__":
    run_benchmarks()
    A = [40, 48, 42, 19, 28, 15, 0, 5, 7, 39, 6, 49, 28, 24, 22, 43, 11, 8, 24, 0]
    print(sum(A))
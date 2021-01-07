##########################################################################
#
#    Tufts University, Comp 160 DP coding assignment
#
#    examples.py
#    DP
#
#   Includes example functions that have been memoized
#
##########################################################################



# Case Analysis:
#   Base Case:
#       fib(k) == k, if k <= 1
#   Recursive Case:
#       fib(n) == fib(n-1) + fib(n-2)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def _memo_fib(n, memo):
    if n in memo:
        return memo[n]
    else:
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = _memo_fib(n-1, memo) + _memo_fib(n-2, memo)
    return memo[n]

def memo_fib(n):
    memo = dict()
    return _memo_fib(n, memo)


# Case Analysis:
#   Base Case(s):
#       LCS("", s2) == ""
#       LCS(s1, "") == ""
#   Recursive Case(s):
#       LCS(s1, s2) == s1[0] + LCS(s1[1:], s2[1:]) if s1[0] == s2[0]
#       LCS(s1, s2) == max(LCS(s1, s2[1:]), LCS(s1[1:], s2)) otherwise
def LCS(s1, s2):
    if not s1 or not s2:
        return ''
    elif s1[0] == s2[0]:
        return str(s1[0]) + LCS(s1[1:], s2[1:])
    else:
        return max(LCS(s1[1:], s2), LCS(s1, s2[1:]), key=len)

def _memo_LCS(s1, s2, memo):
    if (s1, s2) in memo:
        return memo[(s1,s2)]
    if not s1 or not s2:
        memo[(s1,s2)] = ""
    elif s1[0] == s2[0]:
        memo[(s1[1:], s2[1:])] = _memo_LCS(s1[1:], s2[1:], memo)
        memo[(s1, s2)] = str(s1[0]) + memo[(s1[1:], s2[1:])]
    else:
        memo[(s1[1:], s2)] = _memo_LCS(s1[1:], s2, memo)
        memo[(s1, s2[1:])] = _memo_LCS(s1, s2[1:], memo)
        memo[(s1, s2)] = max(memo[(s1[1:], s2)], memo[(s1, s2[1:])], key=len)
    return memo[(s1, s2)]

def memo_LCS(s1, s2):
    memo = dict()
    return _memo_LCS(s1, s2, memo)


# Implementing function: cut_rod(prices, rod_size)
#
# Base case:
# cut_rod(prices, 0) == 0 -- Can't cut anything else
#
# Recursive case:
# -- We have to try all possible rod cuts and take the maximum
# cut_rod(prices, n) == 
#           max(prices[i] + cut_rod(prices, n - i - 1) for i in range(n))) 

def cut_rod(prices, rod_size):
    if rod_size == 0:
        return 0
    else:
        best_price = max(prices[i] + cut_rod(prices, rod_size - i - 1)
                                                for i in range(rod_size))
        return best_price

def _memo_cut_rod(prices, rod_size, memo):
    if rod_size in memo:
        return memo[rod_size]
    else:
        if rod_size <= 0:
            memo[rod_size] = 0
        else:
            for i in range(rod_size):
                memo[rod_size - i - 1] = _memo_cut_rod(prices, rod_size - i - 1, memo)
            memo[rod_size] = max(prices[i] + memo[rod_size - i - 1] for i in range(rod_size))
        return memo[rod_size]

def memo_cut_rod(prices, rod_size):
    memo = dict()
    return _memo_cut_rod(prices, rod_size, memo)

import time
from random import choice, randint
from string import ascii_lowercase

def benchmark_fib():
    vals = [10, 20, 30, 36]
    for val in vals:
        t1 = time.time()
        r = fib(val)
        t2 = time.time()
        print("#"*80)
        print(f"Recursive fib({val}): {r}; took {t2 - t1} seconds")
        t1 = time.time()
        r = memo_fib(val)
        t2 = time.time()
        print(f"Memoized  fib({val}): {r}; took {t2 - t1} seconds")

def benchmark_LCS():
    vals = [1, 2, 5, 10, 13]
    for val in vals:
        s1 = "".join(choice(ascii_lowercase) for _ in range(val))
        s2 = "".join(choice(ascii_lowercase) for _ in range(val))
        t1 = time.time()
        r = LCS(s1, s2)
        t2 = time.time()
        print("#"*80)
        print(f"Recursive LCS(\"{s1}\", \"{s2}\"): \"{r}\"; took {t2 - t1} seconds")
        t1 = time.time()
        r = memo_LCS(s1, s2)
        t2 = time.time()
        print(f"Memoized  LCS(\"{s1}\", \"{s2}\"): \"{r}\"; took {t2 - t1} seconds")

def benchmark_cut_rod():
    vals = [5, 10, 15, 23]
    for val in vals:
        prices = [randint(1,50) for _ in range(val)]
        t1 = time.time()
        r = cut_rod(prices, val)
        t2 = time.time()
        print("#"*80)
        print(f"Recursive cut_rod({prices}, {val}): {r}; took {t2 - t1} seconds")
        t1 = time.time()
        r = memo_cut_rod(prices, val)
        t2 = time.time()
        print(f"Memoized  cut_rod({prices}, {val}): {r}; took {t2 - t1} seconds")


def run_tests():
    benchmark_fib()
    print("-"*80)
    benchmark_LCS()
    print("-"*80)
    benchmark_cut_rod()


if __name__ == "__main__":
    run_tests()
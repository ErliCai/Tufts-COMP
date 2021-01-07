#include <unordered_map>
#include <string>
#include <vector>
#include <algorithm>
#include "examples.h"


using namespace std;


//////////////////////////////////////////////////////////////////////
//  Example 1: Fibonacci
//////////////////////////////////////////////////////////////////////


// Case Analysis:
//     Base Case(s):
//         fib(k) == k if k <= 1
//     Recursive Case(s):
//         fib(n) == fib(n - 1) + fib(n - 2)
int fib(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
}


// helper for memoized function
int _memo_fib(int n, unordered_map<int, int> &memoizer) {
    // if we've already memoized the case, return it
    if (memoizer.find(n) != memoizer.end()) {
        return memoizer[n];
    }

    // whatever we do, save our work to the memoizer
    if (n <= 1) {
        memoizer[n] = n;
    } else {
        int recurse = _memo_fib(n - 1, memoizer) + _memo_fib(n - 2, memoizer);
        memoizer[n] = recurse;
    }
    
    return memoizer[n];
}


// memoized wrapper
int memo_fib(int n) {
    unordered_map<int, int> memoizer;
    return _memo_fib(n, memoizer);
}



//////////////////////////////////////////////////////////////////////
//  Example 2: LCS
//////////////////////////////////////////////////////////////////////



// helper function to compare lengths of 2 string
string max_len(const string &s1, const string &s2) {
    return s1.size() < s2.size() ? s2 : s1;
}


// Case Analysis:
//     Base Case(s):
//         LCS("", s2) == ""
//         LCS(s1, "") == ""
//     Recursive Case(s):
//         LCS(s1, s2) == s1[0] + LCS(s1[1:], s2[1:]) if s1[0] == s2[0]
//         LCS(s1, s2) == max_len(LCS(s1, s2[1:]), LCS(s1[1:], s2)) otherwise
string LCS(string s1, string s2) {
    if (s1 == "" or s2 == "") {
        return "";
    } else if (s1[0] == s2[0]) {
        return string(1, s1[0]) + LCS(s1.substr(1), s2.substr(1));
    } else {
        return max_len(LCS(s1, s2.substr(1)), LCS(s1.substr(1), s2));
    }
}


// helper for memoized function
string _memo_LCS(string s1, string s2,
            unordered_map<string, unordered_map<string, string>> &memoizer) {
    // if we've already memoized the case, return it
    if (memoizer.find(s1) != memoizer.end() 
    and memoizer[s1].find(s2) != memoizer[s1].end()) {
        return memoizer[s1][s2];
    }

    // whatever we do, save our work to the memoizer
    if (s1 == "" or s2 == "") {
        memoizer[s1][s2] = "";
    } else if (s1[0] == s2[0]) {
        string eq_case = _memo_LCS(s1.substr(1), s2.substr(1), memoizer);
        memoizer[s1.substr(1)][s2.substr(1)] = eq_case;

        memoizer[s1][s2] = string(1, s1[0]) + eq_case;
    } else {
        string s1_subs2 = _memo_LCS(s1, s2.substr(1), memoizer);
        memoizer[s1][s2.substr(1)] = s1_subs2;

        string subs1_s2 = _memo_LCS(s1.substr(1), s2, memoizer);
        memoizer[s1.substr(1)][s2] = subs1_s2;

        memoizer[s1][s2] = max_len(s1_subs2, subs1_s2);
    }

    return memoizer[s1][s2];
}


// memoized wrapper
string memo_LCS(string s1, string s2) {
    unordered_map<string, unordered_map<string, string>> memoizer;
    return _memo_LCS(s1, s2, memoizer);
}


//////////////////////////////////////////////////////////////////////
//  Example 3: rod cutting
//////////////////////////////////////////////////////////////////////


// Case Analysis:
//     Base Case(s):
//         cut_rod(prices, 0) == 0
//     Recursive Case(s):
//         cut_rod(prices, n) == 
//                        max(prices[i] + cut_rod(prices, n - i - 1) for all i)
int cut_rod(const vector<int> &prices, int rod_size) {
    if (rod_size <= 0) {
        return 0;
    } else {
        // assume all prices are positive
        int best_price = -1;
        for (int i = 0; i < rod_size; ++i) {
            best_price = max(best_price,
                             prices[i] + cut_rod(prices, rod_size - i - 1));
        }
        return best_price;
    }
}


// helper for memoized function
int _memo_cut_rod(const vector<int> &prices, int rod_size,
                            unordered_map<int, int> &memoizer) {
    // if we've already memoized the case, return it
    if (memoizer.find(rod_size) != memoizer.end()) {
        return memoizer[rod_size];
    }
    
    // whatever we do, save our work to the memoizer
    if (rod_size <= 0) {
        memoizer[rod_size] = 0;
    } else {
        int best_price = -1;
        for (int i = 0; i < rod_size; ++i) {
            int ith_rod = _memo_cut_rod(prices, rod_size - i - 1, memoizer);
            memoizer[rod_size - i - 1] = ith_rod;
            best_price = max(best_price, prices[i] + ith_rod);
        }
        memoizer[rod_size] = best_price;
    }

    return memoizer[rod_size];
}


// memoized wrapper
int memo_cut_rod(const vector<int> &prices, int rod_size) {
    unordered_map<int, int> memoizer;
    return _memo_cut_rod(prices, rod_size, memoizer);
}
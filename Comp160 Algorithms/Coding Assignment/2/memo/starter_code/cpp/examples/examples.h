////////////////////////////////////////////////////////////////////////////
//
//    Tufts University, Comp 160 DP coding assignment  
//
//    examples.h
//    DP
//
//    includes example brute-force and memoized functions
//
////////////////////////////////////////////////////////////////////////////


#pragma once

#include <string>
#include <vector>


using namespace std;


int fib(int n);
int memo_fib(int n);


string LCS(string s1, string s2);
string memo_LCS(string s1, string s2);


int cut_rod(const vector<int> &prices, int rod_size);
int memo_cut_rod(const vector<int> &prices, int rod_size);
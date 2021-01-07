////////////////////////////////////////////////////////////////////////////
//
//    Tufts University, Comp 160 DP coding assignment  
//
//    memo.h
//    DP
//
//    includes function students need to implement
//
////////////////////////////////////////////////////////////////////////////

#include <unordered_map>
#include "memo.h"


using namespace std;


int rob(const vector<int> &houses, int i) {
    if (i < 0) {
        return 0;
    } else if (i == 0) {
        return houses[0];
    } else {
        return max(rob(houses, i - 1), houses[i] + rob(houses, i - 2));
    }
}


int memo_rob(const vector<int> &houses, int i) {
    (void)houses;
    (void)i;
    return 0;
}


bool SBS(const vector<int> &A, int target, int i) {
    if (target == 0) {
        return true;
    } else if (i < 0 and target != 0) {
        return false;
    } else if (A[i] > target) {
        return SBS(A, target, i - 1);
    } else {
        return SBS(A, target, i - 1) or SBS(A, target - A[i], i - 1);
    }
}


bool memo_SBS(const vector<int> &A, int target, int i) {
    (void)A;
    (void)target;
    (void)i;
    return false;
}
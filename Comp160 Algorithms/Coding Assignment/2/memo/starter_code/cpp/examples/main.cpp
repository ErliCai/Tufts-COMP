////////////////////////////////////////////////////////////////////////////
//
//    Tufts University, Comp 160 DP coding assignment  
//
//    main.cpp
//    DP
//
//    simple main to benchmark example functions
//
////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <chrono>
#include "examples.h"


using namespace std;


string to_string(const vector<int> &v);
void benchmark_fib();
void benchmark_LCS();
void benchmark_cut_rod();



int main(void) {
    string separator(80, '-');
    srand(time(NULL));
    cout << separator << endl;
    benchmark_fib();
    cout << separator << endl;
    benchmark_LCS();
    cout << separator << endl;
    benchmark_cut_rod();
    cout << separator << endl;
    return 0;
}


string to_string(const vector<int> &v) {
    string s = "[";
    for (unsigned i = 0; i < v.size() - 1; ++i) s += to_string(v[i]) + ", ";
    s += to_string(v[v.size() - 1]) + "]";
    return s;
}


void benchmark_fib() {
    string separator(80, '#');
    vector<int> tests{10, 20, 40, 45, 47};
    for (int& i : tests) {
        cout << separator << endl;
        auto t1 = chrono::high_resolution_clock::now();
        int f = fib(i);
        auto t2 = chrono::high_resolution_clock::now();
        float d = chrono::duration_cast<chrono::microseconds>(t2 - t1).count();
        float t = d / 1000000;
        cout << "Recursive fib(" << i << "): " << f
                << "; took " << t << " seconds\n";
        
        t1 = chrono::high_resolution_clock::now();
        f = memo_fib(i);
        t2 = chrono::high_resolution_clock::now();
        d = chrono::duration_cast<chrono::microseconds>(t2 - t1).count();
        t = d / 1000000;
        cout << "Memoized  fib(" << i << "): " << f
                << "; took " << t << " seconds\n";
    }
}


void benchmark_LCS() {
    string separator(80, '#');
    vector<int> strlens{1, 5, 10, 12, 15};

    for (int &l : strlens) {
        cout << separator << endl;
        string s1 = "", s2 = "";
        for (int i = 0; i < l; ++i) {
            s1.push_back('a' + (rand() % 26));
            s2.push_back('a' + (rand() % 26));
        }

        auto t1 = chrono::high_resolution_clock::now();
        string lcs = LCS(s1, s2);
        auto t2 = chrono::high_resolution_clock::now();
        float d = chrono::duration_cast<chrono::microseconds>(t2 - t1).count();
        float t = d / 1000000;
        cout << "Recursive LCS(\"" << s1 << "\", \"" << s2 << "\"): \"" << lcs
                                << "\"; took " << t << " seconds\n";
        
        t1 = chrono::high_resolution_clock::now();
        lcs = memo_LCS(s1, s2);
        t2 = chrono::high_resolution_clock::now();
        d = chrono::duration_cast<chrono::microseconds>(t2 - t1).count();
        t = d / 1000000;
        cout << "Memoized  LCS(\"" << s1 << "\", \"" << s2 << "\"): \"" << lcs
                                << "\"; took " << t << " seconds\n";
    }
}


void benchmark_cut_rod() {
    string separator(80, '#');
    vector<int> rod_sizes{10, 20, 25, 30, 32};
    for (int &r : rod_sizes) {
        cout << separator << endl;
        vector<int> prices;
        for (int i = 0; i < r; ++i) {
            prices.push_back(rand() % 50);
        }

        auto t1 = chrono::high_resolution_clock::now();
        int best_price = cut_rod(prices, r);
        auto t2 = chrono::high_resolution_clock::now();
        float d = chrono::duration_cast<chrono::microseconds>(t2 - t1).count();
        float t = d / 1000000;
        cout << "Recursive cut_rod(" << to_string(prices) << ", " 
             << r << "): " << best_price << "; took " << t << " seconds\n";
        
        t1 = chrono::high_resolution_clock::now();
        best_price = memo_cut_rod(prices, r);
        t2 = chrono::high_resolution_clock::now();
        d = chrono::duration_cast<chrono::microseconds>(t2 - t1).count();
        t = d / 1000000;
        cout << "Memoized  cut_rod(" << to_string(prices) << ", " 
             << r << "): " << best_price << "; took " << t << " seconds\n";
    }
}
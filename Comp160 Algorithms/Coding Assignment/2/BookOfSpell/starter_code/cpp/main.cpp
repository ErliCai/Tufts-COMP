////////////////////////////////////////////////////////////////////////////
//
//    Tufts University, Comp 160 interpretSpell coding assignment  
//
//    main.cpp
//    word interpret
//
//    simple main to test interpretSpell
//    NOTE: this main is only for you to test interpretSpell. We will compile
//          your code against a different main in our autograder directory
//
////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include "interpret.h"

using namespace std;


int main(void) {
    string inputSpell = "1234";
    if (interpretSpell(inputSpell) != 3) {
        cout << "Noo!\n";
    } else {
        cout << "Yay!\n";
    }
    return 0;
}

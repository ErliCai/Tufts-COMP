//
//  ArrayList.hpp
//  Comp15
//
//  Created by Erli Cai on 03/08/2020.
//  Copyright © 2020 Erli Cai. All rights reserved.
//

#include <stdio.h>
#include <iostream>


class ArrayList{
    
public:
    // big-3 and default constructor
    ArrayList();  // default constructor
    ArrayList& operator=(const ArrayList &other); // Assignment operator overload
    ~ArrayList(); //  deconstructor
    ArrayList(const ArrayList &other); // Copy Constructor
    
    void insert(int x);
    bool find(int x) const;
    void remove(int x);
    int elementAt(int x) const;
    int getSize() const;
    int getCapacity() const;
    std::string toString() const;
    
    
private:
    // resize is a private function we use to help us create an array on heap
    // with specified capacity (here we use half or two times of the original capacity,
    // depending on whether we need to shrink the array or enlarge the array).
    // And then copy the item from the original array to the new array.
    // finally let the pointer points to the new array.
    void resize(int new_capacity);
    int *array;
    int size, capacity;
};



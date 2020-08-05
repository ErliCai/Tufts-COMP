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
    
    // Insert an integer to the back of the list, and resize if necessary
    void insert(int x);
    
    // Return true if the given element is in the list - false otherwise
    bool find(int x) const;
    
    // Remove the first instance of x, if it exists in the list, and resize if necessary.
    void remove(int x);
    
    // Return the element at the specified location in the list.
    // If the given value is outside the range of the list, throw an std::out_of_range exception.
    int elementAt(int x) const;
    
    // Return the number of elements in the list.
    // Size should be initialized to 0.
    int getSize() const;
    
    // Return the current capacity of the list
    // Capacity should be initialized to 100.
    int getCapacity() const;
    
    // Return a string containing the list.
    // Elements should be separated by spaces.
    // No space or newline at the end of the string.
    std::string toString() const;
    
    
private:
    // resize is a private function we use to help us create an array on heap
    // with specified capacity (here we use half or two times of the original capacity,
    // depending on whether we need to shrink the array or enlarge the array).
    // And then copy the item from the original array to the new array.
    // finally let the pointer points to the new array.
    void resize(int new_capacity);
    
    // create an array pointer later used to point to the array that stores the data on the heap
    int *array;
    
    // private field size and capacibility
    // can not be accessed directly
    // in order to prevent accidental change.
    int size, capacity;
};



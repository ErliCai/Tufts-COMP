//
//  ArrayList.cpp
//  Comp15
//
//  Created by Erli Cai on 03/08/2020.
//  Copyright © 2020 Erli Cai. All rights reserved.
//

#include "ArrayList.hpp"
#include <iostream>
#include <sstream>

ArrayList::ArrayList(){
    this->array = new int[100];
    this->size = 0  ;
    this->capacity = 100;
}

// deconstructor, responsible to delete the array assigned on the heap
ArrayList::~ArrayList(){
    delete [] array;
}

ArrayList::ArrayList(const ArrayList &other){
    this->array = new int[other.size];
    for (int i = 0; i < other.size; i++){
        this->array[i] = other.array[i];
    }
    this->size = other.size;
    this->capacity = other.capacity;
}

ArrayList& ArrayList::operator=(const ArrayList &other){
    if (this != &other){
        delete [] this->array;
        this->array = new int[other.size];
        for (int i=0; i<other.size; i++){
            this->array[i] = other.array[i];
        }
        this->size = other.size;
        this->capacity = other.capacity;
    }
    return *this;
}

// resize the array if neccessary
void ArrayList::insert(int x){
    if (size > capacity * 3 / 4)
        resize(capacity*2);
    
    array[size] = x;
    size++;
}

// resize the array if neccessary
void ArrayList:: remove(int x){
    for(int i=0; i<size; i++ ){
        if (array[i] == x){
            for (int j=i; j<size-1;j++ ){
                array[j] = array[j+1];
            }
            if (size-- < capacity/4){
                resize(capacity/2);
            }
            return;
        }
    }
}

bool ArrayList::find(int x) const{
    for (int i=0; i<size; i++){
        if (array[i] == x)
            return true;
    }
    return false;
}

int ArrayList::elementAt(int x) const{
    return array[x];
}

int ArrayList::getSize() const{
    return size;
}

int ArrayList::getCapacity() const{
    return capacity;
}

std::string ArrayList::toString() const{
    if (size == 0){return "";}
    std::stringstream s;
    s << array[0];
    for (int i=1; i<size; i++){
        s << " " << array[i];
    }
    std::string str = s.str();
    return str;
}

void ArrayList::resize(int new_capacity){
    int *auxillary_Array = new int[new_capacity];
    for (int i=0; i<this->getSize(); i++){
        auxillary_Array[i] = elementAt(i);
    }
    delete [] array;
    this->array = auxillary_Array;
    capacity = new_capacity;
}

//std::string t01(){
//    ArrayList l;
//    for (int i=0;i<20;i++){
//        l.insert(i);
//    }
//    std::cout << l.getCapacity() << std::endl;
//    l.remove(4);
//    std::cout << l.getSize() << std::endl;
//    return l.toString();
//}

//int main(){
//    // std::cout << t01() << std::endl;
//    return 0;
//}

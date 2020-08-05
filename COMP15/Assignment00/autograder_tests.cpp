#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<stdexcept>
#include "ArrayList.hpp"
/*
 * using name assert for convenience - this is not the same as cassert's assert.
 * this function throws a logic error if the assertion is false.
 */

// Out of mysterious reason, this file does not work with my compiler(Xcode)
// So I create another file named "Tests.cpp" to test the functionality of ArrayList.cpp


void assert(bool test){
  if ( !test ) throw std::logic_error("assertion failed");
}

/*
 * Default constructor test
 */
void t00(){
    ArrayList l;
}

/*
 * First insert test.
 */
void t01(){
    ArrayList l;
    l.insert(1);
}

/*
 * Second insert test.
 */
void t02(){
  ArrayList l;

  for (int i = 0; i < 100; i++){
    l.insert(i);
  }
}

/*
 * First find test
 */
void t03(){
  ArrayList l;

  for (int i = 0; i < 100; i += 2){
    l.insert(i);
    assert(l.find(i));
  }

  for (int i = 0; i < 100; i += 2){
    assert(l.find(i));
  }

  for (int i = 1; i < 100; i += 2){
    assert(!l.find(i));
  }
}

/*
 * Copy Constructor 1
 */
void t04(){
  ArrayList l;

  for (int i = 0; i < 10; i++){
    l.insert(i);
  }

  ArrayList x(l);
}

/*
 * Copy Constructor 2
 */
void t05(){
  ArrayList l;

  for (int i = 100; i >= 0; i--){
    l.insert(i);
  }

  ArrayList x(l);

  for (int i = 100; i >= 0; i--){
    assert(x.find(i));
  }
}

/*
 * Copy Constructor 3
 */
void t06(){
  ArrayList *l = new ArrayList();

  for (int i = 50; i < 100; i += 2){
    l->insert(i);
  }

  ArrayList x(*l);
  delete l;

  for (int i = 50; i < 100; i += 2){
    assert(x.find(i));
  }
}

/*
 * Copy Constructor 4
 */
void t07(){
  ArrayList l;
  ArrayList x(l);

  for (int i = 50; i < 100; i += 2){
    l.insert(i);
  }

  for (int i = 50; i < 100; i += 2){
    assert(!x.find(i));
  }
}

/*
 * Assignment Operator Overload 1
 */
void t08(){
  ArrayList l;
  ArrayList x;

  for (int i = 50; i < 100; i += 2){
    l.insert(i);
  }

  x = l;
}

/*
 * Assignment Operator Overload 2
 */
void t09(){
  ArrayList l, x;

  for (int i = 50; i < 100; i += 2){
    l.insert(i);
  }

  x = l;

  for (int i = 50; i < 100; i += 2){
    assert(x.find(i));
  }
}

/*
 * Assignment Operator Overload 3
 */
void t10(){
  ArrayList *l = new ArrayList();
  ArrayList x;

  for (int i = 50; i < 100; i += 2){
    l->insert(i);
  }

  x = *l;
  delete l;

  for (int i = 50; i < 100; i += 2){
    assert(x.find(i));
  }
}

/*
 * Assignment Operator Overload 4
 */
void t11(){
  ArrayList l;
  ArrayList x = l;

  for (int i = 50; i < 100; i += 2){
    l.insert(i);
  }

  for (int i = 50; i < 100; i += 2){
    assert(!x.find(i));
  }
}

/*
 * toString 1
 */
void t12(){
  ArrayList l;

  for (int i = 20; i >= 0; i -= 3){
    l.insert(i);
  }

  assert(l.toString() == "20 17 14 11 8 5 2");

  ArrayList x(l);

  assert(x.toString() == "20 17 14 11 8 5 2");
}

/*
 * toString 2
 */
void t13(){
  ArrayList l;

  assert(l.toString() == "");
}

/*
 * Remove 1
 */
void t14(){
  ArrayList l;

  for (int i = 0; i < 100; i++){
    l.insert(i);
  }

  for (int i = 100; i >= 0; i--){
    l.remove(i);
    assert(!l.find(i));
  }
}

/*
 * Remove 2
 */
void t15(){
  ArrayList l;
  for (int i = 0; i < 100; i++){
    l.insert(i);
  }

  for (int i = 98; i >= 0; i -= 2){
    l.remove(i);
    assert(!l.find(i));
    assert(l.find(i + 1));
  }

  for (int i = 0; i < 1000; i += 50){
    l.insert(i);
  }

  for (int i = 0; i < 1000; i++){
    l.remove(i);
    assert(!l.find(i));
  }
}

/*
 * remove 3
 */
void t16(){
  ArrayList l;
  l.remove(5);
}

/*
 * elementAt 1
 */
void t17(){
  ArrayList l;
  l.insert(5);
  assert(l.elementAt(0) == 5);
}

/*
 * elementat 2
 */
void t18(){
  ArrayList l;
  for (int i = 20; i >= 0; i -= 3){
    l.insert(i);
  }
  assert(l.elementAt(6) == 2);
}

/*
 * getSize
 */
void t19(){
  ArrayList l;
  for (int i = 0; i < 255; i++){
    l.insert(i);
  }
  assert(l.getSize() == 255);
}

/*
 * getCapacity 1
 */
void t20(){
  ArrayList l;
  for (int i = 0; i < 55; i++){
    l.insert(i);
  }
  assert(l.getCapacity() == 96);
}

/*
 * getCapacity 2
 */
void t21(){
  ArrayList l;
  for (int i = 0; i < 100; i++){
    l.insert(i);
  }
  assert(l.getCapacity() == 192);
}


int main(int argc, char **argv){
  //run the tests here.
  return 0;
}

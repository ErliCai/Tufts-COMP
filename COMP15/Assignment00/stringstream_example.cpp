/*
  stringstream_example.cpp
	matt russell
	comp15 summer 2020

	This is a simple example demonstrating the use of stringstreams.
*/

#include<iostream>
#include<sstream> //make sure to include the header file!

int main(){
	std::stringstream s; //declare a stringstream object

	for (int i = 0; i < 10; i++){
		s << i << " ";     //use it just as you would cout!
	}
	s << std::endl;

	std::string str = s.str();  //convert the std::stringstream to a std::string
	std::cout << str;           //send the string to cout!

	return 0;
}

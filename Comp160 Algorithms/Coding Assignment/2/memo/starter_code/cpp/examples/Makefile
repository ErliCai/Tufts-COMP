#############################################################################
#
#    Makefile
#
#############################################################################


CXX      = g++
CXXFLAGS = -std=c++11 -g -O2 -Wall -Wextra

examples: main.o examples.o
	$(CXX) $(CXXFLAGS) -o examples main.o examples.o

main.o: main.cpp examples.h
	$(CXX) $(CXXFLAGS) -c main.cpp

examples.o: examples.cpp examples.h
	$(CXX) $(CXXFLAGS) -c examples.cpp

clean:
	rm -f examples *.o *~
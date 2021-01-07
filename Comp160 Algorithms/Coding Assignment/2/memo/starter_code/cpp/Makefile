#############################################################################
#
#    Makefile
#
#############################################################################


CXX      = g++
CXXFLAGS = -std=c++11 -g -O2 -Wall -Wextra

memo: main.o memo.o
	$(CXX) $(CXXFLAGS) -o memo main.o memo.o

main.o: main.cpp memo.h
	$(CXX) $(CXXFLAGS) -c main.cpp

memo.o: memo.cpp memo.h
	$(CXX) $(CXXFLAGS) -c memo.cpp

clean:
	rm -f memo *.o *~
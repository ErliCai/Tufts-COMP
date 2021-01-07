##########################################################################
#
#    main.py
#    randomized selection
#
#    simple main to test randSelect
#    NOTE: this main is only for you to test randSelect. We will compile
#          your code against a different main in our autograder directory
#
##########################################################################

from randSelect import randSelect


def main():
	v = [3, 4, 5, 1, 2]
	rankWeWant = 3
	ourNumber = randSelect(v, rankWeWant)
	expectedNumber = sorted(v)[rankWeWant]
	print("Nooo!") if ourNumber != expectedNumber else print("Yayy!")


if __name__ == '__main__':
	main()
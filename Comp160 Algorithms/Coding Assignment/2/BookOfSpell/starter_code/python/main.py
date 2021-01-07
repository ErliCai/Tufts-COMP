##########################################################################
#
#    Tufts University, Comp 160 interpretSpell coding assignment
#
#    main.py
#    interpretSpell
#
#    simple main to test interpretSpell
#    NOTE: this main is only for you to test interpretSpell. We will compile
#          your code against a different main in our autograder directory
#
##########################################################################

from interpret import interpretSpell


def main():
	#inputSpell = '91584983398781138415'
	inputSpell='15275217996613369643172721682123315785815698496179798976913285366972876142616479915849833987811384156577122962271972971658196761372364219795357639692377138168857139699936929646259446571924941454262699'
	inputSpell = '53108684246528581296'
	print(interpretSpell(inputSpell))


if __name__ == '__main__':
	main()
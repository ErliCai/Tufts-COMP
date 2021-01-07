##########################################################################
#
#    Tufts University, Comp 160 interpretSpell coding assignment
#
#    interpret.py
#    interpretSpell
#
#    includes function students need to implement
#
##########################################################################


# TODO: implement this function
# NOTE: please implement this with  Python3. The autograder uses Python3

# inputSpell is a string
# function returns an int
def interpretSpell(inputSpell):

    memo = dict()
    memo[-1] = 1
    memo[0] = 1
    if inputSpell[0] == '0':
        return 0
    for i in range(1, len(inputSpell)):
        if inputSpell[i] == '0' and int(inputSpell[i-1:i+1]) > 20:
            return 0
        elif inputSpell[i] == '0' and int(inputSpell[i-1:i+1]) <= 20:
            memo[i] = memo[i - 2]
        else:
            memo[i] = memo[i-1]
            if 10 < int(inputSpell[i-1] + inputSpell[i]) <= 26:
                memo[i] += memo[i-2]
        print(i,memo[i])
    return memo[len(inputSpell)-1]



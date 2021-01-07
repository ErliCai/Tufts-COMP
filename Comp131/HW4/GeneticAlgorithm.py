import random

boxes = [[20, 6], [30, 5], [60, 8],
         [90, 7], [50, 6], [70, 9], [30, 4],
         [30, 5], [70, 4], [20, 9], [20, 2], [60, 1]]


# genome of the problem is a list of 12 binary numbers
# with 1 in k-th place indicating that k-th box is selected and
# 0 means k-th box is not selected

# In our implementation, we cull 50% of the population each generation
# And each survived produce 2 offsprings
# we use a single-point mutation to produce offspring
# Fitness function is just the sum of importance
# Also, I restricted the offspring to have weight under 250, try again if exceeded.

def GetWeightAndImportance(G):
    total_weight = 0
    total_importance = 0
    for i in range(len(G)):
        if G[i] == 1:
            total_weight += boxes[i][0]
            total_importance += boxes[i][1]

    return total_weight, total_importance


def GetInitialPopulation():
    # genome of the problem is a list of 12 binary numbers
    # with 1 in k-th place indicating that k-th box is selected and
    # 0 means k-th box is not selected

    population = []
    # Initial population of size 20
    for i in range(20):
        genome = [0]*12
        g1 = random.randint(0, 11)
        g2 = random.randint(0, 11)

        genome[g1] = 1 - genome[g1]
        genome[g2] = 1 - genome[g2]

        weight, importance = GetWeightAndImportance(genome)

        population.append([genome, weight, importance])
    return population


def Offspring(P):
    genome = P[0].copy()
    i = random.randint(0, 11)
    genome[i] = 1- genome[i]
    weight, importance = GetWeightAndImportance(genome)
    while weight > 250:
        genome = P[0].copy()
        i = random.randint(0, 11)
        genome[i] = 1 - genome[i]
        weight, importance = GetWeightAndImportance(genome)
    return genome, weight, importance


def FitnessFunction(P):
    return P[2]


def Culling(Population):
    P = sorted(Population, key=FitnessFunction)
    P = P[10:]
    return P


def GenerationReplacement(population):
    population = Culling(population)
    newPopulation = []
    for i in population:
        newPopulation.append(Offspring(i))
        newPopulation.append(Offspring(i))
    return newPopulation


def GeneticAlgorithm():
    p = GetInitialPopulation()
    p = sorted(p, key=FitnessFunction)
    best_fit = p[-1]
    for i in range(100):
        p = GenerationReplacement(p)
        p = sorted(p, key=FitnessFunction)
        if p[-1][2] > best_fit[2]:
            best_fit = p[-1]
    return p, best_fit


if __name__ == '__main__':
    Answer = GeneticAlgorithm()[1]
    print("The optimal way to fill in the bag is:")
    print(Answer[0])
    print("Its weight is ", Answer[1], " and its importance is ", Answer[2])
    # Output on my computer is shown below
    # The optimal way to fill in the bag is:
    # [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0]
    # Its weight is  250  and its importance is  44




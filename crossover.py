import random
from fuzzyRule import fuzzy


def crossover(p1, p2):
    child = fuzzy()

    return child


def uniform_crossover(p1: fuzzy, p2: fuzzy):
    child1 = p1.rule
    child2 = p2.rule
    for i in range(len(child1)):
        if random.random() > 0.5:
            child1[i], child2[i] = child2[i], child1[i]

    if random.random() > 0.5:
        child = child1
    else:
        child = child2

    return fuzzy(child)


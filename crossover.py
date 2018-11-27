import random, exer4
from fuzzyRule import fuzzy_rule


def rule_set_crossover(p1, p2):
    child = []

    N1 = random.randint(1, len(p1))
    N2 = random.randint(1, len(p2))

    from_1 = random.sample(range(0, len(p1)), N1)
    from_2 = random.sample(range(0, len(p2)), N2)

    for i in from_1:
        child.append(p1[i])
    for j in from_2:
        child.append(p2[j])

    while len(child) > 15:
        child.remove(child[random.randint(0, len(child) - 1)])

    return child


def uniform_crossover(p1: list, p2: list):
    child1 = p1
    child2 = p2
    for i in range(len(child1) - 1):
        if random.random() > 0.5:
            child1[i], child2[i] = child2[i], child1[i]

    child = [child1, child2][random.random() < 0.5]
    return child

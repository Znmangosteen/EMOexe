import random
from fuzzyRule import fuzzy_rule


def rule_set_crossover(p1, p2):
    child = fuzzy_rule()

    return child


def uniform_crossover(p1: fuzzy_rule, p2: fuzzy_rule):
    child1 = p1.rule
    child2 = p2.rule
    for i in range(len(child1) - 1):
        if random.random() > 0.5:
            child1[i], child2[i] = child2[i], child1[i]

    child = [child1, child2][random.random() < 0.5]
    return fuzzy_rule(child)

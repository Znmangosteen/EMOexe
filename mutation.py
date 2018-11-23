from fuzzyRule import fuzzy
import random


def rule_mutation(c: fuzzy):
    rule = c.rule
    k = random.randint(0, len(rule) - 1)
    # 把k位置的membership function变异
    return fuzzy(rule)

def rule_set_mutation(c: fuzzy):
    pass

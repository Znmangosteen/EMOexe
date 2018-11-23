from fuzzyRule import fuzzy_rule
import random


def rule_mutation(c: fuzzy_rule):
    rule = c.rule
    k = random.randint(0, len(rule) - 3)
    # 把k位置的membership function变异
    return fuzzy_rule(rule)

def rule_set_mutation(c: fuzzy_rule):
    pass

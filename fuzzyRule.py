class rule_set:
    def __init__(self):
        pass

class fuzzy_rule:

    # fuzzy rule包括规则的主体(list)和适应度
    def __init__(self, rule: list):
        self.rule = rule
        # 适应度根据rule算出
        self.fitness = self.get_fitness(rule)

    def get_fitness(self, rule):
        return 0

    def __lt__(self, other):
        if self.fitness > other.fitness:
            return 1
        else:
            return -1

import mbFunc as mb
import math
import util
N = 6 # number of membership functions
class rule_set:
    def __init__(self):
        pass

class fuzzy_rule:
    rule = []
    # fuzzy rule包括规则的主体(list)和适应度
    def __init__(self):
        pass

    def get_fitness(self, rule):
        return 0

    def __lt__(self, other):
        if self.fitness > other.fitness:
            return 1
        else:
            return -1
    def genRule(self, pattern):
        rule = []
        print(pattern[:-1])

        for x in pattern[:-1]:
            maxV = -float("inf")
            index = -1
            print(x)
            print(rule)
            for n in range(2,N+1):

                score = mb.u(n,x)
                print("u",n,":",score)
                if(score > maxV):
                    maxV = score
                    index = n
            rule.append(index)
        print(rule)
        return rule


data = util.readData("./data/iris.dat")
vector=data[0]
rule = fuzzy_rule()
rule.genRule(vector)

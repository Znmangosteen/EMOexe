import mbFunc as mb
import random
import util
import copy
N = 15 # number of membership functions
class rule_set:
    pareto = 0
    rules = []
    fitness = 0

    def __lt__(self, other):
        if self.pareto > other.pareto:
            return 1
        else:
            return -1
    def __init__(self, trainingData):
        pop = []
        for p in trainingData:
            rule = fuzzy_rule(p, trainingData)
            if(rule.CFq > 0):
                pop.append(rule)
        self.rules = pop

    def classify(self,xp):

        #print("pattern:",xp)
        scores = []
        for i in range(0,len(self.rules)):
            rule = self.rules[i]
            score = (fuzzy_rule.getCompGrade(rule.rule, xp))*rule.CFq
            scores.append([rule.Cq,score,i])
        scores.sort(key = lambda x:x[1],reverse = True)
        #print(scores[0])
        #print("-----------")
        return scores[0][0],scores[0][2]

        pass
    def getFitness(self,testData):
        fitness = 0
        hit = [0]*len(self.rules)
        for data in testData:
            result, index = self.classify(data)
            if(result == data[-1]):
                fitness += 1
                hit[index]+=1
        self.fitness = fitness
        # print(hit)
        for i in range(len(self.rules)):
            self.rules[i].fitness = hit[i]
        return self.fitness/len(testData)



class fuzzy_rule:
    pDC = 0.1#probablity of don't care
    rule = []
    Cq = 0
    CFq = 0
    fitness = 0
    # fuzzy rule包括规则的主体(list)和适应度
    def __init__(self, pattern, trainingData):
        if type(pattern)==fuzzy_rule:
            self.rule = copy.deepcopy(pattern.rule)
        else:
            self.rule = self.genRule(pattern)
        self.Cq, self.CFq = self.getCqCFq(self.rule, trainingData)

    def get_fitness(self, rule):
        return 0

    def __lt__(self, other):
        if self.fitness > other.fitness:
            return 1
        else:
            return -1

    def genRule(self, pattern):
        rule = []
        for x in pattern[:-1]:
            maxV = -float("inf")
            index = -1
            if(random.random()>self.pDC):
                for n in range(2,N+1):

                    score = mb.u(n,x)
                    if(score > maxV):
                        maxV = score
                        index = n
            else:
                index = 1
            rule.append(index)
        return rule

    def getCqCFq(self,p,trainingData):
        total = 0
        c = [0] * (N + 1)
        for pattern in trainingData:
            # print("pattern:",pattern)
            score = fuzzy_rule.getCompGrade(p[:-1],pattern)
            c[pattern[-1]] += score
            total += score
        for i in range(len(c)):
            c[i] /= total
        # print("_____", p, ":", c)
        cqh = max(c)
        result = c.index(cqh)
        CFq = cqh
        for x in c:
            if (x != cqh):
                CFq -= x
        return result, CFq

    def getCompGrade(r,pattern):
        score = 1
        for i in range(len(r)):
            score *= mb.u(r[i], pattern[i])
        return score

    def fitRule(self,rule,dataSet):
        pass

    def prints(self,list):
        for i in list:
            print(i)





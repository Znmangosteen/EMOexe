import mbFunc as mb
import random
import util
N = 6 # number of membership functions
class rule_set:
    def __init__(self):
        pass

class fuzzy_rule:
    pDC = 0.1#probablity of don't care
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
    def initPopulation(self,trainingPatterns,N):
        self.print#s(trainingData)
        pop = []
        for p in trainingData:
            rule = self.genRule(p)
            pop.append(rule)

        for p in pop:
            total = 0
            c = [0]*(N+1)
            for pattern in trainingData:
                #print("pattern:",pattern)
                score = 1
                for i in range(len(p)):
                    score *= mb.u(p[i],pattern[i])
                c[pattern[-1]]+=score
                total += score
            for i in range(len(c)):
                c[i] /= total
            #print("_____", p, ":", c)
            cqh = max(c)
            result = c.index(cqh)
            CFq = cqh
            for x in c:
                if(x !=cqh ):
                    CFq -= x

            p.append([result,CFq])
            print(p)

        #self.prints(pop)
    def prints(self,list):
        for i in list:
            print(i)

data,NClass,dictL2I,dictI2L = util.readData("./data/iris.dat")
pData = 0.2 # proportion of training data
trainingData = []
testData = []
for d in data:
    if(random.random() < pData):
        trainingData.append(d)
    else:
        testData.append(d)

#print("train: ",len(trainingData))
#print("test: ",len(testData))
vector=data[0]
rule = fuzzy_rule()
rule.initPopulation(trainingData,NClass)

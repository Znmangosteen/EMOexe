import fuzzyRule as fr
import random
import util
import matplotlib.pyplot as mb
import copy

data,NClass,dictL2I,dictI2L = util.readData("./data/a1_va3.csv")
pData =0.1# proportion of training data
xs = []
ys = []
f1 = fr.fuzzy_rule(data[0],data)
print(f1.rule)
f2=copy.deepcopy(f1)
f1.rule = [1,2,3,4,5,6]
print(f1.rule)
print(f2.rule)
f2 = fr.fuzzy_rule(f1,data)
f1.rule=  [3,2,3]
print(f1.rule)
print(f2.rule)

# for i in range(0, 101, 5):
    # pData = i/100
#     nRight = 0
#     accuracy = 0
#     N = max(int(pData * len(data)),2)
#     trainingData = []
#     testData = []
#     random.shuffle(data)
#     trainingData = data[:N]
#     testData = data
#     RS = fuzzyRule.rule_set(trainingData)
#     y = RS.getFitness(data)
#     print("train:",N/len(data), "fitness:", y)
#     xs.append(N/len(data))
#     ys.append(y)
# mb.plot(xs,ys)
# mb.xlabel("training%")
# mb.ylabel("accuracy")

# mb.xlim(0,1)
# mb.ylim(0,1)
# ax = mb.gca()
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data',0)) # set position of x spine to x=0
# mb.grid()
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data',0))   # set position of y spine to y=0
# mb.show()
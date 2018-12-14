import init, algorithm, util, random, time
import fuzzyRule

data, NClass, dictL2I, dictI2L = util.readData("./data/a1_va3.csv")
# data, NClass, dictL2I, dictI2L = util.readData("./data/iris.dat")
pData = 0.3  # proportion of training data
N = int(pData * len(data))
random.shuffle(data)
trainingData = data[:N]
testData = data

if __name__ == '__main__':
    # 初期个体数
    size = 50
    gen_num = 20
    # size = 20
    # gen_num = 1
    accuracy = 0

    population = []
    while len(population) < size:
        # use_data = random.randint(1, 15)
        use_data = 200
        init_trainingData_idx = random.sample(range(0, len(trainingData)), use_data)
        init_trainingData = []

        for idx in init_trainingData_idx:
            init_trainingData.append(trainingData[idx])
        RS = fuzzyRule.rule_set(init_trainingData)
        if len(RS.rules) > 0:
            RS.getFitness(trainingData)
            population.append(RS)

    for RS in population:
        print(str(RS.fitness) + '  ' + str(40 - RS.fitness2))

    while True:

        # p = [0.9, 0.25, 0.5, 0.9, 0.25]
        p = [0.9, 0.25, 0.5, 0.9, 0.25]
        constant = [1]

        time_start = time.time()
        print("start")
        pareto_set, population = algorithm.NSGAII(population=population, p=p, gen_num=gen_num, constant=constant,
                                                  size=size)

        time_end = time.time()
        time_cost = time_end - time_start

        print("time cost: " + str(time_cost))
        print("time each gen: " + str(time_cost / gen_num))
        print()
        print('Result')
        shown = set()
        for RS in pareto_set:
            if RS.fitness2 in shown:
                pass
            else:
                shown.add(RS.fitness2)
                print("Before refit: " + str(RS.fitness) + '  ' + str(40 - RS.fitness2) + '  ' + str(RS.correct_num))
                RS.getFitness(testData)
                print("After refit: " + str(RS.fitness) + '  ' + str(40 - RS.fitness2) + '  ' + str(RS.correct_num))

        if input() == "no":
            break

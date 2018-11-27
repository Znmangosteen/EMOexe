import init, algorithm, util, random, time
import fuzzyRule

data, NClass, dictL2I, dictI2L = util.readData("./data/a1_va3.csv")
pData = 0.2  # proportion of training data
N = int(pData * len(data))
random.shuffle(data)
trainingData = data[:N]
testData = data

if __name__ == '__main__':
    # 初期个体数
    size = 50
    gen_num = 200
    accuracy = 0

    population = []
    for i in range(size):
        use_data = random.randint(1, 15)
        init_trainingData_idx = random.sample(range(0, len(trainingData)), use_data)
        init_trainingData = []

        for idx in init_trainingData_idx:
            init_trainingData.append(trainingData[idx])
        RS = fuzzyRule.rule_set(init_trainingData)
        RS.getFitness(trainingData)
        population.append(RS)

    for RS in population:
        print(str(RS.fitness) + '  ' + str(40 - RS.fitness2))

    p = [0.9, 0.25, 0.5, 0.9, 0.25]
    constant = [1]

    time_start = time.time()

    pareto_set = algorithm.NSGAII(population, p, gen_num, constant, size)

    time_end = time.time()
    time_cost = time_end - time_start

    print("time cost: " + str(time_cost))
    print("time each gen: " + str(time_cost / gen_num))
    print()
    print('Result')
    for RS in pareto_set:
        print("Before refit: " + str(RS.fitness) + '  ' + str(40 - RS.fitness2) + '  ' + str(RS.correct_num))
        RS.getFitness(testData)
        print("After refit: " + str(RS.fitness) + '  ' + str(40 - RS.fitness2) + '  ' + str(RS.correct_num))

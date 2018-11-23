import crossover, mutation, selection, random, init


def NSGAII(population, p, gen_num, constant, size=100) -> list:
    pc = p[0]
    pm = p[1]
    pMchi = p[2]
    N = constant[0]

    # 进化gen_num代
    for j in range(gen_num):
        offspring_population = []
        pareto_ranking(population)

        # 生成子代个体并放到offspring_population
        for i in range(size):
            p1, p2 = selection.binary_tournament_selection(population)

            if random.random() < pc:
                # crossover for rule set
                child = crossover.rule_set_crossover(p1, p2)
                pass
            else:
                child = [p1, p2][random.random() < 0.5]

            if random.random() < pm:
                child = mutation.rule_set_mutation(child)

            if random.random() < pMchi:
                child = michigan(child, N, p[3:5])

            offspring_population.append(child)

        # 合并父子代并选择
        population = merge_and_select(population, offspring_population, size)
    pareto_ranking(population)
    pareto_set = []
    for solution in population:
        if solution.pareto == 1:
            pareto_set.append(solution)
    return pareto_set


def merge_and_select(population: list, offspring_population: list, size):
    total_population = population + offspring_population

    pareto_ranking(total_population)
    total_population.sort()

    return total_population[:size]


def pareto_ranking(population: list):
    size = len(population)
    n = [0] * size
    S = [set()] * size
    for i in range(size - 1):
        for j in range(i + 1, size):
            s1 = population[i]
            s2 = population[j]

            if (s1.fit1 >= s2.fit1 and s1.fit2 >= s2.fit2) and (s1.fit1 > s2.fit1 or s1.fit1 > s2.fit1):
                n[i] += 1
                S[i].add(j)
            elif (s1.fit1 <= s2.fit1 and s1.fit2 <= s2.fit2) and (s1.fit1 < s2.fit1 or s1.fit1 < s2.fit1):
                n[j] += 1
                S[j].add(i)

    F = set()
    for i in range(size):
        if n[i] == 0:
            F.add(i)

    H = set()
    pareto_num = 1
    while len(F) > 0:
        for k in F:
            population[k].pareto = pareto_num

            for i in S[k]:
                n[i] -= 1
                if n[i] == 0:
                    pass
                    H.add(i)
        F = H
        H.clear()
        pareto_num += 1


def michigan(population: list, N, p):
    pc = p[0]
    pm = p[1]

    # sort population
    population.sort()

    child_set = []

    for i in range(N):
        p1, p2 = selection.binary_tournament_selection(population)

        if random.random() < pc:
            # crossover for rule
            child = crossover.uniform_crossover(p1, p2)
        else:
            child = [p1, p2][random.random() < 0.5]

        if random.random() < pm:
            child = mutation.rule_mutation(child)

        child_set.append(child_set)

    population[:N] = child_set

    return population

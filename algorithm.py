import crossover, mutation, selection, random, init


def NSGAII(p, gen_num, constant, size=100) -> list:
    pc = p[0]
    pm = p[1]
    pMchi = p[2]
    N = constant[0]
    population = init.initialization(size)

    # 进化gen_num代
    for j in range(gen_num):
        offspring_population = []

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


def merge_and_select(population, offspring_population, size):
    total_popution = population + offspring_population



    return total_popution[:size]


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

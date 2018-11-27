import random
from fuzzyRule import fuzzy_rule


def binary_tournament_selection(front: list):
    results = []

    if front is None:
        raise Exception('The front is null')
    elif len(front) == 0:
        raise Exception('The front is empty')

    if len(front) == 1:
        results = [front[0], front[0]]
    else:
        for a in range(2):
            # Sampling without replacement
            i, j = random.sample(range(0, len(front)), 2)
            solution1 = front[i]
            solution2 = front[j]

            flag = solution1 < solution2

            if flag == -1:
                result = solution1
            elif flag == 1:
                result = solution2
            else:
                result = [solution1, solution2][random.random() < 0.5]
            results.append(result)
    return results

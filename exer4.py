import init, algorithm

if __name__ == '__main__':
    # 初期个体数
    size = 100
    # 种群
    # population = []
    # 生成并评价所有规则
    population = init.initialization(size)


    while True:
        # 遗传变异
        # Pittsburge
        child = []
        child = algorithm.michigan(child)
        # 替换操作
        # 判断终止条件
        # 从所有世代中选择识别精度最高的种群作为最终识别器，删除无用规则

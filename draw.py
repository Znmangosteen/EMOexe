import numpy as np
import matplotlib.pyplot as plt

N = 1000
x = [1,2,3,4,5]
# y=[0.635,0.34,0.17,0.08,0.07]
y=[0.6645,0.34,0.19,0.07,0.07]
# y = [0.67,0.34,0.12,0.11,0.09]
# x = [1, 3, 4, 5, 6, 7, 8]
# y = [0.57, 0.313, 0.2988, 0.296, 0.2932, 0.2902, 0.2845]
# x = [1, 3, 4, 5, 6, 7, 8]
# y = [0.57, 0.3468, 0.333, 0.3313,0.3399, 0.3405, 0.3404]
plt.scatter(x, y, alpha=1, edgecolors='black', c='k')  # edgecolors = 'w',亦可
# plt.title('Result on iris data set')#显示图表标题
plt.xlabel('Number of rules')  # x轴名称
# plt.ylabel('error rate on training patterns')  # y轴名称
plt.ylabel('error rate on test patterns')  # y轴名称
plt.show()

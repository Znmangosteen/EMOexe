import matplotlib.pyplot as plt

name_list = ['200', '400', '600']
num_list = [1.5, 0.6, 7.8]
num_list1 = [1, 2, 3]
x = list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n

plt.bar(x, num_list, width=width, label='non parallel', fc='blue')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list1, width=width, label='parallel', tick_label=name_list, fc='green')
plt.legend()

plt.xlabel('number of generations')  # x轴名称
plt.ylabel('time(s)')  # y轴名称

plt.show()

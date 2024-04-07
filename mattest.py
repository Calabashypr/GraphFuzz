import matplotlib.pyplot as plt
import numpy as np

# 数据
frameworks = ['PyTorch', 'TensorFlow', 'MindSpore']
values1 = [35873, 38580, 22137]  # 第一个柱子的值
values2 = [15320, 13955, 6281]   # 第二个柱子的值
values3 = [1842, 1921, 3811]     # 第三个柱子的值

bar_width = 0.2  # 柱子宽度
spacing = 0.05  # 间距

plt.figure(dpi=400,figsize=(18,15))
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

r1 = np.arange(len(frameworks))
r2 = [x + bar_width + spacing for x in r1]
r3 = [x + 2 * (bar_width + spacing) for x in r1]

plt.bar(r1, values1, color='#9BC985', width=bar_width, label='Issue Counts')
plt.bar(r2, values2, color='#F7D58B', width=bar_width, label='Defect Counts')
plt.bar(r3, values3, color='#B595BF', width=bar_width, label='HP Defect Counts')

for i in range(len(r1)):
    plt.text(r1[i], values1[i], str(values1[i]), ha='center', va='bottom',fontdict={'size':25})
    plt.text(r2[i], values2[i], str(values2[i]), ha='center', va='bottom',fontdict={'size':25})
    plt.text(r3[i], values3[i], str(values3[i]), ha='center', va='bottom',fontdict={'size':25})

plt.xticks([r + bar_width + spacing for r in range(len(frameworks))], frameworks, fontsize=30)
plt.tick_params(axis='y', labelsize=30)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=3,frameon=False,fontsize=25)
plt.savefig('my_plot.pdf', format='pdf')
# plt.show()
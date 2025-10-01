import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False  # 正确显示负号

# 数据规模
sizes = [1000, 5000, 10000, 50000, 100000]

# 各种排序算法的运行时间（秒）
times = {
    "快速排序": [0.0000, 0.0049, 0.0099, 0.0578, 0.1285],
    "归并排序": [0.0009, 0.0059, 0.0119, 0.0717, 0.1664],
    "希尔排序": [0.0010, 0.0069, 0.0149, 0.1086, 0.2752],
    "插入排序": [0.0109, 0.2780, 1.1043, 29.2342, 119.6586],
    "冒泡排序": [0.0239, 0.6180, 2.4993, 64.1793, 278.8231],
    "基数排序": [0.0010, 0.0029, 0.0069, 0.0458, 0.1016],
    "选择排序": [0.0099, 0.2481, 0.9707, 26.0600, 157.5239]
}

# 创建画布
plt.figure(figsize=(12, 8))

# 定义不同的标记和线条样式
markers = ['o', 's', '^', 'D', 'p', 'h', 'd']
linestyles = ['-', '--', '-.', ':', '-', '-.', '--']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# 绘制每条曲线
for i, (algorithm, time_data) in enumerate(times.items()):
    plt.plot(sizes, time_data,
             label=algorithm,
             marker=markers[i % len(markers)],
             linestyle=linestyles[i % len(linestyles)],
             color=colors[i % len(colors)],
             linewidth=2,
             markersize=8)

# 设置图表标题和坐标轴标签
plt.title('排序算法时间效率对比（线性坐标）', fontsize=16, pad=20)
plt.xlabel('数据规模（元素个数）', fontsize=14)
plt.ylabel('运行时间（秒）', fontsize=14)

# 添加网格和图例
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12, loc='upper left')




# 显示图像
plt.show()

# 可选：保存图像
plt.savefig('排序算法线性坐标对比.png')

import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False  # 正确显示负号

# 数据规模
sizes = [10, 100, 1000, 10000, 100000]

# 各种排序算法的运行时间（秒）
times = {
    "快速排序": [0.0000, 0.0000, 0.0000, 0.0100, 0.1325],
    "归并排序": [0.0000, 0.0000, 0.0011, 0.0129, 0.1582],
    "插入排序": [0.0000, 0.0000, 0.0110, 1.1115, 121.0710],
    "冒泡排序": [0.0000, 0.0000, 0.0239, 2.5026, 280.3791],
    "选择排序": [0.0000, 0.0000, 0.0110, 0.9735, 151.2436]
}

# 创建画布
plt.figure(figsize=(12, 8))

# 定义不同的标记和线条样式
markers = ['o', 's', '^', 'D', 'p']
linestyles = ['-', '--', '-.', ':', '-']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

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

import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False  # 正确显示负号

# 数据规模
sizes = [1000, 5000, 10000, 50000, 100000]

# 各种排序算法的运行时间（秒），包含插入排序和冒泡排序的完整数据
# 注：实际数据可能因硬件不同而有差异，这里是模拟的合理值
times = {
    "快速排序": [0.0012, 0.0068, 0.0145, 0.0823, 0.1765],
    "归并排序": [0.0018, 0.0095, 0.0203, 0.1157, 0.2432],
    "希尔排序": [0.0053, 0.0327, 0.0702, 0.4185, 0.9217],
    "插入排序": [0.0421, 0.9876, 3.8762, 96.8215, 387.5421],  # 完整保留所有数据
    "冒泡排序": [0.0876, 2.1032, 8.4521, 211.3054, 845.1236]   # 完整保留所有数据
}

# 创建画布
plt.figure(figsize=(12, 7))

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
plt.title('排序算法时间效率对比（包含所有算法完整数据）', fontsize=15, pad=20)
plt.xlabel('数据规模（元素个数）', fontsize=12)
plt.ylabel('运行时间（秒）', fontsize=12)

# 添加网格和图例
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10, loc='upper left')

# 为了更清晰展示差异，使用对数坐标（因为时间差异太大）
plt.yscale('log')
plt.text(50000, 10, '使用对数坐标便于观察差异', fontsize=9,
         bbox=dict(facecolor='white', alpha=0.8))

# 调整布局
plt.tight_layout()

# 显示图像
plt.show()

# 可选：保存图像
# plt.savefig('完整排序算法效率对比.png', dpi=300, bbox_inches='tight')

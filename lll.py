import random
import time


# 生成指定规模的不重复随机数数组
def generate_unique_randoms(size):
    max_val = size * 10  # 确保取值范围足够大，避免重复
    return random.sample(range(max_val), size)


# 1. 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# 2. 冒泡排序
def bubble_sort(arr):
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy


# 3. 插入排序
def insertion_sort(arr):
    arr_copy = arr.copy()
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy


# 4. 选择排序
def selection_sort(arr):
    arr_copy = arr.copy()
    for i in range(len(arr_copy)):
        min_idx = i
        for j in range(i + 1, len(arr_copy)):
            if arr_copy[min_idx] > arr_copy[j]:
                min_idx = j
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
    return arr_copy


# # 5. 希尔排序
# def shell_sort(arr):
#     arr_copy = arr.copy()
#     n = len(arr_copy)
#     gap = n // 2
#
#     while gap > 0:
#         for i in range(gap, n):
#             temp = arr_copy[i]
#             j = i
#             while j >= gap and arr_copy[j - gap] > temp:
#                 arr_copy[j] = arr_copy[j - gap]
#                 j -= gap
#             arr_copy[j] = temp
#         gap //= 2
#     return arr_copy


# 6. 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 7. 基数排序
# def radix_sort(arr):
#     arr_copy = arr.copy()
#     if not arr_copy:
#         return arr_copy
#
#     # 找到最大数，确定最大位数
#     max_num = max(arr_copy)
#     max_digits = len(str(max_num))
#
#     # 进行基数排序
#     for digit in range(max_digits):
#         # 创建10个桶
#         buckets = [[] for _ in range(10)]
#
#         # 将数字分配到对应的桶中
#         for num in arr_copy:
#             # 计算当前位的值
#             current_digit = (num // (10 ** digit)) % 10
#             buckets[current_digit].append(num)
#
#         # 从桶中收集数字
#         arr_copy = [num for bucket in buckets for num in bucket]
#
#     return arr_copy


# 排序算法计时函数
def time_sorting_algorithm(sort_func, arr, size):
    # 复制数组以避免修改原始数据
    arr_copy = arr.copy()

    # 记录开始时间
    start_time = time.time()

    # 执行排序
    sorted_arr = sort_func(arr_copy)

    # 记录结束时间
    end_time = time.time()

    # 计算运行时间（秒）
    elapsed_time = end_time - start_time

    # 验证排序结果
    is_sorted = all(sorted_arr[i] <= sorted_arr[i + 1] for i in range(len(sorted_arr) - 1))

    return elapsed_time, is_sorted


# 生成5个不同规模的不重复随机数数组
sizes = [10, 100, 1000, 10000, 100000]
arrays = {
    10: generate_unique_randoms(10),
    100: generate_unique_randoms(100),
    1000: generate_unique_randoms(1000),
    10000: generate_unique_randoms(10000),
    100000: generate_unique_randoms(100000)
}

# 定义要测试的排序算法
sorting_algorithms = {
    "快速排序": quick_sort,
    "冒泡排序": bubble_sort,
    "插入排序": insertion_sort,
    "选择排序": selection_sort,
    #"希尔排序": shell_sort,
    "归并排序": merge_sort,
    #"基数排序": radix_sort
}

# 存储所有测试结果
results = {}

# 执行排序测试
print("排序算法性能测试开始...\n")
for name, func in sorting_algorithms.items():
    results[name] = {}
    print(f"测试{name}...")
    for size in sizes:
        # 对于大规模数据，跳过O(n²)算法以节省时间
        if size > 100000000 and name in ["冒泡排序", "插入排序", "选择排序"]:
            print(f"  规模 {size}: 跳过（数据量过大，耗时太长）")
            results[name][size] = ("跳过", True)
            continue

        arr = arrays[size]
        elapsed_time, is_sorted = time_sorting_algorithm(func, arr, size)
        results[name][size] = (elapsed_time, is_sorted)
        print(f"  规模 {size}: 运行时间 = {elapsed_time:.6f} 秒, 排序正确: {is_sorted}")
    print()

# 打印总结表格
print("=" * 80)
print(
    f"{'排序算法':<10} | {'10元素':<12} | {'100元素':<12} | {'1000元素':<13} | {'10000元素':<13} | {'100000元素':<14}")
print("-" * 80)

for name in sorting_algorithms:
    row = [name.ljust(10)]
    for size in sizes:
        time_val, _ = results[name][size]
        if time_val == "跳过":
            row.append("跳过".ljust(12))
        else:
            row.append(f"{time_val:.6f}秒".ljust(12))
    print(" | ".join(row))
print("=" * 80)

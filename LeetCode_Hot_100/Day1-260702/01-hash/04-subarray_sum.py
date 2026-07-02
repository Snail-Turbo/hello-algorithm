"""
给你一个整数数组nums和一个整数k，请你统计并输出 该数组中和为 k 的子数组的个数。

子数组是数组中元素的连续非空序列。
"""

num_count, sum_target = map(int, input().split())
nums = list(map(int, input().split()))

prefix_sum_count = {0: 1}

current_sum = 0
count = 0

for num in nums:
    current_sum += num
    diff = current_sum - sum_target

    if diff in prefix_sum_count:
        count += prefix_sum_count[diff]
    
    prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

print(count)

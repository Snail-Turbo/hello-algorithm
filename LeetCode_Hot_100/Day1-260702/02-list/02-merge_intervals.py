"""
题目为Leetcode 56.合并区间问题。给定以数组intervals表示的若干个区间的集合，其中单个区间为intervals[i] = [starti, endi] 。任务是合并所有重叠的区间，并输出一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
"""

count = int(input())
intervals = [list(map(int, input().split())) for _ in range(count)]

# 关键思路：按区间起始位置排序，然后遍历合并
intervals.sort(key=lambda x: x[0])

merged = []

for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

from pprint import pprint
pprint(merged)
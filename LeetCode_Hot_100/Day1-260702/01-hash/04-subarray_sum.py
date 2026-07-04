"""
给你一个整数数组nums和一个整数k，请你统计并输出 该数组中和为 k 的子数组的个数。

子数组是数组中元素的连续非空序列。
"""


# 关键思路：前缀和计数
num_count, sum_target = map(int, input().split())
nums = list(map(int, input().split()))


class Solution:
    def subarray_sum(self, nums: list[int], k: int) -> int:
        prefix_sum_count = {0: 1}

        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            diff = current_sum - k # 求的是 和为k 的子数组，所以当前前缀和 = diff + k ，diff = current_sum - k 若存在 即 有 到当前的一段 和为k

            if diff in prefix_sum_count:
                count += prefix_sum_count[diff] # diff = current_sum - k 若存在 x个 即 有x个 到当前的一段 和为k

            # 【核心】 记录当前前缀和的出现次数，方便后续计算；且位置不能在if diff之前，因为需要先更新当前有几个到现在可以的，再记录上当前以给后续可记录当前
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

        return count
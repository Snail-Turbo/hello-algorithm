"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4] -4 -1 -1 0 1 2
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
 
"""

# 关键思路：
# 使用双指针技术，
#
# 1. 先对数组进行排序
# 2.然后固定一个数，用两个指针分别指向剩余数组的首尾，根据三数之和与目标值的大小关系移动指针


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        if length < 3:
            return []

        nums.sort()

        answers = []

        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:  # 【核心易错】 减少重复
                continue

            current_diff = -nums[i]

            j, k = i + 1, length - 1
            while j < k:
                current_sum = nums[j] + nums[k]

                if current_sum == current_diff:
                    answers.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:  # 【核心易错】 减少重复
                        j += 1

                    while j < k and nums[k] == nums[k+1]:  # 【核心易错】 减少重复
                        k -= 1

                elif current_sum < current_diff:
                    j += 1
                else:
                    k -= 1

        return answers


nums = [-1, 0, 1, 2, -1, -4]

import sys
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

        # 插入位置 一定是这个 left，左侧的都是小于他的，他可以放到 >= 的位置，即使是最后
        return left

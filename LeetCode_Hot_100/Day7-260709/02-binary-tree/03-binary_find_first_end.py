from typing import List


class Solution:
    def search_first(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2

            if nums[mid_index] < target:
                left = mid_index + 1
            else:
                right = mid_index - 1

        if left < len(nums) and nums[left] == target:
            return left + 1

        return -1

    def search_last(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = (left + right) // 2

            if target >= nums[mid_index]:
                left = mid_index + 1

            else:
                right = mid_index - 1

        if right >= 0 and nums[right] == target:
            return right + 1

        return -1

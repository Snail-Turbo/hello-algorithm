"""
quick sort
"""
import random

class Solution:
    def quick_sort(self, nums:list[int], left_idx:int, right_idx:int)-> None:
        if left_idx >= right_idx:
            return
        
        # 关键：随机选择一个元素作为基准，避免最坏情况的出现
        pivot_idx = random.randint(left_idx, right_idx)
        nums[pivot_idx], nums[right_idx] = nums[right_idx], nums[pivot_idx]

        x = nums[right_idx]

        i = left_idx
        
        for j in range(left_idx, right_idx):
            if nums[j] <= x:
                nums[i], nums[j] = nums[j], nums[i]

                i += 1
        
        # 此时 i 的位置 就是原来的 right_idx的数 的 正确位置
        nums[i], nums[right_idx] = nums[right_idx], nums[i]


        self.quick_sort(nums, left_idx=left_idx, right_idx=i-1)

        self.quick_sort(nums, left_idx=i+1, right_idx=right_idx)
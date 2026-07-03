"""
化简题面:给定一个数组 nums，将所有 0 原地的 移动到数组的末尾，同时保持非零元素的相对顺序。[0 1 0 3 12]→[1 3 12 0 0]
"""

class Solution:
    def move_zeros(self, nums:list[int]):
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]

                i += 1

        return nums

nums = [1,2,3,0,0,0,4,5,6]
so = Solution()

print(so.move_zeros(nums))


# [2] 快慢双指针拓展-quick sort 的 partition 操作
a = [3,1,7,4,5]
x = 4

i = 0
for j in range(len(a)):
    if a[j] <= x:
        a[i], a[j] = a[j], a[i]

        i += 1

print(','.join(map(str, a)))
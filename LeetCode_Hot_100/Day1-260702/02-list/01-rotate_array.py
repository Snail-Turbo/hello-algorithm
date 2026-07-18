"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
"""

count = int(input())
nums = list(map(int, input().split()))
k = int(input())


def rotate(count, nums, k):

    if count == 0:
        return

    k %= count

    if k == 0:
        return

    # 旧算法：O(n) 时间复杂度，O(n) 空间复杂度
    # nums[:] = nums[-k:] + nums[:-k]

    # 新算法：O(n) 时间复杂度，O(1) 空间复杂度
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

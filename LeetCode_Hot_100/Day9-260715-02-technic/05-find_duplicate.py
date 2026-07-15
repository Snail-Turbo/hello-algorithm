from typing import List


def findDuplicate(nums: List[int]) -> int:
    visited = set()

    current = 0  # 题干写了，包含 [1, n] 的 n+1 个数的数组

    while True:
        next = nums[current]

        if next in visited:
            return next

        visited.add(next)

        current += 1


def findDuplicate(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # 2b -b = k*c
    # b - a = kc - a

    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast

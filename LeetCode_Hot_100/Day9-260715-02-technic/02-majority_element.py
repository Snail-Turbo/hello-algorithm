from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票法
        now = -1
        count = 0

        for i in range(len(nums)):
            current_num = nums[i]

            if count == 0:
                now = current_num
                count += 1
            elif now == current_num:
                count += 1
            else:
                count -= 1

        return now

    def majorityElement(self, nums: List[int]) -> int:
        # 普通 stack 做法
        tmp_stack = []

        for num in nums:
            if tmp_stack and tmp_stack[-1] != num:
                tmp_stack.pop()
            else:
                tmp_stack.append(num)

        return tmp_stack[0]

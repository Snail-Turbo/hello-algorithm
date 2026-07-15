from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if not nums or len(nums) == 1:
            return nums

        slow = 0
        fast = 0

        while fast < len(nums):
            if nums[fast] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

            fast += 1

        fast -= 1
        slow = fast

        while fast > -1:
            if nums[fast] == 2:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow -= 1

            fast -= 1

    def sortColors(self, nums: List[int]) -> None:
        len_nums = len(nums)

        head = 0
        last = len_nums - 1

        fast = head

        while fast <= last:  # 这里是 fast <= last，因为 head 是slow，fast可能会撞到超过右边；【fast 只走未排序】
            if nums[fast] == 0:
                nums[head], nums[fast] = nums[fast], nums[head]
                head += 1

                fast += 1
            elif nums[fast] == 2:
                nums[last], nums[fast] = nums[fast], nums[last]
                last -= 1
            else:
                fast += 1

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        can_right = 1
        target = len(nums)

        for i, num in enumerate(nums):
            if i+1 > can_right:
                return False

            current_right = i+1+num

            can_right = max(current_right, can_right)

            if can_right >= target:
                return True

        return False

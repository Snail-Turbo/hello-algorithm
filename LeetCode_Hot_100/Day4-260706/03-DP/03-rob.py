class Solution:
    def rob(self, nums: list[int]) -> int:

        count = 0

        dp = [-1] * (len(nums)+1)

        # f[i] = max(f[i-2] + nums[i], f[i-1])
        dp[0] = 0
        dp[1] = nums[0]
        # f[2] = max(nums[:2])

        def get_nums_index(current_index):
            return current_index-1

        for end_index in range(2, len(nums) + 1):
            dp[end_index] = max(dp[end_index-2] + nums[get_nums_index(end_index)], dp[end_index-1])

            # dp[2] = max(dp[0]+nums[1], dp[1])
            # dp[2] = max(0+2, 1) = 2
            # dp[3] = max(1+3, 2) = 4
            # dp[4] = max(2+1, 4) = 4

        return dp[-1]

    def rob_compressed(self, nums: list[int]) -> int:

        dp1 = 0
        dp2 = nums[0]

        for i in range(1, len(nums)):
            current = max(dp1 + nums[i], dp2)

            dp1 = dp2
            dp2 = current

        return current


nums1 = [1, 2, 3, 1]
nums2 = [2, 7, 9, 3, 1]
so = Solution()
print(so.rob(nums1))
print(so.rob(nums2))

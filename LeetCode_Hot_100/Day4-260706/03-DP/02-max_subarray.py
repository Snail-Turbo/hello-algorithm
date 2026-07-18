class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        INF = float('inf')
        dp = [-INF] * (len(nums)+1)

        max_result = dp[0]

        # dp[i] = max(dp[i-1], 0) + nums[current_i -1]
        for i in range(1, len(nums) + 1):
            dp[i] = max(dp[i-1], 0) + nums[i-1]
            max_result = max(dp[i], max_result)

        # print(dp)
        return max_result

    def maxSubArray_spatial(self, nums: list[int]) -> int:

        last_max = nums[0]
        max_result = nums[0]

        for i in range(1, len(nums)):
            current_max = max(last_max, 0) + nums[i]
            max_result = max(max_result, current_max)

            last_max = current_max

        return max_result


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
so = Solution()
print(so.maxSubArray(nums))

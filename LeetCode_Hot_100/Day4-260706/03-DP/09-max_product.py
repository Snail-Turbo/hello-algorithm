class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        max_dp = [nums[0]]
        min_dp = [nums[0]]

        for i in range(1, len(nums)):

            choice_0 = nums[i]
            choice_1 = max_dp[i-1] * nums[i]
            choice_2 = min_dp[i-1] * nums[i]

            max_dp.append(max(choice_0, choice_1, choice_2))
            min_dp.append(min(choice_0, choice_1, choice_2))

        return max(max_dp)

    def maxProduct(self, nums: list[int]) -> int:
        last_max = nums[0]
        last_min = nums[0]

        max_value = nums[0]

        for i in range(1, len(nums)):
            last_min, last_max = min(nums[i], last_max*nums[i], last_min*nums[i]
                                     ), max(nums[i], last_max*nums[i], last_min*nums[i])

            max_value = max(max_value, last_max)

        return max_value

    # def maxProduct(self, nums: list[int]) -> int:
    #     dp = [-1] * len(nums)

    #     dp[0] = nums[0]

    #     ans = 1

    #     last_negative_idx = -10
    #     for i in range(len(nums)):
    #         if nums[i] < 0:
    #             last_negative_idx = i

    #     start_idx = -1

    #     for i in range(1, len(nums)):
    #         if nums[i] == 0:
    #             start_idx = i+1
    #             dp[i] = 0
    #             continue

    #         if nums[i] > 0:
    #             dp[i] = nums[i] * dp[i-1] if dp[i-1] > 0 else nums[i]
    #             continue

    #         if last_negative_idx >= start_idx:
    #             dp[i] = nums[i] * nums[last_negative_idx]
    #             if i - last_negative_idx > 1 and last_negative_idx < i-1 < i:
    #                 dp[i] *= dp[i-1]

    #             if last_negative_idx-1 >= 0 and dp[last_negative_idx-1] > 0:
    #                 dp[i] *= dp[last_negative_idx-1]

    #         else:
    #             dp[i] = nums[i]

    #         last_negative_idx = i

    #     return max(dp)


nums_test = [2, 3, -2, 4]
nums_test2 = [-2, 0, -1]
nums_test3 = [-2, -1, -1]
nums_test4 = [7, -2, -4]
nums_test5 = [1, 0, -1, 2, 3, -5, -2]
nums_test6 = [1, -2, 3, -4, -3, -4, -3]
so = Solution()

print(so.maxProduct(nums=nums_test))
print(so.maxProduct(nums=nums_test2))
print(so.maxProduct(nums=nums_test3))
print(so.maxProduct(nums=nums_test4))
print(so.maxProduct(nums=nums_test5))
print(so.maxProduct(nums=nums_test6))

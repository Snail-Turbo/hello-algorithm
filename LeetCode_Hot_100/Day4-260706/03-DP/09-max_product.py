"""
152. 乘积最大子数组

核心思路（一句话）：
  同时维护以 i 结尾的【最大乘积】和【最小乘积】，
  因为负数一来，最小的（负的）瞬间变成最大的（正的）。

为什么不能像"最大子数组和"那样只记一个 max？
  和：正数加正数变大，负数加正数变小 → 单调 → 记一个 max 就够了
  积：正数乘负数变负，再乘负数又变正 → 来回跳 → 必须同时记 min 和 max

状态转移：
  以 i 结尾的最大乘积 = max(  nums[i] 自己单干,
                             前一个最大 * nums[i],
                             前一个最小 * nums[i]  )    ← 负负得正！

  以 i 结尾的最小乘积 = min(  同上三个  )              ← 留给后面的负数来翻盘

一句话记：
  乘积会变号 → 最大最小都留着 → 负数来了让最小的翻盘。
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_dp = [nums[0]]  # 以 i 结尾的【最大乘积】
        min_dp = [nums[0]]  # 以 i 结尾的【最小乘积】

        for i in range(1, len(nums)):
            choices = (
                nums[i],
                max_dp[i-1] * nums[i],
                min_dp[i-1] * nums[i]
            )

            max_dp.append(max(choices))
            min_dp.append(min(choices))

        return max(max_dp)  # 所有结尾中，最大的

    def maxProduct_compressed(self, nums: list[int]) -> int:
        max_result = nums[0]
        last_max = nums[0]
        last_min = nums[0]

        for i in range(1, len(nums)):
            choices = (
                nums[i],
                last_max * nums[i],
                last_min * nums[i]
            )

            last_max = max(choices)
            last_min = min(choices)

            max_result = max(max_result, last_max)

        return max_result

    def maxProduct(self, nums: list[int]) -> int:

        max_dp = [nums[0]]  # 以 i 结尾的最大乘积
        min_dp = [nums[0]]  # 以 i 结尾的最小乘积（等着被负数翻盘）

        for i in range(1, len(nums)):

            choice_0 = nums[i]                # 自己单干（前面的累赘不如不要）
            choice_1 = max_dp[i-1] * nums[i]  # 接在前面的最大值后面
            choice_2 = min_dp[i-1] * nums[i]  # 接在前面的最小值后面（负负得正！）

            max_dp.append(max(choice_0, choice_1, choice_2))
            min_dp.append(min(choice_0, choice_1, choice_2))

        return max(max_dp)

    # 空间优化版：只记上一个 max/min，不用整个数组
    def maxProduct_optimized(self, nums: list[int]) -> int:
        last_max = nums[0]
        last_min = nums[0]
        max_value = nums[0]

        for i in range(1, len(nums)):
            # 注意：必须同时赋值，否则 last_max 被修改后会影响 last_min 的计算
            last_min, last_max = (
                min(nums[i], last_max * nums[i], last_min * nums[i]),
                max(nums[i], last_max * nums[i], last_min * nums[i])
            )
            max_value = max(max_value, last_max)

        return max_value


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

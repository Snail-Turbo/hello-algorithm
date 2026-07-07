"""
1.动态规划的两大关键：状态和转移

2.动态规划的核心解题技巧：

1.题目问什么，我们定义什么状态

2.转移：总是考虑最后一个元素的状态
"""


class Solution:
    def numSquares(self, n: int) -> int:

        min_count = 999

        dp = [0] * n

        # 0 1 2 3 4 5 6
        # 1 2 3 4 5 6 7
        # 1 2 3 1 2 3 4
        # dp[i] = dp[last_wanquanpingfangshu] + dp[i-last_wanquanping]
        # dp[i] = 1 + dp[i-last_square]

        dp[0] = 1
        dp[1] = 2
        current_base = 1
        naxt_square = (current_base+1)**2
        already_square = [1]

        for i in range(1, n):
            if (i+1) == naxt_square:
                already_square.append(i+1)

                dp[i] = 1

                current_base += 1
                naxt_square = (current_base+1)**2
                continue

            # 这个 dp[i] 要遍历所有他能取的 square，min(dp[i-square]) + 1：
            # 即 数为i+1，min(dp[i-square]) + 1 = dp[i]
            dp[i] = min([dp[i-square] for square in already_square]) + 1

        return dp[-1]


n = 12
so = Solution()
print(so.numSquares(n))

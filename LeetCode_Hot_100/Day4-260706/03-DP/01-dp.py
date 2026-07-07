class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)

        # dp[2] = 2
        dp[1] = 1
        dp[0] = 1  # dp[2] = dp[1] + dp[0], dp[0] = dp[2] - dp[1]

        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]

    def climbStairs_dynamic(self, n: int) -> int:
        # dp[i] = dp[i-1] + dp[i-2] 共 3 个
        dp = [0] * 3

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[2] = dp[0] + dp[1]

            dp[0] = dp[1]
            dp[1] = dp[2]

        return dp[-1]


so = Solution()
print(so.climbStairs(4))
print(so.climbStairs_dynamic(4))


# 关键思路：
# 0. 异常输入直接 终止 【关键】
#
# 1. 题目问什么，就定义什么状态： 定义函数 f(i) 为 爬到 第i个台阶的不同方法数
# 2. 状态转移方程：从 【最后一个元素】 的状态开始，i 要么 i-1来 要么 i-2来，所以 f(i) = f(i-1) + f(i-2)
# 3. 初始状态 或者 终止状态定义：
#       f(1)：这个好说，知道只有一种
#       f(0)：这个如何理解，不如 f(2) - f(1) = f(0)

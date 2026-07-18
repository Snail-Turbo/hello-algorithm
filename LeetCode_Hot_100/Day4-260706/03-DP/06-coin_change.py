class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        max_impossible = amount+1  # 必须是 amount+1，因为最多是 amount 个 1
        dp = [max_impossible] * (amount+1)

        dp[0] = 0

        for i in range(1, amount+1):

            for coin in coins:
                if coin > i:  # 只有 i >= coin 才能放   【转移限制】
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[-1] if dp[-1] != amount+1 else -1


coins = [1]
amount = 0

so = Solution()
print(so.coinChange(coins, amount))

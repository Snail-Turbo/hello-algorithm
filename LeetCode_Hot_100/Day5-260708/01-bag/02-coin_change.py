class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        len_coins = len(coins)

        max_impossible = amount + 1
        dp = [[max_impossible] * (amount + 1) for _ in range(len_coins + 1)]

        for i in range(len_coins + 1):
            dp[i][0] = 0

        for i in range(1, len_coins + 1):
            for j in range(1, amount + 1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]] + 1 if j-coins[i-1] >= 0 else max_impossible)

        return dp[-1][-1] if dp[-1][-1] != max_impossible else -1

    def coinChange(self, coins: list[int], amount: int) -> int:

        len_coins = len(coins)

        dp = [[amount+1] * (amount+1) for _ in range(len_coins+1)]

        for i in range(len_coins+1):
            dp[i][0] = 0

        for i in range(1, len_coins+1):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]

                if j >= coins[i-1]:
                    dp[i][j] = min(dp[i][j], dp[i][j-coins[i-1]]+1)

        return dp[len_coins][amount] if dp[len_coins][amount] != amount+1 else -1


coins = [1, 2, 5]
amount = 11

so = Solution()
print(so.coinChange(coins, amount))

from pprint import pprint


def solve():
    budget = int(input())
    prices_input = input().strip()
    prices = list(map(int, prices_input.split()))
    prices.sort()
    
    remaining = budget

    # dp 数组
    dp = [0] * (remaining + 1)
    dp[0] = 1

    # 状态转移
    for p in prices:
        for j in range(remaining, p - 1, -1):
            dp[j] += dp[j - p]

            # print(p, j)
            # print(dp[j], dp[j - p])
            # pprint(dp)


    pprint(dp)
    # print(dp)

if __name__ == "__main__":
    solve()
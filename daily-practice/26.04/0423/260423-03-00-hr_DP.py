def solve():
    budget = int(input())
    prices_input = input().strip()
    prices = list(map(int, prices_input.split()))
    prices.sort()

    min_cost = sum(prices)

    if min_cost > budget:
        print(0)
        return
    
    remaining = budget - min_cost

    # dp 数组
    dp = [0] * (remaining + 1)
    dp[0] = 1

    # 状态转移
    for p in prices:
        for j in range(p, remaining + 1):
            dp[j] += dp[j - p]
            from pprint import pprint
            print(p, j)
            print(dp[j], dp[j - p])
            pprint(dp)

    from pprint import pprint
    pprint(dp)
    print(dp[remaining])

if __name__ == "__main__":
    solve()
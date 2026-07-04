"""
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12

"""

# 思路：取k个元素，意味着剩下的是一个连续的子数组，长度为n-k
# 找到长度为n-k的连续子数组中元素和最小的，用总和减去它就是答案

# 两个指针同向移动，维护一个连续区间，每次只变一头，另一头不用回头。
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        card_count = len(cardPoints)
        total_sum = sum(cardPoints)

        mid_length = card_count - k

        if mid_length == 0:
            return total_sum
        
        mid_sum = sum(cardPoints[:mid_length])
        min_mid_sum = mid_sum


        for j in range(mid_length, card_count):
            mid_sum += cardPoints[j]
            mid_sum -= cardPoints[j-mid_length]

            min_mid_sum = min(min_mid_sum, mid_sum) # 差值应该是最小，因为要取 另外一堆

        return total_sum - min_mid_sum




card_points = [1,2,3,4,5,6,1]
k_input = 3

so = Solution()
print(so.maxScore(card_points, k_input))


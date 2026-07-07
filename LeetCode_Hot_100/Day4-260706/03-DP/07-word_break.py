"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。


"""
# 关键思路：
# end_index为dp条件
# 然后遍历每个的 mid_index，是否有 [:mid_index] True 且 [mid_index: end_index] in wordDict


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        n = len(s)

        dp = [False] * (n+1)
        dp[0] = True

        wordDict = set(wordDict)

        for end_index in range(1, n+1):

            for mid_index in range(n+1):  # 从0开始，后面的mid_index就不需要每次 -1 了
                if dp[mid_index] and s[mid_index:end_index] in wordDict:
                    dp[end_index] = True
                    continue

        return dp[-1]


so = Solution()

s = "leetcode"
word_dict = ["leet", "code"]
print(so.wordBreak(s, word_dict))

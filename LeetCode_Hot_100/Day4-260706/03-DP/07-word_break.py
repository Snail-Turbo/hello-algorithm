"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。


"""
# 关键思路：
# end_index为dp条件
# 然后遍历每个的 mid_index，是否有 [:mid_index] True 且 [mid_index: end_index] in wordDict


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        LeetCode 139. 单词拆分

        DP 思路：
          dp[end] = s[:end] 能否被字典拆分
          转移：遍历切分点 mid，若 dp[mid] 且 s[mid:end] 在字典中，则 dp[end]=True

        时间 O(n^2)，空间 O(n)
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        word_set = set(wordDict)

        for end in range(1, n + 1):
            for mid in range(end):  # 优化：mid 只需到 end，超过 end 切片为空无意义
                if dp[mid] and s[mid:end] in word_set:
                    dp[end] = True
                    break  # 优化：找到一种拆分即可，无需继续：因为先遍历的end，然后遍历起点

        return dp[-1]

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)

        dp = [0] * (n+1)
        dp[0] = 1

        for end in range(1, n + 1):
            for mid in range(end):
                if dp[mid] and s[mid:end] in word_set:
                    dp[end] = 1
                    break

        return dp[-1]


so = Solution()

s = "leetcode"
word_dict = ["leet", "code"]
print(so.wordBreak(s, word_dict))

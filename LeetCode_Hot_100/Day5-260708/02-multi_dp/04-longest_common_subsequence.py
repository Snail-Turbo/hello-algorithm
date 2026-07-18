"""
1143. 最长公共子序列 (LCS)

核心思路（DP）：
  dp[i][j] = text1 前 i 个字符 与 text2 前 j 个字符 的 LCS 长度。

  字符相等（text1[i-1] == text2[j-1]）：
    → dp[i][j] = dp[i-1][j-1] + 1    两人都消掉这个字符，↖ + 1

  字符不等：
    → dp[i][j] = max(dp[i-1][j], dp[i][j-1])   至少一人扔掉这个字符，max(↑, ←)

一句话记：
  相等取左上角+1，不等取 max(上方, 左方)。
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_text1 = len(text1)
        len_text2 = len(text2)

        # dp[i][j]: text1[:i] 与 text2[:j] 的 LCS
        dp = [[0] * (len_text2 + 1) for _ in range(len_text1 + 1)]

        for i in range(1, len_text1 + 1):
            for j in range(1, len_text2 + 1):
                if text1[i - 1] == text2[j - 1]:       # 相等 → ↖ + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:                                   # 不等 → max(↑, ←)
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


so = Solution()
print(so.longestCommonSubsequence("abcde", "ac"))

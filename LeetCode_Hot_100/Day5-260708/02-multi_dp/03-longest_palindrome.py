"""
5. 最长回文子串

给你一个字符串 s，找到 s 中最长的 回文 子串。


示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"


提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)

        dp = [[False] * (len_s+1) for _ in range(len_s+1)]

        for i in range(len_s+1):
            dp[i][i] = True

        max_length = 1
        max_start, max_end = 1, 1
        for i in range(len_s-1, 0, -1):
            for j in range(i+1, len_s+1):

                if j-i == 1:
                    dp[i][j] = s[i-1] == s[j-1]
                elif j-i > 1:
                    dp[i][j] = s[i-1] == s[j-1] and dp[i+1][j-1]

                if dp[i][j] and j-i+1 > max_length:
                    max_length = j-i+1
                    max_start, max_end = i, j

        return s[max_start-1:max_end]

    def longestPalindrome_2(self, s: str) -> str:
        len_s = len(s)

        dp = [[False] * (len_s+1) for _ in range(len_s+1)]

        max_length = 0  # 不额外循环一次
        max_start, max_end = 0, 0
        for i in range(len_s, 0, -1):
            for j in range(i, len_s+1):
                if j == i:
                    dp[i][j] = True

                elif s[i-1] == s[j-1]:  # 相同if先判断，剪枝
                    dp[i][j] = True
                    if j-i > 1:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j-i+1 > max_length:
                    max_length = j-i+1
                    max_start, max_end = i, j

        return s[max_start-1:max_end]


input_s_1 = "babad"
input_s_2 = "aaaa"
so = Solution()
print(so.longestPalindrome(input_s_1))
print(so.longestPalindrome(input_s_2))

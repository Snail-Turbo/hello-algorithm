"""
32. 最长有效括号

核心思路（DP）：
  dp[i] = 以 i 结尾的最长有效括号子串长度。
  以 '(' 结尾 → dp[i] = 0（永远不可能有效）。
  以 ')' 结尾 → 看它跟谁配对，分两种情况。

两种情况图解：
  情况1：前一个是 '(' → 直接配对
    ... ( )
         ↑ ↑
        i-1 i
    dp[i] = dp[i-2] + 2

  情况2：前一个是 ')' → 跳过前一个的整个有效段，看再前面那个
    ... (   ( ... )   )
         ↑   ↑     ↑   ↑
        mid  i-dp[i-1]-1  i-1  i
         └── dp[mid-1] ──┘└─ dp[i-1] ─┘
    mid = i - dp[i-1] - 1
    如果 s[mid] == '('：配对成功！
    dp[i] = dp[i-1] + 2 + dp[mid-1]
            └内部有效段┘ └配对┘ └配对前有效段┘

一句话记：
  遇到 ) ，看前一个：是 ( → 直接配对；是 ) → 跳过内部有效段找配对的 ( 。
"""


class Solution:
    def longestValidParentheses_ng(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        dp = [0] * n
        dp[1] = 2 if s[0] == '(' and s[1] == ')' else 0  # 关键

        for i in range(2, n):
            if s[i] == '(':
                continue

            if s[i-1] == '(':
                dp[i] = 2 + dp[i-2]
                continue

            mid = i-dp[i-1]-1
            if mid >= 0 and s[mid] == '(':
                dp[i] = dp[i-1] + 2 + (dp[mid-1] if mid-1 >= 0 else 0)  # 关键：(dp[mid-1] if mid-1 >= 0 else 0)

        return max(dp)

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        # dp[i] = 以 s[i-1] 结尾的最长有效括号长度（1-indexed，方便处理 i-2）
        dp = [0] * (n + 1)

        for end_index in range(2, n + 1):
            current_index_s = end_index - 1

            # 以 '(' 结尾 → dp = 0
            if s[current_index_s] == '(':
                continue

            # 情况1：前一个是 '(' → "()" 直接配对
            if s[current_index_s - 1] == '(':
                dp[end_index] = dp[end_index - 2] + 2
                continue

            # 情况2：前一个是 ')' → 跳过内部有效段，找配对的 '('
            # mid = 当前 ) 的配对 ( 应该在的位置
            mid = current_index_s - dp[end_index - 1] - 1
            if mid >= 0 and s[mid] == '(':
                dp[end_index] = dp[end_index - 1] + 2 + dp[mid]  # dp[mid] = dp[mid_index+1] = dp[mid-1+2]
                #                    └内部有效段┘ └配对┘ └配对前┘

        return max(dp)

    # 0-indexed 版本（逻辑同上，不偏移索引）
    def longestValidParentheses_0indexed(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        dp = [0] * n

        for i in range(1, n):
            if s[i] == '(':         # 以 ( 结尾 → 无效
                continue

            # 情况1：前一个是 ( → "()" 配对
            if s[i - 1] == '(':
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                continue

            # 情况2：前一个是 ) → 跳过内部有效段找配对
            inner_len = dp[i - 1]          # 内部有效段长度
            mid = i - inner_len - 1        # 可能配对的 ( 位置
            if mid >= 0 and s[mid] == '(':
                dp[i] = inner_len + 2 + (dp[mid - 1] if mid >= 1 else 0)

        return max(dp)


s = "(()))())("
so = Solution()
print(so.longestValidParentheses(s))

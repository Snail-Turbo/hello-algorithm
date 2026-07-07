class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # dp[i] 为 以 i 结尾的 最长的 有效括号子串长度
        # dp[i] = dp[i-1] if s[i] == '(' else
        n = len(s)

        if n < 2:
            return 0

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0

        for end_index in range(2, n+1):

            current_index_s = end_index-1

            # current 是 (
            if s[current_index_s] == '(':
                dp[end_index] = 0
                continue

            # current is )
            # current-1 是 (  or
            if s[current_index_s-1] == '(':
                dp[end_index] = dp[end_index-2] + 2
                continue

            if current_index_s-dp[end_index-1]-1 >= 0 and s[current_index_s-dp[end_index-1]-1] == '(':
                dp[end_index] = dp[end_index-1] + 2 + dp[current_index_s-dp[end_index-1]-1]

        return max(dp)

    def longestValidParentheses_2(self, s: str) -> int:

        # dp[i] 为 以 i 结尾的 最长的 有效括号子串长度
        # dp[i] = dp[i-1] if s[i] == '(' else
        n = len(s)

        if n < 2:
            return 0

        dp = [0] * n
        dp[0] = 0

        for i in range(1, n):

            # current 是 (
            if s[i] == '(':
                dp[i] = 0
            else:
                # ....(....)
                inner_length = dp[i-1]
                mid_index = i-inner_length-1

                if mid_index < 0 or s[mid_index] != '(':
                    continue

                # current-1 是 (  or
                if mid_index == 0:
                    dp[i] = dp[i-1] + 2
                    continue

                if mid_index > 0:
                    dp[i] = dp[i-1] + 2 + dp[mid_index-1]

        return max(dp)


s = "(()))())("

"a(()))())("
"0002460800"
# 0 1 2 3 4 5
# 1 2 3 4 5 6
# end_index = 7
# current_index = 6

so = Solution()
print(so.longestValidParentheses(s))

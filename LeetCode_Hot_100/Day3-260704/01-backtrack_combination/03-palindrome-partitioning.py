"""
131. 分割回文串

给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。


示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
 

提示：

1 <= s.length <= 16
s 仅由小写英文字母组成
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:

        result = []

        path = []

        def backtrack(start_index):

            if start_index == len(s):  # 结束条件 且 path合适条件：切到最后了
                result.append(path[:])
                return

            for right_cut in range(start_index + 1, len(s) + 1):
                current_slice = s[start_index: right_cut]

                if current_slice != current_slice[::-1]:  # 非合适区间，跳过就行了
                    continue

                path.append(current_slice)
                backtrack(right_cut)
                path.pop()

        backtrack(0)

        return result


s = "aab"
so = Solution()
print(so.partition(s))

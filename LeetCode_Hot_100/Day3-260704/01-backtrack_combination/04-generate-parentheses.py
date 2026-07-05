"""
22. 括号生成

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8
"""


class Solution:
    # 2n 个位置，看放什么，约束条件是 左括号在前
    def generateParenthesis(self, n: int) -> list[str]:

        result = []

        path = []

        def backtrack(left_count, right_count):
            if left_count == right_count == 0:
                result.append("".join(path))
                return

            if left_count > 0:
                path.append("(")
                backtrack(left_count-1, right_count)
                path.pop()

            if right_count > left_count:
                path.append(")")
                backtrack(left_count, right_count-1)
                path.pop()

        backtrack(n, n)

        return result

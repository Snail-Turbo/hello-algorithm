"""
17. 电话号码的字母组合
已解答
中等
相关标签
premium lock icon
相关企业
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



 

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = "2"
输出：["a","b","c"]
 

提示：

1 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # 这个天然自带 不重复，不需要used
        phone_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        results = []
        path = []
        n = len(digits)

        def backtrack(current_index):
            if current_index == n:
                results.append(''.join(path))
                return

            current_digits = phone_map[digits[current_index]]

            for digit in current_digits:
                path.append(digit)

                backtrack(current_index+1)

                path.pop()

        backtrack(0)

        return results

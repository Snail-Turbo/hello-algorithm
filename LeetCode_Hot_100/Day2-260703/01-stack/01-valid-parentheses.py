"""
LeetCode 20. 有效的括号

在线刷题

给定一个只包括 '(', ')', '{', '}', '[', ']' 的字符串 s，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

输入：([[]])

输出：true

1 <= s.length <= 10^4
s 仅由括号 '()[]{}' 组成

c
"""

class Solution:
    def is_valid(self, string:str) -> bool:
        stack = []

        map_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in string:
            if char in map_dict:
                if stack and stack[-1] == map_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
    

if __name__ == "__main__":
    s = Solution()
    string = "([[]])"
    print(string,s.is_valid(string))  # 输出: True
    print("({)}",s.is_valid("({)}"))  # 输出: False
"""
LeetCode 394. 字符串解码

在线刷题

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encodedstring]，表示其中方括号内部的 encodedstring 正好重复 k次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a或 2[4]的输入。

输入：3[a]2[bc]

输出：aaabcbc

1 <= s.length <= 30
s由小写英文字母、数字和方括号 '[]' 组成
s保证是一个 有效 的输入。
s中所有整数的取值范围为 [1, 300]
"""


class Solution:
    def decode_string(self, string: str) -> str:
        stack = []

        for char in string:
            if char != ']':
                stack.append(char)

            else:
                # 此时 ']' 出现了，不入栈
                tmp_string = ''
                # "10[abc3[cba]]"
                while stack[-1] != '[':
                    tmp_string += stack.pop()
                stack.pop()  # 弹出'['

                tmp_string = tmp_string[::-1]  # 记得反转

                tmp_num_string = ''
                while stack and stack[-1].isdigit():  # 【注意】 这里要 stack 判断非空
                    tmp_num_string += stack.pop()
                tmp_num_string = tmp_num_string[::-1]  # 记得反转

                tmp_num = int(tmp_num_string)

                for _ in range(tmp_num):
                    for ch in tmp_string:
                        stack.append(ch)

        return "".join(stack)


if __name__ == "__main__":
    intput_string = "2[abc3[cba]]"

    so = Solution()

    print(so.decode_string(intput_string))

"""
LeetCode 71. 简化路径

在线刷题

给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格绝对路径（以 '/' 开头），请你将其转化为更加简洁的规范路径。

在 Unix 风格的文件系统中，规则如下：
一个点 '.' 表示当前目录本身。
此外，两个点 '..' 表示将目录切换到上一级（指向父目录）。
任意多个连续的斜杠（即，'//' 或 '///' ）都被视为单个斜杠 '/' 。
任何其他格式的点（例如，'...' 或 '....' ）均被视为有效的文件/目录名称。

返回的简化路径必须遵循下述格式：
始终以斜杠 '/' 开头。
两个目录名之间必须只有一个斜杠 '/' 。
最后一个目录名（如果存在）不能以 '/' 结尾。
此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..' ）。

返回简化后得到的规范路径。

输入
path = "/.../a/./../b/c/../d/./"

输出
"/.../b/d"

1 ≤ |path| ≤ 3000
path 由英文字母、数字、'.'、'/'、'_' 组成
path 保证是一个合法的 Unix 风格绝对路径
"""



# input: path = "/.../a/../b/c/../d/"
# output: "/.../b/d"

# 思路：使用栈来处理路径，先把路径按 '/' 分割，然后遍历每个部分：
# 1. 如果是空字符串或者 '.'，则跳过。
# 2. 如果是 '..'，则弹出栈顶元素（如果栈不为空）。
# 3. 否则，将当前部分压入栈中。
class Solution:
    def simplify_path(self, path_original:str)->str:
        stack = []
        
        split_path = path_original.split('/')

        for name in split_path:
            if name == '' or name == '.':
                continue
            elif name == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(name)
        
        if not stack:
            return '/'
        
        return '/' + '/'.join(stack) # 记得 '/' 开头


if __name__ == "__main__":

    str_path = "/.../a//../b/c/../d/./"
    so = Solution()
    print(so.simplify_path(str_path))
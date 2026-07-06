"""
79. 单词搜索

给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        y_len = len(board)
        x_len = len(board[0])

        used = [[0] * x_len for _ in range(y_len)]
        path = []
        n_target = len(word)
        direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def backtrack(y, x):
            if len(path) == n_target:
                return "".join(path) == word

            for diff_y, diff_x in direction:
                new_y, new_x = y + diff_y, x + diff_x
                if new_y not in range(y_len) or new_x not in range(x_len) or used[new_y][new_x] or board[new_y][new_x] not in word:
                    continue

                path.append(board[new_y][new_x])
                used[new_y][new_x] = 1

                if backtrack(new_y, new_x):
                    return True

                path.pop()
                used[new_y][new_x] = 0

            return False

        for y in range(y_len):
            for x in range(x_len):

                if board[y][x] == word[0]:
                    path.append(board[y][x])
                    used[y][x] = 1
                    if backtrack(y, x):
                        return True
                    path.pop()
                    used[y][x] = 0

        return False

    def exist_v2(self, board: list[list[str]], word: str) -> bool:
        y_len = len(board)
        x_len = len(board[0])

        used = [[0] * x_len for _ in range(y_len)]

        path = []
        n_target = len(word)

        direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def backtrack(y, x, index) -> bool:
            if index == n_target:
                return True

            if x < 0 or x > x_len-1 or y < 0 or y > y_len - 1 or used[y][x] or board[y][x] != word[index]:
                return False

            used[y][x] = 1
            for diff_y, diff_x in direction:
                new_y, new_x = y + diff_y, x + diff_x
                if backtrack(new_y, new_x, index+1):
                    return True

            used[y][x] = 0
            return False

        for y in range(y_len):
            for x in range(x_len):
                if backtrack(y, x, 0):
                    return True

        return False

    def exist_v3(self, board: list[list[str]], word: str) -> bool:
        y_len = len(board)
        x_len = len(board[0])

        n_target = len(word)

        direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def backtrack(y, x, index):
            if index == n_target:
                return True

            if x < 0 or x > x_len-1 or y < 0 or y > y_len - 1 or board[y][x] != word[index]:
                return False

            temp = board[y][x]
            board[y][x] = '?'

        for y in range(y_len):
            for x in range(x_len):
                if backtrack(y, x, 0):
                    return True

        return False


board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
word = "ABCCED"

so = Solution()
print(so.exist(board, word))

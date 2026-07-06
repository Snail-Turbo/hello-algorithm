"""
51. N 皇后

按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        results = []

        path = [["."] * n for _ in range(n)]

        col_used = set()
        main_diag_used = set()
        anti_diag_used = set()

        def backtrack(current_y):

            if current_y == n:
                results.append(["".join(row) for row in path])
                return

            for current_x in range(n):
                current_main_diag = current_y - current_x
                current_anti_diag = current_y + current_x
                if current_x in col_used or current_anti_diag in anti_diag_used or current_main_diag in main_diag_used:
                    continue

                path[current_y][current_x] = 'Q'
                col_used.add(current_x)
                main_diag_used.add(current_main_diag)
                anti_diag_used.add(current_anti_diag)

                backtrack(current_y+1)

                path[current_y][current_x] = '.'
                col_used.remove(current_x)
                main_diag_used.remove(current_main_diag)
                anti_diag_used.remove(current_anti_diag)

        backtrack(0)

        return results

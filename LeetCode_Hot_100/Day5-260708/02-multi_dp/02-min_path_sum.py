"""
64. 最小路径和

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

 

示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12
 

"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        max_impossible = float('inf')

        len_y = len(grid)
        len_x = len(grid[0])
        dp = [[max_impossible] * (len_x + 1) for _ in range(len_y + 1)]

        dp[0][1] = 0

        for i in range(1, len_y+1):
            for j in range(1, len_x+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        return dp[-1][-1]


so = Solution()
print(so.minPathSum([[100, 100, 100, 100]]))

"""
给定一个 m×n的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用原地算法
"""

# 关键思路：
# 1. 使用两个标记数组分别记录每一行和每一列是否需要被置零，最后再遍历一遍矩阵，将需要置零的行和列置零。
# 2. 使用矩阵的第一行和第一列作为标记数组，最后再根据第一行和第一列的标记来置零，同时需要额外记录第一行和第一列是否需要被置零。

class Solution:
    def set_zeros(self, matrix: list[list[int]]) -> None:
        count_col = len(matrix[0])
        count_row = len(matrix)

        first_col_has_zero = any(matrix[i][0] == 0 for i in range(count_row))
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(count_col))

        for i in range(1, count_row):
            for j in range(1, count_col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, count_row):
            for j in range(1, count_col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_col_has_zero:
            for i in range(count_row):
                matrix[i][0] = 0

        if first_row_has_zero:
            for j in range(count_col):
                matrix[0][j] = 0
        
        return matrix
    

if __name__ == "__main__":
    """
    3 3
    1 1 1
    1 0 1
    1 1 1
    """

    count_row, count_col = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(count_row)]

    solution = Solution()
    result = solution.set_zeros(matrix)
    
    for i in range(count_row):
        print(" ".join(map(str, result[i])))
        
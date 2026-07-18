"""
编写一个 高效算法 来 搜索 m x n 矩阵 matrix 中的目标值 target。

该矩阵具有以下特性：

1. 每行的元素 从左到右升序排列
2. 每列的元素 从上到下升序排列
"""

"""
5 5
1 4 7 11 15
2 5 8 12 19
3 6 9 16 22
10 13 14 17 24
18 21 23 26 30
5
"""


def is_target_in_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])

    # 选择从右上角开始搜索
    i, j = 0, n - 1

    while i < m and j >= 0:
        if matrix[i][j] == target:
            return True

        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1

    return False


if __name__ == "__main__":
    """
    5 5
    1 4 7 11 15
    2 5 8 12 19
    3 6 9 16 22
    10 13 14 17 24
    18 21 23 26 30
    5
    """

    m, n = map(int, input().split())

    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    target = int(input())

    result = is_target_in_matrix(matrix, target)
    print(result)

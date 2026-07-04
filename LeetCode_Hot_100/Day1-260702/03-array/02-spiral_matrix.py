"""
给你一个 m 行 n 列的矩阵 matrix，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素
"""

def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
    
    m, n = len(matrix), len(matrix[0])
    result = []

    top, bottom, left, right = 0, m - 1, 0, n - 1

    while top <= bottom and left <= right: # <= 是为了处理只有一行或一列的情况
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom: # 小关键，因为前面的循环可能已经改变了 top 和 bottom 的值
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

        if left <= right: # 小关键，因为前面的循环可能已经改变了 left 和 right 的值
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(spiral_order(matrix))
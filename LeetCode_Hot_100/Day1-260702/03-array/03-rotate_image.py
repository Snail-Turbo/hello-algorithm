"""
从题目中提取关键信息：给定一个n×n的二维矩阵matrix表示图像，要求将图像顺时针旋转90° ，并且必须在原地旋转图像，即直接修改输入的二维矩阵，不要使用额外的矩阵。
"""

# 先中线就是逆时针
# 先主对角线就是顺时针
def my_rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)

    # 【关键】 为什么不能先沿垂直中线翻转再沿主对角线翻转？因为这样会导致元素位置不正确，最终结果会是逆时针旋转90°而不是顺时针旋转90°。

    # 先沿主对角线翻转
    for i in range(n):
        for j in range(i + 1, n): # 这里为什么 i+1？因为主对角线上的元素不需要交换，i+1表示从主对角线的下一个元素开始交换
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 再沿垂直中线翻转
    for i in range(n):
        matrix[i].reverse()

if __name__ == "__main__":

    n = int(input())

    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    my_rotate(matrix)

    for row in matrix:
        print(" ".join(map(str, row)))
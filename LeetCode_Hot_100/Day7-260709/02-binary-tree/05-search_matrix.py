from typing import List


def _value_at_flat_index(matrix: list[list[int]], index: int, m: int):
    return matrix[index // m][index % m]


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0

        n, m = len(matrix), len(matrix[0])

        right = n * m - 1

        while left <= right:
            mid_index = (left + right) // 2
            current_value = _value_at_flat_index(matrix, mid_index, m)

            if current_value < target:
                left = mid_index + 1

            elif current_value > target:
                right = mid_index - 1

            else:
                return True

        return False

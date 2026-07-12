from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid_index = (left + right) // 2

            current_num = nums[mid_index]

            if current_num < target:
                left = mid_index + 1
                continue
            elif current_num > target:
                right = mid_index - 1
            else:
                return True

        return False


def main():
    # 读取数组长度 n 和查询次数 Q
    n, Q = map(int, input().split())

    # 读取升序数组
    nums = list(map(int, input().split()))

    # 创建 Solution 对象
    solution = Solution()

    # 对每个查询进行二分查找
    for _ in range(Q):
        # 读取每次查询的目标值
        target = int(input())

        # 调用函数并输出查询结果
        if solution.search(nums, target) != -1:
            print("YES")
        else:
            print("NO")


"""
8 1
1 2 4 5 7 10 11 13
7
YES
"""


if __name__ == "__main__":
    main()

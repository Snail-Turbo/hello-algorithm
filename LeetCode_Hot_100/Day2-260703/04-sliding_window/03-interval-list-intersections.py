"""
给定两个由若干个 闭区间 组成的列表，分别为 firstList 和 secondList。

每个区间列表内部的区间都是两两不相交的，并且已经按照区间起点从小到大排序。

请你求出这两个区间列表的所有交集。

形式上，闭区间 [a,b] 表示所有满足 a≤x≤b 的实数 x。

两个闭区间的交集要么为空，要么仍然是一个闭区间。例如，[1,3] 和 [2,4] 的交集为 [2,3]。
"""


from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0

        results = []

        n, m = len(firstList), len(secondList)

        while i<n and j<m:
            current_first = firstList[i]
            current_second = secondList[j]

            left_first, right_first = current_first[0], current_first[1]
            left_second, right_second = current_second[0], current_second[1]

            max_left = max(left_first, left_second)
            min_right = min(right_first, right_second)


            if max_left <= min_right:
                results.append([max_left, min_right])

            if right_first < right_second: # 关键点，否则 [9,20] ; [14,16], [17,20] 会被漏下，即保留未来可匹配段
                i += 1
            else:
                j += 1


        return results


if __name__ == "__main__":
    # 读取两个区间列表的长度
    n, m = 4, 4

    # 读取第一个区间列表
    # firstList = [list(map(int, input().split())) for _ in range(n)]
    firstList = [[0,2],[5,10],[13,23],[24,25]]

    # 读取第二个区间列表
    # secondList = [list(map(int, input().split())) for _ in range(m)]
    secondList = [[1,5],[8,12],[15,24],[25,26]]

    # 调用函数并输出结果
    solution = Solution()
    result = solution.intervalIntersection(firstList, secondList)

    # 输出交集区间数量
    print(len(result))

    # 输出每个交集区间
    for x, y in result:
        print(x, y)

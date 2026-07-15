"""
207. 课程表 — 拓扑排序判环

核心思路：
  问题本质：有向图是否能完成拓扑排序（是否无环）。
  有环 → 有课永远有前置依赖 → 修不完 → False。
  无环 → 所有课都能排出一个先后顺序 → True。

BFS 做法（Kahn 算法）：
  1. 建图：edges[from] = [to1, to2, ...]，同时记录每个点的入度
  2. 所有入度为 0 的节点入队（不依赖任何课的课先上）
  3. 每弹出一个节点：count++，把它指向的所有后继入度 -1
     如果哪个后继入度变成 0，入队
  4. 最后 count == numCourses → 全修完了 → True
     否则有环 → count < numCourses → False

一句话记：
  入度为 0 就入队 → 弹出一个消一条边 → 后继入度减到 0 就入队 → 数修了几门课。
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 邻接表：edges[i] = 修完 i 之后可以修的课的列表
        edges = [[] for _ in range(numCourses)]
        # 入度：in_degrees[i] = 修 i 之前必须先修多少门课
        in_degrees = [0] * numCourses

        # 建图：prereq = [课, 前置课] → 前置课 → 课
        for current_end, current_start in prerequisites:
            edges[current_start].append(current_end)
            in_degrees[current_end] += 1

        # 所有不需要前置的课（入度为 0）入队
        q_tmp = []
        for i, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                q_tmp.append(i)

        # BFS：用 head 指针模拟队列出队（避免 pop(0) 的 O(n) 开销）
        count = 0
        head = 0
        while head < len(q_tmp):
            current_lesson_idx = q_tmp[head]
            count += 1  # 修了一门课
            head += 1

            # 消边：这门课修完了，它指向的后继课入度 -1
            for son in edges[current_lesson_idx]:
                in_degrees[son] -= 1
                if in_degrees[son] == 0:  # 后继课的前置全部修完
                    q_tmp.append(son)

        # 修完的课 == 总课数 → 无环 → 能修完
        return count == numCourses


numCourses = 2
prerequisites = [[1, 0]]

prerequisites2 = [[1, 0], [0, 1]]


so = Solution()
print(so.canFinish(numCourses, prerequisites))
print(so.canFinish(numCourses, prerequisites2))

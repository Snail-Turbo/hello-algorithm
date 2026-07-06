

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        edges = [[] for _ in range(numCourses)]

        in_degrees = [0] * numCourses

        for current_end, current_start in prerequisites:

            edges[current_start].append(current_end)
            in_degrees[current_end] += 1

        q_tmp = []
        for i, in_degree in enumerate(in_degrees):  # 如果有向环图，这里in_degrees都是非0
            if in_degree == 0:
                q_tmp.append(i)

        count = 0
        head = 0
        while head < len(q_tmp):
            current_lession_idx = q_tmp[head]
            count += 1
            head += 1

            for son in edges[current_lession_idx]:
                in_degrees[son] -= 1
                if in_degrees[son] == 0:
                    q_tmp.append(son)

        return count == numCourses


numCourses = 2
prerequisites = [[1, 0]]

prerequisites2 = [[1, 0], [0, 1]]


so = Solution()
print(so.canFinish(numCourses, prerequisites))
print(so.canFinish(numCourses, prerequisites2))

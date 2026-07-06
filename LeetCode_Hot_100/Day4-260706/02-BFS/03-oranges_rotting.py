class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        len_y = len(grid)
        len_x = len(grid[0])

        dist = [[-1] * len_x for _ in range(len_y)]
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        q = []
        head = 0
        max_minutes = 0

        for y in range(len_y):
            for x in range(len_x):
                if grid[y][x] == 2:
                    q.append((y, x))
                    dist[y][x] = 0  # 进就标记 visited，多源BFS，源全为0时候

        while head < len(q):
            current_y, current_x = q[head]  # 只增不减的 queue，避免 O(n)
            head += 1

            for diff_y, diff_x in directions:
                new_y, new_x = diff_y + current_y, diff_x+current_x

                # 新的得符合数组不超限；
                # 新的需要没被提前 标记腐化过
                # 新的需要 是 需要被腐化的      【重点，不能忘记】
                if new_y not in range(len_y) or new_x not in range(len_x) or dist[new_y][new_x] != -1 or grid[new_y][new_x] != 1:
                    continue

                q.append((new_y, new_x))
                dist[new_y][new_x] = dist[current_y][current_x] + 1  # 进，就 visited，and 更新距离

                # 顺便计算 max，避免多一个 for 循环
                max_minutes = max(max_minutes, dist[new_y][new_x])

        for i in range(len_y):
            for j in range(len_x):
                if grid[i][j] == 1 and dist[i][j] == -1:
                    return -1

        return max_minutes


grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
so = Solution()
print(so.orangesRotting(grid=grid))

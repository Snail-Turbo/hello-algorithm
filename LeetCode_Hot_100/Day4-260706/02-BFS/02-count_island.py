

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        grid = [list(map(int, grid_x)) for grid_x in grid]

        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        visited = set()

        len_y, len_x = len(grid), len(grid[0])

        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        count = 0

        def bfs(y, x):
            tmp_queue = [(y, x)]
            grid[y][x] = 0

            head = 0
            while head < len(tmp_queue):
                current_y, current_x = tmp_queue[head]
                head += 1

                for diff_y, diff_x in directions:
                    new_y, new_x = current_y + diff_y, current_x + diff_x
                    if 0 <= new_y < len_y and 0 <= new_x < len_x and grid[new_y][new_x] == 1:
                        grid[new_y][new_x] = 0
                        tmp_queue.append((new_y, new_x))

        for y in range(len_y):
            for x in range(len_x):
                if grid[y][x] == 1:
                    count += 1
                    bfs(y, x)

        return count


so = Solution()
grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]

print(so.numIslands(grid))

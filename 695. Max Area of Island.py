class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        self.total = 0
        result = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.total = 0
                    self.bfs(grid, i, j)
                    result = max(result, self.total)

        return result

    def bfs(self, grid, x, y):
        self.total += 1
        grid[x][y] = 0

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                self.bfs(grid, new_x, new_y)

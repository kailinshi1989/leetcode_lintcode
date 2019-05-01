class Solution_1(object):
    def numIslands(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])

        visited = [[False for i in xrange(n)] for i in xrange(m)]
        result = 0

        for i in xrange(m):
            for j in xrange(n):
                if visited[i][j] == False and grid[i][j] == '1':
                    result += 1
                    self.bfs(grid, visited, i, j)

        return result

    def bfs(self, grid, visited, i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and visited[i][j] == False and grid[i][j] == '1':
            visited[i][j] = True
            self.bfs(grid, visited, i - 1, j)
            self.bfs(grid, visited, i + 1, j)
            self.bfs(grid, visited, i, j - 1)
            self.bfs(grid, visited, i, j + 1)


"""
Solution 2： Union & Find 解法
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        islands = set()
        self.result = 0
        self.father = {}

        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    islands.add((x, y))
                    self.result += 1
                    self.father[(x, y)] = (x, y)
                    dx = [1, -1, 0, 0]
                    dy = [0, 0, 1, -1]
                    for i in range(4):
                        new_x = x + dx[i]
                        new_y = y + dy[i]
                        if (new_x, new_y) in islands:
                            self.union((x, y), (new_x, new_y))

        return self.result

    def union(self, point, new_point):
        root = self.find(point)
        new_root = self.find(new_point)

        if root != new_root:
            self.father[root] = new_root
            self.result -= 1

    def find(self, point):
        path = []
        while point != self.father[point]:
            path.append(point)
            point = self.father[point]

        for p in path:
            self.father[p] = point
        return point
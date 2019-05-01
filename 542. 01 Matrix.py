from collections import deque


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []

        q = deque([])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = m + n

        while q:
            x, y = q.popleft()
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                    continue
                if matrix[new_x][new_y] > matrix[x][y]: # 洼地找高地
                    matrix[new_x][new_y] = matrix[x][y] + 1
                    q.append((new_x, new_y))
        return matrix
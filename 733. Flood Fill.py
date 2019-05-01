from collections import deque


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        start_color = image[sr][sc] # 只有颜色相同才变
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = deque([(sr, sc)])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while q:
            x, y = q.popleft()
            image[x][y] = newColor
            visited[x][y] = True
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and visited[new_x][new_y] == False and image[new_x][new_y] == start_color:
                    q.append((new_x, new_y))

        return image
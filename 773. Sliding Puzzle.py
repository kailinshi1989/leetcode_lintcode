class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        self.visited = {}
        target = [[1, 2, 3], [4, 5, 0]]
        x = 0
        y = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    x = i
                    y = j
                    break
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        q = [(board, x, y, 0)]

        while q:
            b, x1, y1, times = q.pop(0)
            if b == target:
                return times
            self.visited[self.convert2string(b)] = True
            for i in range(4):
                newX = x1 + dx[i]
                newY = y1 + dy[i]
                newB = [row[:] for row in b]
                if newX >= 0 and newX < 2 and newY >= 0 and newY < 3:
                    newB[x1][y1], newB[newX][newY] = newB[newX][newY], newB[
                        x1][y1]
                    b_string = self.convert2string(newB)
                    if b_string not in self.visited:
                        q.append((newB, newX, newY, times + 1))
        return -1

    def convert2string(self, board):
        result = ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                result += str(board[i][j])
        return result

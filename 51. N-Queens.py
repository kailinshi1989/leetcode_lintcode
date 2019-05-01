"""
The n-queens puzzle is the problem of placing n queens on 
an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        self.dfs(n, [])
        return self.result

    def dfs(self, n, path):
        if len(path) == n:
            self.result.append(self.draw(path))
            return
        for i in range(n):
            if self.check(path, i):
                self.dfs(n, path + [i])

    def check(self, path, n):
        cur_level = len(path)
        for i in range(len(path)):
            if path[i] == n:
                return False
            if path[i] - i == n - cur_level:
                return False
            if path[i] + i == n + cur_level:
                return False
        return True

    def draw(self, path):
        result = []
        n = len(path)
        for i in range(n):
            row = ""
            for j in range(n):
                if j != path[i]:
                    row += '.'
                else:
                    row += 'Q'
            result.append(row)
        return result
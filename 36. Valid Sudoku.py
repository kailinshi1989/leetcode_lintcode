class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set([]) for _ in xrange(9)]
        col = [set([]) for _ in xrange(9)]
        box = [set([]) for _ in xrange(9)]

        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row[i]:
                    return False
                if board[i][j] in col[j]:
                    return False
                p = i / 3 * 3 + j / 3
                if board[i][j] in box[p]:
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[p].add(board[i][j])
        return True

"""
Leetcode 85: Maximal Rectangle 的变形
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        result = 0
        hs = [0 for _ in range(n)]
        for row in matrix:
            for i in range(len(row)):
                if row[i] == '1':
                    hs[i] += 1
                else:
                    hs[i] = 0
            result = max(result, self.helper(hs))
        return result

    def helper(self, hs):
        stack = []
        hs += [-1]
        result = 0

        for i, h in enumerate(hs):
            while stack and hs[stack[-1]] > h:
                hightest_index = stack.pop()
                left_index = stack[-1] if stack else -1
                side = min((i - left_index - 1), hs[hightest_index]) # 因为是正方形，所以4条边要相等
                area = side * side
                result = max(result, area)
            stack.append(i)
        return result
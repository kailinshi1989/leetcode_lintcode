class Solution(object):
    def maximalRectangle(self, matrix):
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
        heights = [0 for _ in range(n)]
        result = 0

        for row in matrix:
            for i, n in enumerate(row):
                heights[i] = heights[i] + 1 if n == '1' else 0
            result = max(result, self.helper(heights))

        return result

    def helper(self, hs):
        result = 0
        stack = []
        hs += [-1]
        for i, h in enumerate(hs):
            while stack and hs[stack[-1]] > h:
                highest_index = stack.pop()
                left_index = stack[-1] if stack else -1
                area = (i - left_index - 1) * hs[highest_index]
                result = max(result, area)
            stack.append(i)
        return result
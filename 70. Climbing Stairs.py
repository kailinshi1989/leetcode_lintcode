class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 2:
            return n
        dp = [1, 2]
        for _ in range(n - 2):
            dp.append(dp[-2] + dp[-1])
        return dp[-1]

"""
方法二， 空间复杂度O(1)
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 2:
            return n
        a, b = 1, 1
        for i in range(2, n + 1):
            a, b = b, a + b

        return b
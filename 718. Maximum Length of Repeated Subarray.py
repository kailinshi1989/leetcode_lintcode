class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        result = 0
        m = len(A)
        n = len(B)
        dp = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                dp[i][j] = dp[i-1][j-1] + 1 if A[i-1] == B[j-1] else 0
                result = max(result, dp[i][j])
        return result
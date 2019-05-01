"""
s:    "bbbab"
dp:   [4,3,3,1,1]
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return len(s)
        dp = [1] * len(s)
        for i in xrange(1, len(s)):
            pre = dp[i]
            for j in reversed(xrange(i)):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre + 2 if j+1 <= i-1 else 2
                else:
                    dp[j] = max(dp[j], dp[j+1])
                pre = tmp
        return dp[0]

"""
二维数组dp
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        m = [[ 0 for _ in range(l)] for _ in range(l)]
        for i in reversed(range(l)):
            m[i][i] = 1
            for j in range(i+1, l):
                if s[i] == s[j]:
                    m[i][j] = m[i+1][j-1] + 2
                else:
                    m[i][j] = max(m[i+1][j], m[i][j-1])
        return m[0][l-1]
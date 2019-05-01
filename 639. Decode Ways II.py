class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        mod = 1000000007
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in xrange(1, n + 1):
            if s[i - 1] == '*':
                dp[i] = (dp[i] + 9 * dp[i - 1]) % mod
                if i >= 2:
                    if s[i - 2] == '1':
                        dp[i] = (dp[i] + 9 * dp[i - 2]) % mod
                    elif s[i - 2] == '2':
                        dp[i] = (dp[i] + 6 * dp[i - 2]) % mod
                    elif s[i - 2] == '*':
                        dp[i] = (dp[i] + 15 * dp[i - 2]) % mod
            else:
                if s[i - 1] >= '1' and s[i - 1] <= '9':
                    dp[i] = (dp[i] + dp[i - 1]) % mod
                if i >= 2:
                    if s[i - 2] == '*':
                        if s[i - 1] >= '0' and s[i - 1] <= '6':
                            dp[i] = (dp[i] + 2 * dp[i - 2]) % mod
                        elif s[i - 1] >= '7' and s[i - 1] <= '9':
                            dp[i] = (dp[i] + dp[i - 2]) % mod
                    else:
                        twoDigits = int(s[i - 2: i])
                        if twoDigits >= 10 and twoDigits <= 26:
                            dp[i] = (dp[i] + dp[i - 2]) % mod
        return dp[n]

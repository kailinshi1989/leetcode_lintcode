"""
思路：定义一个数组dp[]，dp[i]表示字符串的前i个字符能否用字典表示，
初始化dp[0]=true，i从1开始，那么对于前i+1个字符，
我们需要判断在前i个字符串中存不存在一个点j，
这个点dp[j]为true，并且[j,i]的字符串在字典中出现
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(wordDict) == 0:
            return len(s) == 0
        n = len(s)
        f = [False] * (n+1)
        f[0] = True
        maxL = max(len(word) for word in wordDict)
        for i in xrange(1, n+1):
            for j in xrange(1, min(i, maxL)+1): # j表示单词的长度 0.....j...i,即j到i的长度
                if not f[i-j]:
                    continue
                if s[i-j: i] in wordDict:
                    f[i] = True
        return f[n]



"""
方法二
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(wordDict) == 0:
            return len(s) == 0
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i): # j表示0-j的长度
                if not dp[j]:
                    continue
                if s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]

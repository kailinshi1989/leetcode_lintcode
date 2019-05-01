class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        lo = 0
        result = 0
        hash = {}
        for i in range(len(s)):
            char = s[i]
            if char in hash and hash[char] >= lo:
                lo = hash[char] + 1
            hash[char] = i
            result = max(result, i - lo + 1)
        return result


"""
Solution 2
"""
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        result = 0
        hash = {}
        tmp = ''
        for i in xrange(len(s)):
            c = s[i]
            if c in tmp:
                tmp = s[hash[c]+1:i+1]
            else:
                tmp += c
            hash[c] = i
            if len(tmp) > result:
                result = len(tmp)
        return result
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lo = 0
        hi = len(s) - 1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1
        return s

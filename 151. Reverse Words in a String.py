class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = list(s.split())
        lo = 0
        hi = len(s) - 1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1
        return ' '.join(s)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        result = strs[0]
        for str in strs:
            result = self.helper(result, str)
            if result == "":
                return result
        return result

    def helper(self, s1, s2):
        ret = ""
        p = 0
        while p < len(s1) and p < len(s2):
            if s1[p] == s2[p]:
                ret += s1[p]
                p += 1
            else:
                return ret
        return ret


"""
Solution 2
"""


class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ""
        p = 0
        minL = min(len(s) for s in strs)
        while p < minL:
            for i in xrange(1, len(strs)):
                if strs[i][p] != strs[i - 1][p]:
                    return strs[0][:p]
            p += 1
        return strs[0][:p]

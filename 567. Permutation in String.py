class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        missing = len(s1)
        hash = {}
        for c in s1:
            if c in hash:
                hash[c] += 1
            else:
                hash[c] = 1
        for i in range(len(s2)):
            c = s2[i]
            if c in hash:
                if hash[c] > 0:
                    missing -= 1
                hash[c] -= 1
            if i >= len(s1):
                last_index = i - len(s1)
                last_c = s2[last_index]
                if last_c in hash:
                    hash[last_c] += 1
                    if hash[last_c] > 0:
                        missing += 1
            if missing == 0:
                return True
        return False
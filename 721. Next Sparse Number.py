class Solution:
    """
    @param x: a number
    @return: return the next sparse number behind x
    """
    def nextSparseNum(self, x):
        # write your code here
        if x == 0:
            return 0
        s = ""
        while x > 0:
            s = str(x % 2) + s
            x /= 2
        if self.is_sparse(s):
            return int(s, 2)

        s = ['0'] + list(s)
        n = len(s)
        s[n - 1] = '1'
        last_index = n - 1
        for i in xrange(n - 2, 0, -1):
            if s[i] == '1' and s[i + 1] == '1' and s[i - 1] == '0':
                s[i - 1] = '1'
                k = i
                while k <= last_index:
                    s[k] = '0'
                    k += 1
                last_index = i - 1
        s = "".join(s)
        return int(s, 2)

    def is_sparse(self, s):
        for i in xrange(len(s)):
            if i != 0 and s[i] == '1' and s[i-1] == '1':
                return False
        return True

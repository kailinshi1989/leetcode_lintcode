class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = 1
        if x >= 0:
            result = self.helper(x)
        else:
            result = -1 * self.helper(-x)

        return 0 if result >= 1 << 31 or result < -1 << 31 else result

    def helper(self, x):
        x = list(str(x))
        lo = 0
        hi = len(x) - 1
        while lo < hi:
            x[lo], x[hi] = x[hi], x[lo]
            lo += 1
            hi -= 1
        return int(''.join(x))
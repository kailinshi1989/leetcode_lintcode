"""
超时做法
"""
class NumArray_1(object):

    def __init__(self, nums):
        lenN = len(nums)
        self.n = nums
        self.l = [None] * lenN
        if lenN != 0:
            self.l[0] = nums[0]

            for i in xrange(1, lenN):
                self.l[i] = self.l[i - 1] + nums[i]


    def update(self, i, val):
        diff = val - self.n[i]
        self.n[i] = val

        for x in xrange(i, len(self.l)):
            self.l[x] += diff


    def sumRange(self, i, j):
        if i > j or i < 0 or j < 0 or j > len(self.l):
            return 0

        if i == 0:
            return self.l[j]
        else:
            return self.l[j] - self.l[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

"""
AC: 用binary indexed tree
"""
"""
x & (-x)
-x = -x + 1
5 & -5
0101 & (1010 + 1) 
==> 0101 & 1011
==> 0001 ==> 2
"""


class NumArray_2(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.btree = [0 for _ in range(self.n + 1)]
        for i in range(self.n):
            x = i + 1
            while x <= self.n:
                self.btree[x] += nums[i]
                x += self.lowbit(x)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        diff = val - (self.sumTree(i) - self.sumTree(i - 1))
        i += 1
        while i <= self.n:
            self.btree[i] += diff
            i += self.lowbit(i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumTree(j) - self.sumTree(i - 1)

    def sumTree(self, i):
        sum = 0
        i += 1
        while i > 0:
            sum += self.btree[i]
            i -= self.lowbit(i)
        return sum

    def lowbit(self, x):
        return x & (-x)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
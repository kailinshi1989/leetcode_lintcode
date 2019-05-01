class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        [n1, n2, n3, n4]
        => [1, n1, n1*n2, n1*n2*n3]
        => [n2*n3*n4, n1*n3*n4, n1*n2*n4, n1*n2*n3]
        """
        p = 1
        result = []
        for i in xrange(len(nums)):
            result.append(p)
            p *= nums[i]
        p = 1
        for i in xrange(len(result) - 1, -1, -1):
            result[i] *= p
            p *= nums[i]
        return result

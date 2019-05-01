class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        hash = {}
        hash[0] = -1
        total = 0
        result = 0
        for i in xrange(len(nums)):
            n = nums[i]
            if n == 0:
                total -= 1
            else:
                total += 1
            if total in hash:
                result = max(result, i - hash[total])
            else:
                hash[total] = i
        return result

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        if nums is None or len(nums) == 0:
            return result
        for i in xrange(len(nums)):
            if nums[i] != nums[result]:
                result += 1
                nums[result] = nums[i]
        return result + 1



"""
另一种方法
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        lo = 1
        hi = 1
        cur = nums[0]
        while hi < len(nums):
            while hi < len(nums) and nums[hi] == cur:
                hi += 1
            if hi < len(nums):
                cur = nums[hi]
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi += 1
        return lo

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []
        for i in xrange(len(nums)):
            p = abs(nums[i]) - 1
            nums[p] = nums[p] if nums[p] < 0 else -nums[p]

        result = []
        for i in xrange(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result

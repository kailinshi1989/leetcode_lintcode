class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        lo = 0
        hi = len(nums) - 1
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid
        return min(nums[lo], nums[hi])
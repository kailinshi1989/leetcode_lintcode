class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        result = 0
        for i in range(len(nums) - 2):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total < target:
                    result += hi - lo
                    lo += 1
                else:
                    hi -= 1
        return result
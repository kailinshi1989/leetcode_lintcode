class Solution:
    """
    @param nums: the array
    @param target: the target
    @return: the number of subsets which meet the following conditions
    """
    def subsetWithTarget(self, nums, target):
        # Write you code here
        if nums is None or len(nums) == 0:
            return 0
        nums = sorted(nums)
        result = 0
        hi = len(nums) - 1
        for i in xrange(len(nums)):
            while hi >= i and nums[i] + nums[hi] >= target:
                hi -= 1
            if hi >= i:
                result += 1 << (hi - i)
        return result

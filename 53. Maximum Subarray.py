class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return
        minS, result, sum = 0, nums[0], 0
        for num in nums:
            sum += num
            result = max(result, sum - minS)
            minS = min(minS, sum)
        return result



"""
方法二: 不定义result
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = None
        minTotal = 0
        total = 0
        for num in nums:
            total += num
            result = total - minTotal if result is None else max(
                result, total - minTotal)
            minTotal = min(total, minTotal)
        return result
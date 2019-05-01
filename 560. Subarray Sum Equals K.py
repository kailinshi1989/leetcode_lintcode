class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash = {}
        total = 0
        result = 0
        hash[0] = 1
        for num in nums:
            total += num
            if total - k in hash:
                result += hash[total - k]
            if total in hash:
                hash[total] += 1
            else:
                hash[total] = 1
        return result

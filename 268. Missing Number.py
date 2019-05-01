class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        for num in nums:
            hash[num] = True

        for i in range(len(nums) + 1):
            if i not in hash:
                return i
        return -1


"""
用等差数列的求和公式求出0到n之间所有的数字之和
然后再遍历数组算出给定数字的累积和，然后做减法，差值就是丢失的那个数字
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for num in nums:
            total += num

        n = len(nums)

        return n * (n + 1) / 2 - total

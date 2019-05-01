"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        lo, hi = 0, 0
        while hi < len(nums):
            if nums[hi] != 0:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
            hi += 1



"""
双指针
数字0一个指针
非0数字一个指针
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return []
        zero_p = 0
        num_p = 0

        while num_p < len(nums) and zero_p < len(nums):
            while zero_p < len(nums) and nums[zero_p] != 0:
                zero_p += 1
            while num_p < len(nums) and nums[num_p] == 0:
                num_p += 1
            if zero_p < num_p and num_p < len(nums) and zero_p < len(nums):
                nums[zero_p], nums[num_p] = nums[num_p], nums[zero_p]
                zero_p += 1
                num_p += 1
            else:
                num_p += 1

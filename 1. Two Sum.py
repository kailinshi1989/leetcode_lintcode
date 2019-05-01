class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            find_num = target - nums[i]
            if find_num in hash:
                return [hash[find_num][0], i]

            if nums[i] in hash:
                hash[nums[i]].append(i)
            else:
                hash[nums[i]] = [i]
        return [-1, -1]
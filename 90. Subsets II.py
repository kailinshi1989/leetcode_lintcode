"""
Given a collection of integers that might contain duplicates, nums, 
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return
        self.result = []
        nums = sorted(nums)
        self.helper(nums, [])
        return self.result

    def helper(self, nums, tmp):
        self.result.append(tmp[:])
        for i in xrange(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            self.helper(nums[i + 1:], tmp + [nums[i]])



"""
方法二
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        self.result = []
        visited = [False for _ in range(len(nums))]
        self.dfs(nums, [], 0, visited)
        return self.result

    def dfs(self, nums, path, index, visited):
        self.result.append(path[:])
        for i in range(index, len(nums)):
            if i == 0 or nums[i] != nums[i - 1] or visited[i - 1] == True:
                visited[i] = True
                self.dfs(nums, path + [nums[i]], i + 1, visited)
                visited[i] = False

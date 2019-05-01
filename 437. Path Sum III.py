# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        if root is None:
            return self.result
        self.dfs(root, sum, [], 0)
        return self.result

    def dfs(self, root, target, tmp, totalSum):
        if root is None:
            return
        totalSum += root.val
        tmp.append(root.val)

        if totalSum == target:
            self.result += 1

        tmpSum = totalSum
        if len(tmp) > 1:
            for i in range(len(tmp) - 1):
                tmpSum -= tmp[i]
                if tmpSum == target:
                    self.result += 1

        self.dfs(root.left, target, tmp[:], totalSum)
        self.dfs(root.right, target, tmp[:], totalSum)

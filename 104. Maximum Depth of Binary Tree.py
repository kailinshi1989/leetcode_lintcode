# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)

        return max(left, right) + 1
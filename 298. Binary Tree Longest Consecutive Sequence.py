# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.result = 1
        self.helper(root, 1)
        return self.result

    def helper(self, root, cur):
        if root.left:
            if root.val == root.left.val - 1:
                self.result = max(self.result, cur + 1)
                self.helper(root.left, cur + 1)
            else:
                self.helper(root.left, 1)

        if root.right:
            if root.val == root.right.val - 1:
                self.result = max(self.result, cur + 1)
                self.helper(root.right, cur + 1)
            else:
                self.helper(root.right, 1)

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
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        self.result = []
        self.helper(root, sum, [root.val])
        return self.result
    
    def helper(self, root, target, path):
        if root.val == target and root.left is None and root.right is None:
            self.result.append(path[:])
            return
        if root.left:
            self.helper(root.left, target - root.val, path + [root.left.val])
        if root.right:
            self.helper(root.right, target - root.val, path + [root.right.val])
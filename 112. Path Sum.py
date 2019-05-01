"""
BFS 解法
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return
        q = deque([(root, sum)])

        while q:
            node, remaining = q.popleft()
            if node.val == remaining and node.left is None and node.right is None:
                return True
            remaining -= node.val
            if node.left:
                q.append((node.left, remaining))
            if node.right:
                q.append((node.right, remaining))
        return False



"""
DFS解法
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)

        return left or right
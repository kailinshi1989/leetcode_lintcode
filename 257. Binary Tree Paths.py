# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        result = []
        if root is None:
            return result
        self.dfs(root, str(root.val), result)
        return result

    def dfs(self, root, path, result):
        if root is None:
            return
        if root.left is None and root.right is None:
            result.append(path)
        if root.left:
            self.dfs(root.left, path + '->' + str(root.left.val), result)
        if root.right:
            self.dfs(root.right, path + '->' + str(root.right.val), result)



"""
另一种方法
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        if root is None:
            return self.result
        self.helper(root, '')
        return self.result

    def helper(self, root, path):
        path += str(root.val) + '->'
        if root.left is None and root.right is None:
            path = path[:-2]
            self.result.append(path)
            return

        if root.left:
            self.helper(root.left, path)
        if root.right:
            self.helper(root.right, path)

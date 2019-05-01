# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
方法1：recursion
"""


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None or root.right is None:
                root = root.left if root.left else root.right
            else:
                replace_node = root.right
                while replace_node.left:
                    replace_node = replace_node.left
                root.val = replace_node.val
                root.right = self.deleteNode(root.right, replace_node.val)
        return root


"""
方法2：iteration
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        pre, cur = None, root
        while cur:
            if cur.val == key:
                break
            pre = cur
            if cur.val > key:
                cur = cur.left
            else:
                cur = cur.right
        if cur is None:
            return root
        if pre is None:
            return self.helper(cur)
        if pre.left and pre.left.val == key:
            pre.left = self.helper(cur)
        else:
            pre.right = self.helper(cur)
        return root

    def helper(self, node):
        if node.left is None and node.right is None:
            return None
        if node.left is None or node.right is None:
            return node.left if node.left else node.right
        pre = node
        cur = node.right
        while cur.left:
            pre = cur
            cur = cur.left
        node.val = cur.val
        if pre == node:
            pre.right = cur.right
        else:
            pre.left = cur.right
        return node

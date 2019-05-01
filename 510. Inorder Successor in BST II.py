"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""


class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        result = None
        if node.right:
            result = node.right
            while result and result.left:
                result = result.left
        else:
            result = node.parent
            while result and result.val < node.val:
                result = result.parent
        return result
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from collections import deque


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):
        # write your code here
        if root is None:
            return ""
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append('#')
        return ','.join(result)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):
        # write your code here
        if data == '':
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if nodes[i] != '#':
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1
            if nodes[i] != '#':
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
        return root

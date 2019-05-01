"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        self.stack = []
        dummyNode = Node(-1, None, None)
        head = dummyNode
        self.helper(root)
        for n in self.stack:
            node = Node(n, None, None)
            head.right = node
            node.left = head
            head = node
        head.right = dummyNode.right
        dummyNode.right.left = head
        return dummyNode.right

    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        self.stack.append(root.val)
        self.helper(root.right)


"""
Solution 2
"""


class Solution2(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        pre = None
        cur = root
        stack = []
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                cur = node.right
                if pre:
                    pre.right = node
                    node.left = pre
                else:
                    head = node
                pre = node
        pre.right = head
        head.left = pre
        return head


"""
Solution 3
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution3(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        dummyNode = Node(-1, None, None)
        head = dummyNode
        cur = root
        stack = []
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                head.right = node
                node.left = head
                cur = node.right
                head = node
        head.right = dummyNode.right
        dummyNode.right.left = head
        return dummyNode.right



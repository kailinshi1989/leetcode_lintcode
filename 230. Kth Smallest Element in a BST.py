"""
中序遍历
当遍历过的个数等于k的时候，赋值result，返回
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        self.result = root.val
        self.count = 0
        self.dfs(root, k)
        return self.result

    def dfs(self, root, k):
        if root is None or self.count >= k:
            return
        self.dfs(root.left, k)
        self.count += 1
        if self.count == k:
            self.result = root.val
        self.dfs(root.right, k)



"""
方法二
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        dummyNode = TreeNode(0)
        dummyNode.right = root
        stack = [dummyNode]
        for i in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if len(stack) == 0:
                break
        return stack[-1].val
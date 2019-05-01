"""
所以pre[0]是根节点，也就是post[-1];
post[-2]时候右子树的根节点，因此在前序遍历中找到post[-2]的位置idx就能分开两棵子树。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre or not post:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        idx = pre.index(post[-2])
        root.left = self.constructFromPrePost(pre[1:idx], post[:idx - 1])
        root.right = self.constructFromPrePost(pre[idx:], post[idx - 1:-1])
        return root
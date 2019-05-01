# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q = [(root, 0)]
        result = {}
        while q:
            node, cur = q.pop(0)
            if node:
                if cur in result:
                    result[cur].append(node.val)
                else:
                    result[cur] = [node.val]
                q.append((node.left, cur - 1))
                q.append((node.right, cur + 1))
        result = sorted(result.items(), key=lambda item: item[0])
        return [ret[1] for ret in result]


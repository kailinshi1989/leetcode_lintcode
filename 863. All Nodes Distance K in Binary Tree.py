"""
题意是让我们在一颗二叉树中，给定节点 Target, 寻找和target节点距离 为 K的所有节点，
我们可以把这颗树看成一个无向图， 没有顺序就意味着，二叉树的旁边的指节也是可以算距离的。 
我们可以先把二叉树转化为无向图，再在图中进行 BFS 搜索应该就可以得到答案。 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.hash = defaultdict(list)
        self.helper(None, root)
        result = []
        q = deque([(target.val, 0, None)])
        while q:
            n, level, parent = q.popleft()
            if level < K:
                for child in self.hash[n]:
                    if parent is not None and child == parent:
                        continue
                    q.append((child, level + 1, n))
            else:
                result.append(n)
        return result

    def helper(self, parent, child):
        if parent and child:
            self.hash[parent.val].append(child.val)
            self.hash[child.val].append(parent.val)
        if child.left:
            self.helper(child, child.left)
        if child.right:
            self.helper(child, child.right)

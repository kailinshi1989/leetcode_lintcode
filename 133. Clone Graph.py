"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if node is None:
            return node
        hash = {}
        nodes = set()
        q = deque([node])
        root = node
        while q:
            node = q.popleft()
            nodes.add(node)
            for neighbor in node.neighbors:
                if neighbor not in nodes:
                    q.append(neighbor)

        for node in nodes:
            hash[node] = Node(node.val, [])

        for node in nodes:
            newNode = hash[node]
            for neighbor in node.neighbors:
                newNode.neighbors.append(hash[neighbor])

        return hash[root]

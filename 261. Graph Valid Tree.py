from collections import defaultdict
from Queue import Queue


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) + 1 != n:
            return False
        hash = defaultdict(list)
        visited = {}
        for edge in edges:
            hash[edge[0]].append(edge[1])
            hash[edge[1]].append(edge[0])
        q = Queue()
        q.put(0)
        while not q.empty():
            num = q.get()
            visited[num] = True
            for child in hash[num]:
                if child not in visited:
                    q.put(child)
        return len(visited) == n


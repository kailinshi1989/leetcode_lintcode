from collections import defaultdict, deque


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        hash = defaultdict(list)
        nums = set([])

        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            hash[n1].append(n2)
            hash[n2].append(n1)

        result = 0
        for num in range(n):
            if num not in nums:
                result += 1
                q = deque([num])
                while q:
                    cur = q.popleft()
                    nums.add(cur)
                    for child in hash[cur]:
                        if child not in nums:
                            q.append(child)
        return result



"""
Union & Find方法
"""
from collections import defaultdict


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        hash = defaultdict(list)
        nums = set([])
        self.father = {}

        self.result = n

        # 每个点的根都是自己
        for i in range(n):
            self.father[i] = i

        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            self.union(n1, n2)

        return self.result

    def union(self, n1, n2):
        n1_father = self.find(n1)
        n2_father = self.find(n2)
        if n1_father != n2_father:
            self.father[n1_father] = n2_father
            self.result -= 1

    def find(self, n):
        path = []
        while n != self.father[n]:
            path.append(n)
            n = self.father[n]

        for num in path:
            self.father[num] = n

        return n

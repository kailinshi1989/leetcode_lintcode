from collections import defaultdict


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        num_of_prep = defaultdict(int)
        following_nums = defaultdict(list)
        points = set()

        for seq in seqs:
            points |= set(seq)
            for i in range(len(seq)):
                if i == 0:
                    num_of_prep[seq[i]] += 0
                else:
                    num_of_prep[seq[i]] += 1
                    following_nums[seq[i - 1]].append(seq[i])

        q = []
        for num in num_of_prep:
            if num_of_prep[num] == 0:
                q.append(num)

        result = []
        while len(q):
            if len(q) > 1:
                return False
            point = q.pop(0)
            result.append(point)
            for child in following_nums[point]:
                num_of_prep[child] -= 1
                if num_of_prep[child] == 0:
                    q.append(child)

        if len(result) == len(points) and result == org:
            return True
        return False

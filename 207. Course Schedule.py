class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        nun_of_prep = [0 for _ in range(numCourses)]
        following_course = [[] for _ in range(numCourses)]

        for pair in prerequisites:
            c1 = pair[0]
            c2 = pair[1]
            nun_of_prep[c1] += 1
            following_course[c2].append(c1)

        q = []
        for i in range(len(nun_of_prep)):
            if nun_of_prep[i] == 0:
                q.append(i)

        result = 0
        while q:
            course = q.pop(0)
            result += 1
            for child in following_course[course]:
                nun_of_prep[child] -= 1
                if nun_of_prep[child] == 0:
                    q.append(child)

        return result == numCourses

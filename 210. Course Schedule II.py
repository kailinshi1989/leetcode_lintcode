class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        num_of_prep = [0 for _ in range(numCourses)]
        following_course = [[] for _ in range(numCourses)]

        for pair in prerequisites:
            c0 = pair[0]
            c1 = pair[1]
            num_of_prep[c0] += 1
            following_course[c1].append(c0)

        q = []
        for i in range(numCourses):
            if num_of_prep[i] == 0:
                q.append(i)

        result = []
        while q:
            course = q.pop(0)
            result.append(course)
            for child in following_course[course]:
                num_of_prep[child] -= 1
                if num_of_prep[child] == 0:
                    q.append(child)

        return result if len(result) == numCourses else []
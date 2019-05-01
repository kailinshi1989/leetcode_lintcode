"""
方法一：不用if的方法
"""
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        i = 1
        p3 = 1
        p5 = 1

        while i <= n:
            while i <= n and i < p3 * 3 and i < p5 * 5:
                result.append(str(i))
                i += 1

            if i <= n and p3 * 3 == p5 * 5:
                result.append("FizzBuzz")
                p3 += 1
                p5 += 1
                i += 1
                continue

            while i <= n and i >= p3 * 3:
                result.append("Fizz")
                p3 += 1
                i += 1

            while i <= n and i >= p5 * 5:
                result.append("Buzz")
                p5 += 1
                i += 1

        return result



"""
方法二： 常规方法
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        i = 1
        while i <= n:
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 5 == 0:
                result.append("Buzz")
            elif i % 3 == 0:
                result.append("Fizz")
            else:
                result.append(str(i))
            i += 1
        return result
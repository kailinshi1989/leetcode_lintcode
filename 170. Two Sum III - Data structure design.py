class TwoSum(object):
    def __init__(self):
        self.map = {}

    def add(self, number):
        if number in self.map:
            self.map[number] += 1
        else:
            self.map[number] = 1

    def find(self, value):
        for number in self.map:
            if value - number in self.map and (value - number != number
                                               or self.map[number] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

"""
精简版
"""
class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number in self.hash:
            self.hash[number] += 1
        else:
            self.hash[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.hash:
            target = value - num
            if target == num and self.hash[num] > 1:
                return True
            elif target in self.hash and target != num:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
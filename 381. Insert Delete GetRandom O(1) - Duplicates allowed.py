class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num2index = {}
        self.index2num = {}
        self.n = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        flag = not val in self.num2index
        if flag:
            self.num2index[val] = set()
        self.num2index[val].add(self.n)
        self.index2num[self.n] = val
        self.n += 1
        return flag

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.num2index:
            return False
        val_index = self.num2index[val].pop()
        if len(self.num2index[val]) == 0:
            del (self.num2index[val])
        last_val = self.index2num.pop(self.n - 1)
        if val_index != self.n - 1:
            self.num2index[last_val].remove(self.n - 1)
            self.num2index[last_val].add(val_index)
            self.index2num[val_index] = last_val
        self.n -= 1
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return self.index2num[random.randint(0, self.n - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
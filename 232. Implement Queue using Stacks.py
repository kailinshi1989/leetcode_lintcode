class MyQueue1(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        item = self.stack1.pop()
        self.stack1, self.stack2 = sorted(self.stack2), self.stack1
        return item

    def peek(self):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        item = self.stack2[-1]
        # for x in sorted(self.stack2):
        #     print x
        self.stack1, self.stack2 = sorted(self.stack2), self.stack1
        return item

    def empty(self):
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
方法2:
只要stack2不为空，那pop和peek操作都在stack2中进行，因为stack2已经是倒序了
"""
class MyQueue2(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        self.helper()
        return self.stack2.pop()

    def peek(self):
        self.helper()
        return self.stack2[-1]

    def empty(self):
        return len(self.stack1) + len(self.stack2) == 0

    def helper(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
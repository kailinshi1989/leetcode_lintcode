class doubleLinkedNode(object):
    def __init__(self, key=None, val=None, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.key2node = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        self.remove(node)
        self.setHead(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key2node:
            node = self.key2node[key]
            node.val = value
            self.remove(node)
        else:
            node = doubleLinkedNode(key, value)
            if len(self.key2node) >= self.capacity:
                del (self.key2node[self.tail.key]) # 要先删除 tail，才能加新的 node
                self.remove(self.tail)
            self.key2node[key] = node
        self.setHead(node)

    def remove(self, node):
        if node.pre:
            node.pre.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.pre = node.pre
        else:
            self.tail = node.pre

    def setHead(self, node):
        node.next = self.head
        node.pre = None

        if self.head:
            self.head.pre = node
        self.head = node

        if self.tail is None:
            self.tail = self.head


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
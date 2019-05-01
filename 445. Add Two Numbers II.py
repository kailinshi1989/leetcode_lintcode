# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        dummyNode = ListNode(-1)
        head = dummyNode
        total = 0
        while l1 or l2 or total:
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            head.next = ListNode(total % 10)
            head = head.next
            total /= 10
        return self.reverse(dummyNode.next)

    def reverse(self, root):
        if root is None:
            return

        cur = root
        head = root
        while cur.next:
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = head
            head = tmp
        return head



"""
方法二： 不翻转列表，直接求和
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.helper(l1)
        n2 = self.helper(l2)
        n = n1 + n2
        n = list(str(n))
        dummyNode = ListNode(-1)
        head = dummyNode
        for i in range(len(n)):
            head.next = ListNode(n[i])
            head = head.next
        return dummyNode.next

    def helper(self, node):
        total = 0
        while node:
            total = 10 * total + int(node.val)
            node = node.next
        return total
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head
        loHead = ListNode(-1)
        loTail = loHead
        hiHead = ListNode(-1)
        hiTail = hiHead

        while head:
            if head.val < x:
                loTail.next = head
                loTail = loTail.next
            else:
                hiTail.next = head
                hiTail = hiTail.next
            head = head.next

        hiTail.next = None
        loTail.next = hiHead.next
        return loHead.next

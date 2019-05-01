# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        dummyHead = ListNode(-1)
        dummyHead.next = head
        curValue = head.val
        lo = head
        hi = lo
        while hi:
            while hi and hi.val == curValue:
                hi = hi.next
            if hi:
                curValue = hi.val
                lo.next = hi
                lo = lo.next
                hi = hi.next
        lo.next = None
        return dummyHead.next
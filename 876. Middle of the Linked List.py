# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        slow = head
        fast = slow.next
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return slow

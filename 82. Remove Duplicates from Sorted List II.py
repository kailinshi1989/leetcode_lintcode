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
        dummyNode = ListNode(-1)
        dummyNode.next = head
        parentNode = dummyNode
        curNode = head
        curVal = None
        while curNode and curNode.next:
            if curNode.val == curNode.next.val:
                curVal = curNode.val
                while curNode and curNode.val == curVal:
                    curNode = curNode.next
                parentNode.next = curNode
            else:
                curNode = curNode.next
                parentNode = parentNode.next
        return dummyNode.next

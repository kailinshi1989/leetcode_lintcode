# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)

        slow = head
        fast = head.next

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None  # 把链表断开
        midNode = TreeNode(mid.val)

        midNode.left = self.sortedListToBST(head)
        midNode.right = self.sortedListToBST(mid.next)

        return midNode

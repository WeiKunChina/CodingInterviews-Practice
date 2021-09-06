# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, current = None, head
        while current:
            tmp = current.next
            current.next = pre
            pre = current
            current = tmp
        return pre

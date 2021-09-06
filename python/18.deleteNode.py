# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        找到前驱节点和后置节点，pre.next = cur.next 即刻删除当前节点
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head.val == val:
            return head.next
        pre, current = head, head.next
        while current and current.val != val:
            pre, current = current, current.next
        if current:
            pre.next = current.next
        return head

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoListsRecursion(self, l1, l2):
        """
        递归
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoListsRecursion(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecursion(l1, l2.next)
            return l2

    def mergeTwoLists(self, l1, l2):
        """
        递归
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
            result = result.next
        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        if l1 is not None:
            result.next = l1
        else:
            result.next = l2
        return dummy.next

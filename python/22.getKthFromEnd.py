# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEndDirect(self, head, k):
        """
        顺序查找，假设当前链表的长度为 n，则我们知道链表的倒数第 k 个节点即为正数第 n−k 个节点，此时我们只需要顺序遍历到链表的第 n - k 个节点即为倒数第 k 个节点。
        我们首先求出链表的长度 n，然后顺序遍历到链表的第 n - k 个节点返回即可。
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node, n = head, 0
        while node:
            node = node.next
            n += 1

        node = head
        for _ in range(n - k):
            node = node.next
        return node

    def getKthFromEnd(self, head, k):
        """
        快慢指针的思想。我们将第一个指针 fast 指向链表的第 k + 1个节点，第二个指针 slow 指向链表的第一个节点，此时指针 fast 与 slow 二者之间刚好间隔 k 个节点。
        此时两个指针同步向后走，当第一个指针 fast 走到链表的尾部空节点时，则此时 slow 指针刚好指向链表的倒数第k个节点。
        :param head:
        :param k:
        :return:
        """
        fast, slow = head, head
        while fast and k > 0:
            fast, k = fast.next, k - 1
        while fast:
            fast, slow = fast.next, slow.next

        return slow

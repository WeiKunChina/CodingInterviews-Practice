# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        双指针的解法:
        分别构造 2 个指针去遍历 2 个链表，无论哪个指针到尾部时，让其重新回到对方的头部，最终会在第一个公共节点相遇，如果没有，则会在 null 处相遇
        时间复杂度：设 A 链表非公共长度为 m，B 链表非公共长度为 n，公共部分为 b，则复杂度为 O(m+n+b)
        空间复杂度：O(1)
        :param headA:
        :param headB:
        :return:
        """
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

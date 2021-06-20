
#方法一：小节点置前
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        node = ListNode(None, None)
        node.next = head
        head = node

        pre = head
        while pre.next != None and pre.next.val < x:
            pre = pre.next
        p = pre

        while p.next != None:
            if p.next.val < x:
                node = p.next
                p.next = p.next.next
                node.next = pre.next
                pre.next = node
                pre = pre.next
            else:
                p = p.next

        return head.next

#方法二：两个链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        node = ListNode(None, None)
        head_s = node
        node = ListNode(None, None)
        head_l = node

        ps = head_s
        pl = head_l

        p = head
        while p != None:
            if p.val < x:
                ps.next = p
                ps = ps.next
            else:
                pl.next = p
                pl = pl.next

            p = p.next

        ps.next = None
        pl.next = None
        ps.next = head_l.next

        return head_s.next


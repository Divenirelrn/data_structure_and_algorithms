# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        p = res

        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val <= p2.val:
                node = ListNode(p1.val)
                p1 = p1.next
            else:
                node = ListNode(p2.val)
                p2 = p2.next

            p.next = node
            p = p.next

        while p1:
            node = ListNode(p1.val)
            p.next = node
            p = p.next

            p1 = p1.next

        while p2:
            node = ListNode(p2.val)
            p.next = node
            p = p.next

            p2 = p2.next

        return res.next
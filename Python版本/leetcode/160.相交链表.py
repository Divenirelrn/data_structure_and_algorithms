# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        p1, p2 = headA, headB
        while p1 or p2:
            if p1 == p2:
                return p1

            if hasattr(p1, "arrival") and p1.arrival == 'B':
                return p1

            if hasattr(p2, "arrival") and p2.arrival == 'A':
                return p2

            if p1:
                p1.arrival = 'A'
                p1 = p1.next

            if p2:
                p2.arrival = 'B'
                p2 = p2.next

        return None
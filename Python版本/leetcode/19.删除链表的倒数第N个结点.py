
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        s = f = head

        for i in range(n+1):
            f = f.next
            if not f:
                if i < n:
                    head = head.next
                else:
                    head.next = head.next.next
                return head

        while f:
            s = s.next
            f = f.next

        s.next = s.next.next

        return head
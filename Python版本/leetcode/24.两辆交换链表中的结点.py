
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head

        node = ListNode(None)
        node.next = head
        head = node

        s = f = head
        f = f.next
        f = f.next
        while f:
            s.next.next = f.next
            f.next = s.next
            s.next = f
            f = f.next

            s = s.next
            s = s.next

            f = f.next
            if not f:
                break
            f = f.next

        return head.next
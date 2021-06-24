# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        node = ListNode(None, None)
        node.next = head
        head = node

        p = head
        idx = 1

        while p != None:
            if idx == left:
                l_pre = p
            if idx == right:
                r = p.next
                break

            idx += 1
            p = p.next

        while l_pre.next != r:
            p = l_pre.next
            l_pre.next = l_pre.next.next
            p.next = r.next
            r.next = p

        return head.next

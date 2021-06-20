
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        node = ListNode(None, None)
        node.next = head
        head = node

        pre = head
        p = head.next
        while p.next != None:
            if p.next.val != p.val:
                pre.next = p
                pre = pre.next

            p = p.next

        pre.next = p

        return head.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return

        # Get the middle node
        slow = head
        fast = head

        while fast:
            fast = fast.next

            if fast and fast.next:
                fast = fast.next
                slow = slow.next

        # Split linkList
        head2 = slow.next
        slow.next = None

        # Reverse head2
        slow = None
        cur = head2
        fast = cur.next

        while cur:
            cur.next = slow
            slow = cur
            cur = fast
            fast = cur and cur.next

        # Merge listNode
        cur = head
        fast = slow.next

        while slow:
            slow.next = cur.next
            cur.next = slow
            cur = cur.next.next

            slow = fast
            fast = slow and slow.next










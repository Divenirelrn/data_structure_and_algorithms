
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        flag = 0
        while fast:
            fast = fast.next

            if fast == slow:
                flag = 1
                break

            fast = fast and fast.next
            slow = slow.next

        if not flag:
            return None

        ptr = head
        slow = slow.next
        while ptr != slow:
            slow = slow.next
            ptr = ptr.next

        return slow
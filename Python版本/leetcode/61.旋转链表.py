# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head

        tail = head
        n = 1
        while tail.next != None:
            tail = tail.next
            n += 1

        tail.next = head

        head_pos = k % n
        for _ in range(n - head_pos - 1):
            head = head.next

        tail = head
        head = head.next
        tail.next = None

        return head


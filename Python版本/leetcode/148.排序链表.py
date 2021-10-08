# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left, right):
        head = ListNode(None)
        p, p1, p2 = head, left, right
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next

            p = p.next

        if p1:
            p.next = p1
        elif p2:
            p.next = p2

        return head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        dummyNode = ListNode(None)
        dummyNode.next = head
        head = dummyNode

        size = 1
        while size < n:
            prev, cur = head, head.next
            while cur:
                left = cur
                for _ in range(size - 1):
                    if cur.next:
                        cur = cur.next
                    else:
                        break
                right = cur.next
                cur.next = None
                cur = right

                for _ in range(size - 1):
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break

                succ = None
                if cur:
                    succ = cur.next
                    cur.next = None

                merged = self.merge(left, right)
                prev.next = merged
                while prev.next:
                    prev = prev.next

                cur = succ

            size <<= 1

        return head.next
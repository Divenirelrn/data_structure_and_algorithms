# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        dummyNode = ListNode(None)
        dummyNode.next = head
        head = dummyNode

        lastSorted = head.next
        node = head.next.next
        while node:
            if node.val >= lastSorted.val:
                lastSorted = node
                node = node.next
            else:
                # find insert index
                p = head
                while p.next.val < node.val:
                    p = p.next

                # delete and insert
                lastSorted.next = node.next
                node.next = p.next
                p.next = node

                node = lastSorted.next

        return head.next



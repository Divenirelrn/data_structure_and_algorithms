
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
        flag = 0

        while p.next != None:
            if p.next.val != p.val:
                if flag == 0:
                    pre = pre.next
                else:
                    pre.next = p.next
                    flag = 0
            else:
                flag = 1
            p = p.next

        if flag == 1:
            pre.next = p.next

        return head.next

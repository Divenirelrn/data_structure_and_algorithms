# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h1 = l1
        h2 = l2

        res = ListNode()
        tail = res
        carry = 0
        while(h1 or h2):
            num1 = h1.val if h1 else 0
            num2 = h2.val if h2 else 0

            s = num1 + num2 + carry
            if s < 10:
                node = ListNode(s)
                carry = 0
            else:
                node = ListNode(s % 10)
                carry = 1

            tail.next = node
            tail = node

            h1 = h1.next if h1 else h1
            h2 = h2.next if h2 else h2

        if carry == 1:
            node = ListNode(1)
            tail.next = node
            tail = node

        return res.next
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow = pHead
        fast = pHead

        while fast:
            slow = slow.next
            if not fast.next:
                return None
            fast = fast.next.next
            if fast == slow:
                ptr = pHead
                while ptr != slow:
                    slow = slow.next
                    ptr = ptr.next

                return ptr

        return None


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None

        pre = None
        cur = pHead
        post = None
        while cur:
            post = cur.next
            cur.next = pre

            pre = cur
            cur = post

        return pre
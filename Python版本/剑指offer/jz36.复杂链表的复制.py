# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None

        vHead = RandomListNode(pHead.label)
        hashT = dict()
        hashT[pHead] = vHead

        p = pHead
        while p:
            if not p.next:
                hashT[p].next = None
            else:
                if p.next not in hashT:
                    hashT[p.next] = RandomListNode(p.next.label)

                hashT[p].next = hashT[p.next]

            if not p.random:
                hashT[p].random = None
            else:
                if p.random not in hashT:
                    hashT[p.random] = RandomListNode(p.random.label)

                hashT[p].random = hashT[p.random]

            p = p.next

        return vHead






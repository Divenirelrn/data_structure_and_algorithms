# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            n = n & 0xffffffff

        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1

        return count


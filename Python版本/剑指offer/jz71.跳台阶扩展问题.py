# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1

        a2 = 2
        for i in range(3, number + 1):
            a2 = a2 + a2

        return a2

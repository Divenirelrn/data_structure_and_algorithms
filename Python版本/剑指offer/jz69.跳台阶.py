# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1

        a1 = 1
        a2 = 2

        for i in range(3, number + 1):
            a2, a1 = a1 + a2, a2

        return a2
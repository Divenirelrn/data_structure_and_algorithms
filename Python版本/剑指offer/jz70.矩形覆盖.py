# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1

        a1, a2 = 1, 2
        for _ in range(3, number + 1):
            a2, a1 = a1 + a2, a2

        return a2
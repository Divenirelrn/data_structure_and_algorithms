# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 1 or n == 2:
            return 1

        a0 = 1
        a1 = 1

        for i in range(2, n):
            a1, a0 = a0 + a1, a1

        return a1
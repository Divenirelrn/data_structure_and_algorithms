# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1

        def pow(n):
            if n == 1:
                return base

            if n % 2 == 0:
                return pow(n // 2) * pow(n // 2)
            else:
                return pow(n // 2) * pow(n // 2) * base

        return pow(exponent) if exponent > 0 else 1 / pow(-exponent)


#方法二：位运算
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1

        flag = 0
        if exponent < 0:
            exponent = - exponent
            flag = 1

        ans = 1.0
        while exponent > 0:
            if exponent % 2 == 1:
                ans *= base

            base = base * base
            exponent //= 2

        return ans if flag == 0 else 1 / ans

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number long长整型
# @return long长整型
#
class Solution:
    def cutRope(self, number: int) -> int:
        # write code here
        def pow3(n):
            if n == 0:
                return 1
            if n == 1:
                return 3

            half = pow3(n // 2)
            if n % 2 == 0:
                return half * half % 998244353
            else:
                return 3 * half * half % 998244353

        if number == 2:
            return 1
        if number == 3:
            return 2

        count = number // 3
        if number % 3 == 0:
            return pow3(count) % 998244353
        elif number % 3 == 1:
            return pow3(count - 1) * 2 * 2 % 998244353
        else:
            return pow3(count) * 2 % 998244353
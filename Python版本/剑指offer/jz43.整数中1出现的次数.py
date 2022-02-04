#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def NumberOf1Between1AndN_Solution(self, n: int) -> int:
        # write code here
        res = 0
        base = 1
        forePart = n
        while base <= n:
            cur = (n // base) % 10
            forePart = (n // base) // 10
            postPart = n % base
            if cur == 0:
                res += forePart * base
            elif cur == 1:
                res += (postPart + 1) + forePart * base
            else:
                res += (forePart + 1) * base

            base *= 10

        return res





#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def Sum_Solution(self, n: int) -> int:
        # write code here
        res = 0

        def getSum(n):
            nonlocal res
            res += n
            n > 1 and getSum(n - 1)

        getSum(n)

        return res
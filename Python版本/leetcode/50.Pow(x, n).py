
#方法一：递归+快速幂
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n == 1:
            return x

        if n == -1:
            return 1 / x

        if n < 0:
            n = -n
            x = 1 / x

        def inner(x, n):
            if n <= 1:
                return x

            mid = n // 2
            ans = inner(x, mid)
            return ans * ans if n % 2 == 0 else ans * ans * x

        return inner(x, n)


#方法二：二进制+快速幂
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n == 1:
            return x

        if n == -1:
            return 1 / x

        if n < 0:
            n = -n
            x = 1 / x

        ans = 1
        b = n % 2
        base = x
        if b == 1:
            temp = base
        else:
            temp = 1
        n //= 2
        ans *= temp

        while n > 0:
            b = n % 2
            base *= base
            if b == 0:
                temp = 1
            else:
                temp = base

            ans *= temp
            n //= 2

        return ans
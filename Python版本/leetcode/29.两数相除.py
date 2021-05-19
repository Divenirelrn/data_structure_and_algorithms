
import math

class Solution:
    def mul(a, b):
        ans = 0
        while b > 0:
            if b & 1 == 1:
                ans += a
            a += a

        return ans


    def divide(self, dividend: int, divisor: int) -> int:
        MAX_VALUE = int(math.pow(2, 31) - 1)
        MIN_VALUE = -int(math.pow(2, 31))

        if dividend == 0:
            return 0

        if divisor == 1:
            return dividend

        flag = 1
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            flag = -1

        if dividend < 0:
            dividend = -dividend

        if divisor < 0:
            divisor = -divisor

        l, r = 0, dividend
        while l <= r:
            mid = (l + r) >> 1
            if mul(mid, divisor) > dividend:
                r = mid - 1
            else:
                l = mid + 1

        if flag == 1:
            return l - 1 if l - 1 <= MAX_VALUE else MAX_VALUE
        else:
            return -(l-1) if -(l-1) >= MIN_VALUE else MAX_VALUE
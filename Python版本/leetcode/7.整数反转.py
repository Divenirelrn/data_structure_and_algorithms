
import math

class Solution:
    def reverse(self, x: int) -> int:
        MAX_VALUE = math.pow(2, 31) - 1
        MIN_VALUE = -math.pow(2, 31)

        flag = 1
        if x < 0:
            x = -x
            flag = -1

        res = 0
        while x > 0:
            low = x % 10
            res = res * 10 + low

            x = x // 10

        if flag == 1:
            if res > MAX_VALUE:
                return 0
            return res

        if flag == -1:
            res = -res
            if res < MIN_VALUE:
                return 0
            return res

#方法一：按位相加
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)

        i, j = len_a - 1, len_b - 1
        flag = 0
        ans = ""
        while i >= 0 or j >= 0:
            ai = int(a[i]) if i >= 0 else 0
            bj = int(b[j]) if j >= 0 else 0
            s = ai + bj + flag

            if s >= 2:
                flag = 1
            else:
                flag = 0

            ans += str(s % 2)

            i -= 1
            j -= 1

        if flag == 1:
            ans += '1'

        return ans[::-1]


#方法二：位运算
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)

        while y:
            ans = x ^ y
            carry = (x & y) << 1
            x, y = ans, carry

        return bin(x)[2:]









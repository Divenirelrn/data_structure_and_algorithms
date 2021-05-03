
#方法一：
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        res = ["" for _ in range(numRows)]
        len_s = len(s)

        direct = 'down'
        j = 0
        for i in range(len_s):
            res[j] += s[i]

            if j >= numRows - 1:
                direct = 'up'
            if j <= 0:
                direct = 'down'

            if direct == 'down':
                j += 1
            else:
                j -= 1

        return "".join(res)
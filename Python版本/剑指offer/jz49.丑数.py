#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param index int整型
# @return int整型
#
class Solution:
    def GetUglyNumber_Solution(self, index: int) -> int:
        # write code here
        if index == 0:
            return 0
        res = [1]
        i = j = k = 0
        while len(res) < index:
            nextMin = min(res[i] * 2, res[j] * 3, res[k] * 5)
            if nextMin not in res:
                res.append(nextMin)
            if res[i] * 2 == nextMin:
                i += 1
            elif res[j] * 3 == nextMin:
                j += 1
            elif res[k] * 5 == nextMin:
                k += 1
        print(res)

        return res[-1]








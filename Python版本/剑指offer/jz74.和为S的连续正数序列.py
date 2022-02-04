#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param sum int整型
# @return int整型二维数组
#
class Solution:
    def FindContinuousSequence(self, sum: int) -> List[List[int]]:
        # write code here
        if sum <= 2:
            return []
        res = []
        i = j = 1
        s = 1
        while i <= sum // 2:
            if s < sum:
                j += 1
                s += j
            elif s > sum:
                s -= i
                i += 1
            else:
                res.append([k for k in range(i, j + 1)])
                s -= i
                i += 1

        return res
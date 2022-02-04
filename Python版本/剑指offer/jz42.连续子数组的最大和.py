#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型
#
class Solution:
    def FindGreatestSumOfSubArray(self, array: List[int]) -> int:
        # write code here
        n = len(array)
        if n == 1:
            return array[0]
        value = array[0]
        maxValue = -100
        for i in range(1, n):
            value = max(value + array[i], array[i])
            if value > maxValue:
                maxValue = value

        return maxValue
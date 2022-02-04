#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def reOrderArray(self, array):
        # write code here
        n = len(array)
        if n == 0:
            return []

        ans = list()
        for i in range(n):
            if array[i] % 2 == 1:
                ans.append(array[i])

        for i in range(n):
            if array[i] % 2 == 0:
                ans.append(array[i])

        return ans

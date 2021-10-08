#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param target int整型
# @param array int整型二维数组
# @return bool布尔型
#
class Solution:
    def Find(self, target: int, array: List[List[int]]) -> bool:
        # write code here
        m, n = len(array), len(array[0])
        if m == 0 or n == 0:
            return False

        #从左下角开始
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if array[i][j] < target:
                j += 1
            elif array[i][j] > target:
                i -= 1
            else:
                return True

        return False


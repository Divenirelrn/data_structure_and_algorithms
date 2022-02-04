#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
class Solution:
    def duplicate(self, numbers):
        # write code here
        n = len(numbers)
        if n == 0:
            return -1

        cache = dict()

        for i in range(n):
            if numbers[i] >= n:
                return -1

            if numbers[i] in cache:
                return numbers[i]
            else:
                cache[numbers[i]] = 1
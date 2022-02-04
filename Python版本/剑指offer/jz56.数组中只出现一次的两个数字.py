#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def FindNumsAppearOnce(self, array: List[int]) -> List[int]:
        # write code here
        n = len(array)
        res = 0
        for num in array:
            res ^= num

        mask = 1
        while mask & res == 0:
            mask = mask << 1

        a, b = 0, 0
        for num in array:
            if num & mask == 0:
                a ^= num
            else:
                b ^= num

        return [a, b] if a < b else [b, a]
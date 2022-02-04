#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @param sum int整型
# @return int整型一维数组
#
class Solution:
    def FindNumbersWithSum(self, array: List[int], sum: int) -> List[int]:
        # write code here
        if len(array) == 0:
            return []
        left, right = 0, len(array) - 1
        while left < right:
            if array[left] + array[right] == sum:
                return [array[left], array[right]]
            elif array[left] + array[right] < sum:
                left += 1
            else:
                right -= 1

        return []
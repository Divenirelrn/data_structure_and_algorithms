#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return bool布尔型
#
class Solution:
    def IsContinuous(self, numbers: List[int]) -> bool:
        # write code here
        nonZero = []
        count = 0
        for i in range(5):
            if numbers[i] == 0:
                count += 1
            else:
                if numbers[i] in nonZero:
                    return False
                else:
                    nonZero.append(numbers[i])

        nonZero = sorted(nonZero)
        if count == 4:
            return True
        cur = nonZero[0] + 1
        for i in range(4):
            if cur in nonZero:
                cur += 1
            elif count != 0:
                count -= 1
                cur += 1
            else:
                return False

        return True







#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num1 int整型
# @param num2 int整型
# @return int整型
#
class Solution:
    def Add(self, num1: int, num2: int) -> int:
        # write code here
        num1 &= 0xffffffff
        num2 &= 0xffffffff
        while num2:
            c = ((num1 & num2) << 1) & 0xffffffff
            s = num1 ^ num2
            num2 = c
            num1 = s

        return num1 if num1 < 0x8fffffff else ~(num1 ^ 0xffffffff) #结果为补码，将结果转化为原码，正数原码等于补码，负数按位取反后再整体取反

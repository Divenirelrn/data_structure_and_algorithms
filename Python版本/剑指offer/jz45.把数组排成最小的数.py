#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return string字符串
#
from functools import cmp_to_key


class Solution:
    def PrintMinNumber(self, numbers: List[int]) -> str:
        # write code here
        def cmp(x, y):
            return 1 if x + y > y + x else -1

        if len(numbers) == 0:
            return ""
        numbers = [str(num) for num in numbers]
        numbers = sorted(numbers, key=cmp_to_key(cmp))

        return "".join(numbers)












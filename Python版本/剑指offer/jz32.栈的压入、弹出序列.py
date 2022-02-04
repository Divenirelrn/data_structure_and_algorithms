#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pushV int整型一维数组
# @param popV int整型一维数组
# @return bool布尔型
#
class Solution:
    def IsPopOrder(self, pushV: List[int], popV: List[int]) -> bool:
        # write code here
        stack = list()
        m, n = len(pushV), len(popV)
        i, j = 0, 0

        while i < m:
            if pushV[i] != popV[j]:
                stack.append(pushV[i])
                i += 1
            else:
                i += 1
                j += 1
                while j < n and len(stack) and popV[j] == stack[-1]:
                    stack.pop()
                    j += 1

        return not len(stack)
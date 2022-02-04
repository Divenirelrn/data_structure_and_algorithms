#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @param n int整型
# @return string字符串
#
class Solution:
    def LeftRotateString(self, str: str, n: int) -> str:
        # write code here
        length = len(str)
        if length == 0:
            return ""
        queue = list()
        for s in str:
            queue.append(s)
        for _ in range(n):
            val = queue.pop(0)
            queue.append(val)

        return "".join(queue)
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return string字符串
#
class Solution:
    def ReverseSentence(self, str: str) -> str:
        # write code here
        n = len(str)
        res = ""
        temp = ""
        for i in range(n):
            if str[i] == ' ':
                res = ' ' + temp + res
                temp = ""
            else:
                temp += str[i]
        res = temp + res

        return res
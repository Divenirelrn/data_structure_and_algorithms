#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return string字符串
#
class Solution:
    def replaceSpace(self, s):
        # write code here
        ans = ""
        for i in range(len(s)):
            if s[i] != " ":
                ans += s[i]
            else:
                ans += "%20"

        return ans
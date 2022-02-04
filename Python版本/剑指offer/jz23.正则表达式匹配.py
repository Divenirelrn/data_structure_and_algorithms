#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @param pattern string字符串
# @return bool布尔型
#
class Solution:
    def match(self, str, pattern):
        # write code here
        lenStr, lenPattern = len(str), len(pattern)
        if lenStr == 0 and lenPattern == 0:
            return True
        elif lenStr > 0 and lenPattern == 0:
            return False
        elif lenStr == 0 and lenPattern > 0:
            if lenPattern >= 2 and pattern[1] == '*':
                return self.match(str, pattern[2:])
            else:
                return False

        if lenPattern >= 2 and pattern[1] == '*':
            if str[0] == pattern[0] or pattern[0] == '.':
                return self.match(str, pattern[2:]) or self.match(str[1:], pattern) \
                       or self.match(str[1:], pattern[2:])
            else:
                return self.match(str, pattern[2:])
        elif str[0] == pattern[0] or pattern[0] == '.':
            return self.match(str[1:], pattern[1:])
        else:
            return False


#方法二：动态规划
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @param pattern string字符串
# @return bool布尔型
#
class Solution:
    def match(self, str, pattern):
        # write code here
        lenStr, lenPattern = len(str), len(pattern)
        dp = [[False] * (lenPattern + 1) for _ in range(lenStr + 1)]

        for i in range(lenStr + 1):
            for j in range(lenPattern + 1):
                if j == 0:
                    dp[i][j] = i == 0
                else:
                    if pattern[j - 1] != '*':
                        if i >= 1 and (str[i - 1] == pattern[j - 1] \
                                       or pattern[j - 1] == '.'):
                            dp[i][j] = dp[i - 1][j - 1]
                    else:
                        if j >= 2:
                            dp[i][j] |= dp[i][j - 2]

                        if i >= 1 and j >= 2 and (str[i - 1] == pattern[j - 2] \
                                                  or pattern[j - 2] == '.'):
                            dp[i][j] |= dp[i - 1][j]

        return dp[lenStr][lenPattern]





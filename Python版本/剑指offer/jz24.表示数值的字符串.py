#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return bool布尔型
#
class Solution:
    def isNumeric(self, str):
        # write code here
        # delete blank
        n = len(str)
        i, j = 0, n - 1
        while i < n and str[i] == ' ':
            i += 1
        while j >= 0 and str[j] == ' ':
            j -= 1
        if i > j:
            return False

        s = str[i:j + 1]
        n = len(s)
        hasE = False
        hasDot = False
        hasSign = False

        for i in range(n):
            if s[i] == 'e' or s[i] == 'E':
                if i == n - 1 or i == 0 or hasE \
                        or (i >= 1 and (s[i - 1] == '+' or s[i - 1] == '-')):
                    return False
                hasE = True
            elif s[i] == '.':
                if len(s) == 1 or hasDot or hasE:
                    return False
                elif i == n - 1 and i >= 1 and (s[i - 1] < '0' or s[i - 1] > '9'):
                    return False
                hasDot = True
            elif s[i] == '+' or s[i] == '-':
                if hasSign and i >= 1 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                elif not hasSign and i != 0 and i >= 1 \
                        and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                elif i == n - 1:
                    return False
                hasSign = True
            else:
                if s[i] < '0' or s[i] > '9':
                    return False

        return True




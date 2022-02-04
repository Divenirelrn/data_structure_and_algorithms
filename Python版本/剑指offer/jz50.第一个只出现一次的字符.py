#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return int整型
#
class Solution:
    def FirstNotRepeatingChar(self, str: str) -> int:
        # write code here
        n = len(str)
        hashTable = dict()
        for i in range(n):
            if str[i] not in hashTable:
                hashTable[str[i]] = i
            else:
                hashTable[str[i]] = -1

        minIndex = n
        for k, v in hashTable.items():
            if v != -1 and v < minIndex:
                minIndex = v

        return minIndex if minIndex < n else -1



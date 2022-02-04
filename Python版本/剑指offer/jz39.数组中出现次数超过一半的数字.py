#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
class Solution:
    def MoreThanHalfNum_Solution(self, numbers: List[int]) -> int:
        # write code here
        n = len(numbers)
        hashTable = dict()
        for i in range(n):
            if numbers[i] not in hashTable:
                hashTable[numbers[i]] = 1
            else:
                hashTable[numbers[i]] += 1

        for i in range(n):
            if hashTable[numbers[i]] > n // 2:
                return numbers[i]

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param A int整型一维数组
# @return int整型一维数组
#
class Solution:
    def multiply(self, A: List[int]) -> List[int]:
        # write code here
        n = len(A)
        leftArr = [1]
        for i in range(n - 1):
            leftArr.append(leftArr[i] * A[i])

        rightArr = [1]
        for i in range(n - 1, 0, -1):
            rightArr.append(rightArr[n - i - 1] * A[i])

        res = []
        for i in range(n):
            res.append(leftArr[i] * rightArr[n - i - 1])

        return res




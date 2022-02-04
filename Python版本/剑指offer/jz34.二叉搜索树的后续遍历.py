#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param sequence int整型一维数组
# @return bool布尔型
#
class Solution:
    def VerifySquenceOfBST(self, sequence: List[int]) -> bool:
        # write code here
        n = len(sequence)
        if n == 0:
            return False

        def isBST(left, right):
            if left >= right:
                return True

            root = sequence[right]
            i = 0
            while i < right and sequence[i] < root:
                i += 1
            j = i
            while j < right:
                if sequence[j] < root:
                    return False
                j += 1

            return isBST(left, i - 1) and isBST(i, right - 1)

        return isBST(0, n - 1)


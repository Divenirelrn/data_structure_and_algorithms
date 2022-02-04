#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param input int整型一维数组
# @param k int整型
# @return int整型一维数组
#
class Solution:
    def GetLeastNumbers_Solution(self, input: List[int], k: int) -> List[int]:
        # write code here
        def getPivot(left, right):
            pivot = input[right]
            l, r = left, right
            while l < r:
                while l < r and input[l] <= pivot:
                    l += 1
                input[r] = input[l]
                while l < r and input[r] >= pivot:
                    r -= 1
                input[l] = input[r]

            input[r] = pivot
            return r

        if k == 0:
            return []

        n = len(input)
        left, right = 0, n - 1
        while left <= right:
            pivot = getPivot(left, right)
            if pivot + 1 == k:
                return input[:k]
            elif pivot + 1 < k:
                left = pivot + 1
            else:
                right = pivot - 1

#方法二：优先队列
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param input int整型一维数组
# @param k int整型
# @return int整型一维数组
#
from heapq import heappush, heappop


class Solution:
    def GetLeastNumbers_Solution(self, input: List[int], k: int) -> List[int]:
        # write code here
        if k == 0:
            return []

        n = len(input)
        input = [-val for val in input]
        pQueue = []
        for i in input:
            if len(pQueue) < k:
                heappush(pQueue, i)
            else:
                value = heappop(pQueue)
                if i > value:
                    heappush(pQueue, i)
                else:
                    heappush(pQueue, value)

        return [-val for val in pQueue]
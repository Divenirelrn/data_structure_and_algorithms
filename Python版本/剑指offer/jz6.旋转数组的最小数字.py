# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        n = len(rotateArray)

        first, last = 0, n - 1
        while first < last:
            mid = (first + last) // 2
            if rotateArray[first] < rotateArray[last]:
                return rotateArray[first]
            elif rotateArray[first] < rotateArray[mid]:
                first = mid + 1
            elif rotateArray[last] > rotateArray[mid]:
                last = mid
            else:
                first += 1

        return rotateArray[first]

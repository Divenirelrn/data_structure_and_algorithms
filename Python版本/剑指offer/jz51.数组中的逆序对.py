#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param data int整型一维数组
# @return int整型
#
class Solution:
    def __init__(self):
        self.count = 0
        self.mod = 1000000007

    def InversePairs(self, data: List[int]) -> int:
        # write code here
        n = len(data)
        if n == 0:
            return 0
        self.mergeSort(data, 0, n - 1)
        return self.count % self.mod

    def mergeSort(self, arr, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid + 1, right)
        self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        leftArr = arr[left:mid + 1]
        rightArr = arr[mid + 1:right + 1]
        i, j, k = 0, 0, left
        while i < mid - left + 1 and j < right - mid:
            if leftArr[i] > rightArr[j]:
                arr[k] = rightArr[j]
                j += 1
                k += 1
                self.count += mid - left + 1 - i
            else:
                arr[k] = leftArr[i]
                i += 1
                k += 1

        while i < mid - left + 1:
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < right - mid:
            arr[k] = rightArr[j]
            j += 1
            k += 1







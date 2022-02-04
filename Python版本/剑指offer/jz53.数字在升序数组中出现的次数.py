#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param data int整型一维数组
# @param k int整型
# @return int整型
#
class Solution:
    def GetNumberOfK(self, data: List[int], k: int) -> int:
        # write code here
        n = len(data)
        if n == 0:
            return 0
        left, right = 0, n - 1
        flag = False
        while left <= right:
            mid = (left + right) // 2
            if data[mid] == k:
                flag = True
                break
            elif data[mid] < k:
                left = mid + 1
            else:
                right = mid - 1

        if not flag:
            return 0

        count = 1
        left, right = mid - 1, mid + 1
        while left >= 0 and data[left] == k:
            count += 1
            left -= 1
        while right < n and data[right] == k:
            count += 1
            right += 1

        return count

















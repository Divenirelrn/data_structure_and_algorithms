#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @param size int整型
# @return int整型一维数组
#
class Solution:
    def maxInWindows(self, num: List[int], size: int) -> List[int]:
        # write code here
        n = len(num)
        if size == 0 or size > n:
            return None
        queue = []
        i = 0
        res = []
        while i < n:
            while len(queue) and num[queue[-1]] < num[i]:
                queue.pop()
            queue.append(i)
            if i - queue[0] + 1 > size:
                queue.pop(0)
            if i >= size - 1:
                res.append(num[queue[0]])

            i += 1

        return res












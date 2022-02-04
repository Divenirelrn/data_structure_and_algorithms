# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        def cal(num):
            res = 0
            while num > 0:
                res += num % 10
                num //= 10

            return res

        def centerCount(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols \
                    or (i, j) in visited or cal(i) + cal(j) > threshold:
                return 0

            visited.add((i, j))

            return 1 + centerCount(i + 1, j) + centerCount(i - 1, j) \
                   + centerCount(i, j + 1) + centerCount(i, j - 1)

        visited = set()
        return centerCount(0, 0)


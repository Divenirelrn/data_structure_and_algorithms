
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1],[1,1]]

        res = [[1], [1,1]]
        for i in range(2, numRows):
            pre = res[-1]
            temp = [1]
            for j in range(len(pre) - 1):
                temp.append(pre[j] + pre[j+1])

            temp.append(1)
            res.append(temp)

        return res

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1,1]

        temp = [1,1]
        for i in range(1, rowIndex):
            res = [1]
            for j in range(len(temp) - 1):
                res.append(temp[j] + temp[j+1])

            res.append(1)
            temp = res

        return res
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            a0 = (columnNumber - 1) % 26 + 1
            res = chr(a0 + 65 - 1) + res
            columnNumber = (columnNumber - a0) // 26

        return res
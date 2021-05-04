
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        len_s = len(strs)

        j = 0
        while True:
            if j < len(strs[0]):
                c = strs[0][j]
            else:
                break

            flag = True
            for i in range(1, len_s):
                if j >= len(strs[i]) or strs[i][j] != c:
                    flag = False
                    break

            if not flag:
                break

            res += c
            j += 1

        return res
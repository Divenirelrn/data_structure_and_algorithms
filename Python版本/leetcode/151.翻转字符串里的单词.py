class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)

        res = list()
        temp = ""
        for i in range(n):
            if s[i] != ' ':
                temp += s[i]
            else:
                if len(temp):
                    res.append(temp[:])
                    temp = ""

        if len(temp):
            res.append(temp)

        return ' '.join(res[::-1])

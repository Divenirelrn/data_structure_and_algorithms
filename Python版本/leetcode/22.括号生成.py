
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def char_count(char):
            l = r = 0
            for i in char:
                if i == '(':
                    l += 1
                else:
                    r += 1
            return l, r

        s = ['(']
        res = []
        while len(s):
            char = s.pop()
            if len(char) < 2 * n:
                l, r = char_count(char)
                if l+1 <= n:
                    s.append(char + '(')

                if r+1 <= l:
                    s.append(char + ')')

            else:
                res.append(char)

        return res

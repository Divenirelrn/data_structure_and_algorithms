
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        hash_t = {2: 'abc', 3: 'def', 4: 'ghi', 5:'jkl',
                  6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

        s = []
        res = []

        for i in hash_t[int(digits[0])]:
            s.append(i)

        len_d = len(digits)
        while len(s):
            char = s.pop()
            if len(char) < len_d:
                for i in hash_t[int(digits[len(char)])]:
                    s.append(char + i)
            else:
                res.append(char)

        return res
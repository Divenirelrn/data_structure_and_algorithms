
class Solution:
    def romanToInt(self, s: str) -> int:
        roman2int = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                     'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        res = 0
        for v in roman2int.keys():
            while len(s) and s[0] == v:
                res += roman2int[v]
                s = s[1:]

            while len(s) > 1 and s[:2] == v:
                res += roman2int[v]
                s = s[2:]

            if not len(s):
                break

        return res
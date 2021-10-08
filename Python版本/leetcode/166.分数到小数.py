
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag = 1
        if numerator / denominator < 0:
            flag = -1
        numerator, denominator = abs(numerator), abs(denominator)

        res = ""
        dec = int(numerator / denominator)
        res += str(dec) + "."

        numerator = (numerator % denominator) * 10
        if numerator == 0:
            return res[:-1] if flag > 0 else '-' + res[:-1]

        cache = {numerator: 0}
        k = 1
        while numerator % denominator:
            s = int(numerator / denominator)
            res += str(s)

            numerator = (numerator % denominator) * 10
            if numerator in cache:
                k = cache[numerator]
                break
            else:
                cache[numerator] = k
                k += 1

        if numerator % denominator == 0:
            s = int(numerator / denominator)
            res += str(s)
            return res if flag > 0 else '-' + res
        else:
            temp1, temp2 = res.split('.')
            temp2 = list(temp2)
            temp2.insert(k, '(')
            temp2 = ''.join(temp2)
            res = temp1 + '.' + temp2 + ')'
            return res if flag > 0 else '-' + res


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        len_d = len(digits)
        flag = 0
        digits[-1] += 1
        for i in range(len_d - 1, -1, -1):
            digits[i] += flag
            if digits[i] >= 10:
                flag = 1
            else:
                flag = 0

            digits[i] %= 10

        if flag == 1:
            digits.insert(0, 1)

        return digits
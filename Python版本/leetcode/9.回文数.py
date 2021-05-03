
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        if x % 10 == 0:
            return False

        temp = 0
        while x > 0:
            low = x % 10
            temp = temp * 10 + low

            if temp == x:
                return True

            x //= 10

            if temp == x:
                return True

        return False
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        p1, p2 = 0, n - 1

        while p1 < p2:
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
                while p1 < n and numbers[p1] == numbers[p1 - 1]:
                    p1 += 1
            elif numbers[p1] + numbers[p2] > target:
                p2 -= 1
                while p2 >= 0 and numbers[p2] == numbers[p2 + 1]:
                    p2 -= 1
            else:
                return [p1 + 1, p2 + 1]
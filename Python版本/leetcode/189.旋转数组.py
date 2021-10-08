class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(m, n):
            temp = m
            m = n
            n = temp

            return m, n

        def gcd(m, n):
            if m > n:
                m, n = swap(m, n)

            res = 1
            for i in range(1, m + 1):
                if m % i == 0 and n % i == 0:
                    res = i

            return res

        n = len(nums)
        k = k % n
        count = gcd(k, n)
        for i in range(count):
            temp = nums[i]
            x = (i + k) % n

            while x != i:
                temp, nums[x] = swap(temp, nums[x])
                x = (x + k) % n

            temp, nums[x] = swap(temp, nums[x])


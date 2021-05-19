
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp


        len_num = len(nums)
        if len_num == 1:
            return

        flag = True
        for i in range(len_num-2, -1, -1):
            if nums[i] < nums[i+1]:
                flag = False
                j = i
                value = nums[i]
                while j < len_num - 1 and value < nums[j+1]:
                    j += 1

                swap(i, j)

                i += 1
                k = len_num - 1
                while i < k:
                    swap(i, k)
                    i += 1
                    k -= 1

                break

        if flag:
            for i in range(len_num // 2):
                swap(i, len_num - i - 1)

#方法一：
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)

        nums1 += [0] * len_nums2

        i = len_nums1 - 1
        j = len_nums2 - 1
        k = len_nums1 + len_nums2 - 1
        while (i >= 0 and j >= 0):
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        mid = (len_nums1 + len_nums2 - 1) // 2
        if (len_nums1 + len_nums2) % 2 != 0 or (len_nums1 + len_nums2) == 1:
            return float(nums1[mid])
        else:
            return (nums1[mid] + nums1[mid + 1]) / 2


#方法二：
    pass
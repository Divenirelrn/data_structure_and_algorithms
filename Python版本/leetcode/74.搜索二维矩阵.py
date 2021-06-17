
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = [0, 0], [m-1, n-1]

        while left[0] * n + left[1] <= right[0] * n + right[1]:
            mid = (left[0] * n + left[1] + right[0] * n + right[1]) // 2
            mid_x = mid // n
            mid_y = mid - mid_x * n

            if matrix[mid_x][mid_y] == target:
                return True
            elif matrix[mid_x][mid_y] < target:
                left = mid + 1
                if left > m * n - 1:
                    break
                left_x = left // n
                left_y = left - left_x * n
                if left_y < 0:
                    break

                left = [left_x, left_y]
            else:
                right = mid - 1
                if right < 0:
                    break
                r_x = right // n
                r_y = right - r_x * n
                if r_y < 0:
                    break

                right = [r_x, r_y]

        return False


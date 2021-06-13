
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        len_intv = len(intervals)
        if len_intv == 0:
            return [newInterval]

        new_left, new_right = newInterval[0], newInterval[1]
        ans = []
        block = newInterval
        flag = 0
        for i in range(len_intv):
            if intervals[i][1] < new_left:
                ans.append(intervals[i])
            elif intervals[i][0] > new_right:
                if not flag:
                    ans.append(block)
                    flag = 1
                ans.append(intervals[i])
            else:
                left = min(intervals[i][0], block[0])
                right = max(intervals[i][1], block[1])
                block = [left, right]

        if not flag:
            ans.append(block)

        return ans

#方法一：多叉树
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        len_c = len(candidates)
        def inner(target, idx):
            for i in range(idx, len_c):
                if target - candidates[i] == 0:
                    res.append((temp + [candidates[i]])[:])
                elif target - candidates[i] > 0:
                    temp.append(candidates[i])
                    inner(target - candidates[i], i)
                    temp.pop()

        inner(target, 0)

        return res


#方法二：二叉树
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        len_c = len(candidates)

        def inner(target, idx):
            if target == 0:
                res.append(temp[:])
                return

            if idx == len_c:
                return

            inner(target, idx + 1)

            if target - candidates[idx] >= 0:
                temp.append(candidates[idx])
                inner(target - candidates[idx], idx)
                temp.pop()

        inner(target, 0)

        return res
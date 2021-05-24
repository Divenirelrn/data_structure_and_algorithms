
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []

        hash_t = {}
        for value in candidates:
            if hash_t.get(value, -1) != -1:
                hash_t[value] += 1
            else:
                hash_t[value] = 1

        cands = list(hash_t.keys())
        len_c = len(cands)

        def inner(target, idx):
            if target == 0:
                res.append(temp[:])
                return

            if idx == len_c: #此判断条件放在后面，防止最后一个元素添加不进temp
                return

            inner(target, idx + 1)

            for i in range(1, hash_t[cands[idx]] + 1): #i元素用于去重
                if target - i * cands[idx] >= 0:
                    for j in range(i):
                        temp.append(cands[idx])
                    inner(target - i * cands[idx], idx + 1)
                    for j in range(i):
                        temp.pop()

        inner(target, 0)

        return res
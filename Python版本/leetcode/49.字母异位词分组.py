
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_t = {}
        len_s = len(strs)
        for i in range(len_s):
            text = "".join(sorted(strs[i]))

            if text in hash_t:
                hash_t[text].append(i)
            else:
                hash_t[text] = [i]

        ans = []
        for _, value in hash_t.items():
            temp = []
            for idx in value:
                temp.append(strs[idx])

            ans.append(temp)

        return ans 
#哈希表存下标
#全局与迭代器思想

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        hash_t = dict()
        begin = max_v = 0

        for i in range(len_s):
            if hash_t.get(s[i], -1) != -1 and hash_t[s[i]] >= begin:
                begin = hash_t[s[i]] + 1
                hash_t[s[i]] = i
            else:
                if i - begin + 1 > max_v:
                    max_v = i - begin + 1

                hash_t[s[i]] = i

        return max_v
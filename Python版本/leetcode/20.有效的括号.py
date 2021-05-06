
class Solution:
    def isValid(self, s: str) -> bool:
        hash_t = {'(':')', '[':']','{':'}'}

        stack = []
        stack.append(s[0])
        len_s = len(s)
        for i in range(1,len_s):
            if len(stack):
                char = stack.pop()
                if hash_t.get(char, -1) != -1 and hash_t[char] == s[i]:
                    continue
                else:
                    stack.append(char)
                    stack.append(s[i])
            else:
                stack.append(s[i])

        if len(stack):
            return False

        return True
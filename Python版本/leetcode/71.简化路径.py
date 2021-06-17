
class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        len_p = len(paths)

        s = []
        for i in range(len_p):
            if paths[i] == "" or paths[i] == ".":
                continue

            if paths[i] == "..":
                if len(s):
                    s.pop()
                else:
                    continue
            else:
                s.append(paths[i])

        if not len(s):
            return "/"

        ans = ""
        while len(s):
            p = s.pop()
            ans = '/' + p + ans

        return ans
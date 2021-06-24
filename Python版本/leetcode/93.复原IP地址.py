class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        len_s = len(s)

        def inner(root):
            if len(temp) and len(temp[-1]) > 1 and temp[-1][0] == '0' \
                    or len(temp) and int(temp[-1]) > 255:
                return

            if len(temp) == 4 and len(root) == 0:
                ans.append('.'.join(temp[:]))
                return

            if len(temp) == 4 or len(root) == 0:
                return

            for count in [1, 2, 3]:
                if len(root[:count]) != count:
                    continue
                temp.append(root[:count])
                inner(root[count:])
                temp.pop()

        ans = []
        temp = []
        inner(s)

        return ans
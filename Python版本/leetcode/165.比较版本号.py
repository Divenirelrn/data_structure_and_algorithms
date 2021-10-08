class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        n1, n2 = len(v1), len(v2)
        i = j = 0
        while i < n1 or j < n2:
            temp1 = int(v1[i]) if i < n1 else 0
            temp2 = int(v2[j]) if j < n2 else 0

            if temp1 > temp2:
                return 1
            elif temp1 < temp2:
                return -1

            i += 1
            j += 1

        return 0




